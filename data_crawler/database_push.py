from backend.common import folder_path,common
import json,aiohttp,asyncio

file_paths = folder_path.util.get_tree(folder_path.Data.Hacom.path)
headers = {
    "Content-Type": "application/json"
}
class PushAPI:
    def __init__(self) -> None:
        self.base_url = common.get_url(common.get_config('server'))
        self.session : aiohttp.ClientSession = None
    def start(self) :
        self.session = aiohttp.ClientSession(self.base_url)
    async def stop(self) :
        await self.session.close()
        self.session = None
    async def push_product(self,data : dict):
        try:
            async with(self.session.post(url='/product',data = json.dumps(data),headers=headers)) as response:
                if (response.status == 200):
                    return True
                else:
                    return False
        except Exception as e:
            print(e)
            return False
    def format(self,data : dict):
        basic = [
            'price','name','images'
        ]
        result = {}
        data_infos = data['info']        
        i=0
        if (data_infos == []):
            return None
        for info in data_infos:
            result['basic_info_{}'.format(i)] = info
            i+=1
        i=0
        data_detail_infos = data['detail_info']
        for info in data_detail_infos:
            result['detail_info_{}'.format(i)] = info
            i+=1
        images = data['images']
        i=0
        for image in images:
            images[i] = {
                'path' : image,
                'order' : i
            }
            i+=1
        i=0
        notices = data['notices']
        for notice in notices:
            result['notice_{}'.format(i)] = notice
            i+=1
        if (len(images) == 0):
            return None
        for key in basic:
            result[key] = data[key]
        result['thumbnail'] = images[0]['path']
        for key in data:
            if (key not in basic and key not in ['thumbnail','info','detail_info','notices']):
                result[key] = data[key]
        return result

async def process():
    handler = PushAPI()
    handler.start()
    for key in file_paths:
        if ('links.json' not in key and 'exception.json' not in key):
            with open(file_paths[key],'r') as file:
                data = json.loads(file.read())
                formated_data = handler.format(data)
                if (formated_data == None):
                    continue
                await handler.push_product(formated_data)
            #     raise Exception
            # break
    await handler.stop()
asyncio.run(process())
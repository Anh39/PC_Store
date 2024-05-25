from backend.common import folder_path,common
import aiohttp
headers = {
    "Content-Type": "application/json"
}
class BaseDBAPI:
    def __init__(self) -> None:
        self.base_url = common.get_url(common.get_config('database'))
        self.session : aiohttp.ClientSession = None
    def start(self) :
        self.session = aiohttp.ClientSession(self.base_url)
    async def stop(self) :
        await self.session.close()
        self.session = None

class DatabaseAPI(BaseDBAPI):
    async def get_full_data(
        self
    ) -> dict[str,object]:
        try:
            async with(self.session.get(url='/product/full',params={'limit' : 999999,'mode' : '-'},headers=headers)) as response:
                if (response.status == 200):
                    results : list[dict] = await response.json()
                    final_results = {}
                    for result in results:
                        infos : list = []
                        for key in result:
                            if ('basic_info' in key):
                                infos.append(result[key])
                        final_result = {
                            'price' : result['price'],
                            'category' : result['category'],
                            'info' : ' '.join(infos)
                        }
                        final_results[result['id']] = final_result
                    return final_results
                else:
                    print('ERR')
        except Exception as e:
            print(e)
from backend.common import folder_path
import json

file_paths = folder_path.util.get_tree(folder_path.Data.HacomRaw.path)


def process_flow(file_path : str):
    print(file_path)
    with open(file_path,'r') as file:
        data = json.loads(file.read())
    if ('lap' in file_path):
        data['category'] = 'laptop'
    elif ('pc' in file_path):
        data['category'] = 'pc'
    elif ('display' in file_path):
        data['category'] = 'display'
    elif ('auxility' in file_path):
        data['category'] = 'auxility'
    else:
        data['category'] = 'other'
    if (data['info'] == None):
        data['info'] = []
    else:
        data['info'] = data['info'].split('\n')
    if (data['detail_info'] == None):
        data['detail_info'] = []
    else:
        data['detail_info'] = data['detail_info'].split('\n')
        
    info = []
    for ele in data['info']:
        if (ele not in ['','\t']):
            info.append(ele)
    data['info'] = info

        
    detail_info = []
    for ele in data['detail_info']:
        if (ele not in ['','\t']):
            detail_info.append(ele)
    data['detail_info'] = detail_info


    with open(file_path.replace('hacom_raw','hacom'),'w') as file:
        file.write(json.dumps(data))
        


for key in file_paths:
    if ('links.json' not in key and 'exception.json' not in key):
        process_flow(file_paths[key])
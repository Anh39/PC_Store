import json
from backend.common import folder_path

config_info = {}

def get_config(module_name : str = 'all'):
    mapping = {
        'all' : config_info,
        'server' : config_info['server'],
        'database' : config_info['database'],
        'ai' : config_info['ai'],
        'react' : config_info['react']
    }
    return mapping[module_name]

class Util:
    @classmethod
    def load_config(cls):
        global config_info
        with open(folder_path.Common.config,'r') as file:
            config_info = json.loads(file.read())
            
Util.load_config()
import json
from backend.common import folder_path
import uuid

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
def gen_key(username : str = None,password : str = None):
    token = str(uuid.uuid4())
    return token
def get_url(config : dict) -> str:
    return 'http://' + config['host']+':'+str(config['port']) + '/'
class Util:
    @classmethod
    def load_config(cls):
        global config_info
        with open(folder_path.Common.config,'r') as file:
            config_info = json.loads(file.read())
            
Util.load_config()
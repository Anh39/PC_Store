import os,json

join = os.path.join
_project_path = os.getcwd()
backend = os.path.join(_project_path,'backend')
class Config:
    path = join(_project_path,'config')
    config_name = 'config'
class Common:
    path = join(backend,'common')
    config = join(path,'config.json')
    

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
    
class Storage:
    path = join(backend,'storage')
    class Images:
        path = join(backend,'storage','images')
        posts = join(path,'posts')
        products = join(path,'products')
        users = join(path,'users')
    class Videos:
        path = join(backend,'storage','videos')

class Data:
    path = join(_project_path,'data_crawler','data')
    class Hacom:
        path = join(_project_path,'data_crawler','data','hacom')
        pc_game = join(path,'pc_game')
        pc_graphic = join(path,'pc_graphic')
        pc_office = join(path,'pc_office')
    
class util:
    @classmethod
    def get_tree(self,folder_path : str):
        temp_result = set()
        self._recurse_get_file(temp_result,folder_path)
        result = {}
        for key in temp_result:
            result[os.path.normpath(self.to_relative(key,folder_path))] = key
        return result
    @classmethod
    def to_relative(self,path : str,relto : str):
        relpath = os.path.relpath(path,relto)
        return relpath
    @classmethod
    def _recurse_get_file(self,result : set,input_path : str):
        for file_name in os.listdir(input_path):
            file_path = join(input_path,file_name)
            if (os.path.isdir(file_path)):
                self._recurse_get_file(result,file_path)
            else:
                result.add(file_path)

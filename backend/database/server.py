from fastapi import FastAPI
from backend.server.model import *
from backend.common import common
import hydra
from omegaconf import DictConfig, OmegaConf
from backend.common import folder_path
import uvicorn
from backend.database.crud.user import UserCRUD
from sqlalchemy import Engine,create_engine
from backend.database.schema.user import BaseSchema

class DatabaseServer:
    def __init__(self) -> None:
        config = common.get_config('server')
        self.host : str = config['host']
        self.port : int = config['port']
        self.app : FastAPI = FastAPI()
        self.engine : Engine = create_engine("sqlite:///"+'database.db',echo=True)
    
        BaseSchema.metadata.create_all(self.engine)
        
        self.user : UserCRUD = UserCRUD(self.engine)

    def start(self):
        self.app.add_api_route('/user',self.user.get_user,methods=["GET"])
        self.app.add_api_route('/user',self.user.create_user,methods=["POST"])
        self.app.add_api_route('/user',self.user.update_user,methods=["PATCH"])
        self.app.add_api_route('/user',self.user.delete_user,methods=["DELETE"])
        
        uvicorn.run(
            app = self.app,
            host = self.host,
            port = self.port
        )
    


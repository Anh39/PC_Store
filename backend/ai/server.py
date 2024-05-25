from fastapi import FastAPI
import uvicorn
from backend.ai.model import *
from backend.common import common
from .ml import TFIDF,BaseModel

class AIServer:
    def __init__(self) -> None:
        config = common.get_config('ai')
        self.host : str = config['host']
        self.port : int = config['port']
        self.app : FastAPI = FastAPI()
        self.server : uvicorn.Server = None
        
        self.model : BaseModel = TFIDF()
        
    def _add_route(self):
        self.app.add_api_route('/product',self.model.predict,methods=['GET'],tags=['Product'])
        
    # def start(self):
    #     self._add_route()
    #     uvicorn.run(
    #         app = self.app,
    #         host = self.host,
    #         port = self.port
    #     )
    
    async def async_start(self):
        await self.model.train()
        self._add_route()
        server_config = uvicorn.Config(
            self.app,
            host=self.host,
            port=self.port
        )
        self.server = uvicorn.Server(server_config)
        await self.server.serve()
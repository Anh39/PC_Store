from fastapi import FastAPI
from backend.server.model import *
from backend.common import common
from sqlalchemy import Engine,create_engine
from backend.database.schema.user import BaseSchema
import uvicorn
from .crud import *
import logging

class DatabaseServer:
    def __init__(self) -> None:
        config = common.get_config('database')
        self.host : str = config['host']
        self.port : int = config['port']
        self.app : FastAPI = FastAPI()
        self.engine : Engine = create_engine("sqlite:///"+'database.db',echo=False)
        BaseSchema.metadata.create_all(self.engine)
        
        self.cruds : dict[str,BaseCRUD] = {
            'cart' : CartCRUD(),
            'order' : OrderCRUD(),
            'product' : ProductCRUD(),
            'user' : UserCRUD(),
            'map' : MapCRUD()
        }
        for key in self.cruds:
            self.cruds[key].engine = self.engine
    def _add_route(self):
        for key in self.cruds:
            self.app.add_api_route('/{}'.format(key),self.cruds[key].get,methods=['GET'],tags=[key])
            self.app.add_api_route('/{}'.format(key),self.cruds[key].update,methods=['PATCH'],tags=[key])
            self.app.add_api_route('/{}'.format(key),self.cruds[key].create,methods=['POST'],tags=[key])
            self.app.add_api_route('/{}'.format(key),self.cruds[key].delete,methods=['DELETE'],tags=[key])

        self.app.add_api_route('/user/order',self.cruds['user'].get_order,methods=['GET'],tags=['user_relation'])
        self.app.add_api_route('/user/voucher',self.cruds['user'].get_voucher,methods=['GET'],tags=['user_relation'])
        self.app.add_api_route('/user/rating',self.cruds['user'].get_rating,methods=['GET'],tags=['user_relation'])
        
        self.app.add_api_route('/product/full',self.cruds['product'].full_create,methods=['POST'],tags=['product'])
        self.app.add_api_route('/product/full',self.cruds['product'].full_get,methods=['GET'],tags=['product'])

        self.app.add_api_route('/cart_item',self.cruds['cart'].modify_item,methods=['POST'],tags=['cart'])
    def start(self):
        self._add_route()
        uvicorn.run(
            app = self.app,
            host = self.host,
            port = self.port
        )
    
    async def async_start(self):
        self._add_route()
        server_config = uvicorn.Config(
            self.app,
            host=self.host,
            port=self.port
        )
        self.server = uvicorn.Server(server_config)
        await self.server.serve()
        

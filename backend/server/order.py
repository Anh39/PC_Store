from .model import *
from .request_model import *
from backend.server.api.order import OrderDBAPI
from ..common import common
from fastapi import HTTPException,Header
from .validator import UserValidator
from .cart import CartManager

get_token = Header

class OrderManager:
    def __init__(self,validator : UserValidator) -> None:
        self.order_api = OrderDBAPI()
        self.order_api.start()
        self.validator : UserValidator = validator
    async def get_orders(self,token : str = get_token()) :
        result = await self.order_api.get_orders(
            token=token
        )
        if (len(result) == 0):
            result = []
        return result
    async def create_order(self,token : str = get_token()) :
        data = {
            'token' : token
        }
        result = await self.order_api.create_order(data)
        return result
    async def add_product_to_cart(self,body : CartChangeRequest,token : str = get_token()):
        return await self.__change_cart(body.id,token,command='Add')
    async def change_amount(self,body : CartChangeRequest,token : str = get_token()):
        return await self.__change_cart(body.id,token,command=body.amount)
    async def delete_product_in_cart(self,id : int,token : str = get_token()):
        return await self.__change_cart(id,token,command='Delete')
    async def __change_cart(self,id : int,token : str,command : str | int): 
        return await self.order_api.modify_cart(
            token=token,
            command=command,
            id=id
        )
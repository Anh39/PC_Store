from .model import *
from .request_model import *
from backend.server.api.cart import CartDBAPI
from ..common import common
from fastapi import HTTPException,Header
from .validator import UserValidator
from typing import Literal

get_token = Header

class CartManager:
    def __init__(self,validator : UserValidator) -> None:
        self.cart_api = CartDBAPI()
        self.cart_api.start()
        self.validator : UserValidator = validator
    async def get_cart(self,token : str = get_token(None)) : # completed
        result = await self.cart_api.get_cart(
            token=token
        )
        if (len(result) == 0):
            result = {}
        return Cart.model_validate(result).items
    async def add_product_to_cart(self,body : CartChangeRequest,token : str = get_token()):
        return await self.__change_cart(body.id,token,command='Add')
    async def increase_decrease_product_in_cart(self,body : CartChangeRequest,token : str = get_token()):
        return await self.__change_cart(body.id,token,command=body.command)
    async def delete_product_in_cart(self,id : int,token : str = get_token()):
        return await self.__change_cart(id,token,command='Delete')
    async def __change_cart(self,id : int,token : str,command : str = Literal['+','-','Add','Delete']): 
        return await self.cart_api.modify_cart(
            token=token,
            command=command,
            id=id
        )
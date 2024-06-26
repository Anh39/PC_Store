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
    async def get_cart(self,token : str = get_token()) : # completed
        valid = self.validator.validate(token)
        if (not valid):
            raise HTTPException(status_code=401)
        result = await self.cart_api.get_cart(
            token=token
        )
        if (result == None or len(result) == 0):
            return []
        return result['items']
    async def add_product_to_cart(self,body : CartChangeRequest,token : str = get_token()):
        valid = self.validator.validate(token)
        if (not valid):
            raise HTTPException(status_code=401)
        return await self.__change_cart(body.id,token,command='Add')
    async def change_amount(self,body : CartChangeRequest,token : str = get_token()):
        valid = self.validator.validate(token)
        if (not valid):
            raise HTTPException(status_code=401)
        return await self.__change_cart(body.id,token,command=body.amount)
    async def delete_product_in_cart(self,id : int,token : str = get_token()):
        valid = self.validator.validate(token)
        if (not valid):
            raise HTTPException(status_code=401)
        return await self.__change_cart(id,token,command='Delete')
    async def __change_cart(self,id : int,token : str,command : str | int): 
        return await self.cart_api.modify_cart(
            token=token,
            command=command,
            id=id
        )
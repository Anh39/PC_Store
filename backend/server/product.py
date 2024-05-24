from .model import *
from fastapi import HTTPException,Header
from .validator import UserValidator
from .api.product import ProductDBAPI
from typing import Literal

get_token = Header
class ProductManager:
    def __init__(self,validator : UserValidator) -> None:
        self.product_api : ProductDBAPI = ProductDBAPI()
        self.product_api.start()
        self.validator = validator
    async def get_category(self,admin_token : str = get_token(None)) -> list[str]:
        valid = await self.validator.admin_validate(admin_token)
        if (valid):
            list_data = await self.product_api.get_category()
            result = set()
            for row in list_data:
                result.add(row['value'])
            return list(result)
        else:
            return []
    async def create_product(self,data : Product,admin_token : str = get_token(None)) -> None | int:
        valid = await self.validator.admin_validate(admin_token)
        if (valid):
            dict_data = data.model_dump()
            dict_data.pop('id')
            result = await self.product_api.create_product(dict_data)
            if (result):
                return result
        return None
    async def search_products(self,data : dict,token : str | None = get_token()) -> list[Product]:
        validate_result = await self.validator.guest_validate(token)
        if (validate_result):
            result = await self.product_api.search_product(data)
            if (result):
                return result
        return False
    async def get_product(self,id : int | None = None,mode : Literal['random','none'] = 'random',offset : int = 0,limit : int = 50,token : str | None = get_token()) -> list:
        validate_result = await self.validator.guest_validate(token)
        if (validate_result):
            dict_data = {
                'id' : id,
                'mode' : mode,
                'offset' : offset,
                'limit' : limit
            }
            print(dict_data)
            result = await self.product_api.get_product(dict_data)
            if (result):
                return result
        return False
    async def recommend_products(self,data : dict) -> list[Product]:
        return [Product.get_test()]
    async def change_product(self,data : dict) -> Product:
        return Product.get_test()
    async def delete_product(self,data : dict) -> bool:
        return True
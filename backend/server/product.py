from .model import *
from fastapi import HTTPException,Header
from .validator import UserValidator
from .api.product import ProductDBAPI
from .api.ai import AIAPI
from typing import Literal

get_token = Header
class ProductManager:
    def __init__(self,validator : UserValidator) -> None:
        self.product_api : ProductDBAPI = ProductDBAPI()
        self.ai_api : AIAPI = AIAPI()
        self.ai_api.start()
        self.product_api.start()
        self.validator = validator
        self.category_cache = None
    async def get_category(self) -> list:

        if (self.category_cache != None):
            return self.category_cache
        list_data = await self.product_api.get_product({})
        result = set()
        for row in list_data:
            result.add(row['category'])
        self.category_cache = list(result)
        return self.category_cache
    async def create_product(self,data : Product,admin_token : str = get_token(None)) -> None | int:
        valid = self.validator.validate(admin_token)
        if (not valid):
            raise HTTPException(status_code=401)
        dict_data = data.model_dump()
        dict_data.pop('id')
        result = await self.product_api.create_product(dict_data)
        if (result):
            return result
        return None
    async def get_product(self,id : int | None = None,mode : Literal['random','none'] = 'random',offset : int = 0,limit : int = 50,name : str | None = None,category : str | None = None) -> list:
        dict_data = {
            'id' : id,
            'mode' : mode,
            'offset' : offset,
            'limit' : limit,
            'name' : name,
            'category' : category
        }
        print(dict_data)
        result = await self.product_api.get_product(dict_data)
        if (result):
            return result
        return []
    async def get_product_detail(self,id : int | None = None,mode : Literal['random','none'] = 'random',offset : int = 0,limit : int = 50) -> list:
        dict_data = {
            'id' : id,
            'mode' : mode,
            'offset' : offset,
            'limit' : limit
        }
        print(dict_data)
        result = await self.product_api.get_product_detail(dict_data)
        if (result):
            return result
        return False
    async def recommend_products(self,id : int,limit : int = 8) -> list:
        results = await self.ai_api.product_based_recommend(
            id=id,
            amount=limit
        )
        product_results = []
        for result in results:
            product_result = await self.product_api.get_product({'id' : result[0]})
            product_result = product_result[0]
            product_results.append(product_result)
        return product_results
    async def change_product(self,id : int,data : dict,admin_token : str = get_token()) -> bool:
        valid = self.validator.validate(admin_token)
        if (not valid):
            raise HTTPException(status_code=401)
        return await self.product_api.update_product(
            id=id,
            data=data
        )
    async def delete_product(self,id : int, admin_token : str = get_token()) -> bool:
        valid = self.validator.validate(admin_token)
        if (not valid):
            raise HTTPException(status_code=401)
        return await self.product_api.delete(id)
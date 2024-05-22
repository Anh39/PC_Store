from .model import *
from fastapi import HTTPException,Header
from .validator import UserValidator
from .api.product import ProductDBAPI

get_token = Header
class ProductManager:
    def __init__(self,validator : UserValidator) -> None:
        self.product_api : ProductDBAPI = ProductDBAPI()
        self.product_api.start()
        self.validator = validator
    async def create_product(self,data : Product,admin_token : str = get_token(None)) -> None | int:
        validate_result = await self.validator.admin_validate(admin_token)
        if (validate_result):
            dict_data = data.model_dump()
            dict_data.pop('id')
            result = await self.product_api.create_product(dict_data)
            if (result):
                return result
        return None
    async def search_products(self,data : dict) -> list[Product]:
        return [Product.get_test()]
    async def get_product(self,id : int,token : str | None = get_token()):
        validate_result = await self.validator.guest_validate(token)
        if (validate_result):
            dict_data = {
                "id" : id
            }
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
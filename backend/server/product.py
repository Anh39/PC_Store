from .model import *
from fastapi import HTTPException,Header
from .validator import UserValidator
from .api.product import ProductDBAPI

get_token = Header
class ProductManager:
    def __init__(self,validator : UserValidator) -> None:
        self.db_api : ProductDBAPI = ProductDBAPI()
        self.db_api.start()
        self.validator = validator
    async def create_product(self,data : Product,admin_token : str = get_token(None)) -> bool:
        validate_result = await self.validator.admin_validate(admin_token)
        if (validate_result):
            result = await self.db_api.create_product(data.model_dump())
            if (result):
                return True
        return False
    async def search_products(self,data : dict) -> list[Product]:
        return [Product.get_test()]
    async def get_product(self,data : dict) -> Product:
        return Product.get_test()
    async def recommend_products(self,data : dict) -> list[Product]:
        return [Product.get_test()]
    async def change_product(self,data : dict) -> Product:
        return Product.get_test()
    async def delete_product(self,data : dict) -> bool:
        return True
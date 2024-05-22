from .model import *

class ProductManager:
    def __init__(self) -> None:
        self.database = None
    async def create_product(self,data : dict) -> Product:
        return Product.get_test()
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
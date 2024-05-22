from .model import *

class OrderManager:
    def __init__(self) -> None:
        self.database = None
    async def create_order(self,data : dict) -> Order:
        return Order.get_test()
    async def search_orders(self,data : dict) -> list[Order]:
        return [Order.get_test()]
    async def get_order(self,data : dict) -> Post:
        return Order.get_test()
    async def recommend_orders(self,data : dict) -> list[Order]:
        return [Order.get_test()]
    async def change_order(self,data : dict) -> Order:
        return Order.get_test()
    async def delete_order(self,data : dict) -> bool:
        return True
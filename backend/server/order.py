from .model import *
from .request_model import *
from backend.server.api.user import UserDBAPI
from ..common import common
from fastapi import HTTPException,Header
from .validator import UserValidator

get_token = Header

class OrderManager:
    def __init__(self,validator : UserValidator) -> None:
        self.user_api = UserDBAPI()
        self.user_api.start()
        self.validator : UserValidator = validator
    async def get_cart(self,token : str = get_token(None)) -> Cart: # completed
        result = await self.user_api.get_user_cart(
            token=token
        )
        if (len(result) == 0):
            result = {
                'products' : list(),
                'voucher' : None,
                'value' : 0
            }
        return Cart.model_validate(result)
    async def change_cart(self,request : CartChangeRequest,token : str = get_token(None)) -> Cart: 
        return Cart.get_test()
    async def get_orders(self,token : str = get_token()) -> list[Order]: # completed
        results = await self.user_api.get_user_voucher(
            token=token
        )
        final_results = []
        for result in results:
            final_results.append(Order.model_validate(result))
        return final_results
    async def get_vouchers(self,token : str = get_token()) -> list[Voucher]: # completed
        results = await self.user_api.get_user_voucher(
            token=token
        )
        final_results = []
        for result in results:
            final_results.append(Order.model_validate(result))
        return final_results
    
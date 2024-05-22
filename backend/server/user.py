from .model import *
from .request_model import *
from backend.server.api.user import UserDBAPI
from ..common import common

class UserManager:
    def __init__(self) -> None:
        self.user_api = UserDBAPI()
        self.user_api.start()
    async def validate(self,token : str) -> bool: # Untest
        result = await self.user_api.get_user({
            'token' : token
        })
        return len(result) > 0
    async def admin_validate(self,token : str) -> bool: # Untest
        result = await self.user_api.get_user({
            'token' : token
        })
        return len(result) > 0 and result[0]['role'] == 'Admin'
    async def login(self,request : LoginRequest) -> str | None: # Completed
        result = await self.user_api.get_user({
            'email' : request.email,
            'password' : request.password
        })
        if (len(result) > 0):
            return result[0]['token']
        else:
            return None
    async def register(self,request : RegisterRequest) -> str | None: # Completed
        token = common.gen_key()
        data = {
            'email' : request.email,
            'name' : request.username,
            'password' : request.password,
            'token' : token
        }
        result = await self.user_api.create_user(data)
        if (result):
            return token
        else:
            return None
    async def reset_password(self,request : ResetPasswordRequest) -> str:
        return 'reset_password'
    async def get_user_info(self,token : str) -> User: # get minimum info only # Partly completed
        result = await self.user_api.get_user({
            'token' : token
        })
        return User.model_validate(result[0])
    async def delete_user(self,request : ChangeUserInfoRequest) -> bool: # completed
        result = await self.user_api.delete_user(
            token=request.token,
            password=request.password
        )
        return result
    async def change_user_info(self,request : ChangeUserInfoRequest) -> bool: # completed
        result = await self.user_api.update_user(
            token=request.token,
            password=request.password,
            data=request.data
        )
        return result
    async def get_cart(self,token : str) -> Cart:
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
    async def change_cart(self,request : ChangeCartRequest) -> Cart:
        return Cart.get_test()
    async def get_orders(self,token : str) -> list[Order]:
        results = await self.user_api.get_user_order(
            token=token
        )
        final_results = []
        for result in results:
            final_results.append(Order.model_validate(result))
        return final_results
    async def get_vouchers(self,token : str) -> list[Voucher]:
        return [Voucher.get_test()]
    
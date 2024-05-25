from .model import *
from .request_model import *
from backend.server.api.user import UserDBAPI
from ..common import common
from fastapi import HTTPException,Header
from .validator import UserValidator

get_token = Header

class UserManager:
    def __init__(self,validator : UserValidator) -> None:
        self.user_api = UserDBAPI()
        self.user_api.start()
        self.validator : UserValidator = validator
    async def login(self,request : LoginRequest) -> AuthenticationResponse: # Completed
        result = await self.user_api.get_user({
            'email' : request.email,
            'password' : request.password
        })
        role = 'Customer' 
        token = result[0]['token']
        validate_result = await self.validator.admin_validate(token)
        if (validate_result):
            role = 'Admin'
        if (len(result) > 0):
            return AuthenticationResponse(
                success=True,
                token=token,
                role=role
            )
        else:
            return AuthenticationResponse(
                success=False,
                token=None
            )
    async def register(self,request : RegisterRequest) -> AuthenticationResponse: # Completed
        token = common.gen_key()
        data = {
            'email' : request.email,
            'name' : request.username,
            'password' : request.password,
            'token' : token
        }
        result = await self.user_api.create_user(data)
        if (result):
            return AuthenticationResponse(
                success=True,
                token=token
            )
        else:
            return AuthenticationResponse(
                success=False,
                token=None
            )
    # async def get_user_info(self,token : str = get_token(None)) -> User: # get minimum info only # Partly completed
    #     result = await self.user_api.get_user({
    #         'token' : token
    #     })
    #     if (len(result) > 0):
    #         return User.model_validate(result[0])
    #     else:
    #         raise HTTPException(status_code=404)
    # async def delete_user(self,request : ChangeUserInfoRequest,token : str = get_token(None)) -> bool: # completed
    #     result = await self.user_api.delete_user(
    #         token=token,
    #         password=request.confirm_password
    #     )
    #     return result
    async def change_user_info(self,request : ChangeUserInfoRequest,token : str = get_token(None)) -> bool: # completed
        result = await self.user_api.update_user(
            token=token,
            password=request.confirm_password,
            data=request.data
        )
        return result

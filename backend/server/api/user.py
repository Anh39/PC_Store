from backend.common import common
import aiohttp
from .base import BaseDBAPI
import json
from ..model import User
headers = {
    "Content-Type": "application/json"
}
class UserDBAPI(BaseDBAPI):
    async def get_user(
        self,
        data : dict[str,object]
    ) -> dict[str,object]:
        try:
            async with(self.session.get(url='/user',params = data,headers=headers)) as response:
                if (response.status == 200):
                    result = await response.json()
                    return result
                else:
                    print('ERR')
        except Exception as e:
            print(e)
    
    async def create_user(
        self,
        data : User
    ) -> bool:
        try:
            async with(self.session.post(url='/user',data = json.dumps(data),headers=headers)) as response:
                if (response.status == 200):
                    return True
                else:
                    return False
        except Exception as e:
            print(e)
            return False
    async def update_user(
        self,
        token : str,
        password : str,
        data : User
    ) -> bool:
        try:
            params = {
                'token' : token,
                'password' : password
            }
            async with(self.session.patch(url='/user',params = params,data=json.dumps(data),headers=headers)) as response:
                if (response.status == 200):
                    return True
                else:
                    return False
        except Exception as e:
            print(e)
            return False
    async def delete_user(
        self,
        token : str,
        password : str
    ) -> bool:
        try:
            params = {
                'token' : token,
                'password' : password
            }
            async with(self.session.delete(url='/user',params = params,headers=headers)) as response:
                if (response.status == 200):
                    return True
                else:
                    return False
        except Exception as e:
            print(e)
            return False
    
    async def get_user_cart(
        self,
        token : dict[str,object]
    ) -> dict[str,object]:
        try:
            params = {
                'token' : token
            }
            async with(self.session.get(url='/user/cart',params = params,headers=headers)) as response:
                if (response.status == 200):
                    result = await response.json()
                    return result
                else:
                    print('ERR')
        except Exception as e:
            print(e)
            
    async def get_user_order(
        self,
        token : dict[str,object]
    ) -> list[dict[str,object]]:
        try:
            params = {
                'token' : token
            }
            async with(self.session.get(url='/user/order',params = params,headers=headers)) as response:
                if (response.status == 200):
                    result = await response.json()
                    return result
                else:
                    print('ERR')
        except Exception as e:
            print(e)
            
    
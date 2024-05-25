from backend.common import common
import aiohttp
from .base import BaseDBAPI
import json
from ..model import Product
from typing import Literal
headers = {
    "Content-Type": "application/json"
}
class MapDBAPI(BaseDBAPI):
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
    
    async def create_product(
        self,
        data : dict[str,object]
    ) -> bool:
        try:
            async with(self.session.post(url='/product',data = json.dumps(data),headers=headers)) as response:
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
        data : Product
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
    

from backend.common import common
import aiohttp
from .base import BaseDBAPI
import json
from ..model import Product
from typing import Literal
headers = {
    "Content-Type": "application/json"
}
class ProductDBAPI(BaseDBAPI):
    async def get_product(
        self,
        data : dict[str,object|None]
    ) -> dict[str,object]:
        try:
            del_keys = []
            for key in data:
                if (data[key] == None):
                    del_keys.append(key)
            for key in del_keys:
                data.pop(key)
            async with(self.session.get(url='/product/full',params = data,headers=headers)) as response:
                if (response.status == 200):
                    result = await response.json()
                    return result
                else:
                    print('ERR')
        except Exception as e:
            print(e)
            
    async def search_product(
        self,
        data : dict[str,object]
    ) -> list[dict[str,object]]:
        try:
            async with(self.session.get(url='/product/full',params = data,headers=headers)) as response:
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
    ) -> bool | int:
        try:
            async with(self.session.post(url='/product/full',data = json.dumps(data),headers=headers)) as response:
                if (response.status == 200):
                    result = await response.text()
                    return int(result)
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
    async def _get_user_relation(
        self,
        kind : Literal['order','cart','rating','voucher'],
        token : str
    ) -> dict[str,object] | list[dict[str,object]]:
        try:
            params = {
                'token' : token
            }
            async with(self.session.get(url='/user/{}'.format(kind),params = params,headers=headers)) as response:
                if (response.status == 200):
                    result = await response.json()
                    return result
                else:
                    print('ERR')
        except Exception as e:
            print(e)
    
    

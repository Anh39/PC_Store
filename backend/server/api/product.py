from backend.common import common
from .base import BaseDBAPI
import json
from ..model import Product
from typing import Literal
headers = {
    "Content-Type": "application/json"
}
class ProductDBAPI(BaseDBAPI):
    async def get_product_detail(
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
            async with(self.session.get(url='/product',params = data,headers=headers)) as response:
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
        
    async def update_product(
        self,
        id : int,
        data : dict[str,object]
    ) -> bool:
        try:
            async with(self.session.patch(url='/product/full',params={'id' : id},data = json.dumps(data),headers=headers)) as response:
                if (response.status == 200):
                    result = await response.text()
                    return True
                else:
                    return False
        except Exception as e:
            print(e)
            return False
    
    async def delete(
        self,
        id : int
    ) -> bool:
        try:
            params = {
                'id' : id
            }
            async with(self.session.delete(url='/product',params = params,headers=headers)) as response:
                if (response.status == 200):
                    return True
                else:
                    print('ERR')
                    return False
        except Exception as e:
            print(e)
            return False
    
    

from backend.common import common
from .base import BaseDBAPI
import json
from ..model import User
from typing import Literal
headers = {
    "Content-Type": "application/json"
}
class OrderDBAPI(BaseDBAPI):
    async def get_orders(
        self,
        token : str
    ) -> dict[str,object]:
        try:
            async with(self.session.get(url='/order',params = {'token' : token},headers=headers)) as response:
                if (response.status == 200):
                    result = await response.json()
                    return result
                else:
                    print('ERR')
        except Exception as e:
            print(e)
    
    async def create_order(
        self,
        data : dict
    ) -> bool:
        try:
            async with(self.session.post(url='/order',data = json.dumps(data),headers=headers)) as response:
                if (response.status == 200):
                    return True
                else:
                    return False
        except Exception as e:
            print(e)
            return False
    async def update_order(
        self,
        id : int,
        data : dict
    ) -> bool:
        try:
            params = {
                'id' : id
            }
            async with(self.session.patch(url='/order',params=params,data=json.dumps(data),headers=headers)) as response:
                if (response.status == 200):
                    return True
                else:
                    return False
        except Exception as e:
            print(e)
            return False
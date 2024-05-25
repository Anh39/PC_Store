from backend.common import common
import aiohttp
from .base import BaseDBAPI
import json
from ..model import User
from typing import Literal
headers = {
    "Content-Type": "application/json"
}
class CartDBAPI(BaseDBAPI):
    async def get_cart(
        self,
        token : str
    ) -> dict[str,object]:
        try:
            async with(self.session.get(url='/cart',params = {'token' : token},headers=headers)) as response:
                if (response.status == 200):
                    result = await response.json()
                    return result
                else:
                    print('ERR')
        except Exception as e:
            print(e)
    
    async def modify_cart(
        self,
        token : str,
        command : str | int,
        id : int
    ) -> bool:
        try:
            data = {
                'token' : token,
                'id' : id,
                'command' : command
            }
            async with(self.session.post(url='/cart_item',data = json.dumps(data),headers=headers)) as response:
                if (response.status == 200):
                    return True
                else:
                    return False
        except Exception as e:
            print(e)
            return False
    
from backend.common import common
from .base import BaseDBAPI
import json
from typing import Literal
headers = {
    "Content-Type": "application/json"
}
class AIAPI(BaseDBAPI):
    def __init__(self) -> None:
        super().__init__()
        self.base_url = common.get_url(common.get_config('ai'))
    async def product_based_recommend(
        self,
        id : int,
        amount : int
    ) -> dict[str,object]:
        try:
            params = {
                'id' : id,
                'amount' : amount
            }
            async with(self.session.get(url='/product',params = params,headers=headers)) as response:
                if (response.status == 200):
                    result = await response.json()
                    return result
                else:
                    print('ERR')
        except Exception as e:
            print(e)
    
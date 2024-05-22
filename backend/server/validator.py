from backend.server.api.user import UserDBAPI

class UserValidator:
    def __init__(self) -> None:
        self.user_api = UserDBAPI()
        self.user_api.start()
    async def validate(self,token : str ) -> bool: # Untest
        result = await self.user_api.get_user({
            'token' : token
        })
        return len(result) > 0
    async def admin_validate(self,token : str) -> bool: # Untest
        result = await self.user_api.get_user({
            'token' : token
        })
        return len(result) > 0 and result[0]['role'] == 'Admin'
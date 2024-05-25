from backend.server.api.user import UserDBAPI

class UserValidator:
    def __init__(self) -> None:
        self.user_api = UserDBAPI()
        self.user_api.start()
        self.bypast = False
    async def validate(self,token : str ) -> bool: # Untest
        if (self.bypast):
            return True
        result = await self.user_api.get_user({
            'token' : token
        })
        return len(result) > 0
    async def admin_validate(self,token : str) -> bool: # Untest
        if (self.bypast):
            return True
        result = await self.user_api.get_user({
            'token' : token
        })
        return (len(result) > 0 and result[0]['role'] == 'Admin') 
    async def guest_validate(self,token : str | None = None) -> bool:
        if (self.bypast):
            return True
        return True
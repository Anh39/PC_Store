from pydantic import BaseModel

class LoginRequest(BaseModel):
    email : str
    password : str
    
class RegisterRequest(LoginRequest):
    username : str
    
class ResetPasswordRequest(BaseModel):
    email : str | None
    code : str | None
    
class ChangeUserInfoRequest(BaseModel):
    password : str
    data : dict[str,object]
    
class ChangeCartRequest(BaseModel):
    data : dict[str,object]
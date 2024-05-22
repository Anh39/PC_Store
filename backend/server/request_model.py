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
    token : str
    password : str
    data : dict[str,object]
    
class ChangeCartRequest(BaseModel):
    token : str
    data : dict[str,object]
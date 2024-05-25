from pydantic import BaseModel
from typing import Literal

class LoginRequest(BaseModel):
    email : str
    password : str
    
class RegisterRequest(LoginRequest):
    username : str | None
    
class ChangeUserInfoRequest(BaseModel):
    confirm_password : str
    data : dict[str,object]
    
class CartChangeRequest(BaseModel):
    id : int
    amount : int | None = None
from pydantic import BaseModel,Field

class AuthenticationResponse(BaseModel):
    success : bool
    token : str | None = Field(
        min_length=0,
        max_length=50
    )
    role : str | None = 'Customer'
    @classmethod
    def get_test(cls):
        result = AuthenticationResponse(
            success=True,
            token='example_token'
        )
        return result
    
class User(BaseModel):
    email : str
    name : str = 'Noname'
    birthday : str | None = None
    phone : str | None = None
    gender : str | None = None
    address : str | None = None
    avatar : str | None = None
    card : str | None = None

class ProductImageInfo(BaseModel):
    path : str
    order : int
class Product(BaseModel):
    id : int | None = None
    price : float 
    thumbnail : str
    images : list[ProductImageInfo]
    name : str
    class Config:
        extra = 'allow'
    


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
    @classmethod
    def get_test(cls):
        result = User(
            email='hello@gmail.com',
            name='test_name',
            birthday='birthday',
            phone='013123',
            gender='male',
            address='address',
            avatar='a/b.png',
            card='card'
        )
        return result
class Voucher(BaseModel):
    id : int
    discount : float
    received_time : str
    expire_time : str
    category_apply : str
    description : str
    @classmethod
    def get_test(cls):
        result = Voucher(
            id=123,
            discount=0.12,
            received_time='received_time',
            expire_time='expire_time',
            category_apply='category_apply',
            description='description'
        )
        return result

class Cart(BaseModel):
    items : list[dict]
    @classmethod
    def get_test(cls):
        result = Cart(
            products=[Product.get_test()]
        )
        return result
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
    @classmethod
    def get_test(cls):
        result = Product(
            id=12,
            price=123.2,
            images=[],
            name='test_product',
            ratings=[Rating.get_test()]
        )
        return result
    
class Post(BaseModel):
    id : int
    content : str
    time_created : str
    time_modified : str
    user_name : str
    @classmethod
    def get_test(cls):
        result = Post(
            id=1232,
            content='content',
            time_created='time_created',
            time_modified='time_modified',
            user_name='user_name'
        )
        return result

class OrderInfo(BaseModel):
    address : str | None
    phone : str | None

class Order(BaseModel):
    id : int
    items : list[dict] | None
    status : str | None
    time_created : str | None
    time_completed : str | None
    value : float | None
    address : str | None
    phone : str | None
    user_id : int | None
    @classmethod
    def get_test(cls):
        result = Order(
            id=132123123,
            items=[OrderItem.get_test()],
            status='completed',
            time_created='time_created',
            time_completed='time_completed',
            value=1312.22,
            address='address',
            phone='0123132',
            user_id=123132
        )
        return result

class OrderItem(BaseModel):
    product_id : int
    amount : int
    @classmethod
    def get_test(cls):
        result = OrderItem(
            product_id=14213,
            amount=2
        )
        return result
class Rating(BaseModel):
    user_name : str
    user_id : int
    value : float
    product_id : float
    @classmethod
    def get_test(cls):
        result = Rating(
            user_id=1231312,
            user_name='user_name',
            value=1232.222,
            product_id=13222
        )
        return result
    

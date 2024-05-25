import uvicorn
from fastapi import FastAPI
from backend.common import common
from .product import ProductManager
from .user import UserManager
from .validator import UserValidator
from .media import MediaManager
from .cart import CartManager
from .order import OrderManager
from .transaction import TransactionManager
from fastapi.middleware.cors import CORSMiddleware

class FastAPIServer:
    def __init__(self) -> None:
        config = common.get_config('server')
        self.host : str = config['host']
        self.port : int = config['port']
        self.app : FastAPI = FastAPI()
        self.server : uvicorn.Server = None
        
        self.validator = UserValidator()
        
        self.product = ProductManager(self.validator)
        self.user = UserManager(self.validator)
        self.media = MediaManager(self.validator)
        self.cart = CartManager(self.validator)
        self.order = OrderManager(self.validator)
        self.transaction = TransactionManager(self.validator,self.cart,self.order)
        
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=[
                'http://127.0.0.1:3000',
                'http://localhost:3000'
            ],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"]
        )
        
    def _add_route(self):
        self.app.add_api_route('/login',self.user.login,methods=['POST'],tags=['User'])
        self.app.add_api_route('/register',self.user.register,methods=['POST'],tags=['User'])
        self.app.add_api_route('/reset_password',self.user.reset_password,methods=['PATCH'],tags=['User'])
        self.app.add_api_route('/user',self.user.change_user_info,methods=['PATCH'],tags=['User'])
        self.app.add_api_route('/user',self.user.get_user_info,methods=['GET'],tags=['User'])
        self.app.add_api_route('/user',self.user.delete_user,methods=['DELETE'],tags=['User'])
        
        self.app.add_api_route('/cart',self.cart.get_cart,methods=['GET'],tags=['Cart'])
        self.app.add_api_route('/cart',self.cart.add_product_to_cart,methods=['POST'],tags=['Cart'])
        self.app.add_api_route('/cart',self.cart.change_amount,methods=['PATCH'],tags=['Cart'])
        self.app.add_api_route('/cart',self.cart.delete_product_in_cart,methods=['DELETE'],tags=['Cart'])
        self.app.add_api_route('/orders',self.order.get_orders,methods=['GET'],tags=['Order'])
        self.app.add_api_route('/order',self.order.create_order,methods=['POST'],tags=['DEBUG'])
        
        self.app.add_api_route('/image',self.media.upload_image,methods=['POST'],tags=['Media'])
        self.app.add_api_route('/image',self.media.delete_image,methods=['DELETE'],tags=['Media'])
        
        self.app.add_api_route('/product/category',self.product.get_category,methods=['GET'],tags=['Product'])
        self.app.add_api_route('/product',self.product.get_product,methods=['GET'],tags=['Product'])
        self.app.add_api_route('/recommend',self.product.recommend_products,methods=['GET'],tags=['Product'])
        self.app.add_api_route('/product_detail',self.product.get_product_detail,methods=['GET'],tags=['Product'])
        self.app.add_api_route('/product',self.product.change_product,methods=['PATCH'],tags=['Product'])
        self.app.add_api_route('/product',self.product.create_product,methods=['POST'],tags=['Product'])
        self.app.add_api_route('/product',self.product.delete_product,methods=['DELETE'],tags=['Product'])
        
        self.app.add_api_route('/transaction/create',self.transaction.create_payment,methods=['GET'],tags=['Transaction'])
        self.app.add_api_route('/transaction/return',self.transaction.payment_return,methods=['GET'],tags=['Transaction'])
        # self.app.add_api_route('/transaction/excute',self.transaction.excute_payment,methods=['POST'],tags=['Transaction'])
        
    def start(self):
        self._add_route()
        uvicorn.run(
            app = self.app,
            host = self.host,
            port = self.port
        )
    
    async def async_start(self):
        self._add_route()
        server_config = uvicorn.Config(
            self.app,
            host=self.host,
            port=self.port
        )
        self.server = uvicorn.Server(server_config)
        await self.server.serve()
        
    


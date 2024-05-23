import uvicorn
from fastapi import FastAPI
from backend.common import common
from .post import PostManager
from .product import ProductManager
from .user import UserManager
from .voucher import VoucherManager
from .validator import UserValidator
from .media import MediaManager
from fastapi.middleware.cors import CORSMiddleware

class FastAPIServer:
    def __init__(self) -> None:
        config = common.get_config('server')
        self.host : str = config['host']
        self.port : int = config['port']
        self.app : FastAPI = FastAPI()
        self.server : uvicorn.Server = None
        
        self.validator = UserValidator()
        
        self.post = PostManager()
        self.product = ProductManager(self.validator)
        self.user = UserManager(self.validator)
        self.media = MediaManager(self.validator)
        self.voucher = VoucherManager()
        
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
        self.app.add_api_route('/reset_password',self.user.reset_password,methods=['POST'],tags=['User'])
        self.app.add_api_route('/user',self.user.change_user_info,methods=['PATCH'],tags=['User'])
        self.app.add_api_route('/user',self.user.get_user_info,methods=['GET'],tags=['User'])
        self.app.add_api_route('/user',self.user.delete_user,methods=['DELETE'],tags=['User'])
        self.app.add_api_route('/my_cart',self.user.get_cart,methods=['GET'],tags=['User'])
        self.app.add_api_route('/my_vouchers',self.user.get_vouchers,methods=['GET'],tags=['User'])
        self.app.add_api_route('/my_orders',self.user.get_orders,methods=['GET'],tags=['User'])
        
        self.app.add_api_route('/image',self.media.upload_image,methods=['POST'],tags=['Media'])
        self.app.add_api_route('/image',self.media.delete_image,methods=['DELETE'],tags=['Media'])
        
        self.app.add_api_route('/product',self.product.get_product,methods=['GET'],tags=['Product'])
        self.app.add_api_route('/products',self.product.search_products,methods=['GET'],tags=['Product'])
        self.app.add_api_route('/product',self.product.change_product,methods=['PATCH'],tags=['Product'])
        self.app.add_api_route('/product',self.product.create_product,methods=['POST'],tags=['Product'])
        self.app.add_api_route('/product',self.product.delete_product,methods=['DELETE'],tags=['Product'])
        
        self.app.add_api_route('/post',self.post.get_post,methods=['GET'],tags=['Post'])
        self.app.add_api_route('/post',self.post.create_post,methods=['POST'],tags=['Post'])
        self.app.add_api_route('/post',self.post.change_post,methods=['PATCH'],tags=['Post'])
        self.app.add_api_route('/post',self.post.delete_post,methods=['DELETE'],tags=['Post'])
        
        self.app.add_api_route('/voucher',self.voucher.get_voucher,methods=['GET'],tags=['Voucher'])
        self.app.add_api_route('/voucher',self.voucher.create_voucher,methods=['POST'],tags=['Voucher'])
        self.app.add_api_route('/voucher',self.voucher.change_voucher,methods=['PATCH'],tags=['Voucher'])
        self.app.add_api_route('/voucher',self.voucher.delete_voucher,methods=['DELETE'],tags=['Voucher'])
        
        
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
        
    


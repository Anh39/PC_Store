from fastapi import HTTPException,Response,Header
from fastapi.responses import RedirectResponse
from fastapi.responses import JSONResponse
from .validator import UserValidator
from .cart import CartManager
from .order import OrderManager
import paypalrestsdk
import asyncio
from backend.common import folder_path,common

paypalrestsdk.configure(folder_path.API.get_paypal_configure())
get_token = Header
class TransactionManager:
    def __init__(self,validator : UserValidator,cart_manager : CartManager,order_manager : OrderManager) -> None:
        self.client = paypalrestsdk
        self.validator = validator
        self.payment_queue : dict[str] = {}
        self.cart_manager : CartManager = cart_manager
        self.order_manager : OrderManager = order_manager
        self.return_url = common.get_url(common.get_config('server')) + 'transaction/return'
        self.sucess_url = common.get_url(common.get_config('react')) + ''
        self.failure_url = common.get_url(common.get_config('react')) + ''
        self.cancel_url = common.get_url(common.get_config('react'))
    def convert(self,vnd : str) -> str:
        return str(float(vnd)/25000)
    async def payment_return(self,
            paymentId : str,
            token : str,
            PayerID : str
        ):
        try:
            if (paymentId not in self.payment_queue):
                return Response(status_code=404,content='Payment not found')
            else:
                value = self.payment_queue.pop(paymentId)
                await self.excute_payment(paymentId,PayerID)
                await self.order_manager.create_order(token=value)
                await self.cart_manager.delete_product_in_cart(id=-1,token=value)
                return RedirectResponse(url=self.sucess_url)
        except Exception as e:
            return RedirectResponse(url=self.failure_url)
            return HTTPException(401)
    async def create_payment(self,token : str = get_token(None)):
        valid = self.validator.validate(token)
        if (not valid):
            raise HTTPException(status_code=401)
        cart_items = await self.cart_manager.get_cart(token)
        items = []
        total = 0
        for cart_item in cart_items:
            new_item = {
                'name' : cart_item['name'],
                'sku' : 'item',
                'price' : self.convert(cart_item['price']),
                'currency' : 'USD',
                'quantity' : cart_item['amount']
            }
            total += float(new_item['price']) * new_item['quantity']
            items.append(new_item)
        payment = self.client.Payment({
            "intent" : "sale",
            "payer" : {
                "payment_method" : "paypal"
            },
            "redirect_urls" : {
                "return_url" : self.return_url,
                "cancel_url" : self.cancel_url
            },
            "transactions" : [{
                "item_list" : {
                    "items" : items
                },
                "amount" : {
                    "total" : str(total),
                    "currency" : "USD"
                },
                "description" : "Testo"
            }]
        })
        if (payment.create()):
            for link in payment.links:
                if (link.rel == 'approval_url'):
                    approval_url = str(link.href)
                    if (approval_url):
                        self.payment_queue[payment.id] = token
                        return JSONResponse({"approval_url" : approval_url})
        raise HTTPException(status_code=500,detail="Failed to create payment")
    async def excute_payment(self,payment_id : str,payer_id : str):
        paypal_client = self.client
        payment = paypal_client.Payment.find(payment_id)
        if (payment.execute({"payer_id" : payer_id})):
            return True
        else:
            raise HTTPException(status_code=500,detail="Failed to excute payment")

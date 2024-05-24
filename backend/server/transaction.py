from fastapi import HTTPException,Response,Header
from fastapi.responses import JSONResponse
from .validator import UserValidator
from .cart import CartManager
import paypalrestsdk
import asyncio
from backend.common import folder_path

paypalrestsdk.configure(folder_path.API.get_paypal_configure())
get_token = Header
class TransactionManager:
    def __init__(self,validator : UserValidator,cart_manager : CartManager) -> None:
        self.client = paypalrestsdk
        self.validator = validator
        self.payment_queue : dict[str] = {}
        self.cart_manager : CartManager = cart_manager
    def convert(self,vnd : str) -> str:
        return str(float(vnd)/25000)
    async def payment_return(self,
            paymentId : str,
            token : str,
            PayerID : str
        ):
        if (paymentId not in self.payment_queue):
            return Response(status_code=404,content='Payment not found')
        else:
            value = self.payment_queue.pop(paymentId)
            await self.excute_payment(paymentId,PayerID)
            await self.cart_manager.delete_product_in_cart(id=-1,token=value)
            return Response(status_code=200,content='Payment success, please return to store')
    async def create_payment(self,token : str = get_token(None)):
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
                "return_url" : "http://127.0.0.1:8000/transaction/return",
                "cancel_url" : "http://127.0.0.1:8000/transaction/cancel"
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

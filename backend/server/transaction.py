from fastapi import FastAPI,HTTPException,Response
from fastapi.responses import JSONResponse
from .validator import UserValidator
import paypalrestsdk
import asyncio
import uvicorn
from backend.common import folder_path

paypalrestsdk.configure(folder_path.API.get_paypal_configure())

app = FastAPI()
class TransactionManager:
    def __init__(self,validator : UserValidator) -> None:
        self.client = paypalrestsdk
        self.validator = validator
        self.payment_queue : set[str] = set()
        self.delay = 2
    async def payment_return(self,
            paymentId : str,
            token : str,
            PayerID : str
        ):
        if (paymentId not in self.payment_queue):
            return Response(status_code=404,content='Payment not found')
        else:
            self.payment_queue.remove(paymentId)
            await self.excute_payment(paymentId,PayerID)
            return Response(status_code=200,content='Payment success, please return to store')
    async def create_payment(self):
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
                    "items" : [{
                        "name" : "item_name",
                        "sku" : "item",
                        "price" : "5",
                        "currency" : "USD",
                        "quantity" : 1
                    }]
                },
                "amount" : {
                    "total" : "5",
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
                        self.payment_queue.add(payment.id)
                        return JSONResponse({"approval_url" : approval_url})
        raise HTTPException(status_code=500,detail="Failed to create payment")
    async def excute_payment(self,payment_id : str,payer_id : str):
        paypal_client = self.client
        payment = paypal_client.Payment.find(payment_id)
        if (payment.execute({"payer_id" : payer_id})):
            return True
        else:
            raise HTTPException(status_code=500,detail="Failed to excute payment")

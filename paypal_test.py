from fastapi import FastAPI,HTTPException
from fastapi.responses import JSONResponse
import paypalrestsdk
import uvicorn
from backend.common import folder_path

paypalrestsdk.configure(folder_path.API.get_paypal_configure())

def get_paypal_client():
    return paypalrestsdk

app = FastAPI()

@app.post("/create-payment")
async def create_payment():
    paypal_client = get_paypal_client()
    
    payment = paypal_client.Payment(
        {
            "intent" : "sale",
            "payer" : {
                "payment_method" : "paypal"
            },
            "redirect_urls" : {
                "return_url" : "http://127.0.0.1:3000",
                "cancel_url" : "http://127.0.0.1:3000/product/1832"
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
        }
    )
    if (payment.create()):
        for link in payment.links:
            if (link.rel == 'approval_url'):
                approval_url = str(link.href)
                return JSONResponse({"approval_url" : approval_url})
        return {"payment_id" : payment.id}
    else:
        raise HTTPException(status_code=500,detail="Failed to create payment")
    
@app.post("/excute-payment")
async def excute_payment(payment_id : str,payer_id : str):
    paypal_client = get_paypal_client()
    payment = paypal_client.Payment.find(payment_id)
    if (payment.execute({"payer_id" : payer_id})):
        return {"status" : "Payment excuted successfully"}
    else:
        raise HTTPException(status_code=500,detail="Failed to excute payment")
    
uvicorn.run(
    app=app,
    host='127.0.0.1',
    port=8003
)

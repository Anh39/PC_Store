from fastapi import FastAPI
from fastapi import requests,responses
from backend.server.model import *
from backend.common import common
import uvicorn

app = FastAPI()

@app.get("/",tags=['Test'])
async def root():
    return {"message" : "Konnichiwa Sekai!"}

@app.get("/users",tags=['User','Authentication'])
async def get_user(
    id : str | None = None,
    token : str | None = None,
    username : str | None = None,
    password : str | None = None
) -> UserShort | User:
    if (id != None):
        return UserShort.get_test()
    else:
        return User.get_test()
@app.post("/users",tags=['User'])
async def add_user(
    data : User
) -> responses.JSONResponse:
    content = {'message' : 'Success'}
    return responses.JSONResponse(content=content,status_code=200)
@app.patch("/users",tags=['User'])
async def change_user(
    data : list[InfoChangeUnit]
) -> responses.JSONResponse:
    content = {'message' : 'Success'}
    return responses.JSONResponse(content=content,status_code=200)
@app.delete("/users",tags=['User'])
async def delete_user(
    id : str
) -> responses.JSONResponse:
    content = {'message' : 'Success'}
    return responses.JSONResponse(content=content,status_code=200)


@app.get("/item",tags=['User'])
async def get_item(
    id : str | None = None
) -> Item:
    return Item.get_test()
@app.get("/items",tags=['User','Search'])
async def search_item(
    name_like : str | None = None,
    price_range : tuple[float,float] | None = None,
    info : dict[str,object] | None = None
) -> list[Item]:
    return [Item.get_test()]

@app.get("/basket",tags=['User'])
async def get_basket_for_user(
    user_token : str
) -> Basket:
    return Basket.get_test()
@app.post("/basket",tags=['User'])
async def change_basket_info(
    user_token : str,
    data : list[InfoChangeUnit]
) -> responses.JSONResponse:
    content = {'message' : 'Success'}
    return responses.JSONResponse(content=content,status_code=200)
@app.delete("/basket",tags=['User'])
async def delete_basket_info(
    user_token : str,
    data : list[InfoChangeUnit]
) -> responses.JSONResponse:
    content = {'message' : 'Success'}
    return responses.JSONResponse(content=content,status_code=200)

@app.get("/vouchers",tags=['User','Search'])
async def search_voucher(
    percent : float | None = None
) -> list[Voucher]:
    return [Voucher.get_test()]
@app.get("/voucher",tags=['User'])
async def get_voucher_for_user(
    user_token : str,
) -> ListVoucher:
    return ListVoucher.get_test()
@app.post("/voucher",tags=['User'])
async def add_voucher(
    user_token : str,
    data : list[InfoChangeUnit]
) -> responses.JSONResponse:
    content = {'message' : 'Success'}
    return responses.JSONResponse(content=content,status_code=200)
@app.delete("/voucher",tags=['User'])
async def delete_voucher(
    user_token : str,
    data : list[InfoChangeUnit]
) -> responses.JSONResponse:
    content = {'message' : 'Success'}
    return responses.JSONResponse(content=content,status_code=200)
@app.get("/admin_users",tags=['Admin'])
async def admin_get_all_user(
    admin_token : str,
    user_id : str | None = None
    
) -> list[User] | User:
    if (user_id != None):
        return User.get_test()
    else:
        return [User.get_test()]
@app.post("/admin_user",tags=['Admin'])
async def admin_add_user(
    admin_token : str,
    data : User
) -> responses.JSONResponse:
    content = {'message' : 'Success'}
    return responses.JSONResponse(content=content,status_code=200)
@app.patch("/admin_user",tags=['Admin'])
async def admin_change_user(
    admin_token : str,
    user_token : str,
    data = list[InfoChangeUnit]
) -> responses.JSONResponse:
    content = {'message' : 'Success'}
    return responses.JSONResponse(content=content,status_code=200)
@app.delete("/admin_user",tags=['Admin'])
async def admin_delete_user(
    admin_token : str,
    user_token : str
) -> responses.JSONResponse:
    content = {'message' : 'Success'}
    return responses.JSONResponse(content=content,status_code=200)
@app.get("/admin_vouchers",tags=['Admin'])
async def admin_get_all_vouchers(
    admin_token : str
) -> list[Voucher]:
    return [Voucher.get_test()]
@app.post("/admin_vouchers",tags=['Admin'])
async def admin_add_voucher(
    data : Voucher
)-> responses.JSONResponse:
    content = {'message' : 'Success'}
    return responses.JSONResponse(content=content,status_code=200)
@app.patch("/admin_vouchers",tags=['Admin'])
async def admin_change_voucher(
    voucher_id : str,
    data : list[InfoChangeUnit]
)-> responses.JSONResponse:
    content = {'message' : 'Success'}
    return responses.JSONResponse(content=content,status_code=200)
@app.delete("/admin_vouchers",tags=['Admin'])
async def admin_delete_voucher(
    voucher_id : str
)-> responses.JSONResponse:
    content = {'message' : 'Success'}
    return responses.JSONResponse(content=content,status_code=200)
@app.get("/admin_items",tags=['Admin'])
async def admin_get_all_items(
    admin_token : str
) -> ListItem:
    return ListItem.get_test()
@app.post("/admin_items",tags=['Admin'])
async def admin_add_item(
    data : Item
) -> responses.JSONResponse:
    content = {'message' : 'Success'}
    return responses.JSONResponse(content=content,status_code=200)
@app.patch("/admin_items",tags=['Admin'])
async def admin_change_item(
    item_id : str,
    data : list[InfoChangeUnit]
) -> responses.JSONResponse:
    content = {'message' : 'Success'}
    return responses.JSONResponse(content=content,status_code=200)
@app.delete("/admin_items",tags=['Admin'])
async def admin_delete_item(
    item_id : str
) -> responses.JSONResponse:
    content = {'message' : 'Success'}
    return responses.JSONResponse(content=content,status_code=200)



def start():
    config = common.get_config('server')
    uvicorn.run(app,host=config['host'],port=config['port'])
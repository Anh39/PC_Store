from fastapi import FastAPI
import uvicorn
from backend.server.model import UserInfo,Item
from backend.ai.model import *
from backend.common import common

app = FastAPI()

@app.post("/users")
async def predict(
    user_info : UserInfo
) -> ModelReturn:
    test = ModelReturn.get_test()
    return test
    
def start():
    config = common.get_config('ai')
    uvicorn.run(app,host=config['host'],port=config['port'])

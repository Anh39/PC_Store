from fastapi import FastAPI
from backend.server.model import *
from backend.common import common
import hydra
from omegaconf import DictConfig, OmegaConf
from backend.common import folder_path

app = FastAPI()

class Test:
    async def root():
        return {"message" : "Konnichiwa Sekai!"}
test = Test()



@hydra.main(version_base=None,config_path=folder_path.Config.path,config_name='config')
def start(cfg : DictConfig):
    server = hydra.utils.instantiate(cfg.server.database.server)
    server.run(app,host=cfg.server.database.host,port=cfg.server.database.port)
    


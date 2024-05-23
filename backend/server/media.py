from .model import *
from .request_model import *
from backend.server.api.user import UserDBAPI
from ..common import common,folder_path
from fastapi import HTTPException,Header,File,UploadFile
from .validator import UserValidator
from typing import Literal
import os

get_token = Header

class MediaManager:
    def __init__(self,validator : UserValidator) -> None:
        self.validator = validator
        self.dir_map = {
            'product' : folder_path.Storage.Images.products,
            'post' : folder_path.Storage.Images.posts,
            'user' : folder_path.Storage.Images.posts
        }
    async def upload_image(self,bind_id : int,file : UploadFile ,category : Literal['product','post','user'],token : str = get_token(None)) -> str:
        valid = await self.validator.admin_validate(token)
        if (valid):
            file_name = common.gen_key()
            file_extension = '.'+file.filename.split('.')[-1]
            file_path = folder_path.join(self.dir_map[category],file_name+file_extension)
            with open(file_path,'wb+') as file_object:
                file_object.write(file.file.read())
            return file_name+file_extension
        else:
            return ''
    async def __upload_image(self,file : UploadFile ,category : Literal['product','post','user'],token : str = get_token(None)) -> str:
        valid = await self.validator.admin_validate(token)
        if (valid):
            file_name = common.gen_key()
            file_extension = '.'+file.filename.split('.')[-1]
            file_path = folder_path.join(self.dir_map[category],file_name+file_extension)
            with open(file_path,'wb+') as file_object:
                file_object.write(file.file.read())
            return file_name+file_extension
        else:
            return ''
    async def delete_image(self,url : str,category : Literal['product','post','user'],token : str = get_token(None)) -> bool:
        valid = await self.validator.admin_validate(token)
        if (valid):
            try:
                file_path = folder_path.join(self.dir_map[category],url)
                if (os.path.exists(file_path)):
                    os.remove(file_path)
                    return True
                return False
            except Exception as e:
                return False
        else:
            return
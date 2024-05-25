import json
from .base import BaseCRUD
from ..schema.product import ProductSchema,ProductImageSchema
from ..schema.map import MapSchema
from sqlalchemy.orm import Session
from fastapi import Request,Response
from sqlalchemy import Engine,select,delete,update,func
from typing import Literal

class ProductCRUD(BaseCRUD):
    async def full_create(self,data : dict) ->Response:
        with Session(self.engine) as session:
            product = ProductSchema.model_validate(data)
            session.add(product)
            try:
                session.commit()
                session.refresh(product)
                images = data.get('images',[])
                for image in images:
                    new_image = ProductImageSchema()
                    new_image.path = image['path']
                    new_image.order = image['order']
                    new_image.product_id = product.id
                    session.add(new_image)
                basic_keys = ['images']
                extra_keys = []
                for key in ProductSchema.__table__.columns:
                    basic_keys.append(str(key.name))
                for key in data:
                    if (key not in basic_keys):
                        extra_keys.append(key)
                for key in extra_keys:
                    new_info = MapSchema()
                    new_info.key = key
                    new_info.value = data[key]
                    new_info.product_id = product.id
                    session.add(new_info)
                session.commit()
                return Response(status_code=200,content=str(product.id))
            except:
                return Response(status_code=404)
    async def full_get(
            self,
            id : int | None = None,
            mode : str = Literal['random','none'],
            offset : int = 0,
            limit : int = 50,
            image_metadata : bool = False
        ) -> Response:
        with Session(self.engine) as session:
            query = select(ProductSchema)
            if (id != None):
                query = query.where(ProductSchema.id == id)
            if (mode == 'random'):
                query = query.order_by(func.random())
            query = query.offset(offset).limit(limit)
            results = session.execute(query)
            response_results = []
            for result in results:
                product : ProductSchema = result[0]
                data = product.model_dump()
                infos = product.infos
                images = []
                for image in product.images:
                    image_data : dict = image.model_dump()
                    images.append(image_data)
                for i in range(len(images)):
                    for j in range(i+1,len(images)):
                        if ([images[i]['order'] > images[j]['order']]):
                            images[i],images[j] = images[j],images[i]
                if (image_metadata != True):
                    for i in range(len(images)):
                        images[i] = images[i]['path']
                data['images'] = images
                for info in infos:
                    if (info.key not in data):
                        data[info.key] = info.value
                response_results.append(data)
            return Response(content=json.dumps(response_results),media_type='application/json',status_code=200)
    async def create(self,data : dict) -> Response:
        with Session(self.engine) as session:
            print(data)
            product = ProductSchema.model_validate(data)
            session.add(product)
            session.commit()
            return Response(status_code=200)
    async def update(
            self,
            data : dict,
            id : int | None = None
        ) -> Response: 
        with Session(self.engine) as session:
            query = update(ProductSchema)
            if (id != None):
                query = query.where(ProductSchema.id == id)
            query = query.values(data)
            session.execute(query)
            session.commit()
            return Response(status_code=200)
    async def delete(
            self,
            id : int | None = None
        ) -> Response: 
        with Session(self.engine) as session:
            query = delete(ProductSchema)
            if (id != None):
                query = query.where(ProductSchema.id == id)
            session.execute(query)
            session.commit()
            return Response(status_code=200)
    async def get(
            self,
            id : int | None = None,
            mode : str = Literal['random'],
            offset : int = 0,
            limit : int = 50,
            name : str | None = None,
            category : str | None = None,
        ) -> Response:
        with Session(self.engine) as session:
            query = select(ProductSchema)
            if (id != None):
                query = query.where(ProductSchema.id == id)
            if (mode == 'random'):
                query = query.order_by(func.random())
            if (category != None):
                query = query.where(ProductSchema.category == category)
            if (name != None):
                query = query.where(ProductSchema.name.like(f'%{name}%'))
            query = query.offset(offset).limit(limit)
            results = session.execute(query)
            response_results = []
            for result in results:
                response_results.append(result[0].model_dump())
            return Response(content=json.dumps(response_results),media_type='application/json',status_code=200)
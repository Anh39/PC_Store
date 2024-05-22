import json
from .base import BaseCRUD
from ..schema.product import ProductSchema
from ..schema.map import MapSchema
from sqlalchemy.orm import Session
from fastapi import Request,Response
from sqlalchemy import Engine,select,delete,update

class ProductCRUD(BaseCRUD):
    async def full_create(self,data : dict) ->Response:
        with Session(self.engine) as session:
            product = ProductSchema.model_validate(data)
            session.add(product)

            try:
                session.commit()
                session.refresh(product)
                infos = data.get('infos',{})
                for key in infos:
                    new_info = MapSchema()
                    new_info.key = key
                    new_info.value = infos[key]
                    new_info.product_id = product.id
                    session.add(new_info)
                session.commit()
                return Response(status_code=200,content=str(product.id))
            except:
                return Response(status_code=404)
    async def full_get(
            self,
            id : int | None = None
        ) -> Response:
        with Session(self.engine) as session:
            query = select(ProductSchema)
            if (id != None):
                query = query.where(ProductSchema.id == id)
            results = session.execute(query)
            response_results = []
            for result in results:
                product : ProductSchema = result[0]
                data = product.model_dump()
                infos = product.infos
                ratings = product.have_ratings
                data['ratings'] = []
                for rating in ratings:
                    data['ratings'].append(rating.model_dump())
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
            id : int | None = None
        ) -> Response:
        with Session(self.engine) as session:
            query = select(ProductSchema)
            if (id != None):
                query = query.where(ProductSchema.id == id)
            results = session.execute(query)
            response_results = []
            for result in results:
                response_results.append(result[0].model_dump())
            return Response(content=json.dumps(response_results),media_type='application/json',status_code=200)
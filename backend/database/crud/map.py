import json
from .base import BaseCRUD
from ..schema.map import MapSchema
from sqlalchemy.orm import Session
from fastapi import Request,Response
from sqlalchemy import Engine,select,delete,update

class MapCRUD(BaseCRUD):
    async def create(self,data : dict) -> Response:
        with Session(self.engine) as session:
            user = MapSchema.model_validate(data)
            session.add(user)
            session.commit()
            return Response(status_code=200)
    async def update(
            self,
            data : dict,
            product_id : int | None = None,
            key : str | None = None
        ) -> Response: 
        with Session(self.engine) as session:
            query = update(MapSchema)
            if (product_id != None):
                query = query.where(MapSchema.product_id == product_id)
            if (key != None):
                query = query.where(MapSchema.key == key)
            query = query.values(data)
            session.execute(query)
            session.commit()
            return Response(status_code=200)
    async def delete(
            self,
            product_id : int | None = None,
            key : str | None = None
        ) -> Response: 
        with Session(self.engine) as session:
            query = delete(MapSchema)
            if (product_id != None):
                query = query.where(MapSchema.product_id == product_id)
            if (key != None):
                query = query.where(MapSchema.key == key)
            session.execute(query)
            session.commit()
            return Response(status_code=200)
    async def get(
            self,
            product_id : int | None = None,
            key : str | None = None
        ) -> Response:
        with Session(self.engine) as session:
            query = select(MapSchema)
            if (product_id != None):
                query = query.where(MapSchema.product_id == product_id)
            if (key != None):
                query = query.where(MapSchema.key == key)
            results = session.execute(query)
            response_results = []
            for result in results:
                response_results.append(result[0].model_dump())
            return Response(content=json.dumps(response_results),media_type='application/json',status_code=200)
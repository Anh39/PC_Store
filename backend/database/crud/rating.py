import json
from .base import BaseCRUD
from ..schema.rating import RatingSchema
from sqlalchemy.orm import Session
from datetime import datetime
from fastapi import Request,Response
from sqlalchemy import Engine,select,delete,update

class RatingCRUD(BaseCRUD):
    async def create(self,data : dict) -> Response:
        with Session(self.engine) as session:
            user = RatingSchema.model_validate(data)
            session.add(user)
            session.commit()
            return Response(status_code=200)
    async def update(
            self,
            data : dict,
            id : int | None = None
        ) -> Response: 
        with Session(self.engine) as session:
            query = update(RatingSchema)
            if (id != None):
                query = query.where(RatingSchema.id == id)
            query = query.values(data)
            session.execute(query)
            session.commit()
            return Response(status_code=200)
    async def delete(
            self,
            id : int | None = None,
            product_id : int | None = None
        ) -> Response: 
        with Session(self.engine) as session:
            query = delete(RatingSchema)
            if (id != None):
                query = query.where(RatingSchema.id == id)
            if (product_id != None):
                query = query.where(RatingSchema.product_id == product_id)
            session.execute(query)
            session.commit()
            return Response(status_code=200)
    async def get(
            self,
            id : int | None = None,
            product_id : int | None = None
        ) -> Response:
        with Session(self.engine) as session:
            query = select(RatingSchema)
            if (id != None):
                query = query.where(RatingSchema.id == id)
            if (product_id != None):
                query = query.where(RatingSchema.product_id == product_id)
            results = session.execute(query)
            response_results = []
            for result in results:
                response_results.append(result[0].model_dump())
            return Response(content=json.dumps(response_results),media_type='application/json',status_code=200)
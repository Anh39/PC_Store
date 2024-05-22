
import json
from .base import BaseCRUD
from ..schema.cart import CartSchema
from sqlalchemy.orm import Session
from fastapi import Request,Response
from sqlalchemy import Engine,select,delete,update

class CartCRUD(BaseCRUD):
    async def create(self,data : dict) -> Response:
        with Session(self.engine) as session:
            user = CartSchema.model_validate(data)
            session.add(user)
            session.commit()
            return Response(status_code=200)
    async def update(
            self,
            data : dict,
            user_id : int | None = None
        ) -> Response: 
        with Session(self.engine) as session:
            query = update(CartSchema)
            if (user_id != None):
                query = query.where(CartSchema.id == user_id)
            query = query.values(data)
            session.execute(query)
            session.commit()
            return Response(status_code=200)
    async def delete(
            self,
            user_id : int | None = None
        ) -> Response: 
        with Session(self.engine) as session:
            query = delete(CartSchema)
            if (user_id != None):
                query = query.where(CartSchema.id == user_id)
            session.execute(query)
            session.commit()
            return Response(status_code=200)
    async def get(
            self,
            user_id : int | None = None
        ) -> Response:
        with Session(self.engine) as session:
            query = select(CartSchema)
            if (user_id != None):
                query = query.where(CartSchema.id == user_id)
            results = session.execute(query)
            response_results = []
            for result in results:
                response_results.append(result[0].model_dump())
            return Response(content=json.dumps(response_results),media_type='application/json',status_code=200)
import json
from .base import BaseCRUD
from ..schema.order import OrderSchema
from sqlalchemy.orm import Session
from fastapi import Request,Response
from sqlalchemy import Engine,select,delete,update

class OrderCRUD(BaseCRUD):
    async def create(self,data : dict) -> Response:
        with Session(self.engine) as session:
            user = OrderSchema.model_validate(data)
            session.add(user)
            session.commit()
            return Response(status_code=200)
    async def update(
            self,
            data : dict,
            id : int | None = None,
            user_id : int | None = None
        ) -> Response: 
        with Session(self.engine) as session:
            query = update(OrderSchema)
            if (id != None):
                query = query.where(OrderSchema.id == id)
            if (user_id != None):
                query = query.where(OrderSchema.user_id == user_id)
            query = query.values(data)
            session.execute(query)
            session.commit()
            return Response(status_code=200)
    async def delete(
            self,
            id : int | None = None,
            user_id : int | None = None
        ) -> Response: 
        with Session(self.engine) as session:
            query = delete(OrderSchema)
            if (id != None):
                query = query.where(OrderSchema.id == id)
            if (user_id != None):
                query = query.where(OrderSchema.user_id == user_id)
            session.execute(query)
            session.commit()
            return Response(status_code=200)
    async def get(
            self,
            id : int | None = None,
            user_id : int | None = None
        ) -> Response:
        with Session(self.engine) as session:
            query = select(OrderSchema)
            if (id != None):
                query = query.where(OrderSchema.id == id)
            if (user_id != None):
                query = query.where(OrderSchema.user_id == user_id)
            results = session.execute(query)
            response_results = []
            for result in results:
                response_results.append(result[0].model_dump())
            return Response(content=json.dumps(response_results),media_type='application/json',status_code=200)
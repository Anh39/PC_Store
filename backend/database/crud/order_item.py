import json
from .base import BaseCRUD
from ..schema.order_item import OrderItemSchema
from sqlalchemy.orm import Session
from fastapi import Request,Response
from sqlalchemy import Engine,select,delete,update

class OrderItemCRUD(BaseCRUD):
    async def create(self,data : dict) -> Response:
        with Session(self.engine) as session:
            user = OrderItemSchema.model_validate(data)
            session.add(user)
            session.commit()
            return Response(status_code=200)
    async def update(
            self,
            data : dict,
            order_id : int | None = None,
            product_id : int | None = None
        ) -> Response: 
        with Session(self.engine) as session:
            query = update(OrderItemSchema)
            if (order_id != None):
                query = query.where(OrderItemSchema.product_id == product_id)
            if (product_id != None):
                query = query.where(OrderItemSchema.order_id == order_id)
            query = query.values(data)
            session.execute(query)
            session.commit()
            return Response(status_code=200)
    async def delete(
            self,
            order_id : int | None = None,
            product_id : int | None = None
        ) -> Response: 
        with Session(self.engine) as session:
            query = delete(OrderItemSchema)
            if (order_id != None):
                query = query.where(OrderItemSchema.product_id == product_id)
            if (product_id != None):
                query = query.where(OrderItemSchema.order_id == order_id)
            session.execute(query)
            session.commit()
            return Response(status_code=200)
    async def get(
            self,
            order_id : int | None = None,
            product_id : int | None = None
        ) -> Response:
        with Session(self.engine) as session:
            query = select(OrderItemSchema)
            if (order_id != None):
                query = query.where(OrderItemSchema.product_id == product_id)
            if (product_id != None):
                query = query.where(OrderItemSchema.order_id == order_id)
            results = session.execute(query)
            response_results = []
            for result in results:
                response_results.append(result[0].model_dump())
            return Response(content=json.dumps(response_results),media_type='application/json',status_code=200)
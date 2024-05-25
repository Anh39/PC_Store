import json,datetime
from .base import BaseCRUD
from ..schema.order import OrderSchema,UserSchema,OrderItemSchema
from ..schema.cart import CartSchema,CartItemSchema
from sqlalchemy.orm import Session
from fastapi import Request,Response
from sqlalchemy import Engine,select,delete,update

class OrderCRUD(BaseCRUD):
    async def create(self,data : dict) -> Response:
        with Session(self.engine) as session:
            token = data.get('token')
            data.pop('token')
            user = session.query(UserSchema).filter(UserSchema.token == token).first()
            
            cart : CartSchema = user.have_cart[0]
            item_datas = session.query(CartItemSchema).filter(CartItemSchema.cart_id == cart.user_id)
            if (item_datas.count() == 0):
                return Response(status_code=404)
            order = OrderSchema()
            order.address = user.address
            order.phone = user.phone
            order.time_created = datetime.datetime.now()
            order.status = 'Payed'
            order.user_id = user.id
            session.add(order)
            try:
                session.commit()
                for item_data in item_datas:
                    new_order_item = OrderItemSchema()
                    new_order_item.amount = item_data.amount
                    new_order_item.product_id = item_data.product_id
                    new_order_item.order_id = order.id
                    session.add(new_order_item)
                session.commit()
            except:
                session.delete(order)
                return Response(status_code=404)
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
            token : str = None
        ) -> Response:
        with Session(self.engine) as session:
            query = select(OrderSchema)
            if (id != None):
                query = query.where(OrderSchema.id == id)
            user = session.query(UserSchema).filter(UserSchema.token == token).first()
            if (user == None):
                return Response(status_code=404)
            if user.role != 'Admin':
                query = query.where(OrderSchema.user_id == user.id).order_by(OrderSchema.time_created)
            else:
                query = query.order_by(OrderSchema.time_created)
            results = session.execute(query)
            response_results = []
            for result in results:
                order : OrderSchema = result[0]
                data = order.model_dump()
                item_datas = order.items
                items = []
                for item_data in item_datas:
                    item = item_data.model_dump()
                    product = item_data.product
                    item = {
                        'amount' : item['amount']
                    }
                    item.update(product.model_dump())
                    items.append(item)
                data['items'] = items
                response_results.append(data)
            return Response(content=json.dumps(response_results),media_type='application/json',status_code=200)
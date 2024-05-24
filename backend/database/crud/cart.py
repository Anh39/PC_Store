
import json
from .base import BaseCRUD
from ..schema.cart import CartSchema,CartItemSchema
from ..schema.user import UserSchema
from ..schema.product import ProductSchema
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
    async def modify_item(
            self,
            data : dict
        ) -> Response:
        with Session(self.engine) as session:
            token = data.get('token')
            product_id = data.get('id')
            command = data.get('command')
            if (token == None or command == None or id == None):
                return Response(status_code=402)
            user : UserSchema = session.query(UserSchema).filter(UserSchema.token == token).first()
            user_id = user.id
            cart : CartSchema = session.query(CartSchema).filter(CartSchema.user_id == user_id).first()
            cart_items_query = cart.items
            cart_items : list[CartItemSchema] = []
            for cart_item in cart_items_query:
                cart_items.append(cart_item)
            target_item : CartItemSchema = None
            for cart_item in cart_items:
                    if cart_item.product_id == product_id:
                        target_item = cart_item
                        break
            if (command == 'Add'):
                if (target_item != None):
                    return Response(status_code=404)
                new_cart_item = CartItemSchema()
                new_cart_item.amount = 1
                new_cart_item.cart_id = cart.user_id
                new_cart_item.product_id = product_id
                session.add(new_cart_item)
                session.commit()
            elif (command == 'Delete'):
                if (target_item != None):
                    session.delete(target_item)
                    session.commit()
                else:
                    return Response(status_code=404)
            elif (type(command) == int):
                if (target_item != None):
                    if (command > 0):
                        target_item.amount = command
                        session.commit()
                    else:
                        return Response(status_code=404)
                else:
                    return Response(status_code=404)
            else:
                return Response(status_code=404)
            
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
            token : str,
            info : bool = True
        ) -> Response:
        with Session(self.engine) as session:
            user : UserSchema = session.query(UserSchema).filter(UserSchema.token == token).first()
            cart : CartSchema = user.have_cart[0]
            item_datas = session.query(CartItemSchema).filter(CartItemSchema.cart_id == cart.user_id)
            items = []
            for item_data in item_datas:
                item = item_data.model_dump()
                item.pop('cart_id')
                product_data : ProductSchema = session.query(ProductSchema).filter(ProductSchema.id == item['product_id']).first()
                product = product_data.model_dump()
                item.update(product)
                items.append(item)
            response_results = {
                'items' : items
            }
            
            return Response(content=json.dumps(response_results),media_type='application/json',status_code=200)
import json
from sqlalchemy.orm import Session
from datetime import datetime,time,date
from .base import BaseCRUD
from ..schema.user import UserSchema,CartSchema
from fastapi import Request,Response
from sqlalchemy import Engine,select,delete,update

class UserCRUD(BaseCRUD):
    async def create(self,data : dict) -> Response:
        with Session(self.engine) as session:
            user = UserSchema.model_validate(data)
            session.add(user)
            try:
                session.commit()
                new_cart = CartSchema()
                new_cart.user_id = user.id
                session.add(new_cart)
                print(new_cart)
                session.commit()
                return Response(status_code=200)
            except:
                return Response(status_code=404)
    async def update(
            self,
            data : dict,
            token : str | None = None,
            password : str | None = None
        ) : 
        with Session(self.engine) as session:
            query = update(UserSchema)
            if (password != None):
                query = query.where(UserSchema.password == password)
            if (token != None):
                query = query.where(UserSchema.token == token)
            query = query.values(data)
            result = session.execute(query)
            session.commit()
            if (result.rowcount > 0):
                return Response(status_code=200)
            else:
                return Response(status_code=404)
    async def delete(
            self,
            token : str | None = None,
            id : str | None = None
        ) : 
        with Session(self.engine) as session:
            query = delete(UserSchema)
            if (id != None):
                query = query.where(UserSchema.id == id)
            if (token != None):
                query = query.where(UserSchema.token == token)
            result = session.execute(query)
            session.commit()
            if (result.rowcount > 0):
                return Response(status_code=200)
            else:
                return Response(status_code=404)
    async def get(
            self,
            id : str | None = None,
            token : str | None = None,
            email : str | None = None,
            name : str | None = None,
            password : str | None = None
        ) -> Response:
        with Session(self.engine) as session:
            query = select(UserSchema)
            if (id != None):
                query = query.where(UserSchema.id == id)
            if (token != None):
                query = query.where(UserSchema.token == token)
            if (email != None):
                query = query.where(UserSchema.email == email)
            if (name != None):
                query = query.where(UserSchema.name == name)
            if (password != None):
                query = query.where(UserSchema.password == password) 
            results = session.execute(query)
            response_results = []
            for result in results:
                response_results.append(result[0].model_dump())
            return Response(content=json.dumps(response_results),media_type='application/json',status_code=200)
   
    async def get_order(
            self,
            token : str | None = None
        ) -> Response:
        with Session(self.engine) as session:
            query = select(UserSchema)
            if (token != None):
                query = query.where(UserSchema.token == token)
            results = session.execute(query)
            response_results = []
            for result in results:
                carts = result[0].have_orders
                for cart in carts:
                    response_results.append(cart.model_validate())
                break
            return Response(content=json.dumps(response_results),media_type='application/json',status_code=200)
        
    async def get_voucher(
            self,
            token : str | None = None
        ) -> Response:
        with Session(self.engine) as session:
            query = select(UserSchema)
            if (token != None):
                query = query.where(UserSchema.token == token)
            results = session.execute(query)
            response_results = []
            for result in results:
                vouchers = result[0].have_vouchers
                for voucher in vouchers:
                    response_results.append(voucher.model_validate())
                break
            return Response(content=json.dumps(response_results),media_type='application/json',status_code=200)
        
    async def get_rating(
            self,
            token : str | None = None
        ) -> Response:
        with Session(self.engine) as session:
            query = select(UserSchema)
            if (token != None):
                query = query.where(UserSchema.token == token)
            results = session.execute(query)
            response_results = []
            for result in results:
                ratings = result[0].have_orders
                for rating in ratings:
                    response_results.append(rating.model_validate())
                break
            return Response(content=json.dumps(response_results),media_type='application/json',status_code=200)
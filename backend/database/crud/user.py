import json
from sqlalchemy.orm import Session
from datetime import datetime,time,date
from backend.database.crud.base import BaseCRUD
from backend.database.schema.user import UserSchema
from fastapi import Request,Response
from sqlalchemy import Engine,select,delete,update

class UserCRUD(BaseCRUD):
    async def create_user(self,data : dict) -> Response:
        with Session(self.engine) as session:
            print(UserSchema.get_test().model_dump())
            user = UserSchema.model_validate(data)
            session.add(user)
            session.commit()
            return Response(status_code=200)
    async def update_user(
            self,
            data : dict,
            token : str | None = None,
            id : str | None = None
        ) : 
        with Session(self.engine) as session:
            query = update(UserSchema)
            if (id != None):
                query = query.where(UserSchema.id == id)
            if (token != None):
                query = query.where(UserSchema.token == token)
            values = list(data.items())
            data = {'name' : 'abcde'}
            query = query.values(name='abcdef',id=5)
            session.execute(query)
            # result = None
            # for result in results:
            #     result = result[0]
            #     break
            # result.model_change(data)
            session.commit()
            return Response(status_code=200)
    async def delete_user(
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
            session.execute(query)
            session.commit()
            return Response(status_code=200)
    async def get_user(
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
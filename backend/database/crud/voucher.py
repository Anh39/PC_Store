import json
from .base import BaseCRUD
from ..schema.voucher import VoucherSchema
from sqlalchemy.orm import Session
from datetime import datetime
from fastapi import Request,Response
from sqlalchemy import Engine,select,delete,update

class VoucherCRUD(BaseCRUD):
    async def create(self,data : dict) -> Response:
        with Session(self.engine) as session:
            user = VoucherSchema.model_validate(data)
            session.add(user)
            session.commit()
            return Response(status_code=200)
    async def update(
            self,
            data : dict,
            id : int | None = None
        ) -> Response: 
        with Session(self.engine) as session:
            query = update(VoucherSchema)
            if (id != None):
                query = query.where(VoucherSchema.id == id)
            if 'time_received' in data:
                data['time_received'] = datetime.strptime(data['time_received'],'%Y-%m-%d %H:$M:%S')
            if 'time_expire' in data:
                data['time_expire'] = datetime.strptime(data['time_expire'],'%Y-%m-%d %H:$M:%S')
            query = query.values(data)
            session.execute(query)
            session.commit()
            return Response(status_code=200)
    async def delete(
            self,
            id : int | None = None
        ) -> Response: 
        with Session(self.engine) as session:
            query = delete(VoucherSchema)
            if (id != None):
                query = query.where(VoucherSchema.id == id)
            session.execute(query)
            session.commit()
            return Response(status_code=200)
    async def get(
            self,
            id : int | None = None,
            discount : float | None = None
        ) -> Response:
        with Session(self.engine) as session:
            query = select(VoucherSchema)
            if (id != None):
                query = query.where(VoucherSchema.id == id)
            if (discount != None):
                query = query.where(VoucherSchema.discount == discount)
            results = session.execute(query)
            response_results = []
            for result in results:
                response_results.append(result[0].model_dump())
            return Response(content=json.dumps(response_results),media_type='application/json',status_code=200)
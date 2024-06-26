from sqlalchemy.orm import DeclarativeBase
from abc import abstractmethod
import datetime

class BaseSupport:
    _black_list : list[str] = []

class BaseSchema(DeclarativeBase,BaseSupport):
    @classmethod
    def revert_date(cls,data : dict,key : str) -> dict:
        value = data.get(key,None)
        try:
            if (value != None):
                value = datetime.datetime.strftime(value,'%Y-%m-%d')
                data[key] = value
            return data
        except Exception as e:
            raise Exception('Time parsing exception')
    @classmethod
    def revert_datetime(cls,data : dict,key : str) -> dict:
        value = data.get(key,None)
        try:
            if (value != None):
                value = datetime.datetime.strftime(value,'%Y-%m-%d %H:%M:%S')
                data[key] = value
            return data
        except Exception as e:
            raise Exception('Time parsing exception')
    def convert_date(self,key : str):
        value = getattr(self,key,None)
        try:
            if (value != None):
                value = datetime.datetime.strptime(value,'%Y-%m-%d')
                setattr(self,key,value)
        except Exception as e:
            raise Exception('Time parsing exception')
    def convert_datetime(self,key : str):
        value = getattr(self,key,None)
        try:
            if (value != None):
                value = datetime.datetime.strptime(value,'%Y-%m-%d %H:%M:%S')
                setattr(self,key,value)
        except Exception as e:
            raise Exception('Time parsing exception')
    def model_dump(self) -> dict[str,object]:
        result = {}
        cols = self.__class__.__table__.columns
        for col in cols:
            result[col.name] = getattr(self,col.name)
        return result
    @classmethod
    def _model_validate(cls,data : dict[str,object],schema : 'BaseSchema') -> 'BaseSchema':
        base = schema()
        cols = base.__class__.__table__.columns
        for col in cols:
            setattr(base,col.name,data.get(col.name))
        return base
    
    @classmethod
    @abstractmethod
    def model_validate(cls,data : dict[str,object]) -> 'BaseSchema':
        try:
            return cls._model_validate(data,BaseSchema)
        except Exception as e:
            raise Exception('Validation error')
    

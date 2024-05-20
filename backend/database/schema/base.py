from sqlalchemy.orm import DeclarativeBase
from abc import abstractmethod

class BaseSchema(DeclarativeBase):
    def model_dump(self) -> dict[str,object]:
        result = {}
        cols = self.__class__.__table__.columns
        for col in cols:
            result[col.name] = getattr(self,col.name)
        return result
    def _model_change(self,data : dict[str,object],schema : 'BaseSchema') -> 'BaseSchema':
        base = schema()
        for key in data:
            setattr(base,key,data.get(key))
        return base
    @abstractmethod
    def model_change(self,data : dict[str,object]) -> 'BaseSchema':
        return self._model_change(data,BaseSchema)
    @classmethod
    def _model_validate(cls,data : dict[str,object],schema : 'BaseSchema') -> 'BaseSchema':
        base = schema()
        for key in data:
            setattr(base,key,data.get(key))
        return base
    
    @classmethod
    @abstractmethod
    def model_validate(cls,data : dict[str,object]) -> 'BaseSchema':
        return cls._model_validate(data,BaseSchema)
    

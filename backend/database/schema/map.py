from .base import BaseSchema
from sqlalchemy import ForeignKey,Column,Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column,relationship
from datetime import datetime,date

class MapSchema(BaseSchema):
    __tablename__ = 'map'
    key : Mapped[str] = mapped_column(primary_key=True)
    value : Mapped[str] = mapped_column(nullable=True)
    
    product = relationship('ProductSchema',back_populates='infos')
    product_id = Column(Integer,ForeignKey('product.id'),primary_key=True)
    
    _blacklist = ['product']
    def model_dump(self) -> dict[str, object]:
        result = super().model_dump()
        return result
    @classmethod
    def model_validate(cls, data: dict[str, object]) -> BaseSchema:
        result = super()._model_validate(data,MapSchema)
        return result
    
from .product import ProductSchema
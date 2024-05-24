from .base import BaseSchema
from sqlalchemy import ForeignKey,Column,Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column,relationship
from datetime import datetime,date

class ProductImageSchema(BaseSchema):
    __tablename__ = 'product_image'
    path : Mapped[str] = mapped_column(nullable=True)
    
    order : Mapped[int] = mapped_column(primary_key=True)
    
    product = relationship('ProductSchema',back_populates='images')
    product_id = Column(Integer,ForeignKey('product.id'),primary_key=True)
    
    _blacklist = ['product']
    def model_dump(self) -> dict[str, object]:
        result = super().model_dump()
        return result
    @classmethod
    def model_validate(cls, data: dict[str, object]) -> BaseSchema:
        result = super()._model_validate(data,ProductImageSchema)
        return result
    
from .product import ProductSchema
from .base import BaseSchema
from sqlalchemy import ForeignKey,Column,Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column,relationship
from datetime import datetime,date
from .product_category import product_category_association

class CategorySchema(BaseSchema):
    __tablename__ = 'category'
    id : Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    value : Mapped[str] = mapped_column(nullable=True)
    
    in_products = relationship('ProductSchema',back_populates=None,secondary=product_category_association)
    
    _blacklist = ['in_products']
    def model_dump(self) -> dict[str, object]:
        result = super().model_dump()
        return result
    @classmethod
    def model_validate(cls, data: dict[str, object]) -> BaseSchema:
        result = super()._model_validate(data,CategorySchema)
        return result
    
from .product import ProductSchema

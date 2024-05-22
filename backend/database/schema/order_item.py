from .base import BaseSchema
from sqlalchemy import Column,ForeignKey,Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column,relationship

class OrderItemSchema(BaseSchema):
    __tablename__ = 'order_item'
    amount : Mapped[int]
    
    product_id = Column(Integer,ForeignKey('product.id'),primary_key=True)
    product = relationship('ProductSchema',back_populates=None)
    order_id = Column(Integer,ForeignKey('order.id'),primary_key=True)
    in_order = relationship('OrderSchema',back_populates='items')
    _blacklist = ['in_order','product']
    def model_dump(self) -> dict[str, object]:
        result = super().model_dump()
        return result
    @classmethod
    def model_validate(cls, data: dict[str, object]) -> BaseSchema:
        result = super()._model_validate(data,OrderItemSchema)
        return result
    
from .product import ProductSchema
from .order import OrderSchema

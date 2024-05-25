from .base import BaseSchema
from sqlalchemy import Column,ForeignKey,Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column,relationship

class CartItemSchema(BaseSchema):
    __tablename__ = 'cart_item'
    # id : Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    amount : Mapped[int]
    
    in_cart = relationship('CartSchema',back_populates='items')
    cart_id = Column(Integer,ForeignKey('cart.user_id'),primary_key=True)
    product = relationship('ProductSchema',back_populates=None)
    product_id = Column(Integer,ForeignKey('product.id'),primary_key=True)
    
    _blacklist = ['in_cart','product_id']
    def model_dump(self) -> dict[str, object]:
        result = super().model_dump()
        return result
    @classmethod
    def model_validate(cls, data: dict[str, object]) -> BaseSchema:
        result = super()._model_validate(data,CartItemSchema)
        return result
    
from .cart import CartSchema
from .product import ProductSchema
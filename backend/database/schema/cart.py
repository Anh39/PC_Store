from .base import BaseSchema
from sqlalchemy import Column,ForeignKey,Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column,relationship

class CartSchema(BaseSchema):
    __tablename__ = 'cart'
    user_id : Mapped[int] = Column(Integer,ForeignKey('user.id'),primary_key=True)
    owner = relationship('UserSchema',back_populates='have_cart')
    
    value : Mapped[float]
    
    items = relationship('CartItemSchema',back_populates='in_cart')
    _blacklist = ['owner']
    def model_dump(self) -> dict[str, object]:
        result = super().model_dump()
        return result
    @classmethod
    def model_validate(cls, data: dict[str, object]) -> BaseSchema:
        result = super()._model_validate(data,CartSchema)
        return result
    
from .user import UserSchema
from .cart_item import CartItemSchema
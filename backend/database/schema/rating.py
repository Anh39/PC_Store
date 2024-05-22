from .base import BaseSchema
from sqlalchemy import ForeignKey,Column,Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column,relationship

class RatingSchema(BaseSchema):
    __tablename__ = 'rating'
    id : Mapped[int] = mapped_column(autoincrement=True,primary_key=True)
    product_id = Column(Integer,ForeignKey('product.id'))
    value : Mapped[float]
    
    user_id = Column(Integer,ForeignKey('user.id'))
    owner = relationship('UserSchema',back_populates='have_ratings')
    rated_products = relationship('ProductSchema',back_populates='have_ratings')
    
    _blacklist = ['owner','product']
    @classmethod
    def get_test(cls) -> 'RatingSchema':
        rating = RatingSchema()
        rating.id = 1
        rating.product_id = 2
        rating.value = 3
        rating.user_id = 4
        return rating
    
    def model_dump(self) -> dict[str, object]:
        return super().model_dump()
    @classmethod
    def model_validate(cls, data: dict[str, object]) -> BaseSchema:
        return super()._model_validate(data,RatingSchema)
    
from .user import UserSchema
from .product import ProductSchema
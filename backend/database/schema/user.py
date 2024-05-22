from backend.database.schema.base import BaseSchema
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from datetime import datetime,time,date
from .user_voucher import user_voucher_association

class UserSchema(BaseSchema):
    __tablename__ = 'user'
    id : Mapped[int] = mapped_column(primary_key=True,unique=True,autoincrement=True)
    role : Mapped[str] = mapped_column(nullable=False,default='Customer')
    token : Mapped[str] = mapped_column(unique=True)
    email : Mapped[str] = mapped_column(unique=True)
    password : Mapped[str] = mapped_column(nullable=False)
    name : Mapped[str] = mapped_column(nullable=True)
    birthday : Mapped[date] = mapped_column(nullable=True)
    phone : Mapped[str] = mapped_column(nullable=True)
    gender : Mapped[str] = mapped_column(nullable=True)
    address : Mapped[str] = mapped_column(nullable=True)
    avatar : Mapped[str] = mapped_column(nullable=True)
    card : Mapped[str] = mapped_column(nullable=True)
    
    have_cart = relationship('CartSchema',back_populates='owner')
    have_orders = relationship('OrderSchema',back_populates='owner')
    have_ratings = relationship('RatingSchema',back_populates='owner')
    have_vouchers = relationship('VoucherSchema',back_populates='owners',secondary=user_voucher_association)
    have_posts = relationship('PostSchema',back_populates='owner')
    
    _black_list = ['have_cart','have_orders','have_ratings','have_vouchers','have_posts']
    def model_dump(self) -> dict[str, object]:
        result = super().model_dump()
        self.convert_date('birthday')
        return result
    @classmethod
    def model_validate(cls, data: dict[str, object]) -> 'UserSchema':
        result : UserSchema = cls._model_validate(data,UserSchema)
        result = cls.revert_date(result,'birthday')
        return result
    def model_change(self, data: dict[str, object]) -> 'UserSchema':
        return self._model_change(data,UserSchema)
    
from .post import PostSchema
from .voucher import VoucherSchema
from .rating import RatingSchema
from .order import OrderSchema
from .cart import CartSchema
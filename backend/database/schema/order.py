from .base import BaseSchema
from sqlalchemy import Column,ForeignKey,Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column,relationship
from datetime import datetime,date

class OrderSchema(BaseSchema):
    __tablename__ = 'order'
    id : Mapped[int] = mapped_column(autoincrement=True,primary_key=True)
    time_created : Mapped[datetime] = mapped_column(nullable=False)
    time_completed : Mapped[datetime] = mapped_column(nullable=True)
    address : Mapped[str] = mapped_column(nullable=True)
    phone : Mapped[str] = mapped_column(nullable=True)
    status : Mapped[str]
    
    user_id = Column(Integer,ForeignKey('user.id'))
    owner = relationship('UserSchema',back_populates='have_orders')
    items = relationship('OrderItemSchema',back_populates='in_order',cascade='all, delete-orphan')
    _blacklist = ['owner','items']
    def model_dump(self) -> dict[str, object]:
        result = super().model_dump()
        result = self.revert_datetime(result,'time_created')
        result = self.revert_datetime(result,'time_completed')
        return result
    @classmethod
    def model_validate(cls, data: dict[str, object]) -> BaseSchema:
        result = super()._model_validate(data,OrderSchema)
        result.convert_datetime('time_created')
        result.convert_datetime('time_completed')
        return result

from .user import UserSchema
from .order_item import OrderItemSchema
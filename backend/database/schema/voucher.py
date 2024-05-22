from .base import BaseSchema
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column,relationship
from datetime import datetime,date
from .user_voucher import user_voucher_association

class VoucherSchema(BaseSchema):
    __tablename__ = 'voucher'
    id : Mapped[int] = mapped_column(unique=True,autoincrement=True,primary_key=True)
    discount : Mapped[float] = mapped_column(nullable=False)
    received_time : Mapped[datetime]
    expire_time : Mapped[datetime]
    category_apply : Mapped[str]
    description : Mapped[str]
    
    owners = relationship('UserSchema',secondary=user_voucher_association,back_populates='have_voucher')
    _blacklist = []
    @classmethod
    def get_test(cls) -> 'VoucherSchema':
        voucher = VoucherSchema()
        voucher.id = 1
        voucher.received_time = datetime.now()
        voucher.expire_time = datetime.now()
        voucher.category_apply = 'dnkwa'
        voucher.description = 'dws'
        return voucher
    def model_dump(self) -> dict[str, object]:
        result = super().model_dump()
        result = self.convert_datetime(result,'received_time')
        result = self.convert_datetime(result,'expire_time')
        return result
    @classmethod
    def model_validate(cls, data: dict[str, object]) -> BaseSchema:
        result = super()._model_validate(data,VoucherSchema)
        result.revert_datetime('received_time')
        result.revert_datetime('expire_time')
        return result
    
from .user import UserSchema
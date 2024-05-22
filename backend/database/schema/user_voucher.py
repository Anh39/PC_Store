from .base import BaseSchema
from sqlalchemy import Table,Column,Integer,ForeignKey
from .base import BaseSchema

user_voucher_association =Table(
    'user_voucher_association',BaseSchema.metadata,
    Column('user_id',Integer,ForeignKey('user.id'),primary_key=True),
    Column('voucher_id',Integer,ForeignKey('voucher.id'),primary_key=True)
)
    
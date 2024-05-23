from .base import BaseSchema
from sqlalchemy import Table,Column,Integer,ForeignKey
from .base import BaseSchema

product_category_association =Table(
    'product_category_association',BaseSchema.metadata,
    Column('product_id',Integer,ForeignKey('product.id'),primary_key=True),
    Column('category_id',Integer,ForeignKey('category.id'),primary_key=True)
)
    
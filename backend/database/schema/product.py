from .base import BaseSchema
from sqlalchemy import ForeignKey,Column,Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column,relationship
from datetime import datetime,date
# from .product_category import product_category_association

class ProductSchema(BaseSchema):
    __tablename__ = 'product'
    id : Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    name : Mapped[str]
    price : Mapped[float]
    thumbnail : Mapped[str]
    category : Mapped[str]
    infos = relationship('MapSchema',back_populates='product',cascade='all, delete-orphan')
    images = relationship('ProductImageSchema',back_populates='product',cascade='all, delete-orphan')
    _blacklist = ['infos']
    
    # time_created : Mapped[datetime] 
    # time_modified : Mapped[datetime]
    def model_dump(self) -> dict[str, object]:
        result = super().model_dump()
        # result = self.revert_datetime(result,'time_created')
        # result = self.revert_datetime(result,'time_modified')
        return result
    @classmethod
    def model_validate(cls, data: dict[str, object]) -> BaseSchema:
        result = super()._model_validate(data,ProductSchema)
        # result.convert_datetime('time_created')
        # result.convert_datetime('time_modified')
        return result
    
from .map import MapSchema
from .product_image import ProductImageSchema

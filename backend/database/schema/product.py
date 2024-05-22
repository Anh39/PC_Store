from .base import BaseSchema
from sqlalchemy import ForeignKey,Column,Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column,relationship
from datetime import datetime,date

class ProductSchema(BaseSchema):
    __tablename__ = 'product'
    id : Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    name : Mapped[str]
    time_created : Mapped[datetime]
    time_modified : Mapped[datetime]
    price : Mapped[float]
    
    infos = relationship('MapSchema',back_populates='product')
    have_ratings = relationship('RatingSchema',back_populates='rated_product')
    _blacklist = ['infos','have_ratings']
    def model_dump(self) -> dict[str, object]:
        result = super().model_dump()
        result = self.revert_datetime(result,'time_created')
        result = self.revert_datetime(result,'time_modified')
        return result
    @classmethod
    def model_validate(cls, data: dict[str, object]) -> BaseSchema:
        result = super()._model_validate(data,ProductSchema)
        result.convert_datetime('time_created')
        result.convert_datetime('time_modified')
        return result
    
from .map import MapSchema
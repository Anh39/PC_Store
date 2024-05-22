from .base import BaseSchema
from sqlalchemy import ForeignKey,Column,Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column,relationship
from datetime import datetime,date

class PostSchema(BaseSchema):
    __tablename__ = 'post'
    id : Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    content : Mapped[str]
    time_created : Mapped[datetime]
    time_modified : Mapped[datetime]
    
    user_id = Column(Integer,ForeignKey('user.id'))
    owner = relationship('UserSchema',back_populates='have_posts')
    _blacklist = ['owner']
    def model_dump(self) -> dict[str, object]:
        result = super().model_dump()
        result = self.revert_datetime(result,'time_created')
        result = self.revert_datetime(result,'time_modified')
        return result
    @classmethod
    def model_validate(cls, data: dict[str, object]) -> BaseSchema:
        result = super()._model_validate(data,PostSchema)
        result.convert_datetime('time_created')
        result.convert_datetime('time_modified')
        return result
    
from .user import UserSchema
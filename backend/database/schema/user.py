from backend.database.schema.base import BaseSchema
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from datetime import datetime,time,date

class UserSchema(BaseSchema):
    __tablename__ = 'user'
    id : Mapped[int] = mapped_column(primary_key=True,unique=True,autoincrement=True)
    role : Mapped[str] = mapped_column(nullable=False)
    token : Mapped[str] = mapped_column(nullable=False,unique=True)
    email : Mapped[str] = mapped_column(nullable=False,unique=True)
    password : Mapped[str] = mapped_column(nullable=False)
    name : Mapped[str]
    birthday : Mapped[date]
    phone : Mapped[str]
    gender : Mapped[str]
    address : Mapped[str]
    avatar : Mapped[str]
    card : Mapped[str]
    @classmethod
    def get_test(cls) -> 'UserSchema':
        result = UserSchema()
        result.id = 1
        result.role = 'Customer'
        result.token = 'abcde'
        result.email = 'abcde@gmail.com'
        result.password = '12345'
        result.name = 'abc'
        return result
    def model_dump(self) -> dict[str, object]:
        result = super().model_dump()
        if ('birthday' in result and type(result['birthday']) == date):
            result['birthday'] = result['birthday'].strftime("%Y-%m-%d")
        return result
    @classmethod
    def model_validate(cls, data: dict[str, object]) -> 'UserSchema':
        result : UserSchema = cls._model_validate(data,UserSchema)
        if (type(result.birthday) != date):
            result.birthday = datetime.strptime(result.birthday,"%Y-%m-%d")
        return result
    def model_change(self, data: dict[str, object]) -> 'UserSchema':
        return self._model_change(data,UserSchema)    
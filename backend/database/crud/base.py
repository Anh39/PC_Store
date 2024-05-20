from sqlalchemy import Engine
from sqlalchemy.orm import Session

class BaseCRUD:
    def __init__(self,engine : Engine = None) -> None:
        self.engine : Engine = engine
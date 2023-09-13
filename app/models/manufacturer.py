from db.base import Base
from sqlalchemy import Column, Integer, String


class Manufacturer(Base):
    __tablename__ = "manufacturers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

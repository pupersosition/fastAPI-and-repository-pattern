from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, Float, DECIMAL, BigInteger, DateTime
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class Manufacturer(Base):
    __tablename__ = 'manufacturers'
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String, unique=True)
    cars = relationship("Car", back_populates="manufacturer")


class Car(Base):
    __tablename__ = 'cars'
    id: int = Column(BigInteger, primary_key=True, autoincrement=True)
    url: str = Column(String)
    price: float = Column(DECIMAL)
    year: int = Column(Integer)
    model: str = Column(String)
    condition: str = Column(String)
    cylinders: str = Column(String)
    fuel: str = Column(String)
    odometer: float = Column(DECIMAL)
    title_status: str = Column(String)
    transmission: str = Column(String)
    vin: str = Column(String)
    drive: str = Column(String)
    size: str = Column(String)
    type: str = Column(String)
    paint_color: str = Column(String)
    image_url: str = Column(String)
    description: str = Column(String)
    latitude: float = Column(Float)
    longitude: float = Column(Float)
    posting_date: datetime = Column(DateTime(timezone=True))
    manufacturer_id: int = Column(Integer, ForeignKey('manufacturers.id'))
    manufacturer = relationship("Manufacturer", back_populates="cars")

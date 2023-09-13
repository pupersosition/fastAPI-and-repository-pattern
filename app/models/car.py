from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, BIGINT
from sqlalchemy.sql.sqltypes import DECIMAL
from db.base import Base


class Car(Base):
    __tablename__ = "cars"

    id = Column(BIGINT, primary_key=True, index=True)
    url = Column(String, index=True)
    price = Column(DECIMAL)
    year = Column(Integer)
    manufacturer_id = Column(Integer, ForeignKey("manufacturers.id"))
    model = Column(String, index=True)
    condition = Column(String)
    cylinders = Column(String)
    fuel = Column(String)
    odometer = Column(DECIMAL)
    title_status = Column(String)
    transmission = Column(String)
    vin = Column(String, unique=True)
    drive = Column(String)
    size = Column(String)
    type = Column(String)
    paint_color = Column(String)
    image_url = Column(String)
    description = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    posting_date = Column(DateTime(timezone=True))

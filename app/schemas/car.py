from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class CarBase(BaseModel):
    url: Optional[str]
    price: Optional[float]
    year: Optional[int]
    manufacturer_id: Optional[int] = Field(None, example=32)
    model: Optional[str]
    condition: Optional[str]
    cylinders: Optional[str]
    fuel: Optional[str]
    odometer: Optional[float]
    title_status: Optional[str]
    transmission: Optional[str]
    vin: Optional[str]
    drive: Optional[str]
    size: Optional[str]
    type: Optional[str]
    paint_color: Optional[str]
    image_url: Optional[str]
    description: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]
    posting_date: Optional[datetime]


class CarCreate(CarBase):
    pass


class CarUpdate(BaseModel):
    url: Optional[str] = None
    price: Optional[float] = None
    year: Optional[int] = None
    manufacturer_id: Optional[int] = None
    model: Optional[str] = None
    condition: Optional[str] = None
    cylinders: Optional[str] = None
    fuel: Optional[str] = None
    odometer: Optional[float] = None
    title_status: Optional[str] = None
    transmission: Optional[str] = None
    vin: Optional[str] = None
    drive: Optional[str] = None
    size: Optional[str] = None
    type: Optional[str] = None
    paint_color: Optional[str] = None
    image_url: Optional[str] = None
    description: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    posting_date: Optional[datetime] = None


class Car(CarBase):
    id: int

    class Config:
        orm_mode = True

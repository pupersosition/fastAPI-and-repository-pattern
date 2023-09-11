from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class CarBase(BaseModel):
    url: Optional[str]
    price: Optional[float]
    year: Optional[int]
    manufacturer_id: Optional[int]
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
    url: Optional[str]
    price: Optional[float]
    year: Optional[int]
    manufacturer_id: Optional[int]
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

class Car(CarBase):
    id: int

    class Config:
        orm_mode = True

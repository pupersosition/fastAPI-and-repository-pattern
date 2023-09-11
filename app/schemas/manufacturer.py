from pydantic import BaseModel
from typing import Optional

class ManufacturerBase(BaseModel):
    name: str

class ManufacturerCreate(ManufacturerBase):
    pass

class Manufacturer(ManufacturerBase):
    id: int

    class Config:
        orm_mode = True

class ManufacturerUpdate(BaseModel):
    name: Optional[str]
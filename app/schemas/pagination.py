from typing import List

from pydantic import BaseModel
from schemas.car import Car
from schemas.manufacturer import Manufacturer


class Pagination(BaseModel):
    total: int
    skip: int
    limit: int


class CarPagination(Pagination):
    items: List[Car]


class ManufacturerPagination(Pagination):
    items: List[Manufacturer]

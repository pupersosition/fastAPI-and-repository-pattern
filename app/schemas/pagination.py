from typing import List

from pydantic import BaseModel
from schemas.car import Car


class Pagination(BaseModel):
    total: int
    skip: int
    limit: int


class CarPagination(Pagination):
    items: List[Car]

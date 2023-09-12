from abc import ABC, abstractmethod
from typing import List, Optional
from schemas.car import CarCreate, CarUpdate
from models.car import Car as CarModel
from schemas.manufacturer import ManufacturerCreate, ManufacturerUpdate
from models.manufacturer import Manufacturer as ManufacturerModel

class AbstractCarRepository(ABC):

    @abstractmethod
    async def create(self, car: CarCreate) -> CarModel:
        pass

    @abstractmethod
    async def get_by_id(self, car_id: int) -> Optional[CarModel]:
        pass

    @abstractmethod
    async def get_all(self, skip: int = 0, limit: int = 10) -> List[CarModel]:
        pass

    @abstractmethod
    async def update(self, car_id: int, car: CarUpdate) -> CarModel:
        pass

    @abstractmethod
    async def delete(self, car_id: int) -> None:
        pass

class AbstractManufacturerRepository(ABC):

    @abstractmethod
    async def create(self, manufacturer: ManufacturerCreate) -> ManufacturerModel:
        pass

    @abstractmethod
    async def get_by_id(self, manufacturer_id: int) -> Optional[ManufacturerModel]:
        pass

    @abstractmethod
    async def get_all(self, skip: int = 0, limit: int = 10) -> List[ManufacturerModel]:
        pass

    @abstractmethod
    async def update(self, manufacturer_id: int, manufacturer: ManufacturerCreate) -> ManufacturerModel:
        pass

    @abstractmethod
    async def delete(self, manufacturer_id: int) -> None:
        pass
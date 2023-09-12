from sqlalchemy import delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from repositories.base import AbstractCarRepository
from schemas.car import CarCreate, CarUpdate
from models.car import Car as CarModel
from typing import Optional, List
from models.manufacturer import Manufacturer as ManufacturerModel
from schemas.manufacturer import ManufacturerCreate, ManufacturerUpdate
from repositories.base import AbstractManufacturerRepository


class SQLAlchemyCarRepository(AbstractCarRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, car: CarCreate) -> CarModel:
        db_car = CarModel(**car.dict())
        self.session.add(db_car)
        await self.session.commit()
        await self.session.refresh(db_car)
        return db_car

    async def get_by_id(self, car_id: int) -> Optional[CarModel]:
        result = await self.session.execute(select(CarModel).filter(CarModel.id == car_id))
        return result.scalars().first()

    async def get_all(self, skip: int = 0, limit: int = 10) -> List[CarModel]:
        result = await self.session.execute(select(CarModel).offset(skip).limit(limit))
        return result.scalars().all()

    async def update(self, car_id: int, car: CarUpdate) -> CarModel:
        await self.session.execute(
            update(CarModel)
            .where(CarModel.id == car_id)
            .values(**car.dict())
        )
        await self.session.commit()

        result = await self.session.execute(select(CarModel).filter(CarModel.id == car_id))
        return result.scalars().first()

    async def delete(self, car_id: int) -> None:
        await self.session.execute(delete(CarModel).where(CarModel.id == car_id))
        await self.session.commit()


class SQLAlchemyManufacturerRepository(AbstractManufacturerRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, manufacturer: ManufacturerCreate) -> ManufacturerModel:
        db_manufacturer = ManufacturerModel(**manufacturer.dict())
        self.session.add(db_manufacturer)
        await self.session.commit()
        await self.session.refresh(db_manufacturer)
        return db_manufacturer

    async def get_by_id(self, manufacturer_id: int) -> Optional[ManufacturerModel]:
        result = await self.session.execute(select(ManufacturerModel).filter(ManufacturerModel.id == manufacturer_id))
        return result.scalars().first()

    async def get_all(self, skip: int = 0, limit: int = 10) -> List[ManufacturerModel]:
        result = await self.session.execute(select(ManufacturerModel).offset(skip).limit(limit))
        return result.scalars().all()

    async def update(self, manufacturer_id: int, manufacturer: ManufacturerUpdate) -> ManufacturerModel:
        await self.session.execute(
            update(ManufacturerModel)
            .where(ManufacturerModel.id == manufacturer_id)
            .values(**manufacturer.dict())
        )
        await self.session.commit()

        result = await self.session.execute(select(ManufacturerModel).filter(ManufacturerModel.id == manufacturer_id))
        return result.scalars().first()

    async def delete(self, manufacturer_id: int) -> None:
        await self.session.execute(delete(ManufacturerModel).where(ManufacturerModel.id == manufacturer_id))
        await self.session.commit()
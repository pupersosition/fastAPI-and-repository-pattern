from typing import Optional, List

from core.errors import NotFoundError, CreateError, UpdateError, DeleteError
from core.logging import logger
from models.car import Car as CarModel
from models.manufacturer import Manufacturer as ManufacturerModel
from repositories.base import AbstractCarRepository, AbstractManufacturerRepository
from schemas.car import CarCreate, CarUpdate
from schemas.manufacturer import ManufacturerCreate, ManufacturerUpdate
from sqlalchemy import delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


class SQLAlchemyCarRepository(AbstractCarRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, car: CarCreate) -> CarModel:
        try:
            db_car = CarModel(**car.dict())
            self.session.add(db_car)
            await self.session.commit()
            await self.session.refresh(db_car)
            return db_car
        except Exception as e:
            logger.error(f"Error creating car: {e}")
            raise CreateError(f"Error creating car: {str(e)}")

    async def get_by_id(self, car_id: int) -> Optional[CarModel]:
        result = await self.session.execute(select(CarModel).filter(CarModel.id == car_id))
        car = result.scalars().first()
        if car is None:
            raise NotFoundError(f"Car with id {car_id} not found.")
        return car

    async def get_all(self, skip: int = 0, limit: int = 10) -> List[CarModel]:
        result = await self.session.execute(select(CarModel).offset(skip).limit(limit))
        return result.scalars().all()

    async def update(self, car_id: int, car: CarUpdate) -> CarModel:
        try:
            await self.session.execute(
                update(CarModel)
                .where(CarModel.id == car_id)
                .values(**car.dict())
            )
            await self.session.commit()
            result = await self.session.execute(select(CarModel).filter(CarModel.id == car_id))
            updated_car = result.scalars().first()
            if updated_car is None:
                raise NotFoundError(f"Car with id {car_id} not found after update.")
            return updated_car
        except Exception as e:
            logger.error(f"Error updating car with id {car_id}: {e}")
            raise UpdateError(f"Error updating car with id {car_id}: {str(e)}")

    async def delete(self, car_id: int) -> None:
        try:
            await self.session.execute(delete(CarModel).where(CarModel.id == car_id))
            await self.session.commit()
        except Exception as e:
            logger.error(f"Error deleting car with id {car_id}: {e}")
            raise DeleteError(f"Error deleting car with id {car_id}: {str(e)}")


class SQLAlchemyManufacturerRepository(AbstractManufacturerRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, manufacturer: ManufacturerCreate) -> ManufacturerModel:
        try:
            db_manufacturer = ManufacturerModel(**manufacturer.dict())
            self.session.add(db_manufacturer)
            await self.session.commit()
            await self.session.refresh(db_manufacturer)
            return db_manufacturer
        except Exception as e:
            logger.error(f"Error creating manufacturer: {e}")
            raise CreateError(f"Error creating manufacturer: {str(e)}")

    async def get_by_id(self, manufacturer_id: int) -> Optional[ManufacturerModel]:
        result = await self.session.execute(select(ManufacturerModel).filter(ManufacturerModel.id == manufacturer_id))
        manufacturer = result.scalars().first()
        if manufacturer is None:
            raise NotFoundError(f"Manufacturer with id {manufacturer_id} not found.")
        return manufacturer

    async def get_all(self, skip: int = 0, limit: int = 10) -> List[ManufacturerModel]:
        result = await self.session.execute(select(ManufacturerModel).offset(skip).limit(limit))
        return result.scalars().all()

    async def update(self, manufacturer_id: int, manufacturer: ManufacturerUpdate) -> ManufacturerModel:
        try:
            await self.session.execute(
                update(ManufacturerModel)
                .where(ManufacturerModel.id == manufacturer_id)
                .values(**manufacturer.dict())
            )
            await self.session.commit()
            result = await self.session.execute(
                select(ManufacturerModel).filter(ManufacturerModel.id == manufacturer_id))
            updated_manufacturer = result.scalars().first()
            if updated_manufacturer is None:
                raise NotFoundError(f"Manufacturer with id {manufacturer_id} not found after update.")
            return updated_manufacturer
        except Exception as e:
            logger.error(f"Error updating manufacturer with id {manufacturer_id}: {e}")
            raise UpdateError(f"Error updating manufacturer with id {manufacturer_id}: {str(e)}")

    async def delete(self, manufacturer_id: int) -> None:
        try:
            await self.session.execute(delete(ManufacturerModel).where(ManufacturerModel.id == manufacturer_id))
            await self.session.commit()
        except Exception as e:
            logger.error(f"Error deleting manufacturer with id {manufacturer_id}: {e}")
            raise DeleteError(f"Error deleting manufacturer with id {manufacturer_id}: {str(e)}")

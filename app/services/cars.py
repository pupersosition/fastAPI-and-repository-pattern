from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.car import Car as CarModel
from schemas.car import CarCreate, CarUpdate

async def create_car(db: AsyncSession, car: CarCreate):
    db_car = CarModel(**car.dict())
    db.add(db_car)
    await db.commit()
    await db.refresh(db_car)
    return db_car

async def get_car_by_id(db: AsyncSession, car_id: int):
    result = await db.execute(select(CarModel).filter(CarModel.id == car_id))
    return result.scalars().first()

async def get_all_cars(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(CarModel).offset(skip).limit(limit))
    return result.scalars().all()

async def update_car(db: AsyncSession, car_id: int, car: CarUpdate):
    await db.execute(
        update(CarModel)
        .where(CarModel.id == car_id)
        .values(**car.dict())
    )
    await db.commit()

    result = await db.execute(select(CarModel).filter(CarModel.id == car_id))
    return result.scalars().first()

async def delete_car(db: AsyncSession, car_id: int):
    await db.execute(delete(CarModel).where(CarModel.id == car_id))
    await db.commit()

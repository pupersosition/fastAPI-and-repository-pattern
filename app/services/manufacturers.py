from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import update, delete
from sqlalchemy.future import select
from models.manufacturer import Manufacturer as ManufacturerModel
from schemas.manufacturer import ManufacturerCreate, ManufacturerUpdate


async def create_manufacturer(db: AsyncSession, manufacturer: ManufacturerCreate):
    db_manufacturer = ManufacturerModel(**manufacturer.dict())
    db.add(db_manufacturer)
    await db.commit()
    await db.refresh(db_manufacturer)
    return db_manufacturer


async def get_manufacturer_by_id(db: AsyncSession, manufacturer_id: int):
    result = await db.execute(select(ManufacturerModel).filter(ManufacturerModel.id == manufacturer_id))
    return result.scalars().first()


async def get_all_manufacturers(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(ManufacturerModel).offset(skip).limit(limit))
    return result.scalars().all()


async def update_manufacturer(db: AsyncSession, manufacturer_id: int, manufacturer: ManufacturerUpdate):
    await db.execute(
        update(ManufacturerModel)
        .where(ManufacturerModel.id == manufacturer_id)
        .values(**manufacturer.dict())
    )
    await db.commit()

    result = await db.execute(select(ManufacturerModel).filter(ManufacturerModel.id == manufacturer_id))
    return result.scalars().first()


async def delete_manufacturer(db: AsyncSession, manufacturer_id: int):
    await db.execute(delete(ManufacturerModel).where(ManufacturerModel.id == manufacturer_id))
    await db.commit()

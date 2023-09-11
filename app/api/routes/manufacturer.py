from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.manufacturer import ManufacturerCreate, ManufacturerUpdate, Manufacturer
from services.manufacturers import (
    create_manufacturer,
    get_manufacturer_by_id,
    get_all_manufacturers,
    update_manufacturer,
    delete_manufacturer
)

from db.session import get_db

router = APIRouter()


@router.post("/", response_model=Manufacturer)
async def create_manufacturer_endpoint(manufacturer: ManufacturerCreate, db: AsyncSession = Depends(get_db)):
    return await create_manufacturer(db, manufacturer)


@router.get("/{manufacturer_id}", response_model=Manufacturer)
async def read_manufacturer(manufacturer_id: int, db: AsyncSession = Depends(get_db)):
    db_manufacturer = await get_manufacturer_by_id(db, manufacturer_id)
    if db_manufacturer is None:
        raise HTTPException(status_code=404, detail="Manufacturer not found")
    return db_manufacturer


@router.get("/", response_model=list[Manufacturer])
async def list_manufacturers(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    return await get_all_manufacturers(db, skip=skip, limit=limit)


@router.put("/{manufacturer_id}", response_model=Manufacturer)
async def update_manufacturer_endpoint(manufacturer_id: int, manufacturer: ManufacturerUpdate,
                                       db: AsyncSession = Depends(get_db)):
    return await update_manufacturer(db, manufacturer_id, manufacturer)


@router.delete("/{manufacturer_id}", response_model=Manufacturer)
async def delete_manufacturer_endpoint(manufacturer_id: int, db: AsyncSession = Depends(get_db)):
    return await delete_manufacturer(db, manufacturer_id)

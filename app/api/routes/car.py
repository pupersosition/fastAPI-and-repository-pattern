from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.car import CarCreate, CarUpdate, Car
from services.cars import (
    create_car,
    get_car_by_id,
    get_all_cars,
    update_car,
    delete_car
)

from db.session import get_db

router = APIRouter()

@router.post("/", response_model=Car)
async def create_car_endpoint(car: CarCreate, db: AsyncSession = Depends(get_db)):
    return await create_car(db, car)

@router.get("/{car_id}", response_model=Car)
async def read_car(car_id: int, db: AsyncSession = Depends(get_db)):
    db_car = await get_car_by_id(db, car_id)
    if db_car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return db_car

@router.get("/", response_model=list[Car])
async def list_cars(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    return await get_all_cars(db, skip=skip, limit=limit)

@router.put("/{car_id}", response_model=Car)
async def update_car_endpoint(car_id: int, car: CarUpdate, db: AsyncSession = Depends(get_db)):
    return await update_car(db, car_id, car)

@router.delete("/{car_id}", response_model=Car)
async def delete_car_endpoint(car_id: int, db: AsyncSession = Depends(get_db)):
    return await delete_car(db, car_id)

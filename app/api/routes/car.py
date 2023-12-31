from core.rate_limit import limiter
from db.session import get_db
from fastapi import APIRouter, Depends, Response, Request
from repositories.base import AbstractCarRepository
from repositories.sqlalchemy_repository import SQLAlchemyCarRepository
from schemas.car import CarCreate, CarUpdate, Car
from schemas.pagination import CarPagination
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


def get_car_repo(db: AsyncSession = Depends(get_db)) -> AbstractCarRepository:
    return SQLAlchemyCarRepository(db)


@router.post("/", response_model=Car)
async def create_car_endpoint(car: CarCreate, car_repo: AbstractCarRepository = Depends(get_car_repo)):
    return await car_repo.create(car)

@router.get("/{car_id}", response_model=Car)
@limiter.limit("5/minute")
async def read_car(request: Request, car_id: int, car_repo: AbstractCarRepository = Depends(get_car_repo)):
    return await car_repo.get_by_id(car_id)


@router.get("/", response_model=CarPagination)
async def list_cars(skip: int = 0, limit: int = 10, car_repo: AbstractCarRepository = Depends(get_car_repo)):
    return await car_repo.get_all(skip=skip, limit=limit)


@router.patch("/{car_id}", response_model=Car)
async def update_car_endpoint(car_id: int, car: CarUpdate, car_repo: AbstractCarRepository = Depends(get_car_repo)):
    return await car_repo.update(car_id, car)


@router.delete("/{car_id}", status_code=204)
async def delete_car_endpoint(car_id: int, car_repo: AbstractCarRepository = Depends(get_car_repo)):
    await car_repo.delete(car_id)
    return Response(status_code=204)

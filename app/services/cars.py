from repositories.base import AbstractCarRepository
from schemas.car import CarCreate, CarUpdate

async def create_car(car_repo: AbstractCarRepository, car: CarCreate):
    return await car_repo.create(car)

async def get_car_by_id(car_repo: AbstractCarRepository, car_id: int):
    return await car_repo.get_by_id(car_id)

async def get_all_cars(car_repo: AbstractCarRepository, skip: int = 0, limit: int = 10):
    return await car_repo.get_all(skip, limit)

async def update_car(car_repo: AbstractCarRepository, car_id: int, car: CarUpdate):
    return await car_repo.update(car_id, car)

async def delete_car(car_repo: AbstractCarRepository, car_id: int):
    await car_repo.delete(car_id)

from repositories.base import AbstractManufacturerRepository
from schemas.manufacturer import ManufacturerCreate, ManufacturerUpdate

async def create_car(manufacturer_repo: AbstractManufacturerRepository, manufacturer: ManufacturerCreate):
    return await manufacturer_repo.create(manufacturer)

async def get_manufacturer_by_id(manufacturer_repo: AbstractManufacturerRepository, manufacturer_id: int):
    return await manufacturer_repo.get_by_id(manufacturer_id)

async def get_all_manufacturers(manufacturer_repo: AbstractManufacturerRepository, skip: int = 0, limit: int = 10):
    return await manufacturer_repo.get_all(skip, limit)

async def update_manufacturer(manufacturer_repo: AbstractManufacturerRepository, manufacturer_id: int, manufacturer: ManufacturerUpdate):
    return await manufacturer_repo.update(manufacturer_id, manufacturer)

async def delete_manufacturer(manufacturer_repo: AbstractManufacturerRepository, manufacturer_id: int):
    await manufacturer_repo.delete(manufacturer_id)

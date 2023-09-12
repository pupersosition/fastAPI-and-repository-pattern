from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.manufacturer import ManufacturerCreate, ManufacturerUpdate, Manufacturer
from repositories.sqlalchemy_repository import SQLAlchemyManufacturerRepository
from repositories.base import AbstractManufacturerRepository
from db.session import get_db

router = APIRouter()


def get_manufacturer_repo(db: AsyncSession = Depends(get_db)) -> AbstractManufacturerRepository:
    return SQLAlchemyManufacturerRepository(db)


@router.post("/", response_model=Manufacturer)
async def create_manufacturer_endpoint(manufacturer: ManufacturerCreate,
                                       manufacturer_repo: AbstractManufacturerRepository = Depends(
                                           get_manufacturer_repo)):
    return await manufacturer_repo.create(manufacturer)


@router.get("/{manufacturer_id}", response_model=Manufacturer)
async def read_manufacturer(manufacturer_id: int,
                            manufacturer_repo: AbstractManufacturerRepository = Depends(get_manufacturer_repo)):
    return await manufacturer_repo.get_by_id(manufacturer_id)


@router.get("/", response_model=list[Manufacturer])
async def list_manufacturers(skip: int = 0, limit: int = 10,
                             manufacturer_repo: AbstractManufacturerRepository = Depends(get_manufacturer_repo)):
    return await manufacturer_repo.get_all(skip=skip, limit=limit)


@router.put("/{manufacturer_id}", response_model=Manufacturer)
async def update_manufacturer_endpoint(manufacturer_id: int, manufacturer: ManufacturerUpdate,
                                       manufacturer_repo: AbstractManufacturerRepository = Depends(
                                           get_manufacturer_repo)):
    return await manufacturer_repo.update(manufacturer_id, manufacturer)


@router.delete("/{manufacturer_id}", response_model=Manufacturer)
async def delete_manufacturer_endpoint(manufacturer_id: int,
                                       manufacturer_repo: AbstractManufacturerRepository = Depends(
                                           get_manufacturer_repo)):
    await manufacturer_repo.delete(manufacturer_id)

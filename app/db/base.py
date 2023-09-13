import os

from loguru import logger
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_HOST: str = os.environ['DB_HOST']
DB_NAME: str = os.environ['DB_NAME']
DB_USER: str = os.environ['DB_USER']
DB_PASS: str = os.environ['POSTGRES_PASSWORD']
DATABASE_URL: str = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"

try:
    engine = create_async_engine(DATABASE_URL, echo=True)
    logger.info("Database engine created successfully")
except Exception as e:
    logger.error(f"Error creating database engine: {e}")
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()

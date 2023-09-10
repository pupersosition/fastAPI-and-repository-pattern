from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, DECIMAL, UniqueConstraint, and_, BigInteger
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from sqlalchemy.exc import OperationalError
from sqlalchemy.dialects.postgresql import insert
import pandas as pd
import os
import time
from contextlib import contextmanager
from copy import deepcopy

# Configuration
DB_HOST = os.environ['DB_HOST']
DB_NAME = os.environ['DB_NAME']
DB_USER = os.environ['DB_USER']
DB_PASS = os.environ['POSTGRES_PASSWORD']
CSV_PATH = os.environ['CSV_PATH']
BUFFER_SIZE = 5000
MAX_ATTEMPTS = 5
SLEEP_INTERVAL = 5  # in seconds

Base = declarative_base()

class Manufacturer(Base):
    __tablename__ = 'manufacturers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)
    cars = relationship("Car", back_populates="manufacturer")

class Car(Base):
    __tablename__ = 'cars'
    id = Column(BigInteger, primary_key=True)
    url = Column(String)
    price = Column(DECIMAL)
    year = Column(Integer)
    model = Column(String)
    condition = Column(String)
    cylinders = Column(String)
    fuel = Column(String)
    odometer = Column(DECIMAL)
    title_status = Column(String)
    transmission = Column(String)
    vin = Column(String)
    drive = Column(String)
    size = Column(String)
    type = Column(String)
    paint_color = Column(String)
    image_url = Column(String)
    description = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    manufacturer_id = Column(Integer, ForeignKey('manufacturers.id'))
    manufacturer = relationship("Manufacturer", back_populates="cars")

def create_session():
    for attempt in range(MAX_ATTEMPTS):
        try:
            engine = create_engine(f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}')
            Session = sessionmaker(bind=engine)
            return Session()
        except OperationalError:
            time.sleep(SLEEP_INTERVAL)
    raise Exception(f"Failed to connect to the database after {MAX_ATTEMPTS} attempts.")

@contextmanager
def session_scope():
    session = create_session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

def bulk_insert_avoid_conflicts(session, table, data):
    if not data:
        return
    insert_stmt = insert(table).values(data)
    on_conflict_stmt = insert_stmt.on_conflict_do_nothing()
    session.execute(on_conflict_stmt)

def clean_data(record):
    """Replace all 'nan' values with None for database compatibility."""
    return {k: None if pd.isna(v) else v for k, v in record.items()}

# Processing manufacturers
unique_manufacturers = pd.read_csv(CSV_PATH, usecols=['manufacturer'])['manufacturer'].dropna().unique().tolist()
with session_scope() as session:
    bulk_insert_avoid_conflicts(session, Manufacturer.__table__, [{"name": manufacturer} for manufacturer in unique_manufacturers])

# Processing cars
all_car_mappings = []
chunk_iter = pd.read_csv(CSV_PATH, chunksize=BUFFER_SIZE)
for chunk in chunk_iter:
    car_objects = []

    with session_scope() as session:
        manufacturer_map = {manufacturer.name: manufacturer.id for manufacturer in session.query(Manufacturer).all()}
        for _, row in chunk.iterrows():
            car_mapping = {
                'id': row['id'],
                'url': row['url'],
                'price': row['price'],
                'year': row['year'],
                'model': row['model'],
                'condition': row['condition'],
                'cylinders': row['cylinders'],
                'fuel': row['fuel'],
                'odometer': row['odometer'],
                'title_status': row['title_status'],
                'transmission': row['transmission'],
                'vin': row['VIN'],
                'drive': row['drive'],
                'size': row['size'],
                'type': row['type'],
                'paint_color': row['paint_color'],
                'image_url': row['image_url'],
                'description': row['description'],
                'latitude': row['lat'],
                'longitude': row['long'],
                'manufacturer': row['manufacturer']
            }
            car_mapping = clean_data(car_mapping)
            if car_mapping.get('manufacturer') in manufacturer_map:
                car_mapping['manufacturer_id'] = manufacturer_map[car_mapping['manufacturer']]
            else:
                car_mapping['manufacturer_id'] = None
            if 'manufacturer' in car_mapping:
                del car_mapping['manufacturer']

            car = Car(**car_mapping)
            car_objects.append(car)

        session.bulk_save_objects(car_objects)

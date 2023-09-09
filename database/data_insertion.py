from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, UniqueConstraint, and_, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.exc import OperationalError
import pandas as pd
import os

# Configuration
print("Loading configurations...")
DB_HOST = os.environ['DB_HOST']
DB_NAME = os.environ['DB_NAME']
DB_USER = os.environ['DB_USER']
DB_PASS = os.environ['POSTGRES_PASSWORD']
CSV_PATH = os.environ['CSV_PATH']
MAX_ATTEMPTS = 5
SLEEP_INTERVAL = 5  # in seconds

Base = declarative_base()


class Manufacturer(Base):
    __tablename__ = 'manufacturers'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    cars = relationship("Car", back_populates="manufacturer")


class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    city_url = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    cars = relationship("Car", back_populates="city")
    __table_args__ = (UniqueConstraint('name', 'city_url', name='city_city_url_uc'),)


class Car(Base):
    __tablename__ = 'craigslist_cars'
    id = Column(Integer, primary_key=True)
    url = Column(String)
    price = Column(DECIMAL)
    year = Column(Integer)
    make = Column(String)
    condition = Column(String)
    cylinders = Column(String)
    fuel = Column(String)
    odometer = Column(DECIMAL)
    title_status = Column(String)
    transmission = Column(String)
    VIN = Column(String)
    drive = Column(String)
    size = Column(String)
    type = Column(String)
    paint_color = Column(String)
    image_url = Column(String)
    description = Column(String)
    manufacturer_id = Column(Integer, ForeignKey('manufacturers.id'))
    manufacturer = relationship("Manufacturer", back_populates="cars")
    city_id = Column(Integer, ForeignKey('cities.id'))
    city = relationship("City", back_populates="cars")


def create_session():
    print("Attempting to connect to the database...")
    for attempt in range(MAX_ATTEMPTS):
        try:
            engine = create_engine(f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}')
            Session = sessionmaker(bind=engine)
            print("Connected successfully!")
            return Session()
        except OperationalError:
            print(f"Attempt {attempt + 1} failed. Retrying in {SLEEP_INTERVAL} seconds...")
            time.sleep(SLEEP_INTERVAL)
    print(f"Failed to connect to the database after {MAX_ATTEMPTS} attempts.")
    exit(1)


session = create_session()

print(f"Loading data from {CSV_PATH}...")
df = pd.read_csv(CSV_PATH)

print("Populating the database...")
for index, row in df.iterrows():
    print(f"Processing row {index}...")
    manufacturer = session.query(Manufacturer).filter_by(name=row['manufacturer']).first()
    if not manufacturer:
        manufacturer = Manufacturer(name=row['manufacturer'])
        session.add(manufacturer)
        session.commit()

    city = session.query(City).filter(and_(City.name == row['city'], City.city_url == row['city_url'])).first()
    if not city:
        city = City(name=row['city'], city_url=row['city_url'], latitude=row['lat'], longitude=row['long'])
        session.add(city)
        session.commit()

    car = Car(
        url=row['url'],
        price=row['price'],
        year=row['year'],
        make=row['make'],
        condition=row['condition'],
        cylinders=row['cylinders'],
        fuel=row['fuel'],
        odometer=row['odometer'],
        title_status=row['title_status'],
        transmission=row['transmission'],
        VIN=row['VIN'],
        drive=row['drive'],
        size=row['size'],
        type=row['type'],
        paint_color=row['paint_color'],
        image_url=row['image_url'],
        description=row['desc'],
        manufacturer=manufacturer,
        city=city
    )
    session.add(car)
    session.commit()

print("Data has been successfully added to the database!")
session.close()

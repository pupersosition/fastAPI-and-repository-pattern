import pandas as pd
from typing import List, Dict, Any
import os

from utils import session_scope, bulk_insert_avoid_conflicts, clean_data
from models import Car, Manufacturer
from dateutil.parser import parse

# Configuration
DB_HOST: str = os.environ['DB_HOST']
DB_NAME: str = os.environ['DB_NAME']
DB_USER: str = os.environ['DB_USER']
DB_PASS: str = os.environ['POSTGRES_PASSWORD']
CSV_PATH: str = os.environ['CSV_PATH']
BUFFER_SIZE: int = 5000
MAX_ATTEMPTS: int = 5
SLEEP_INTERVAL: int = 5

if __name__ == '__main__':
    with session_scope(MAX_ATTEMPTS, SLEEP_INTERVAL, DB_USER, DB_PASS, DB_HOST, DB_NAME) as session:
        # Check if there are any records in Manufacturer or Car tables
        if not session.query(Manufacturer).first() and not session.query(Car).first():

            # Processing manufacturers
            unique_manufacturers: List[str] = pd.read_csv(CSV_PATH, usecols=['manufacturer'])[
                'manufacturer'].dropna().unique().tolist()

            bulk_insert_avoid_conflicts(session, Manufacturer.__table__,
                                        [{"name": manufacturer} for manufacturer in unique_manufacturers])

            # Processing cars
            all_car_mappings: List[Dict[str, Any]] = []
            chunk_iter: Any = pd.read_csv(CSV_PATH, chunksize=BUFFER_SIZE)
            for chunk in chunk_iter:
                car_objects: List[Car] = []

                manufacturer_map: Dict[str, int] = {manufacturer.name: manufacturer.id for manufacturer in
                                                    session.query(Manufacturer).all()}
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
                        'posting_date': None if str(row['posting_date']) == 'nan' else parse(str(row['posting_date'])),
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
        else:
            print("The database is already populated.")

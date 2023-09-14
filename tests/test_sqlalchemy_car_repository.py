from datetime import datetime

import pytest
from fastapi.testclient import TestClient
from models.car import Car as CarModel

from app.main import app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def example_car_data():
    return {
        "url": "http://test.car",
        "price": 10000.0,
        "year": 2022,
        "manufacturer_id": 1,
        "model": "ModelX",
        "condition": "new",
        "cylinders": "4",
        "fuel": "gas",
        "odometer": 5000.0,
        "title_status": "clean",
        "transmission": "automatic",
        "vin": "1HGCM82633A004352",
        "drive": "rwd",
        "size": "full-size",
        "type": "sedan",
        "paint_color": "blue",
        "image_url": "http://image.url/car.jpg",
        "description": "A great car",
        "latitude": 34.0522,
        "longitude": -118.2437,
        "posting_date": "2022-01-01T12:00:00"
    }


@pytest.fixture
def example_car_model():
    # Create a mock Car model instance
    return CarModel(
        id=1,
        url="http://test.car",
        price=10000.0,
        year=2022,
        manufacturer_id=1,
        model="ModelX",
        condition="new",
        cylinders="4",
        fuel="gas",
        odometer=5000.0,
        title_status="clean",
        transmission="automatic",
        vin="1HGCM82633A004352",
        drive="rwd",
        size="full-size",
        type="sedan",
        paint_color="blue",
        image_url="http://image.url/car.jpg",
        description="A great car",
        latitude=34.0522,
        longitude=-118.2437,
        posting_date="2022-01-01T12:00:00"
    )


@pytest.fixture
def example_car_model_list():
    return [
        CarModel(
            id=1,
            url="https://example.com/car1",
            price=50000.0,
            year=2022,
            manufacturer_id=1,
            model="ModelX",
            condition="New",
            cylinders="4",
            fuel="Petrol",
            odometer=10.0,
            title_status="Clean",
            transmission="Manual",
            vin="ABC1234567890",
            drive="FWD",
            size="Compact",
            type="Sedan",
            paint_color="Red",
            image_url="https://example.com/images/car1.jpg",
            description="Brand new ModelX",
            latitude=40.7128,
            longitude=-74.0060,
            posting_date=datetime.now()
        ),
        CarModel(
            id=2,
            url="https://example.com/car2",
            price=55000.0,
            year=2022,
            manufacturer_id=2,
            model="ModelY",
            condition="Used",
            cylinders="6",
            fuel="Diesel",
            odometer=5000.0,
            title_status="Clean",
            transmission="Automatic",
            vin="DEF1234567890",
            drive="AWD",
            size="Mid-size",
            type="SUV",
            paint_color="Blue",
            image_url="https://example.com/images/car2.jpg",
            description="Used ModelY in good condition",
            latitude=34.0522,
            longitude=-118.2437,
            posting_date=datetime.now()
        )
    ]


@pytest.fixture
def example_updated_car_data():
    return {
        "price": 52000.0,
        "model": "UpdatedModelX"
    }


@pytest.fixture
def example_updated_car_model(example_car_model):
    updated_car = example_car_model
    updated_car.price = 52000.0
    updated_car.description = "New and improved description"
    return updated_car


def test_create_car(client, example_car_data, mocker, example_car_model):
    mocker.patch("repositories.sqlalchemy_repository.SQLAlchemyCarRepository.create", return_value=example_car_model)
    response = client.post("/cars/", json=example_car_data)
    assert response.status_code == 200
    created_car = response.json()
    assert created_car["model"] == "ModelX"
    assert created_car.get("id") == 1


def test_get_car_by_id(client, example_car_data, mocker, example_car_model):
    mocker.patch("repositories.sqlalchemy_repository.SQLAlchemyCarRepository.get_by_id", return_value=example_car_model)
    response = client.get(f"/cars/{example_car_model.id}/")
    assert response.status_code == 200
    retrieved_car = response.json()
    assert retrieved_car["model"] == "ModelX"
    assert retrieved_car["id"] == example_car_model.id


def test_get_all_cars(client, mocker, example_car_model_list):
    mocker.patch(
        "repositories.sqlalchemy_repository.SQLAlchemyCarRepository.get_all",
        return_value={
            "total": len(example_car_model_list),
            "skip": 0,
            "limit": 10,
            "items": example_car_model_list
        }
    )
    response = client.get("/cars/")
    assert response.status_code == 200
    retrieved_cars = response.json()
    assert len(retrieved_cars["items"]) == len(example_car_model_list)


def test_update_car(client, example_updated_car_data, mocker, example_updated_car_model):
    mocker.patch("repositories.sqlalchemy_repository.SQLAlchemyCarRepository.update",
                 return_value=example_updated_car_model)
    response = client.patch(f"/cars/{example_updated_car_model.id}/", json=example_updated_car_data)
    assert response.status_code == 200
    updated_car = response.json()
    assert updated_car["model"] == "ModelX"  # Assuming the updated model name is "ModelY"
    assert updated_car["id"] == example_updated_car_model.id


def test_delete_car(client, mocker):
    mocker.patch("repositories.sqlalchemy_repository.SQLAlchemyCarRepository.delete", return_value=None)
    car_id_to_delete = 1
    response = client.delete(f"/cars/{car_id_to_delete}/")
    assert response.status_code == 204


if __name__ == "__main__":
    pytest.main()

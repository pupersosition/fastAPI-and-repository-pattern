from datetime import datetime

import pytest
from fastapi.testclient import TestClient
from models.manufacturer import Manufacturer as ManufacturerModel

from app.main import app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def example_manufacturer_data():
    return {
        "name": "audi"
    }


@pytest.fixture
def example_manufacturer_model():
    # Create a mock Manufacturer model instance
    return ManufacturerModel(
        id=1,
        name="bmw"
    )


@pytest.fixture
def example_manufacturer_model_list():
    return [
        ManufacturerModel(
            id=1,
            name="bmw"
        ),
        ManufacturerModel(
            id=2,
            name="mini"
        )
    ]


@pytest.fixture
def example_updated_manufacturer_data():
    return {
        "name": "lada",
    }


@pytest.fixture
def example_updated_manufacturer_model(example_manufacturer_model):
    updated_manufacturer = example_manufacturer_model
    updated_manufacturer.name = "lada"
    return updated_manufacturer


def test_create_manufacturer(client, example_manufacturer_data, mocker, example_manufacturer_model):
    mocker.patch("repositories.sqlalchemy_repository.SQLAlchemyManufacturerRepository.create", return_value=example_manufacturer_model)
    response = client.post("/manufacturers/", json=example_manufacturer_data)
    assert response.status_code == 200
    created_manufacturer = response.json()
    assert created_manufacturer["name"] == "bmw"
    assert created_manufacturer.get("id") == 1


def test_get_manufacturer_by_id(client, example_manufacturer_data, mocker, example_manufacturer_model):
    mocker.patch("repositories.sqlalchemy_repository.SQLAlchemyManufacturerRepository.get_by_id", return_value=example_manufacturer_model)
    response = client.get(f"/manufacturers/{example_manufacturer_model.id}/")
    assert response.status_code == 200
    retrieved_manufacturer = response.json()
    assert retrieved_manufacturer["name"] == "bmw"
    assert retrieved_manufacturer["id"] == example_manufacturer_model.id


def test_get_all_manufacturers(client, mocker, example_manufacturer_model_list):
    mocker.patch("repositories.sqlalchemy_repository.SQLAlchemyManufacturerRepository.get_all",
                 return_value={
                     "total": len(example_manufacturer_model_list),
                     "skip": 0,
                     "limit": 10,
                     "items": example_manufacturer_model_list
                 })
    response = client.get("/manufacturers/")
    assert response.status_code == 200
    retrieved_manufacturers = response.json()
    assert len(retrieved_manufacturers["items"]) == len(example_manufacturer_model_list)



def test_update_manufacturer(client, example_updated_manufacturer_data, mocker, example_updated_manufacturer_model):
    mocker.patch("repositories.sqlalchemy_repository.SQLAlchemyManufacturerRepository.update",
                 return_value=example_updated_manufacturer_model)
    response = client.patch(f"/manufacturers/{example_updated_manufacturer_model.id}/", json=example_updated_manufacturer_data)
    assert response.status_code == 200
    updated_manufacturer = response.json()
    assert updated_manufacturer["name"] == "lada"
    assert updated_manufacturer["id"] == example_updated_manufacturer_model.id


def test_delete_manufacturer(client, mocker):
    mocker.patch("repositories.sqlalchemy_repository.SQLAlchemyManufacturerRepository.delete", return_value=None)
    manufacturer_id_to_delete = 1
    response = client.delete(f"/manufacturers/{manufacturer_id_to_delete}/")
    assert response.status_code == 204


if __name__ == "__main__":
    pytest.main()

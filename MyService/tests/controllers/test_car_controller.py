import json
import pytest
from unittest.mock import MagicMock
from app import create_app
from app.entities.car import Car


@pytest.fixture
def car_service():
    return MagicMock()


@pytest.fixture
def client(car_service):
    app = create_app(car_service=car_service)
    app.config['TESTING'] = True
    return app.test_client()


def test_add_car(client, car_service):
    response = client.post('/cars', json={"plate_number": "ABC123", "brand": "Toyota", "price": 150.0})
    assert response.status_code == 201
    car_service.add_car.assert_called_once()


def test_get_cars(client, car_service):
    car_service.get_cars.return_value = [Car("ABC123", "Toyota", 150.0)]
    response = client.get('/cars')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data[0]['plate_number'] == "ABC123"


def test_get_car(client, car_service):
    car_service.get_car.return_value = Car("ABC123", "Toyota", 150.0)
    response = client.get('/cars/ABC123')
    assert response.status_code == 200
    assert json.loads(response.data)['brand'] == "Toyota"


def test_get_car_not_found(client, car_service):
    car_service.get_car.return_value = None
    response = client.get('/cars/NOTFOUND')
    assert response.status_code == 404


def test_update_car(client, car_service):
    car_service.update_car.return_value = True
    response = client.put('/cars/ABC123', json={"brand": "Honda", "price": 200.0})
    assert response.status_code == 200


def test_update_car_not_found(client, car_service):
    car_service.update_car.return_value = False
    response = client.put('/cars/NOTFOUND', json={"brand": "Honda", "price": 200.0})
    assert response.status_code == 404


def test_delete_car(client, car_service):
    car_service.delete_car.return_value = True
    response = client.delete('/cars/ABC123')
    assert response.status_code == 204


def test_delete_car_not_found(client, car_service):
    car_service.delete_car.return_value = False
    response = client.delete('/cars/NOTFOUND')
    assert response.status_code == 404

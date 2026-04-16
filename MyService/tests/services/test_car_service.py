import pytest
from app.services.car_service import CarService
from app.entities.car import Car


@pytest.fixture
def service():
    return CarService()


def test_add_car(service):
    service.add_car(Car("ABC123", "Toyota", 150.0))
    assert len(service.get_cars()) == 1


def test_get_car(service):
    service.add_car(Car("ABC123", "Toyota", 150.0))
    car = service.get_car("ABC123")
    assert car is not None
    assert car.brand == "Toyota"


def test_get_car_not_found(service):
    assert service.get_car("NOTFOUND") is None


def test_get_cars_multiple(service):
    service.add_car(Car("ABC123", "Toyota", 150.0))
    service.add_car(Car("XYZ789", "Honda", 180.0))
    assert len(service.get_cars()) == 2


def test_update_car(service):
    service.add_car(Car("ABC123", "Toyota", 150.0))
    result = service.update_car("ABC123", Car("ABC123", "Honda", 200.0))
    assert result is True
    assert service.get_car("ABC123").brand == "Honda"


def test_update_car_not_found(service):
    assert service.update_car("NOTFOUND", Car("NOTFOUND", "Toyota", 150.0)) is False


def test_delete_car(service):
    service.add_car(Car("ABC123", "Toyota", 150.0))
    result = service.delete_car("ABC123")
    assert result is True
    assert service.get_car("ABC123") is None


def test_delete_car_not_found(service):
    assert service.delete_car("NOTFOUND") is False

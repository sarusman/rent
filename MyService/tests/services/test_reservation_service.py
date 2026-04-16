import pytest
from unittest.mock import MagicMock
from app.services.reservation_service import ReservationService
from app.entities.car import Car
from app.entities.reservation import Reservation


@pytest.fixture
def car_service():
    mock = MagicMock()
    mock.get_car.return_value = Car("ABC123", "Toyota", 150.0)
    return mock


@pytest.fixture
def service(car_service):
    return ReservationService(car_service)


def test_creer_reservation(service):
    r = Reservation("ABC123", "Jean Dupont", "2024-01-10", "2024-01-15")
    result = service.creer_reservation(r)
    assert result is not None
    assert result.id is not None
    assert result.prix_total == 5 * 150.0


def test_creer_reservation_voiture_inexistante(service, car_service):
    car_service.get_car.return_value = None
    r = Reservation("INVALID", "Jean Dupont", "2024-01-10", "2024-01-15")
    assert service.creer_reservation(r) is None


def test_get_reservation(service):
    created = service.creer_reservation(Reservation("ABC123", "Jean", "2024-01-10", "2024-01-12"))
    found = service.get_reservation(created.id)
    assert found is not None
    assert found.id == created.id


def test_get_reservation_not_found(service):
    assert service.get_reservation("notexist") is None


def test_get_reservations(service):
    service.creer_reservation(Reservation("ABC123", "Jean", "2024-01-10", "2024-01-12"))
    service.creer_reservation(Reservation("ABC123", "Marie", "2024-02-01", "2024-02-05"))
    assert len(service.get_reservations()) == 2


def test_annuler_reservation(service):
    created = service.creer_reservation(Reservation("ABC123", "Jean", "2024-01-10", "2024-01-15"))
    result = service.annuler_reservation(created.id)
    assert result is True
    assert len(service.get_reservations()) == 0


def test_annuler_reservation_not_found(service):
    assert service.annuler_reservation("notexist") is False

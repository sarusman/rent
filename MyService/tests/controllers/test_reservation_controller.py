import json
import pytest
from unittest.mock import MagicMock
from app import create_app
from app.entities.reservation import Reservation


@pytest.fixture
def reservation_service():
    return MagicMock()


@pytest.fixture
def client(reservation_service):
    app = create_app(reservation_service=reservation_service)
    app.config['TESTING'] = True
    return app.test_client()


def test_creer_reservation(client, reservation_service):
    created = Reservation("ABC123", "Jean Dupont", "2024-01-10", "2024-01-15", id="uuid-1", prix_total=750.0)
    reservation_service.creer_reservation.return_value = created
    response = client.post('/reservations', json={
        "plate_number": "ABC123",
        "client_nom": "Jean Dupont",
        "date_debut": "2024-01-10",
        "date_fin": "2024-01-15",
    })
    assert response.status_code == 201
    assert json.loads(response.data)['id'] == "uuid-1"


def test_creer_reservation_voiture_inexistante(client, reservation_service):
    reservation_service.creer_reservation.return_value = None
    response = client.post('/reservations', json={
        "plate_number": "INVALID",
        "client_nom": "Jean",
        "date_debut": "2024-01-10",
        "date_fin": "2024-01-15",
    })
    assert response.status_code == 400


def test_get_reservations(client, reservation_service):
    r = Reservation("ABC123", "Jean", "2024-01-10", "2024-01-15", id="uuid-1", prix_total=750.0)
    reservation_service.get_reservations.return_value = [r]
    response = client.get('/reservations')
    assert response.status_code == 200
    assert len(json.loads(response.data)) == 1


def test_get_reservation(client, reservation_service):
    r = Reservation("ABC123", "Jean", "2024-01-10", "2024-01-15", id="uuid-1", prix_total=750.0)
    reservation_service.get_reservation.return_value = r
    response = client.get('/reservations/uuid-1')
    assert response.status_code == 200
    assert json.loads(response.data)['client_nom'] == "Jean"


def test_get_reservation_not_found(client, reservation_service):
    reservation_service.get_reservation.return_value = None
    response = client.get('/reservations/notfound')
    assert response.status_code == 404


def test_annuler_reservation(client, reservation_service):
    reservation_service.annuler_reservation.return_value = True
    response = client.delete('/reservations/uuid-1')
    assert response.status_code == 204


def test_annuler_reservation_not_found(client, reservation_service):
    reservation_service.annuler_reservation.return_value = False
    response = client.delete('/reservations/notfound')
    assert response.status_code == 404

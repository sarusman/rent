import uuid
from datetime import date


class ReservationService:
    def __init__(self, car_service):
        self._reservations = {}
        self._car_service = car_service

    def creer_reservation(self, reservation):
        car = self._car_service.get_car(reservation.plate_number)
        if not car:
            return None
        debut = date.fromisoformat(reservation.date_debut)
        fin = date.fromisoformat(reservation.date_fin)
        jours = (fin - debut).days
        reservation.id = str(uuid.uuid4())
        reservation.prix_total = jours * car.price
        self._reservations[reservation.id] = reservation
        return reservation

    def get_reservation(self, reservation_id):
        return self._reservations.get(reservation_id)

    def get_reservations(self):
        return list(self._reservations.values())

    def annuler_reservation(self, reservation_id):
        if reservation_id not in self._reservations:
            return False
        del self._reservations[reservation_id]
        return True

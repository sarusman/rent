from flask import Flask
from app.services.car_service import CarService
from app.services.reservation_service import ReservationService
from app.controllers.car_controller import cars_bp
from app.controllers.reservation_controller import reservations_bp


def create_app(car_service=None, reservation_service=None):
    app = Flask(__name__)

    if car_service is None:
        car_service = CarService()
    if reservation_service is None:
        reservation_service = ReservationService(car_service)

    app.car_service = car_service
    app.reservation_service = reservation_service

    app.register_blueprint(cars_bp)
    app.register_blueprint(reservations_bp)

    return app

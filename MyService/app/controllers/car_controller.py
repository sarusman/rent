from flask import Blueprint, jsonify, request, current_app
from app.entities.car import Car

cars_bp = Blueprint('cars', __name__)


@cars_bp.route('/cars', methods=['POST'])
def add_car():
    data = request.get_json()
    car = Car(data['plate_number'], data['brand'], data['price'])
    current_app.car_service.add_car(car)
    return jsonify(car.to_dict()), 201


@cars_bp.route('/cars', methods=['GET'])
def get_cars():
    return jsonify([c.to_dict() for c in current_app.car_service.get_cars()])


@cars_bp.route('/cars/<plate_number>', methods=['GET'])
def get_car(plate_number):
    car = current_app.car_service.get_car(plate_number)
    if not car:
        return jsonify({"error": "not found"}), 404
    return jsonify(car.to_dict())


@cars_bp.route('/cars/<plate_number>', methods=['PUT'])
def update_car(plate_number):
    data = request.get_json()
    car = Car(plate_number, data['brand'], data['price'])
    if not current_app.car_service.update_car(plate_number, car):
        return jsonify({"error": "not found"}), 404
    return jsonify(car.to_dict())


@cars_bp.route('/cars/<plate_number>', methods=['DELETE'])
def delete_car(plate_number):
    if not current_app.car_service.delete_car(plate_number):
        return jsonify({"error": "not found"}), 404
    return '', 204

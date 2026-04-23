from flask import Blueprint, jsonify, request, current_app
from app.entities.reservation import Reservation

reservations_bp = Blueprint("reservations", __name__)


@reservations_bp.route("/reservations", methods=["POST"])
def creer_reservation():
    data = request.get_json()
    reservation = Reservation(
        data["plate_number"],
        data["client_nom"],
        data["date_debut"],
        data["date_fin"],
    )
    result = current_app.reservation_service.creer_reservation(reservation)
    if not result:
        return jsonify({"error": "voiture introuvable"}), 400
    return jsonify(result.to_dict()), 201


@reservations_bp.route("/reservations", methods=["GET"])
def get_reservations():
    return jsonify(
        [r.to_dict() for r in current_app.reservation_service.get_reservations()]
    )


@reservations_bp.route("/reservations/<reservation_id>", methods=["GET"])
def get_reservation(reservation_id):
    reservation = current_app.reservation_service.get_reservation(reservation_id)
    if not reservation:
        return jsonify({"error": "not found"}), 404
    return jsonify(reservation.to_dict())


@reservations_bp.route("/reservations/<reservation_id>", methods=["DELETE"])
def annuler_reservation(reservation_id):
    if not current_app.reservation_service.annuler_reservation(reservation_id):
        return jsonify({"error": "not found"}), 404
    return "", 204

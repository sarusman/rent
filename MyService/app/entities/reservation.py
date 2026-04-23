class Reservation:
    def __init__(
        self, plate_number, client_nom, date_debut, date_fin, id=None, prix_total=0.0
    ):
        self.id = id
        self.plate_number = plate_number
        self.client_nom = client_nom
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.prix_total = prix_total

    def to_dict(self):
        return {
            "id": self.id,
            "plate_number": self.plate_number,
            "client_nom": self.client_nom,
            "date_debut": self.date_debut,
            "date_fin": self.date_fin,
            "prix_total": self.prix_total,
        }

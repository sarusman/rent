from app.entities.reservation import Reservation


def test_constructeur():
    r = Reservation("ABC123", "Jean Dupont", "2024-01-10", "2024-01-15")
    assert r.plate_number == "ABC123"
    assert r.client_nom == "Jean Dupont"
    assert r.date_debut == "2024-01-10"
    assert r.date_fin == "2024-01-15"
    assert r.id is None
    assert r.prix_total == 0.0


def test_constructeur_avec_id_et_prix():
    r = Reservation("ABC123", "Jean", "2024-01-10", "2024-01-15", id="uuid-1", prix_total=750.0)
    assert r.id == "uuid-1"
    assert r.prix_total == 750.0


def test_to_dict():
    r = Reservation("ABC123", "Jean Dupont", "2024-01-10", "2024-01-15", id="uuid-1", prix_total=750.0)
    d = r.to_dict()
    assert d["plate_number"] == "ABC123"
    assert d["client_nom"] == "Jean Dupont"
    assert d["id"] == "uuid-1"
    assert d["prix_total"] == 750.0

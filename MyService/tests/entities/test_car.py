from app.entities.car import Car


def test_constructeur():
    car = Car("ABC123", "Toyota", 150.0)
    assert car.plate_number == "ABC123"
    assert car.brand == "Toyota"
    assert car.price == 150.0


def test_to_dict():
    car = Car("ABC123", "Toyota", 150.0)
    assert car.to_dict() == {"plate_number": "ABC123", "brand": "Toyota", "price": 150.0}


def test_modifier_brand():
    car = Car("ABC123", "Toyota", 150.0)
    car.brand = "Honda"
    assert car.brand == "Honda"


def test_modifier_price():
    car = Car("ABC123", "Toyota", 150.0)
    car.price = 200.0
    assert car.price == 200.0

class Car:
    def __init__(self, plate_number, brand, price):
        self.plate_number = plate_number
        self.brand = brand
        self.price = price

    def to_dict(self):
        return {
            "plate_number": self.plate_number,
            "brand": self.brand,
            "price": self.price,
        }

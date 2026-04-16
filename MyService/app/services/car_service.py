class CarService:
    def __init__(self):
        self._cars = {}

    def add_car(self, car):
        self._cars[car.plate_number] = car

    def get_car(self, plate_number):
        return self._cars.get(plate_number)

    def get_cars(self):
        return list(self._cars.values())

    def update_car(self, plate_number, car):
        if plate_number not in self._cars:
            return False
        self._cars[plate_number] = car
        return True

    def delete_car(self, plate_number):
        if plate_number not in self._cars:
            return False
        del self._cars[plate_number]
        return True

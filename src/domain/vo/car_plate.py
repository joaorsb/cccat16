import re

class CarPlate():
    value: str
    pattern = re.compile(r"^[A-Z]{3}[0-9]{4}$")

    def __init__(self, car_plate: str) -> None:
        if car_plate and self.pattern.match(car_plate):
            self.value = car_plate

    def get_value(self):
        return self.value
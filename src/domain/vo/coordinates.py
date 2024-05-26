class Coordinates():
    _lat: int
    _long: int

    def __init__(self, lat: int, long: int) -> None:
        if (lat < -90 or lat > 90):
            raise Exception("Invalid latitude")
        if (long < -180 or long > 180):
            raise Exception("Invalid longitude")
        self._lat = lat
        self.long = long
    
    def get_lat(self):
        return self._lat
    
    def get_long(self):
        return self._long
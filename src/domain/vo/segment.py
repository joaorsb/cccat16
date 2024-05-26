from math import pi, sin, cos, atan2, sqrt, round
from src.domain.vo.coordinates import Coordinates

class Segment():
    coord_from: Coordinates
    to: Coordinates

    def __init__(self, coord_from: Coordinates, coord_to: Coordinates) -> None:
        self.coord_from = coord_from
        self.to = coord_to

    def get_distance(self, ):
        earth_radius = 6371
        degrees_to_radians = pi / 180
        delta_lat = (self.to.get_lat() - self.coord_from.get_lat()) * degrees_to_radians
        delta_long = (self.to.get_long() - self.coord_from.get_long()) * degrees_to_radians
        a = sin(delta_lat/2) * sin(delta_lat/2) + cos(self.coord_from.get_lat() * degrees_to_radians) * cos(self.to.get_lat() * degrees_to_radians) * sin(delta_long/2) * sin(delta_long/2)
        c = 2 * atan2(sqrt(a), sqrt(1-a))
        distance = earth_radius * c
        return round(distance)
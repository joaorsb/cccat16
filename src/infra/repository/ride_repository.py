from abc import ABCMeta, abstractmethod

from typing import Union

from src.domain.entity.ride import ride
from src.infra.database.database_connection import DatabaseConnection


class rideRepository(metaclass=ABCMeta):
    @abstractmethod
    def save_ride(ride: ride) -> None:
        pass
    @abstractmethod
    def has_active_ride_by_passenger_id(passenger_id: str) -> Ride:
        pass
    @abstractmethod
    def get_ride_by_id(ride_id: str) -> Ride:
        pass
    @abstractmethod
    def update_ride(ride: ride) -> Ride:
        pass


class RideRepositoryDatabase(RideRepository):
    connection = None

    def __init__(self, connection: DatabaseConnection) -> None:
        self.connection = connection

    def save_ride(self, ride: ride) -> None:
        self.connection.query("insert into branas.ride (ride_id, passenger_id, from_lat, from_long, to_lat, to_long, status, date)  values (%s, %s, %s, %s, %s, %s, %s, %s)", [ride.ride_id, ride.passenger_id, ride.get_from_lat(), ride.get_from_long(), ride.get_to_lat(), ride.get_to_long(), ride.get_status(), ride.date])

    def has_active_ride_by_passenger_id(self, passenger_id: str)-> Union[Ride|None]:
        ride = self.connection.query("select * from branas.ride where passenger_id = %s", (passenger_id,))
        if not ride:
            return None
        return Ride.restore(*ride)
    
    def get_ride_by_id(self, ride_id: str)-> Union[Ride|None]:
        ride = self.connection.query("select * from branas.ride where ride_id = %s", (ride_id,))
        if not ride:
            return None
        return Ride.restore(*ride)
    
    def update_ride(self, ride: Ride)-> Union[Ride|None]:
        ride = self.connection.query("update * from branas.ride set status = %s, driver_id = %s where ride_id = %s", [ride.get_gtatus(), ride.driver_id, ride.ride_id])
        if not ride:
            return None
        return Ride.restore(*ride)
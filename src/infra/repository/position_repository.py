from abc import ABCMeta, abstractmethod

from typing import Union

from src.domain.entity.position import Position
from src.infra.database.database_connection import DatabaseConnection


class PositionRepository(metaclass=ABCMeta):
    @abstractmethod
    def save_position(position: Position) -> None:
        pass


class PositionRepositoryDatabase(PositionRepository):
    connection = None

    def __init__(self, connection: DatabaseConnection) -> None:
        self.connection = connection

    def save_position(self, position: Position) -> None:
        self.connection.query("insert into branas.position (position_id, ride_id, lat, long, date)  values (%s, %s, %s, %s, %s, %s, %s)", [position.position_id, position.ride_id, position.coord.get_lat(), position.coord.get_long(), position.date])


class PositionRepositoryMemory(PositionRepository):
    positions: list = []

    def __init__(self) -> None:
        self.positions = []

    def save_position(self, position: Position) -> None:
        self.positions.append(position)

import re

from uuid import uuid4
from pydantic import BaseModel
from src.domain.validate_cpf import validate_cpf


class AccountInputDTO(BaseModel):
    name: str = None
    email: str = None
    cpf: str = None
    car_plate: str = None
    is_passenger: bool = False
    is_driver: bool = False


class AccountGetDTO(BaseModel):
    account_id: str = None


class AccountOuputDTO(BaseModel):
    accountId: str = None
    name: str = None
    email: str = None
    cpf: str = None
    carPlate: str | None = ''
    isPassenger: bool | None = False
    isDriver: bool | None = False


class Account():
    account_id: str = None
    name: str = None
    email: str = None
    cpf: str = None
    car_plate: str = None
    is_passenger: bool = False
    is_driver: bool = False

    def __init__(
            self,
            account_id: str,
            name: str,
            email: str,
            cpf: str,
            car_plate: str,
            is_passenger: bool,
            is_driver: bool) -> None:
        self.account_id = account_id
        self.name = name
        self.email = email
        self.cpf = cpf
        self.car_plate = car_plate
        self.is_driver = is_driver
        self.is_passenger = is_passenger
        if ' ' not in name:
            raise Exception('Invalid name')
        if '@' not in self.email:
            raise Exception('Invalid email')
        if not validate_cpf(self.cpf):
            raise Exception('Invalid cpf')
        pattern = re.compile(r"^[A-Z]{3}[0-9]{4}$")

        if self.is_driver and self.car_plate and not pattern.match(self.car_plate):
            raise Exception('Invalid car_plate')

    def create(
            name: str,
            email: str,
            cpf: str,
            car_plate: str,
            is_passenger: bool,
            is_driver: bool):
        account_id = str(uuid4())
        return Account(account_id, name, email, cpf, car_plate, is_passenger, is_driver)

    def restore(
            account_id: str,
            name: str,
            email: str,
            cpf: str,
            car_plate: str,
            is_passenger: bool,
            is_driver: bool):
        return Account(account_id, name, email, cpf, car_plate, is_passenger, is_driver)

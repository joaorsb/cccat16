from collections import namedtuple
import random
from uuid import uuid4
from src.domain.account import AccountInputDTO

import pytest

Account = namedtuple('Account', ['account_id', 'name', 'email', 'cpf', 'car_plate', 'is_passenger', 'is_driver'])


@pytest.fixture
def account():
    return Account(
        str(uuid4()), "John Doe", f'john.doe.{random.random()}@gmail.com', "87748248800", None, True, False
    )


@pytest.fixture
def account_passageiro_falha():
    account = AccountInputDTO()
    account.name = "John"
    account.email = f'john.doe.{random.random()}@gmail.com'
    account.cpf = "87748248800"
    account.car_plate = ""
    account.is_passenger = True
    account.is_driver = False
    return account


@pytest.fixture
def account_passageiro():
    account = AccountInputDTO()
    account.name = "John Does"
    account.email = f'john.doe.{random.random()}@gmail.com'
    account.cpf = "87748248800"
    account.car_plate = ""
    account.is_passenger = True
    account.is_driver = False
    return account


@pytest.fixture
def account_passageiro_dict():
    return {
        "name": "João Batista",
        "email": f"joaorsbatista.{random.random()}@gmail.com",
        "cpf": "09319249016",
        "car_plate": "",
        "is_passenger": True,
        "is_driver": False
    }


@pytest.fixture
def account_motorista():
    account = AccountInputDTO()
    account.name = "John Does"
    account.email = f'john.doe.{random.random()}@gmail.com'
    account.cpf = "87748248800"
    account.car_plate = "BUO2434"
    account.is_passenger = False
    account.is_driver = True
    return account


@pytest.fixture
def account_motorista_placa_invalida():
    account = AccountInputDTO()
    account.name = "John Does"
    account.email = f'john.doe.{random.random()}@gmail.com'
    account.cpf = "87748248800"
    account.car_plate = "BUO243"
    account.is_passenger = False
    account.is_driver = True
    return account


@pytest.fixture
def valid_cpfs():
    return [
        "97456321558",
        "71428793860",
        "87748248800"
    ]


@pytest.fixture
def invalid_cpfs():
    return [
        None,
        "11111111111",
        "123",
        "1234566789123456789"
    ]

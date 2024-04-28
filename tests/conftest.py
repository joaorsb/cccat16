from collections import namedtuple
import random
from uuid import uuid4

import pytest

Account = namedtuple('Account', ['account_id', 'name', 'email', 'cpf', 'car_plate', 'is_passenger', 'is_driver'])
AccountSignup = namedtuple('AccountSignup', ['name', 'email', 'cpf', 'car_plate', 'is_passenger', 'is_driver'])


@pytest.fixture
def account():
    return Account(
        str(uuid4()), "John Doe", f'john.doe.{random.random()}@gmail.com', "87748248800", None, True, False
    )


@pytest.fixture
def account_passageiro_falha():
    return AccountSignup(
        "John", f'john.doe.{random.random()}@gmail.com', "87748248800", None, True, False
    )


@pytest.fixture
def account_passageiro():
    return AccountSignup(
        "John Doe", f'john.doe.{random.random()}@gmail.com', "87748248800", None, True, False
    )


@pytest.fixture
def account_passageiro_dict():
    return {
        "name": "João Batista",
        "email": "joaorsbatista@gmail.com",
        "cpf": "09319249016",
        "car_plate": "",
        "is_passenger": True,
        "is_driver": False
    }


@pytest.fixture
def account_motorista():
    return AccountSignup(
        "John Does", f'john.doe.{random.random()}@gmail.com', "87748248800", "BUO2434", False, True
    )


@pytest.fixture
def account_motorista_placa_invalida():
    return AccountSignup(
        "John Does", f'john.doe.{random.random()}@gmail.com', "87748248800", "BUO243", False, True
    )


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

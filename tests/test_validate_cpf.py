import pytest

from src.domain.validate_cpf import validate_cpf


@pytest.mark.parametrize('cpf', [
        "97456321558",
        "71428793860",
        "87748248800"
    ])
def test_verify_valid_cpfs(cpf):
    valid = validate_cpf(cpf)
    assert valid is True


@pytest.mark.parametrize('cpf', [
        False,
        None,
        "11111111111",
        "123",
        "1234566789123456789"
    ])
def test_verify_invalid_cpfs(cpf):
    valid = validate_cpf(cpf)
    assert valid is False

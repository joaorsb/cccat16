import pytest

from src.application import Account
from src.application.get_account import GetAccount
from src.application.signup import Signup
from src.resource.account_dao import AccountDAOMemory
from src.resource.mailer_gateway import MailerGatewayMemory


def test_criar_conta_passageiro(account_passageiro):
    account_dao = AccountDAOMemory()
    mailer_gateway = MailerGatewayMemory()
    signup = Signup(account_dao, mailer_gateway)
    get_account = GetAccount(account_dao)
    output = signup.execute(account_passageiro)
    assert 'account_id' in output
    account = Account(output['account_id'], account_passageiro.name, account_passageiro.email, account_passageiro.cpf, account_passageiro.car_plate, account_passageiro.is_passenger, account_passageiro.is_driver)
    output_account_result = get_account.execute(account)
    assert output_account_result.email == account_passageiro.email


@pytest.mark.xfail
def test_criar_conta_passageiro_falha(
        account_passageiro_falha):
    account_dao = AccountDAOMemory()
    mailer_gateway = MailerGatewayMemory()
    signup = Signup(account_dao, mailer_gateway)
    _ = signup.execute(account_passageiro_falha)


def test_criar_conta_motorista(account_motorista):
    account_dao = AccountDAOMemory()
    mailer_gateway = MailerGatewayMemory()
    signup = Signup(account_dao, mailer_gateway)
    get_account = GetAccount(account_dao)
    output = signup.execute(account_motorista)
    assert 'account_id' in output
    account = Account(output['account_id'], account_motorista.name, account_motorista.email, account_motorista.cpf, account_motorista.car_plate, account_motorista.is_passenger, account_motorista.is_driver)
    output_account_result = get_account.execute(account)
    assert output_account_result.email == account_motorista.email


@pytest.mark.xfail
def test_criar_conta_motorista_placa_invalida(account_motorista_placa_invalida):
    account_dao = AccountDAOMemory()
    mailer_gateway = MailerGatewayMemory()
    signup = Signup(account_dao, mailer_gateway)
    _ = signup.execute(account_motorista_placa_invalida)

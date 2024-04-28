import pytest

from src.application.use_case.get_account import GetAccount
from src.application.use_case.signup import Signup
from src.infra.repository.account_repository import AccountRepositoryMemory
from src.infra.http.fastapi_http_server import FastAPIResponse

from src.infra.gateway.mailer_gateway import MailerGatewayMemory


def test_criar_conta_passageiro(account_passageiro):
    account_repository = AccountRepositoryMemory()
    mailer_gateway = MailerGatewayMemory()
    response_class = FastAPIResponse()
    signup = Signup(account_repository, mailer_gateway, response_class)
    get_account = GetAccount(account_repository, response_class)
    output = signup.execute(account_passageiro)
    assert 'account_id' in output
    output_account_result = get_account.execute(output['account_id'])
    assert output_account_result.email == account_passageiro.email


@pytest.mark.xfail
def test_criar_conta_passageiro_falha(
        account_passageiro_falha):
    account_repository = AccountRepositoryMemory()
    mailer_gateway = MailerGatewayMemory()
    response_class = FastAPIResponse()
    signup = Signup(account_repository, mailer_gateway, response_class)
    _ = signup.execute(account_passageiro_falha)


def test_criar_conta_motorista(account_motorista):
    account_repository = AccountRepositoryMemory()
    mailer_gateway = MailerGatewayMemory()
    response_class = FastAPIResponse()
    signup = Signup(account_repository, mailer_gateway, response_class)
    get_account = GetAccount(account_repository, response_class)
    output = signup.execute(account_motorista)
    assert 'account_id' in output
    output_account_result = get_account.execute(output['account_id'])
    assert output_account_result.email == account_motorista.email


@pytest.mark.xfail
def test_criar_conta_motorista_placa_invalida(account_motorista_placa_invalida):
    account_repository = AccountRepositoryMemory()
    mailer_gateway = MailerGatewayMemory()
    response_class = FastAPIResponse()
    signup = Signup(account_repository, mailer_gateway, response_class)
    _ = signup.execute(account_motorista_placa_invalida)

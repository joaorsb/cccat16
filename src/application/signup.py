import re
from uuid import uuid4
from typing import Any

from src.resource.account_dao import AccountDAO
from src.resource.mailer_gateway import MailerGateway
from src.application.validate_cpf import validate_cpf
from src.application import Account


class Signup():
    account_dao = None
    mailer_gateway = None

    def __init__(self, account_dao: AccountDAO, mailer_gateway: MailerGateway):
        self.account_dao = account_dao
        self.mailer_gateway = mailer_gateway

    def execute(self, input: Any):
        account_id = str(uuid4())
        account = Account(account_id, input.name, input.email, input.cpf, input.car_plate, input.is_passenger, input.is_driver)
        existing = self.account_dao.get_account_by_id(account.account_id)
        if existing:
            raise Exception('Account already exists')
        if ' ' not in account.name:
            raise Exception('Invalid name')
        if '@' not in account.email:
            raise Exception('Invalid email')
        if not validate_cpf(account.cpf):
            raise Exception('Invalid cpf')
        pattern = re.compile(r"^[A-Z]{3}[0-9]{4}$")

        if account.is_driver and account.car_plate and not pattern.match(account.car_plate):
            raise Exception('Invalid car_plate')
        self.account_dao.save_account(account)
        self.mailer_gateway.send(account.email, "Welcome", "")
        return {'account_id': account.account_id}

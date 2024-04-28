from typing import Any

from src.infra.repository.account_repository import AccountRepository
from src.infra.http.http_server import AbstractResponse
from src.domain.account import AccountOuputDTO


class GetAccount():
    account_repository = None
    response_class = None

    def __init__(self, account_repository: AccountRepository, response_class: AbstractResponse):
        self.account_repository = account_repository
        self.response_class = response_class

    def execute(self, account_id: str) -> AccountOuputDTO:
        try:
            account = self.account_repository.get_account_by_id(account_id)
            output = AccountOuputDTO()
            output.accountId = account.account_id
            output.name = account.name
            output.email = account.email
            output.cpf = account.cpf
            output.carPlate = account.car_plate
            output.isPassenger = account.is_passenger
            output.isDriver = account.is_driver
            return output
        except Exception as ex:
            self.response_class.set_content(str(ex))
            self.response_class.set_status(404)
            return self.response_class.instance

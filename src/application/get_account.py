from src.resource.account_dao import AccountDAO
from src.application import Account


class GetAccount():
    account_dao = None

    def __init__(self, account_dao: AccountDAO):
        self.account_dao = account_dao

    def execute(self, input: Account):
        account = self.account_dao.get_account_by_id(input.account_id)
        return account

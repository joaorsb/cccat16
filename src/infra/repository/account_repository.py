from abc import ABCMeta, abstractmethod

from typing import Union

from src.domain.account import Account
from src.infra.database.database_connection import DatabaseConnection


class AccountRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_account_by_email(email: str) -> Account:
        pass

    @abstractmethod
    def get_account_by_id(account_id: str) -> Account:
        pass

    @abstractmethod
    def save_account(account: Account) -> None:
        pass


class AccountRepositoryDatabase(AccountRepository):
    connection = None

    def __init__(self, connection: DatabaseConnection) -> None:
        self.connection = connection

    def get_account_by_email(self, email: str) -> Union[Account | None]:
        account = self.connection.query("select * from branas.account where email = %s", (email,))
        if not account:
            return None
        return Account.restore(*account)

    def get_account_by_id(self, account_id: str) -> Union[Account | None]:
        account = self.connection.query("select * from branas.account where account_id = %s", (account_id,))
        if not account:
            return None
        return Account.restore(*account)

    def save_account(self, account: Account) -> None:
        self.connection.save_one("insert into branas.account (account_id, name, email, cpf, car_plate, is_passenger, is_driver) values (%s, %s, %s, %s, %s, %s, %s)", (account.account_id, account.name, account.email, account.cpf, account.car_plate, account.is_passenger, account.is_driver))


class AccountRepositoryMemory(AccountRepository):
    accounts: list = []

    def __init__(self) -> None:
        self.accounts = []

    def get_account_by_email(self, email: str) -> Union[Account|None]:
        try:
            account = [account for account in self.accounts if account.email == email][0]
            return account
        except IndexError as ex:
            print(ex)
            return None

    def get_account_by_id(self, account_id: str) -> Account:
        try:
            account = [account for account in self.accounts if account.account_id == account_id][0]
            return account
        except IndexError as ex:
            print(ex)
            return None

    def save_account(self, account: Account) -> None:
        self.accounts.append(account)

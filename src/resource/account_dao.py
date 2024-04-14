from abc import ABCMeta, abstractmethod
import psycopg2


class AccountDAO(metaclass=ABCMeta):
    @abstractmethod
    def get_account_by_email(email: str):
        pass

    @abstractmethod
    def get_account_by_id(account_id: str):
        pass

    @abstractmethod
    def save_account(account):
        pass


class AccountDAODatabase(AccountDAO):
    def get_account_by_email(self, email: str):
        conn = psycopg2.connect(
            database="branas",
            host="localhost",
            user="branas",
            password="branas",
            port="5432"
        )
        cursor = conn.cursor()
        cursor.execute("select * from branas.account where email = %s", (email,))
        account = cursor.fetchone()
        conn.close()
        return account

    def get_account_by_id(self, account_id: str):
        conn = psycopg2.connect(
            database="branas",
            host="localhost",
            user="branas",
            password="branas",
            port="5432"
        )
        cursor = conn.cursor()
        cursor.execute("select * from branas.account where account_id = %s", (account_id,))
        account = cursor.fetchone()
        print(account)
        conn.close()
        return account

    def save_account(self, account):
        conn = psycopg2.connect(
            database="branas",
            host="localhost",
            user="branas",
            password="branas",
            port="5432"
        )
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute("insert into branas.account (account_id, name, email, cpf, car_plate, is_passenger, is_driver) values (%s, %s, %s, %s, %s, %s, %s)", (account.account_id, account.name, account.email, account.cpf, account.car_plate, account.is_passenger, account.is_driver))
        conn.close()


class AccountDAOMemory(AccountDAO):
    accounts = []

    def __init__(self):
        self.accounts = []

    def get_account_by_email(self, email: str):
        if len(self.accounts) == 0:
            return None
        return [account for account in self.accounts if account.email == email][0]

    def get_account_by_id(self, account_id: str):
        if len(self.accounts) == 0:
            return None
        return [account for account in self.accounts if account.account_id == account_id][0]

    def save_account(self, account):
        self.accounts.append(account)

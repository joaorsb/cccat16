from abc import ABCMeta, abstractmethod
import psycopg2


class DatabaseConnection(metaclass=ABCMeta):
    @abstractmethod
    def query(statement: str, params: any):
        pass

    @abstractmethod
    def save_one(statement: str, params: any):
        pass

    @abstractmethod
    def close(account):
        pass


class PostgresAdapter(DatabaseConnection):
    connection: None

    def __init__(self) -> None:
        self.connection = psycopg2.connect(
            database="branas",
            host="localhost",
            user="branas",
            password="branas",
            port="5432"
        )
        self.connection.autocommit = True

    def query(self, statement: str, params: any):
        cursor = self.connection.cursor()
        cursor.execute(statement, params)
        account = cursor.fetchone()
        return account

    def save_one(self, statement: str, params: any):
        cursor = self.connection.cursor()
        cursor.execute(statement, params)

    def close(self,):
        return self.connection.close()

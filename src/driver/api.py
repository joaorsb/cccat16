import json

from fastapi import FastAPI
from pydantic import BaseModel

from src.application import Account
from src.application.get_account import GetAccount
from src.application.signup import Signup
from src.resource.account_dao import AccountDAODatabase
from src.resource.mailer_gateway import MailerGatewayMemory


class AccountModel(BaseModel):
    account_id: str | None = None
    name: str
    email: str
    cpf: str
    car_plate: str | None = None
    is_passenger: bool | None = False
    is_driver: bool | None = False


app = FastAPI()


@app.post("/signup")
async def signup(account: AccountModel):
    account_dao = AccountDAODatabase()
    mailer = MailerGatewayMemory()
    signup = Signup(account_dao, mailer)
    saved = signup.execute(account)
    return saved


@app.get('/accounts/{accountId}')
async def get_account(accountId):
    account_dao = AccountDAODatabase()
    get_account = GetAccount(account_dao)
    account = Account(accountId, '', '', '', '', False, False)
    found = get_account.execute(account)
    account = Account(*found)
    return {
        'accountId': account.account_id,
        'name': account.name,
        'email': account.email,
        'carPlate': account.car_plate,
        'isDriver': account.is_driver,
        'isPassenger': account.is_passenger,
    }

from src.application.use_case.get_account import GetAccount
from src.application.use_case.signup import Signup
from src.infra.gateway.mailer_gateway import MailerGatewayMemory
from src.infra.repository.account_repository import AccountRepositoryDatabase
from src.infra.http.fastapi_http_server import FastAPIAdapter, FastAPIResponse
from src.infra.http.account_controller import AccountController
from src.infra.database.database_connection import PostgresAdapter


http_server = FastAPIAdapter()
connection = PostgresAdapter()
response = FastAPIResponse()
account_repository = AccountRepositoryDatabase(connection)
mailer_gateway = MailerGatewayMemory()
signup = Signup(account_repository, mailer_gateway, response)
get_account = GetAccount(account_repository, response)
account_controller = AccountController(http_server, signup, get_account)
http_server.register()
app = http_server.app

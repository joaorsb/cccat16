from src.infra.http.http_server import HttpServer
from src.application.use_case.get_account import GetAccount
from src.application.use_case.signup import Signup
from src.domain.account import AccountOuputDTO


class AccountController():

    def __init__(self, http_server: HttpServer, signup: Signup, get_account: GetAccount):
        http_server.initialize_router('post', "/signup", signup.execute)
        http_server.initialize_router(
            'get',
            '/accounts/{account_id}',
            get_account.execute,
            response_model=AccountOuputDTO,
        )

from src.infra.repository.account_repository import AccountRepository
from src.domain.account import Account, AccountInputDTO
from src.infra.gateway.mailer_gateway import MailerGateway
from src.infra.http.http_server import AbstractResponse


class Signup():
    account_repository = None
    mailer_gateway = None
    response_class = None

    def __init__(self, account_repository: AccountRepository, mailer_gateway: MailerGateway, response_class: AbstractResponse):
        self.account_repository = account_repository
        self.mailer_gateway = mailer_gateway
        self.response_class = response_class

    def execute(self, input: AccountInputDTO):
        try:
            existing = self.account_repository.get_account_by_email(input.email)
            if existing:
                raise Exception('Account already exists')
            account = Account.create(**input.__dict__)
            self.account_repository.save_account(account)
            self.mailer_gateway.send(account.email, "Welcome", "")
            return {'account_id': account.account_id}
        except Exception as ex:
            self.response_class.set_content(str(ex))
            self.response_class.set_status(400)
            return self.response_class.instance

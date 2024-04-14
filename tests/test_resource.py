from src.resource.account_dao import AccountDAODatabase, AccountDAOMemory
from tests.conftest import Account


def test_save_and_get_by_id(account):
    account_dao = AccountDAODatabase()
    account_dao.save_account(account)

    saved_account = account_dao.get_account_by_id(account.account_id)
    new_account = Account(*saved_account)
    assert new_account.account_id == account.account_id
    assert new_account.email == account.email


def test_save_and_get_by_email(account):
    account_dao = AccountDAODatabase()
    account_dao.save_account(account)

    saved_account = account_dao.get_account_by_email(account.email)
    new_account = Account(*saved_account)
    assert new_account.account_id == account.account_id
    assert new_account.email == account.email

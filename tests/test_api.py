import json

import requests


def test_criar_passageiro(account_passageiro_dict):
    response_post = requests.post(
        'http://localhost:8000/signup',
        data=json.dumps(account_passageiro_dict)
    )
    assert response_post.status_code == 200
    account = response_post.json()
    assert account['account_id'] is not None
    print(account)
    account_id = account['account_id']
    response_get = requests.get(f'http://localhost:8000/accounts/{account_id}')
    assert response_get.status_code == 200
    account_get = response_get.json()
    assert account_get['email'] == account_passageiro_dict['email']

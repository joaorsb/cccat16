from collections import namedtuple

Account = namedtuple('Account', ['account_id', 'name', 'email', 'cpf', 'car_plate', 'is_passenger', 'is_driver'])
AccountSignup = namedtuple('AccountSignup', ['name', 'email', 'cpf', 'car_plate', 'is_passenger', 'is_driver'])

import logging
import re


logger = logging.Logger('validate_cpf')
FACTOR_FIRST_DIGIT = 10
FACTOR_SECOND_DIGIT = 11


def validate_cpf(raw_cpf: str) -> True:
    if not raw_cpf:
        return False
    cpf = remove_non_digits(raw_cpf)
    if not is_valid_length(cpf):
        return False
    if all_digits_equal(cpf):
        return False
    first_digit = calculate_digit(cpf, FACTOR_FIRST_DIGIT)
    second_digit = calculate_digit(cpf, FACTOR_SECOND_DIGIT)
    return extract_digit(cpf) == f'{first_digit}{second_digit}'


def remove_non_digits(raw_cpf: str) -> str:
    return re.sub("[^0-9]", "", raw_cpf)


def is_valid_length(cpf):
    return len(cpf) == 11


def all_digits_equal(cpf):
    return len(set(cpf)) == 1


def calculate_digit(cpf: str, factor: int) -> int:
    total = 0
    for digit in cpf:
        if factor > 1:
            total += int(digit) * factor
            factor -= 1
    remainder = total % 11
    return 0 if remainder < 2 else 11 - remainder


def extract_digit(cpf: str) -> str:
    return cpf[9:]

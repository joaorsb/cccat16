import logging
import re
logger = logging.Logger('validate_cpf')

class Cpf():
    FACTOR_FIRST_DIGIT = 10
    FACTOR_SECOND_DIGIT = 11
    value: str

    def __init__(self, cpf) -> None:
        if not self.validate_cpf(cpf):
            raise Exception("Invalid CPF")
        self.value = cpf
        
    def validate_cpf(self, raw_cpf: str) -> True:
        if not raw_cpf:
            return False
        cpf = self.remove_non_digits(raw_cpf)
        if not self.is_valid_length(cpf):
            return False
        if self.all_digits_equal(cpf):
            return False
        first_digit = self.calculate_digit(cpf, self.FACTOR_FIRST_DIGIT)
        second_digit = self.calculate_digit(cpf, self.FACTOR_SECOND_DIGIT)
        return self.extract_digit(cpf) == f'{first_digit}{second_digit}'

    def remove_non_digits(self, cpf: str) -> str:
        return re.sub("[^0-9]", "", cpf)

    def is_valid_length(self, cpf):
        return len(cpf) == 11

    def all_digits_equal(self, cpf):
        return len(set(cpf)) == 1

    def calculate_digit(self, cpf: str, factor: int) -> int:
        total = 0
        for digit in cpf:
            if factor > 1:
                total += int(digit) * factor
                factor -= 1
        remainder = total % 11
        return 0 if remainder < 2 else 11 - remainder

    def extract_digit(self, cpf: str) -> str:
        return cpf[9:]

class Email():
    value: str

    def __init__(self, email: str) -> None:
        if '@' not in email:
            raise Exception('Invalid email')
        self.value = email

    def get_value(self):
        return self.value
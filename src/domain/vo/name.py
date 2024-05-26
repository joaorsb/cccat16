class Name():
    value: str

    def __init__(self, name) -> None:
        if ' ' not in name:
            raise Exception('Invalid name')
        self.value = name

    def get_value(self):
        return self.value
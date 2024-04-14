from abc import ABCMeta, abstractmethod


class MailerGateway(metaclass=ABCMeta):
    @abstractmethod
    def send(recipient: str, subject: str, content: str):
        pass


class MailerGatewayMemory(MailerGateway):
    def send(self, recipient: str, subject: str, content: str):
        print(recipient, subject, content)

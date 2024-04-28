from abc import ABCMeta, abstractmethod


class HttpServer(metaclass=ABCMeta):
    @abstractmethod
    def register():
        pass

    @abstractmethod
    def initialize_router(method: str, url: str, callback: any):
        pass


class AbstractResponse(metaclass=ABCMeta):
    @abstractmethod
    def get_class():
        pass

    @abstractmethod
    def set_status(status: int):
        pass

    @abstractmethod
    def set_content(content: str):
        pass

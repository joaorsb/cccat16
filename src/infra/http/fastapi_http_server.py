from fastapi import FastAPI, APIRouter, Response

from src.infra.http.http_server import HttpServer, AbstractResponse


class FastAPIAdapter(HttpServer):
    app: None
    router: None

    def __init__(self) -> None:
        self.app = FastAPI()
        self.router = APIRouter()

    def register(self):
        self.app.include_router(self.router)

    def initialize_router(self, method: str, url: str, callback: any, response_model: any = None):
        self.router.add_api_route(
            url,
            endpoint=callback,
            methods=[method],
            callbacks=[callback],
            response_model=response_model
        )


class FastAPIResponse(AbstractResponse):
    instance = None
    status = 200

    def __init__(self) -> None:
        super().__init__()
        if not self.instance:
            self.get_class()

    def get_class(self):
        self.instance = Response()

    def set_status(self, status: int):
        self.instance.status_code = status

    def set_content(self, content: str):
        self.instance.content = content

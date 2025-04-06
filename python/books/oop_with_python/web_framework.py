from typing import override
from typing import ByteString


class HttpRequest:
    def __init__(self, method: str, path: str, headers: dict[str, str] | None = None, body: ByteString | None = None):
        self.method: str = method
        self.path: str = path
        self.headers: dict[str, str] = headers or {}
        self.body: ByteString = body or b''


class HttpResponse:
    def __init__(self, status_code: int = 200, headers: dict[str, str]|None = None, body: ByteString = b''):
        self.status_code: int = status_code
        self.headers: dict[str, str] = headers or {}
        self.body: ByteString = body or b''


class BaseController:
    def __init__(self, request: str) -> None:
        self.request: str = request

    def handler_request(self) -> None:
        raise NotImplementedError


class Route:
    def __init__(self, path: str, controller_cls: str) -> None:
        self.path: str = path
        self.controller_cls: str = controller_cls


class Router:
    def __init__(self):
        self.routes: list[str] = []

    def add_route(self, path: str, controller_cls: str) -> None:
        self.routes.append(Route(path, controller_cls))

    def route(self, request: str) -> str | None:
        for route in self.routes:
            if route.path == request.path:
                return route.controller_cls(request)

        return None


# Example usage:
router: Router = Router()


class HelloController(BaseController):
    @override
    def handler_request(self):
        return HttpResponse(body=b'Hello, world!')

router.add_route('/hello', HelloController)

request: HttpRequest = HttpRequest('GET', '/hello')
controller: Router = router.route(request)

if controller:
    response: Route = controller.handler_request()
    print(response.body.decode())

class HttpRequest:
    def __init__(self, method, path, headers=None, body=None):
        self.method = method
        self.path = path
        self.headers = headers or {}
        self.body = body or b''


class HttpResponse:
    def __init__(self, status_code=200, headers=None, body=b''):
        self.status_code = status_code
        self.headers = headers or {}
        self.body = body


class BaseController:
    def __init__(self, request):
        self.request = request

    def handle_request(self):
        raise NotImplementedError


class Route:
    def __init__(self, path, controller_cls):
        self.path = path
        self.controller_cls = controller_cls


class Router:
    def __init__(self):
        self.routes = []

    def add_route(self, path, controller_cls):
        self.routes.append(Route(path, controller_cls))

    def route(self, request):
        for route in self.routes:
            if route.path == request.path:
                return route.controller_cls(request)
        return None


router = Router()

from http.server import BaseHTTPRequestHandler
from ..resources.routes import routes_list


class MainHandler(BaseHTTPRequestHandler):
    print(routes_list)

    def parse_path(self):
        for route in routes_list:
            if self.path in route["path"]:
                self.controller_request = route["controller"]
                return self.controller_request

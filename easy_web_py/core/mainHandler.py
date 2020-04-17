from http.server import BaseHTTPRequestHandler
from resources.routes import routes_list


class MainHandler(BaseHTTPRequestHandler):

    def do_print(self):
        print(self.path)
        print(routes_list)

from http.server import BaseHTTPRequestHandler


class MainHandler(BaseHTTPRequestHandler):

    def get_routes_list(self, routes_list):
        print(routes_list)

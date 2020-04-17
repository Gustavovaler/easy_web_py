from http.server import HTTPServer, BaseHTTPRequestHandler
from urls.router import Router


def run(server=HTTPServer, handler=BaseHTTPRequestHandler):
    server_adress = ('', 8000)
    httpd = server(server_adress, Router)
    httpd.serve_forever()


if __name__ == "__main__":
    print('Runnig on localhost:8000')
    run()

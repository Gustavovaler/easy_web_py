from core.mainHandler import MainHandler
from resources.routes import routes_list


class Router(MainHandler):

    def get_routes(self, routes_list):
        self.routes_list = routes_list

    def do_GET(self):
        message = "<h1>Hola  todos</h1>"
        super().do_print()

        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(message.encode('utf-8'))

    # Según la ruta que viene desde el request
    # asigna la respuesta al controlador indicado en
    #  resources->routes->routes_list
    def call_controller(self):
        pass

    def prepare_response(self):
        pass

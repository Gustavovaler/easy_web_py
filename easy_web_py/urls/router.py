from core.mainHandler import MainHandler


class Router(MainHandler):

    def do_GET(self):
        self.call_controller(super().parse_path())

    # Según la ruta que viene desde el request
    # asigna la respuesta al controlador indicado en
    #  resources->routes->routes_list

    def call_controller(self, path):
        
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        # self.wfile.write(message.encode('utf-8'))

    def prepare_response(self):
        pass

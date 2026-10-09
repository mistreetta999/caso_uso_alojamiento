from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Configurar la respuesta exitosa
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()

        # Enrutar la URL a la función correspondiente
        if self.path == "/":
            self.wfile.write(b"Pagina principal")
        elif self.path == "/saludo":
            self.wfile.write(b"Ejecutando funcion saludo")
        else:
            self.wfile.write(b"Ruta no encontrada")

# Iniciar el servidor en el puerto 8000
if __name__ == "__main__":
    servidor = HTTPServer(("localhost", 8000), MyHandler)
    print("Servidor corriendo en http://localhost:8000")
    servidor.serve_forever()

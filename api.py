# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 21:08:13 2024

@author: Marcell
"""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == 'api':
            try:
                # Leer el archivo JSON
                with open('data.json') as json_file:
                    data = json.load(json_file)
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps(data).encode('utf-8'))
            except FileNotFoundError:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(b'{"error": "Internal Server Error: data.json not found."}')
            except json.JSONDecodeError:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(b'{"error": "Internal Server Error: data.json is not valid JSON."}')
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'{"error": "Not Found"}')

def run(server_class=HTTPServer, handler_class=RequestHandler):
    server_address = ('', 5000)  # Escuchar en el puerto 5000
    httpd = server_class(server_address, handler_class)
    print('Iniciando servidor en http://localhost:5000')
    httpd.serve_forever()

if __name__ == "__main__":
    run()

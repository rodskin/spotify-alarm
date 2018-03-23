#!/usr/bin/python3

import http.server
import os

PORT = 8080
server_address = ("", PORT)
WEB_SERVER_PATH = os.path.dirname(os.path.realpath(__file__))
WEB_SERVER_TEMPLATES_PATH = '/'
print(WEB_SERVER_TEMPLATES_PATH)

server = http.server.HTTPServer
handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = [WEB_SERVER_TEMPLATES_PATH]
print("Serveur actif sur le port :", PORT)

httpd = server(server_address, handler)
httpd.serve_forever()
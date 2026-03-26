import http.server
import os

os.chdir("/Users/vonmattmartin/Desktop/ERG")
handler = http.server.SimpleHTTPRequestHandler
with http.server.HTTPServer(("", 3000), handler) as httpd:
    httpd.serve_forever()

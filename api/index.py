import os
import sys
sys.path.append(os.path.dirname(__file__))
from http.server import BaseHTTPRequestHandler
from weatheraio import runWeatheraio
from cy import runCy
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('charset', 'utf-8')
        self.end_headers()
        self.wfile.write(b'<meta http-equiv=Content-Type content="charset=UTF-8">')
        self.wfile.write(b'<style>*{text-align:center;font-size:120%}</style>')
        if self.path == '/api/weather':
            runWeatheraio(self)
        elif self.path == '/api/cy':
            runCy(self)
        return
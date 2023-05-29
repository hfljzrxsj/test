from http.server import BaseHTTPRequestHandler
import socket
import re

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('103.239.245.166', 38712))
        sock.sendall(bytes([0x16, 0x00, 0xF3, 0x05, 0x0F, 0x31, 0x30, 0x33, 0x2E, 0x32, 0x33, 0x39, 0x2E, 0x32, 0x34, 0x35, 0x2E, 0x31, 0x36, 0x36, 0x97, 0x38, 0x01, 0x01, 0x00]))
        data = b''
        while True:
            buf = sock.recv(1024)
            if not buf:
                break
            data += buf
            if b'}}' in data:
                break
        result = str(data)
        online_pattern = re.compile(r'"online":(\d+)')
        name_pattern = re.compile(r',"name":"(.*?)"')
        online_matches = online_pattern.finditer(result)
        name_matches = name_pattern.finditer(result)
        self.send_response(200)
        self.send_header('Content-Type', 'text/html;charset=utf-8')
        self.end_headers()
        self.wfile.write('<style>*{text-align:center}</style>'.encode())
        for i, match in enumerate(name_matches, 1):
            self.wfile.write(f'<h2>{i}. {match.group(1)}</h2>'.encode())
        for match in online_matches:
            self.wfile.write(f'<h1>&#x5728;&#x7ebf;&#x4eba;&#x6570;&#xff1a;{match.group(1)}</h1>'.encode())
        sock.close()
        return
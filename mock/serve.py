import os
import socketserver
import http.server

PORT = int(os.environ.get("PORT", 3001))
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def log_message(self, format, *args):
        print(f"[{self.address_string()}] {format % args}", flush=True)

    def end_headers(self):
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Connection", "close")
        super().end_headers()

class ThreadedServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True
    daemon_threads = True

with ThreadedServer(("", PORT), Handler) as httpd:
    print(f"Serving ClosetFit mock on http://localhost:{PORT}", flush=True)
    httpd.serve_forever()

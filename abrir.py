import http.server, os, threading, webbrowser
from pathlib import Path
os.chdir(Path(__file__).parent)
try:
    server=http.server.ThreadingHTTPServer(('127.0.0.1',8897),http.server.SimpleHTTPRequestHandler)
except OSError:
    webbrowser.open('http://127.0.0.1:8897/')
else:
    threading.Timer(0.5,lambda:webbrowser.open('http://127.0.0.1:8897/')).start()
    server.serve_forever()

import os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.argv = ['server', '8787']
import http.server
http.server.test(HandlerClass=http.server.SimpleHTTPRequestHandler, port=8787)

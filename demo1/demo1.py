import sys
import locale
import SimpleHTTPServer
import SocketServer
addr = "10.104.153.135"
port = 8080

handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer((addr, port), handler)
print ("HTTP server is at: http://%s:%d/" % (addr, port))
try:
    httpd.serve_forever()
except:
    pass

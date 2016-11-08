import sys
import locale
import SimpleHTTPServer
import SocketServer
addr = "127.0.0.1"
port = 80

handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer((addr, port), handler)
print ("HTTP server is at: http://%s:%d/" % (addr, port))
httpd.serve_forever()

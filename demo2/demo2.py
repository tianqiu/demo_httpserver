import os
import socket
import sys

HTTPIP = "10.104.153.135"
HTTPLISTEN = 8080

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind((HTTPIP, HTTPLISTEN))
serversocket.listen(5)

while True:
    try:
        connection,address = serversocket.accept()
        httprequest = connection.recv(1024)
        print httprequest + "------------------------------------------------------"
        httpresponse = "hello world,this is demo2"
        connection.send(httpresponse)
        connection.close()
    except:
        serversocket.close()


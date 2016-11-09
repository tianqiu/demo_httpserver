import os
import socket
import sys
import time

HTTPIP = "10.104.153.135"
HTTPLISTEN = 8080
cwd = os.getcwd()+"/www"


def dealcgi(path,cgican):
    try:
        print "cmd = " + "python "+cwd+path+" "+cgican
        ff = os.popen("python "+cwd+path+" "+cgican).read()
        print ff
    except:
        ff = "none"
    return ff


def dealresponse(request):
    method=request.split(' ')[0]
    url=request.split(' ')[1]
    path=url.split('?')[0]
    print method,url,path 
    can = ""
    cgican = " "
    try:
        can = url.split("?")[1]
        cgican = can.replace("&","\&")
        print "\ncgican  =  "+cgican
    except:
        pass
    
    type = path.split('.')[-1]
    if type == "py":
        return dealcgi(path,cgican)

    head="HTTP/1.1 200 OK\r\n"
    head+="Date:"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) +"\r\n"
    head+="Server:server of qiutian\r\n"
    head+="Content-Length:"+str(os.path.getsize(cwd+path))+"\r\n"
    head+="Content-Type: text/html\r\n\r\n"

    f = open(cwd + path,"r")
    html = f.read()
    f.close()

    return head+html 






serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind((HTTPIP, HTTPLISTEN))
serversocket.listen(5)

try:
    while True:
        connection,address = serversocket.accept()
        httprequest = connection.recv(1024)
        print httprequest + "\n------------------------------------------------------\n"
        httpresponse = dealresponse(httprequest)
        connection.send(httpresponse)
        connection.close()
except:
    serversocket.close()


from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

def file_download():
    handle = open("ZeroMQ-4.0.4_miru1.0-x64.exe",'rb')
    return xmlrpc.client.Binary(handle.read())
    handle.close()

server = SimpleXMLRPCServer(('localhost',8000))
print ("Listening on port 8000")

server.register_function(file_download,'download')

server.serve_forever()
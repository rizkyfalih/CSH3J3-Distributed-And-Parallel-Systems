from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

def file_download(): #membuat fungsi file_download
    handle = open("ZeroMQ-4.0.4_miru1.0-x64.exe",'rb') #menginisialisasi file yang bisa di download
    return xmlrpc.client.Binary(handle.read()) #mengeluarkan output berupa binner yang bisa dibaca
    handle.close()

server = SimpleXMLRPCServer(('10.20.2.87',8000)) #menginisialisasi server
print ("Listening on port 8000") #melakukan listening ketika server dijalankan

server.register_function(file_download,'download') #meregistrasi fungsi download

server.serve_forever() #server akan selalu menyala hingga dimatikan oleh pengguna
import xmlrpc
import xmlrpc.client

proxy = xmlrpc.client.ServerProxy('http://192.168.1.8:8000') # initialization the network and the port
handle = open("File2.txt","wb") # find the file in server ('The file must be in server/1 folder in server')
handle.write(proxy.download().data) # download the file from server
handle.close() # close the handle when the file was downloaded 

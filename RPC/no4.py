import xmlrpc
import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://10.20.2.87:8000")
handle = open("fetched_file.txt","wb")
handle.write(proxy.download().data)
handle.close()


with open("tugasb.txt",'rb') as handle:
    data = xmlrpc.client.Binary(handle.read())
    handle.close()
    result = proxy.file_upload(data)


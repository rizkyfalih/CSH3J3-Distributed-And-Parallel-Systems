from xmlrpc.server import SimpleXMLRPCServer

def file_upload(filedata): # initialize 'file_upload' function in server
    with open("uploaded_file.txt",'wb') as handle:
        data1=filedata.data #convert from byte to binary IMPORTANT!
        handle.write(data1)
        handle.close()
        return True  #IMPORTANT
# must have return value
# else error messsage: "cannot marshal None unless allow_none is enabled"

server = SimpleXMLRPCServer(('192.168.1.8',8000)) # initialize the network and port
print ("Listening on port 8000") # the output when the server is running

server.register_function(file_upload,'file_upload') # registered the file_download function with new initialize 'download'

server.serve_forever() # server will run forever, until we interrupt it
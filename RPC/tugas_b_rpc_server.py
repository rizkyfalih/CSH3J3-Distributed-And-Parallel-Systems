from xmlrpc.server import SimpleXMLRPCServer

def file_upload(filedata): #menginisialisasi file yang di upload
    with open("uploaded_file.txt",'wb') as handle:
        data1=filedata.data #convert from byte to binary IMPORTANT!
        handle.write(data1)
        handle.close()
        return True  #IMPORTANT
# must have return value
# else error messsage: "cannot marshal None unless allow_none is enabled"

server = SimpleXMLRPCServer(('10.20.2.87',8000)) #menginisialisasi server
print ("Listening on port 8000") #mengeluar kan output listening ketika server sedang berjalan

server.register_function(file_upload,'file_upload') #meregistrasi fungsi upload ke server

server.serve_forever() #Server akan selalu berjalan hingga dimatikan oleh admin
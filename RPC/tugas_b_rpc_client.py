import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://10.20.2.87:8000")#inisiasi jaringan dan port yang akan di koneksi
with open("File2.txt",'rb') as handle: #membuka File2.txt yang sudah di buat (1 folder)
    data = xmlrpc.client.Binary(handle.read()) #membaca isi data yang ada di File2.txt. Kemudian mengubah isi data tersebut ke biner 
    handle.close() #menutup File2.txt
    result = proxy.file_upload(data) #melakukan upload data yg berisikan biner ke dalam proxy
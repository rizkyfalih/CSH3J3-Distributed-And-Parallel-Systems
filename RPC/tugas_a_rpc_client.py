import xmlrpc
import xmlrpc.client

proxy = xmlrpc.client.ServerProxy('http://10.20.2.87:8000') #inisiasi jaringan dan port yang akan di koneksi
handle = open("fetched_file.txt","wb") # membuka file fetched_file.txt dan menyimpannya di variable handle
handle.write(proxy.download().data) #menulis isi dari fetched_file.txt yang akan/telah di download dari proxy
handle.close() #menutup fetched_file.txt 

with open("File2.txt",'rb') as handle: #membuka File2.txt yang sudah di buat (1 folder)
    data = xmlrpc.client.Binary(handle.read()) #membaca isi data yang ada di File2.txt. Kemudian mengubah isi data tersebut ke biner 
    handle.close() #menutup File2.txt
    result = proxy.file_upload(data) #melakukan upload data yg berisikan biner ke dalam proxy
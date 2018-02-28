import xmlrpc
import xmlrpc.client

proxy = xmlrpc.client.ServerProxy('http://10.20.2.87:8000') #inisiasi jaringan dan port yang akan di koneksi
handle = open("fetched_file.txt","wb") # membuka file fetched_file.txt dan menyimpannya di variable handle
handle.write(proxy.download().data) #menulis isi dari fetched_file.txt yang akan/telah di download dari proxy
handle.close() #menutup fetched_file.txt 

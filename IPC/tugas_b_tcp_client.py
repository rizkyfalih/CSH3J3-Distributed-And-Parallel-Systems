import socket

TCP_IP = '10.20.2.112'
TCP_PORT = 5005
BUFFER_SIZE = 1024
# PESAN = "Hello Mang!"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

handle = open("catatan.txt","rb")   #sebagai text biasa
#handle = open("test.txt","rb") # sebagai byte

pesan = handle.read(2) #membaca 2 byte

while pesan != b'': # End of file untuk text
#while data != b'': #End of File untuk byte
    #lakukan sesuatu misalkan print
    #print (pesan)
    s.send(pesan)
    pesan = handle.read(2) # membaca 2 byte selanjutnya


handle.close() # selalu tutup file jika sudah selesai digunakan



#s.send(pesan)
#data = s.recv(BUFFER_SIZE)
s.close()


#print ("pesan diterima:", data.decode())

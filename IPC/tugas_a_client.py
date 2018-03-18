import socket               
 
s = socket.socket()         
port = 3333               
s.connect(('192.168.1.8', port))
print (s.recv(1024).decode())
s.close() 
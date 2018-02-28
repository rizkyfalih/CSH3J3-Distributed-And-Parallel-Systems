import socket               
 
s = socket.socket()         
port = 3333               
s.connect(('10.20.2.112', port))
print (s.recv(1024).decode())
s.close() 
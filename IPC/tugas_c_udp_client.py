import socket

UDP_IP = "10.20.2.112"
UDP_PORT = 5005
PESAN = "Hello Mang!"

print ("target IP:", UDP_IP)
print ("target port:", UDP_PORT)
print ("pesan:", PESAN)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(PESAN.encode(), (UDP_IP, UDP_PORT))
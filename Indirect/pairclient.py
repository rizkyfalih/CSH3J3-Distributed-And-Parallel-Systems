import zmq #melakukan import library zeromq
import random #melakukan import library random
import sys #melakukan import library sys
import time #melakukan import library time

context = zmq.Context() #melakukan inisialisasi context zeromq pada variable context
socket = context.socket(zmq.PAIR) #melakukan insisalisasi socket dengan fungsi pair pada variable socket
socket.connect("tcp://10.20.32.221:5556") #melakukan konreksi socket dengan alamat tcp://localhost:5556

while True: #perulangan apabila benar
    msg = socket.recv() #menyimpan pesan yang diterima dari socket ke dalam variabel msg
    print (msg) #melakukan print msg
    socket.send("client message 1 to server".encode()) #melakukan pengiriman pesan 1 kemudian di encode ke dalam socket
    socket.send("client message 2 to server".encode()) #melakukan pengiriman pesan 2 kemudian di encode ke dalam socket
    time.sleep(1) #melakukan interval istirahat untuk proses selanjutnya


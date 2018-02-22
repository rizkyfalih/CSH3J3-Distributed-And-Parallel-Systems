import zmq #melakukan import library zeromq
import random #melakukan import library random
import sys #melakukan import library sys
import time #melakukan import library time

context = zmq.Context() #melakukan inisialisasi context zeromq pada variable context
socket = context.socket(zmq.PAIR) #melakukan insisalisasi socket dengan fungsi pair pada variable socket
socket.bind("tcp://10.20.32.221:5556") #melakukan binding pada socket dengan port tcp 5556

while True: #perulangan apabila kondisi benar
    socket.send("Server message to client".encode()) #mengirimkan pesan untuk client ke dalam socket kemudian di encode
    msg = socket.recv() #menyimpan pesan yang diterima dari socket ke dalam variable msg
    print (msg) #melakukan print msg
    time.sleep(1) #melakukan istirahat untuk proses berikutnya
 
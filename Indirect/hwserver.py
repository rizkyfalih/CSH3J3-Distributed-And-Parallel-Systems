import time #melakukan import library time
import zmq #melakukan import library ZeroMQ

context = zmq.Context() #melakukan inisialisasi context ZeroMQ pada variable context 
socket = context.socket(zmq.REP) #menginisialisasikan socket(Reply) pada variable context(ZeroMQ)
socket.bind("tcp://10.20.32.221:5555") #melakukan binding socket dengan port tcp 5555

while True: #Looping selama kondisi benar

    message = socket.recv() #menampung pesan yang diterima oleh socket ke dalam variable message
    print("Received request: %s" % message) #melakukan output dari message yang diterima

	# do some work
    time.sleep(1) #waktu interval untuk istirahat/melakukan proses berikutnya


    socket.send(b"World") #mengirim suatu pesan berupa bit pesan ('world') ke dalam socket

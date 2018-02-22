
import zmq #mealkukan import library ZeroMQ

context = zmq.Context() #melakukan inisisalisai context ZeroMQ pada variable context


print("Connecting to hello world server...") #melakukan print string sesuai yang akan dioutputkan
socket = context.socket(zmq.REQ) #menginisialisasi socket pada ZeroMQ dengan fungsi Request pada variabel socket
socket.connect("tcp://10.20.32.221:5555") #melakukan koneksi pada tcp://localhost:5555


for request in range(10): #melakukan perulangan sebanyak 10 kali
    print("Sending request %s ..." % request) # melakukan print sending request dan merequest ke server
    socket.send(b"Hello") #melakukan sending bit berupa pesan ('hello') ke dalam socket


    message = socket.recv() #menginisialisasi pesan yang diterima dari socket ke dalam variable message
    print("Received reply %s [ %s ]" % (request, message)) #melakukan print revived berupa message dan request

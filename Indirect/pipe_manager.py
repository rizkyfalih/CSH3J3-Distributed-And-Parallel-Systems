import zmq #import library zeromq
import time #import library time

context = zmq.Context() #insialisasi konteks zeromq pada variabel konteks

sock = context.socket(zmq.PUSH) #menginisialisasi socket dengan fungsi push pada variable sock
sock.bind("tcp://10.20.32.221:5690") #melakukan bindig socket sesuai ip dan port yang akan dijadikan server

id = 0 #inisialisasi variable id 

while True: #perulangan apabila status true
    time.sleep(1) #melakukan proses istirahat
    id, now = id+1, time.ctime() #menginisialisasi variabel id dan now
    message = "{id} - {time}".format(id=id, time=now) #menginisialisasi variable message
    sock.send(message.encode()) #mengirim pesan kemudian di encode ke dalam socket
    print ("Sent: {msg}".format(msg=message)) #melakukan print pesan terkirim
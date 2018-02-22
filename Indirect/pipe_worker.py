import zmq #import library zeromq

context = zmq.Context() #insialisasi konteks zeromq pada variabel konteks

sock = context.socket(zmq.PULL) #menginisialisasi socket dengan fungsi pull dengan variable sock
sock.connect("tcp://10.20.32.221:5690") #melakukan koneksi pada socket dengan ip dan port tertentu

while True: #melakukan perulangan apabila kondisi true
    message = sock.recv() #menerima pesan yang diterima dari socket dan menyimpannya di variable message
    print ("Received: {msg}".format(msg=message)) #melakukan print pesan yang diterima
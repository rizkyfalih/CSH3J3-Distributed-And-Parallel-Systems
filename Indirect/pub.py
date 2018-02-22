import zmq
import time

context = zmq.Context()

sock = context.socket(zmq.PUB)
sock.bind("tcp://127.0.0.1:5680")

id = 0

while True:
    time.sleep(1)
    id, now = id+1, time.ctime()

    message = "1-Update! >> #{id} >> {time}".format(id=id, time=now)
    sock.send(message.encode('ascii'))

    message = "2-Update! >> #{id} >> {time}".format(id=id, time=now) 
    sock.send(message.encode('ascii'))

    id += 1
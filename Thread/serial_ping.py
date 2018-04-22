import os, re
import time

start = time.time()
received_packages = re.compile(r"Received = (\d)")
status = ("no response","alive but losses","alive")

for suffix in range(1,3):
    ip = "XXX.XXX.X."+str(suffix) # Change XXX.XXX.X your ip address
    ping_out = os.popen("ping -n 2 "+ip,"r")
    print(("... pinging ",ip))

    while True:
        line = ping_out.readline()
        if not line: break
        n_received = received_packages.findall(line)
        if n_received:
            print((ip + ": " + status[int(n_received[0])]))

end = time.time()
print((end-start))

"""
windows: ping x.x.x.x -n 2
received_packages = re.compile(r"Received = (\d)")
melihat Received = xxx (desimal)

Pinging 10.30.32.16 with 32 bytes of data:
Reply from 10.30.32.16: bytes=32 time<1ms TTL=128
Reply from 10.30.32.16: bytes=32 time<1ms TTL=128

Ping statistics for 10.30.32.16:
    Packets: Sent = 2, Received = 2, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms
"""


"""
received_packages = re.compile(r"(\d) received")

$ ping -q -c2 192.168.178.26
PING 192.168.178.26 (192.168.178.26) 56(84) bytes of data.

--- 192.168.178.26 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 999ms
rtt min/avg/max/mdev = 0.022/0.032/0.042/0.010 ms


$ ping -q -c2 192.168.178.23
PING 192.168.178.23 (192.168.178.23) 56(84) bytes of data.

--- 192.168.178.23 ping statistics ---
2 packets transmitted, 0 received, +2 errors, 100% packet loss, time 1006ms
"""

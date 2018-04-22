import os, re, threading
import time

class ip_check(threading.Thread):
    def __init__ (self,ip):
        threading.Thread.__init__(self)
        self.ip = ip
        self.__successful_pings = -1
    def run(self):
        ping_out = os.popen("ping -n 2 "+self.ip,"r")
        while True:
            line = ping_out.readline()
            if not line: break
            n_received = re.findall(received_packages,line)
            if n_received:
                self.__successful_pings = int(n_received[0])
    def status(self):
        if self.__successful_pings == 0:
            return "no response"
        elif self.__successful_pings == 1:
            return "alive, but 50 % package loss"
        elif self.__successful_pings == 2:
            return "alive"
        else:
            return "shouldn't occur"
            
received_packages = re.compile(r"Received = (\d)")

start = time.time()
check_results = []
for suffix in range(1,10):
    ip = "192.168.1."+str(suffix)
    current = ip_check(ip)
    check_results.append(current)
    current.start()

for el in check_results:
    el.join()
    print(("Status from ", el.ip,"is",el.status()))
end = time.time()
print((end-start))

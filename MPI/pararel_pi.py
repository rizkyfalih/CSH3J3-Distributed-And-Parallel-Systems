import time
from mpi4py import MPI
import math

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def Pi(num_steps, rank, size):
    start = time.time()
    step = 1.0/num_steps
    sum = 0
    if rank == 0:
        for i in range(0, math.floor(num_steps/size)):
            x= (i+0.5)*step
            sum = sum + 4.0/(1.0+x*x)
        for i in range(1, size):
            sum += comm.recv(source=i)
    else:
        for i in range(math.floor(num_steps/size * rank),math.floor((num_steps/size) * (rank+1))):
            x= (i+0.5)*step
            sum = sum + 4.0/(1.0+x*x)
        comm.send(sum, dest=0)
    pi = step * sum
    end = time.time()
    print ("Pi with %d steps is %f in %f secs" %(num_steps, pi, end-start))

if __name__ == '__main__':
    Pi(100000,rank,size)


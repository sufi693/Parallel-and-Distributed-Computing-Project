import numpy as np
from mpi4py import MPI
from do_something import do_something

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

array_size = 10
send_data = (rank + 1) * np.arange(array_size, dtype=np.int32)
recv_data = np.zeros(array_size, dtype=np.int32)

print(f"Process {rank} sending {send_data}")

# Reduce operation: sum across all processes
comm.Reduce(send_data, recv_data, root=0, op=MPI.SUM)

if rank == 0:
    results = []
    do_something(5, results)
    print(f"On task {rank}, after Reduce: data = {recv_data}, computed {len(results)} results")

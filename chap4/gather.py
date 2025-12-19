from mpi4py import MPI
from do_something import do_something

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
ROOT = 0

# Each process computes its own value
local_data = (rank + 1) ** 2

# Gather data at root
gathered_data = comm.gather(local_data, root=ROOT)

# Use imported CPU-bound function
results = []
do_something(5, results)

if rank == ROOT:
    print(f"Rank {rank}: gathered data = {gathered_data}, computed {len(results)} results")
    for i in range(1, size):
        print(f" Process {rank} received {gathered_data[i]} from process {i}")

from mpi4py import MPI
from do_something import do_something

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
ROOT = 0

# Define data only at root
data_to_scatter = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] if rank == ROOT else None

# Scatter the data
recvbuf = comm.scatter(data_to_scatter, root=ROOT)

# Perform CPU-bound task
results = []
do_something(recvbuf, results)

print(f"Process {rank}: received {recvbuf}, computed {len(results)} results")

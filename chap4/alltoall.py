from mpi4py import MPI
import numpy as np
from do_something import do_something


comm = MPI.COMM_WORLD
world_size = comm.Get_size()
rank = comm.Get_rank()

# Prepare data for Alltoall communication
send_data = (rank + 1) * np.arange(world_size, dtype=int)
recv_data = np.empty(world_size, dtype=int)

comm.Alltoall(send_data, recv_data)

# Use the imported CPU-bound function
results = []
do_something(5, results)

print(
    f"Process {rank}: "
    f"sent={send_data}, "
    f"received={recv_data}, "
    f"computed_items={len(results)}"
)

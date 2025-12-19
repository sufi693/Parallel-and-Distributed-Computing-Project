from mpi4py import MPI
from do_something import do_something

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
ROOT = 0

# Value defined only at root process
shared_value = 100 if rank == ROOT else None

# Broadcast value to all processes
shared_value = comm.bcast(shared_value, root=ROOT)

# Use imported CPU-bound function
results = []
do_something(shared_value // 10, results)

print(
    f"Process {rank}: "
    f"shared_value={shared_value}, "
    f"computed_results={len(results)}"
)

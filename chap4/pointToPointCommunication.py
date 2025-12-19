from mpi4py import MPI
from do_something import do_something

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print("My rank is:", rank)

# Point-to-point communication
if rank == 0:
    data = 10000000
    destination = 4
    comm.send(data, dest=destination)
    print(f"Process {rank}: sent data {data} to process {destination}")

elif rank == 1:
    data = "hello"
    destination = 8
    comm.send(data, dest=destination)
    print(f"Process {rank}: sent data '{data}' to process {destination}")

elif rank == 4:
    data = comm.recv(source=0)
    print(f"Process {rank}: received {data} from process 0")

elif rank == 8:
    data = comm.recv(source=1)
    print(f"Process {rank}: received {data} from process 1")

# Use imported CPU-bound function
results = []
do_something(5, results)
print(f"Process {rank}: computed {len(results)} results")

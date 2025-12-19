from mpi4py import MPI
from do_something import do_something

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

print("My rank is", rank)

if rank == 1:
    send_data = "a"
    partner = 5

    recv_data = comm.sendrecv(send_data, dest=partner, source=partner)

    results = []
    do_something(5, results)

    print(
        f"Process {rank}: "
        f"sent {send_data} to {partner}, "
        f"received {recv_data}, "
        f"computed {len(results)} results"
    )

elif rank == 5:
    send_data = "b"
    partner = 1

    recv_data = comm.sendrecv(send_data, dest=partner, source=partner)

    results = []
    do_something(5, results)

    print(
        f"Process {rank}: "
        f"sent {send_data} to {partner}, "
        f"received {recv_data}, "
        f"computed {len(results)} results"
    )

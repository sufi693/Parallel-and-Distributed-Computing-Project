from mpi4py import MPI
import numpy as np
import math

# Neighbor directions
UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3
neighbour_processes = [0, 0, 0, 0]

# Worker Function

def do_something(size, out_list):
    """
    Perform a CPU-bound task: calculate squares after an expensive operation.
    """
    for i in range(size):
        result = math.sqrt(i) ** 2  # Simulate computation
        out_list.append(result)
    return out_list



# Main MPI Execution

if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    # Build grid topology
    grid_row = int(np.floor(np.sqrt(size)))
    grid_column = size // grid_row

    if grid_row * grid_column > size:
        grid_column -= 1
    if grid_row * grid_column > size:
        grid_row -= 1

    if rank == 0:
        print(f"\nBuilding a {grid_row} x {grid_column} grid topology:\n")

    # Create Cartesian communicator
    cart_comm = comm.Create_cart((grid_row, grid_column), periods=(True, True), reorder=True)

    # Get coordinates
    my_row, my_col = cart_comm.Get_coords(cart_comm.rank)

    # Find neighbors
    neighbour_processes[UP], neighbour_processes[DOWN] = cart_comm.Shift(0, 1)
    neighbour_processes[LEFT], neighbour_processes[RIGHT] = cart_comm.Shift(1, 1)

    print(f"Process {rank} | row={my_row}, col={my_col}")
    print(f"   UP: {neighbour_processes[UP]}, DOWN: {neighbour_processes[DOWN]}, LEFT: {neighbour_processes[LEFT]}, RIGHT: {neighbour_processes[RIGHT]}")

    # CPU-bound task
    output_list = []
    size_to_compute = 10 + rank  # vary work per process
    do_something(size_to_compute, output_list)

    print(f"Process {rank} completed do_something with {len(output_list)} results.\n")

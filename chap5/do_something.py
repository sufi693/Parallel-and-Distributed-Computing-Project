import math

def do_something(size, out_list):
    """
    Performs a CPU-bound task by calculating sqrt(i)^2
    and storing results in the output list.
    """
    for i in range(size):
        out_list.append(math.sqrt(i) ** 2)

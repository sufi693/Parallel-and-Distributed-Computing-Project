import math

def do_something(size, out_list):
    """
    Perform a CPU-bound task by calculating sqrt(i)^2
    and storing the results in the output list.
    """
    for i in range(size):
        result = math.sqrt(i) ** 2  # simulate CPU-heavy work
        out_list.append(result)

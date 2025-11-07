# do_something.py  (CPU-bound version)
import math

def do_something(size, out_list):
#   Perform a CPU-bound task: calculate squares of numbers after expensive math operations.
    for i in range(size):
        result = math.sqrt(i) ** 2  # simulate CPU-heavy work
        out_list.append(result)
import math

def do_something(size, out_list):
    for i in range(size):
        result = math.sqrt(i) ** 2
        out_list.append(result)

if __name__ == "__main__":
    results = []
    do_something(10000, results)
    print(f"Computed {len(results)} results.")

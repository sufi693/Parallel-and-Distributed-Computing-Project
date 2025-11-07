import multiprocessing
from do_something import do_something

def myFunc(i):
    print(f"Starting process {i}")
    out_list = multiprocessing.Manager().list()
    do_something(i * 1000, out_list)
    print(f"Process {i} finished with {len(out_list)} results.\n")

if __name__ == '__main__':
    processes = []

    for i in range(6):
        p = multiprocessing.Process(target=myFunc, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("All processes completed.")

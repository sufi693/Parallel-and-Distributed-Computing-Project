import multiprocessing
import time
from do_something import do_something

if __name__ == '__main__':
    size = 1000
    out_list1 = multiprocessing.Manager().list()
    out_list2 = multiprocessing.Manager().list()

    p1 = multiprocessing.Process(name='Process 1', target=do_something, args=(size, out_list1))
    p2 = multiprocessing.Process(target=do_something, args=(size, out_list2))

    start_time = time.time()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end_time = time.time()

    print(f'Process 1 output length: {len(out_list1)}')
    print(f'Process 2 output length: {len(out_list2)}')
    print(f'Total execution time: {end_time - start_time:.2f} seconds')

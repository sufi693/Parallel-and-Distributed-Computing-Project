import multiprocessing
import time
from do_something import do_something

def run_task():
    print('Process started...')
    out_list = multiprocessing.Manager().list()
    do_something(10, out_list)
    print(f'Process finished with {len(out_list)} results.')

if __name__ == '__main__':
    p = multiprocessing.Process(target=run_task)
    print('Before start:', p, p.is_alive())
    p.start()
    print('Running:', p, p.is_alive())
    time.sleep(2)
    p.terminate()
    print('Terminated:', p, p.is_alive())
    p.join()
    print('Joined:', p, p.is_alive())
    print('Exit code:', p.exitcode)

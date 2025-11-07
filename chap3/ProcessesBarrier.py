import multiprocessing
from multiprocessing import Barrier, Lock, Process
from time import time
from datetime import datetime
from do_something import do_something

def test_with_barrier(synchronizer, serializer):
    name = multiprocessing.current_process().name
    synchronizer.wait()
    now = time()
    with serializer:
        print(f"{name} ----> {datetime.fromtimestamp(now)}")
        results = []
        do_something(2, results)
        print(f"{name} results: {results}")

def test_without_barrier():
    name = multiprocessing.current_process().name
    now = time()
    print(f"{name} ----> {datetime.fromtimestamp(now)}")
    results = []
    do_something(2, results)
    print(f"{name} results: {results}")

if __name__ == '__main__':
    synchronizer = Barrier(2)
    serializer = Lock()

    Process(name='p1 - with_barrier', target=test_with_barrier, args=(synchronizer, serializer)).start()
    Process(name='p2 - with_barrier', target=test_with_barrier, args=(synchronizer, serializer)).start()
    Process(name='p3 - without_barrier', target=test_without_barrier).start()
    Process(name='p4 - without_barrier', target=test_without_barrier).start()

import multiprocessing
import time
from do_something import do_something

def sa():
    name = multiprocessing.current_process().name
    print(f"Starting {name}\n")

    if name == 'background_process':
        for i in range(5):
            print(f"--> {i}")
            time.sleep(0.3)
    else:
        results = []
        do_something(3, results)
        print(f"{name} results: {results}")
        time.sleep(1)

    print(f"Exiting {name}\n")

if __name__ == '__main__':
    background_process = multiprocessing.Process(
        name='background_process',
        target=sa
    )
    background_process.daemon = True

    normal_process = multiprocessing.Process(
        name='normal_process',
        target=sa
    )
    normal_process.daemon = False

    background_process.start()
    normal_process.start()

    background_process.join(timeout=2)
    normal_process.join()

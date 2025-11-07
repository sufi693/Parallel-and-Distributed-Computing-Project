import threading
import time
from do_something_v2 import do_something

def thread_job(tnum, task_load, shared_list, re_lock):
    """Thread safely re-enters the same lock before performing computation."""
    print(f"[Thread-{tnum}] initiated.")
    with re_lock:
        # demonstrating re-entrant locking (nested lock)
        with re_lock:
            do_something(task_load, shared_list)
    print(f"[Thread-{tnum}] completed.")

if __name__ == "__main__":
    shared_list = []
    re_lock = threading.RLock()

    total_threads = 3
    workload_size = 7

    workers = [
        threading.Thread(target=thread_job, args=(tid, workload_size, shared_list, re_lock))
        for tid in range(total_threads)
    ]

    for worker in workers:
        worker.start()
        time.sleep(0.4)  # short delay for clearer output sequence

    for worker in workers:
        worker.join()

    print("\n✅ Final Data List:", shared_list)
    print("📊 Total Items (RLock):", len(shared_list))

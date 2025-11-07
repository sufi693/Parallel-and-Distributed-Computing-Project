import threading
import time
from do_something_v2 import do_something

def thread_task(tid, chunk_size, shared_data, sem):
    """Thread acquires a semaphore permit before performing its task."""
    print(f"[Worker-{tid}] Requesting access...")
    with sem:
        print(f"[Worker-{tid}] Access granted. Processing...")
        do_something(chunk_size, shared_data)
        print(f"[Worker-{tid}] Task complete.")

if __name__ == "__main__":
    shared_data = []
    sem = threading.Semaphore(2)  # allow 2 threads to execute concurrently
    total_threads = 3
    data_size = 7

    threads = [
        threading.Thread(target=thread_task, args=(tid, data_size, shared_data, sem))
        for tid in range(total_threads)
    ]

    for th in threads:
        th.start()

    for th in threads:
        th.join()

    print("\n✅ Final Shared Data:", shared_data)
    print("📊 Total Elements (Semaphore):", len(shared_data))

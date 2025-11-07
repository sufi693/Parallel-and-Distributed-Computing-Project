import threading
import time
from do_something_v2 import do_something

def execute_job(tno, task_size, results, mutex):
    """Each thread executes a locked CPU-bound operation."""
    print(f"[Worker-{tno}] Execution started.")
    with mutex:
        do_something(task_size, results)
    print(f"[Worker-{tno}] Execution completed.")

if __name__ == "__main__":
    results = []
    mutex = threading.Lock()

    threads_count = 3
    work_units = 7

    workers = [
        threading.Thread(target=execute_job, args=(tno, work_units, results, mutex))
        for tno in range(threads_count)
    ]

    for worker in workers:
        worker.start()
        time.sleep(0.4)  # short delay for visible thread sequencing

    for worker in workers:
        worker.join()

    print("\n✅ Final Result List:", results)
    print("📊 Total Processed (Lock):", len(results))

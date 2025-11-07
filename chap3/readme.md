# 🧠 Python Multiprocessing — Practical Demonstrations

This repository contains a series of Python scripts that demonstrate key concepts of the **`multiprocessing`** module — including process creation, naming, synchronization, management, and termination.

Each example uses a CPU-bound function `do_something()` imported from `do_something.py`, which simulates computational work to test process behavior.

---

## ⚙️ 1. naming_processes.py

### **Purpose**

Illustrates how to explicitly name processes and compare execution times when running concurrently.

### **Core Example**

```python
process_with_name = multiprocessing.Process(
    name='do_something process 1',
    target=do_something,
    args=(1000, out_list1)
)
process_with_default_name = multiprocessing.Process(
    target=do_something,
    args=(1000, out_list2)
)
```

### **Sample Output**

```
Process 1 output list length: 1000
Process 2 output list length: 1000
Total execution time: 0.43 seconds
```

### **Key Insight**

Both processes executed the same task concurrently.
Execution time was significantly reduced compared to sequential runs.

---

## ⚙️ 2. spawning_processes.py

### **Purpose**

Demonstrates spawning multiple processes dynamically using a loop.

### **Core Example**

```python
for i in range(6):
    process = multiprocessing.Process(target=myFunc, args=(i,))
    process.start()
    process.join()
```

### **Sample Output**

```
calling do_something from process no: 0
Process 0 finished with 0 results.
calling do_something from process no: 1
Process 1 finished with 1000 results.
...
```

### **Key Insight**

Each process handled an independent workload (`i * 1000`), verifying that multiprocessing efficiently scales tasks.

---

## ⚙️ 3. killing_processes.py

### **Purpose**

Explains how to start, terminate, and join a process while tracking its lifecycle.

### **Core Example**

```python
p.start()
print('Process running:', p.is_alive())
p.terminate()
print('Process terminated:', p.is_alive())
p.join()
```

### **Sample Output**

```
Process running: True
Process terminated: False
Process joined: False
Exit code: 0
```

### **Key Insight**

Processes can be safely terminated and joined.
Exit code `0` confirms proper and successful shutdown.

---

## ⚙️ 4. run_background_processes_no_daemons.py

### **Purpose**

Shows the difference between **daemon** and **non-daemon** processes and their execution behavior.

### **Core Example**

```python
background_process.daemon = True
NO_background_process.daemon = False
```

### **Sample Output**

```
Starting background_process
---> 0
---> 1
---> 2
Starting NO_background_process
Results from do_something(): [0.0, 1.0, 2.0]
Exiting background_process
Exiting NO_background_process
```

### **Key Insight**

Daemon processes terminate when the main program exits,
while non-daemon processes continue to run independently until completion.

---

## ⚙️ 5. processes_barrier.py

### **Purpose**

Demonstrates process synchronization using a **Barrier** and **Lock**.

### **Core Example**

```python
synchronizer = Barrier(2)
serializer = Lock()
Process(name='p1 - test_with_barrier',
        target=test_with_barrier,
        args=(synchronizer, serializer)).start()
```

### **Sample Output**

```
process p3 - test_without_barrier ----> 2025-11-01 00:27:31
p3 results: [0.0, 1.0]
process p1 - test_with_barrier ----> 2025-11-01 00:27:31
p1 results: [0.0, 1.0]
```

### **Key Insight**

Processes using barriers waited for each other before continuing,
ensuring ordered execution and synchronized output.

---

## ⚙️ 6. process_pool.py

### **Purpose**

Demonstrates parallel computation using a **process pool**.

### **Core Example**

```python
inputs = list(range(0, 10))
pool = multiprocessing.Pool(processes=4)
pool_outputs = pool.map(do_something, inputs)
```

### **Sample Output**

```
Pool: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### **Key Insight**

A process pool distributes workload efficiently across multiple cores,
processing each task concurrently and improving performance.

---

## 🧮 Summary Table

| Script                                 | Purpose                              | Result | Key Observation                         |
| :------------------------------------- | :----------------------------------- | :----: | :-------------------------------------- |
| naming_processes.py                    | Naming & parallel execution          |    ✅   | Concurrent execution reduced total time |
| spawning_processes.py                  | Spawning processes via loop          |    ✅   | Independent, scalable workloads         |
| killing_processes.py                   | Lifecycle management                 |    ✅   | Clean start, terminate, join operations |
| run_background_processes_no_daemons.py | Daemon vs Non-Daemon comparison      |    ✅   | Daemon ends early; non-daemon completes |
| processes_barrier.py                   | Synchronization using Barrier & Lock |    ✅   | Ordered and controlled execution        |
| process_pool.py                        | Parallel execution with Pool         |    ✅   | Efficient workload distribution         |

---

## 🧩 Conclusion

These experiments collectively demonstrate that:

* **Multiprocessing achieves true parallelism** for CPU-bound tasks.
* **Naming, synchronization, and barriers** make process management predictable and organized.
* **Lifecycle methods** (`start()`, `terminate()`, `join()`) ensure proper control.
* **Daemon processes** stop with the main program, while **non-daemon** continue independently.
* **Pools** and **barriers** are essential tools for structured concurrency.

---

## 🧠 Key Takeaways

Python’s `multiprocessing` module is a robust framework for parallel computing.
By understanding how to create, synchronize, and manage processes effectively,
you can build scalable and performance-optimized applications that fully leverage multi-core CPUs.

🧩 DFA Keyword Recognizer with Multithreading and Multiprocessing Comparison

This project checks how much time a DFA (Deterministic Finite Automaton) program takes to run when we use different numbers of threads and processes.
It helps understand how Multithreading and Multiprocessing affect program performance.

We tested the DFA program with 5, 10, and 15 threads and processes.

⚙️ Multithreading Results
Threads	Time Taken
5	0.0210 seconds
10	0.0407 seconds
15	0.0590 seconds
⚙️ Multiprocessing Results
Processes	Time Taken
5	1.1638 seconds
10	1.3755 seconds
15	1.8436 seconds
📊 Comparison Summary

Multithreading is much faster than Multiprocessing.
The DFA code is not very heavy, so threads work faster because they share the same memory.
On the other hand, processes take more time since each process runs separately and uses more system memory.

🧠 Conclusion

From the tests conducted with 5, 10, and 15 threads and processes, it is clear that Multithreading significantly outperforms Multiprocessing for this DFA-based program.
Since the DFA operations are lightweight and CPU-bound for short durations, threads handle the workload more efficiently by sharing memory and running within the same process space.

On the other hand, Multiprocessing introduces higher overhead because each process runs in a separate memory space, leading to more time spent on process creation and inter-process communication.

Overall, Multithreading is the better choice for this type of DFA task, providing faster execution and better resource utilization, while Multiprocessing is more suitable for heavy, independent, and CPU-intensive workloads.
Thread Synchronization Techniques in Python
(Using Lock, RLock, Semaphore & Condition)

This project illustrates how different synchronization tools from Python’s threading module help manage concurrent access to a shared list through a common computation function, do_something.py.

🔒 Synchronization Methods Demonstrated
1. Lock

Purpose: Ensures only one thread can modify the shared list (out_list) at any given time.

Observed Output:

Thread 0 started.
Thread 0 finished.
Thread 1 started.
Thread 1 finished.
Thread 2 started.
Thread 2 finished.
Length of list (Lock): 21


Conclusion:
Threads executed sequentially without interference. Final list length matched the expected value — 21.

2. RLock (Reentrant Lock)

Purpose: Allows a single thread to acquire the same lock multiple times safely.

Observed Behavior:
Execution pattern almost identical to Lock; all threads completed sequentially with accurate list updates.

Conclusion:
Data access remained consistent and thread-safe. Useful in recursive or nested locking scenarios.

3. Semaphore

Purpose: Restricts the number of concurrent threads allowed to access a shared resource.

Observed Output:

Thread 0 waiting for permit...
Thread 0 started.
Thread 1 waiting for permit...
Thread 2 waiting for permit...
Thread 1 started.
Thread 0 finished.
Thread 1 finished.
Thread 2 started.
Thread 2 finished.
Length of list (Semaphore): 21


Conclusion:
Semaphore allowed limited threads to run together. Access was controlled and results remained correct.

4. Condition

Purpose: Lets threads wait for specific signals or states before continuing execution.

Observed Output:

Thread 0 notifying condition.
Thread 1 notifying condition.
Thread 2 notifying condition.
Monitor: Current length = 7
Monitor: Current length = 14
Monitor: Current length = 21


Conclusion:
Condition variables enabled coordination between worker threads and a monitor thread to track progress smoothly.

📊 Comparison Table
Sync Type	Core Function	Behavior Description	Data Safety	Ideal Use Case
Lock	Prevents simultaneous modification	Sequential thread execution	✅ Safe	Basic mutual exclusion
RLock	Lock can be re-acquired by same thread	Same as Lock (reentrant)	✅ Safe	Nested lock situations
Semaphore	Limits number of concurrent threads	Controlled parallel threads	✅ Safe	Managing shared limited resources
Condition	Coordinates using wait/notify	Event-driven coordination	✅ Safe	Producer-consumer, signaling tasks
🧠 Summary

All four synchronization mechanisms — Lock, RLock, Semaphore, and Condition — effectively preserved data integrity during concurrent execution.
Each method ensured the shared list produced 21 items (as expected), avoiding race conditions:

Lock/RLock: Basic mutual exclusion (RLock allows recursive acquisition).

Semaphore: Controls parallel thread count.

Condition: Coordinates threads based on state or signals.

Choose the synchronization primitive according to your concurrency needs.

▶️ Running the Examples

To view each synchronization mechanism in action, execute these files one by one:

python Chapter_02/Lock.py
python Chapter_02/RLock.py
python Chapter_02/Semaphore.py
python Chapter_02/Condition.py
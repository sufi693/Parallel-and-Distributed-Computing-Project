MPI Communication Patterns — 10 Process Comparison
Overview

This project demonstrates and compares various MPI (Message Passing Interface) communication patterns implemented in Python using the mpi4py library. Each program was executed with 10 processes (-n 10) to analyze how data is distributed, exchanged, and collected among processes.

Environment

Language: Python 3.12
Library: mpi4py
MPI Implementation: Microsoft MPI (MS-MPI)
Platform: Windows 10, VS Code Terminal

Execution Command:

mpiexec -n 10 python filename.py

Programs and Observations
Program	Communication Type	Description	Key Observation
scatter.py	One-to-many	Distributes unique data chunks from the root process to all other processes.	Each process received and processed a unique element efficiently.
gather.py	Many-to-one	Collects results from all processes into the root.	Rank 0 gathered all computed results successfully.
broadcast.py	One-to-all	Shares the same data from the root to all processes.	All processes received identical values instantly.
reduce.py	Many-to-one (aggregated)	Reduces distributed data by summing values from all processes.	Root process received correctly combined data.
alltoall.py	All-to-all	Every process communicates with every other process.	All ranks exchanged data, showing heavy but complete communication.
pointtoPointCommunication.py	Pairwise	Direct send/receive between specific processes.	Data sent and received correctly between paired ranks.
deadLockProblems.py	Blocking send/receive	Demonstrates improper synchronization leading to deadlock.	Some processes waited indefinitely due to blocking communication.
virtualtopology.py	Grid / Cartesian topology	Creates a 2D virtual topology (3×3 grid) where each process communicates with its logical neighbors.	Each process correctly identified its grid position and neighbor ranks.
Conclusion

These experiments show that MPI provides a flexible and scalable model for parallel computation. Each communication pattern serves a specific role in distributed systems.

Collective operations such as scatter, gather, broadcast, and reduce are efficient for distributing, collecting, and aggregating data across processes. All-to-all communication enables complete data sharing but introduces higher overhead as the number of processes increases. Point-to-point communication offers precise control and is suitable when full synchronization is not required.

The deadlock example highlights the importance of correct synchronization and careful use of blocking send and receive operations. The virtual topology example demonstrates how MPI can organize processes into structured grids, which is useful in simulations, scientific computing, and image processing.

Overall, MPI enables high performance and scalability in parallel applications, provided that the communication pattern is selected according to the workload and proper synchronization techniques are applied.

References

mpi4py Documentation
https://mpi4py.readthedocs.io

Microsoft MPI (MS-MPI)
https://learn.microsoft.com/en-us/message-passing-interface/microsoft-mpi
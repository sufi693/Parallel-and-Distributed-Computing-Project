# Chapter 06: Distributed Systems and Network Communication

This chapter demonstrates three distinct methods for distributed task execution and remote communication: **Celery** (Task Queues), **Pyro4** (Remote Objects), and **Sockets** (Low-level Networking).

## 1. Celery: Distributed Task Queue
Utilizes a message broker (RabbitMQ/Redis) to offload `GCD` and `LCM` calculations to background workers.

* **Logic**: Mathematical operations are defined as `@app.task`.
* **Workflow**: The client sends a task to the broker, and the worker retrieves and executes it asynchronously.

## 2. Pyro4: Remote Method Invocation (RMI)
Allows the client to call Python objects residing on a different server as if they were local.

* **Name Server**: Acts as a directory for looking up remote objects.
* **Chain Topology**: Demonstrates a "Daisy Chain" where a message and math parameters are passed through multiple servers (1 -> 2 -> 3 -> 1).

## 3. Sockets: TCP/IP Communication
The foundation of network programming using raw streams to exchange data.

* **Math Server**: A TCP server that parses incoming strings (e.g., "48,18") and returns calculated results.
* **File Transfer**: Demonstrates reading and sending binary data (`mytext.txt`) over a network connection.

## Comparison of Technologies

| Technology | Level | Primary Use Case | Scaling Method |
| :--- | :--- | :--- | :--- |
| **Celery** | High | Background job processing | Horizontal worker scaling |
| **Pyro4** | High | Object-oriented distributed systems | Remote Object Proxy |
| **Sockets** | Low | Custom protocols/File transfer | Byte-stream communication |

## Setup and Execution
1. **Celery**: Requires RabbitMQ/Redis and `pip install celery`.
2. **Pyro4**: Requires `pip install Pyro4` and a running Name Server (`python -m Pyro4.naming`).
3. **Sockets**: Built into Python's standard library.
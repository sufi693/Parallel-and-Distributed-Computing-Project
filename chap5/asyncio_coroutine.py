import asyncio
import random
from do_something import do_something


async def cpu_task(task_name: str):
    out_list = []
    size = random.randint(1000, 5000)
    await asyncio.to_thread(do_something, size, out_list)
    print(f"{task_name} processed {len(out_list)} items; last={out_list[-1] if out_list else 'N/A'}")


async def task_A(end_time: float):
    print("task_A called")
    await cpu_task("task_A")

    await asyncio.sleep(random.randint(0, 2))
    if asyncio.get_running_loop().time() + 1.0 < end_time:
        await task_B(end_time)
    else:
        print("Stopping loop from task_A")


async def task_B(end_time: float):
    print("task_B called")
    await cpu_task("task_B")

    await asyncio.sleep(random.randint(0, 2))
    if asyncio.get_running_loop().time() + 1.0 < end_time:
        await task_C(end_time)
    else:
        print("Stopping loop from task_B")


async def task_C(end_time: float):
    print("task_C called")
    await cpu_task("task_C")

    await asyncio.sleep(random.randint(0, 2))
    if asyncio.get_running_loop().time() + 1.0 < end_time:
        await task_A(end_time)
    else:
        print("Stopping loop from task_C")


async def main():
    loop = asyncio.get_running_loop()
    end_time = loop.time() + 60  # ~60 seconds
    await task_A(end_time)


if __name__ == "__main__":
    asyncio.run(main())

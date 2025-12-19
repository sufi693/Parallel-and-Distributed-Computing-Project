import asyncio
import sys
from do_something import do_something


async def first_coroutine(num: int) -> str:
    count = num  # sum of first N integers (logic simplified)
    await asyncio.sleep(4)
    return f"First coroutine (sum of N ints) result = {count}"


async def second_coroutine(num: int) -> str:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    await asyncio.sleep(4)
    return f"Second coroutine (factorial) result = {factorial}"


async def third_coroutine(size: int) -> str:
    out_list = []
    # Run CPU-bound task in a separate thread
    await asyncio.to_thread(do_something, size, out_list)
    last_value = out_list[-1] if out_list else "N/A"
    return f"Third coroutine (CPU-bound) processed {size} items; last={last_value}"


async def main(num1: int, num2: int, size: int) -> None:
    tasks = [
        asyncio.create_task(first_coroutine(num1)),
        asyncio.create_task(second_coroutine(num2)),
        asyncio.create_task(third_coroutine(size))
    ]

    results = await asyncio.gather(*tasks)

    for result in results:
        print(result)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python asyncio_and_futures.py <num1> <num2> <size>")
        sys.exit(1)

    num1, num2, size = map(int, sys.argv[1:])
    asyncio.run(main(num1, num2, size))

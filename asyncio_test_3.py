import asyncio
import time


async def count_async():
    return sum([i for i in range(1000000000000)])


def count_sync():
    return sum([i for i in range(1000000000000)])


async def main_1():
    await asyncio.gather(count_async(), count_async(), count_async())


def main_2():
    return [count_sync for _ in range(3)]

if __name__ == '__main__':
    s = time.perf_counter()
    main_2()
    elapsed_time = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed_time:0.2f} seconds (SYNC)")
    s = time.perf_counter()

    asyncio.run(main_1())
    elapsed_time = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed_time:0.2f} seconds (ASYNC)")

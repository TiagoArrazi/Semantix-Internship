import asyncio
import time


async def count():
    return sum([i for i in range(10000)])


async def main():
    await asyncio.gather(count(), count(), count())


if __name__ == '__main__':
    s = time.perf_counter()
    asyncio.run(main())
    elapsed_time = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed_time:0.2f} seconds")

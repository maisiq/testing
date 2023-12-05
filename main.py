import asyncio
from util.timer_tasks import time_checker

async def cpu_bound():
    c = 0
    for _ in range(10000000):
        c += 1
    return c


async def main():
    task1 = asyncio.create_task(asyncio.sleep(3))
    task2 = asyncio.create_task(time_checker(cpu_bound))

    r, _ = await asyncio.wait([task1, task2])

    print(
        [r.result() for r in r]
        )


asyncio.run(main())
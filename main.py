import asyncio


async def cpu_bound():
    c = 0
    for _ in range(1000000):
        c += 1


async def main():
    task1 = asyncio.create_task(asyncio.sleep(3))
    task2 = asyncio.create_task(cpu_bound())

    r, _ = await asyncio.wait([task1, task2])

    print(
        [r.result() for r in r]
        )


asyncio.run(main())
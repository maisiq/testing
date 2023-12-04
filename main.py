import asyncio



async def main():
    task1 = asyncio.create_task(asyncio.sleep(3))

    r, _ = await asyncio.wait([task1])
    print(
        [r.result() for r in r]
        )


asyncio.run(main())
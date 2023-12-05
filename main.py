import asyncio



async def main():
    task1 = asyncio.create_task(asyncio.sleep(3))
    print('Waiting for results. . .')
    done, _ = await asyncio.wait([task1])
    print(
        [r.result() for r in done]
        )


asyncio.run(main())
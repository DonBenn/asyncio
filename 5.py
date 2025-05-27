import asyncio

async def coro_1():
    print('Coroutine 1 is done')

async def coro_2():
    print('Coroutine 2 is done')

async def coro_3():
    print('Coroutine 3 is done')

async def main():
    tasks = []
    for i, coro in enumerate([coro_3, coro_2, coro_1], start=1):
        tasks.append(asyncio.create_task(coro()))
        await asyncio.sleep(1 / i)
    await asyncio.gather(*tasks)

asyncio.run(main())

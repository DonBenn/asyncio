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



import asyncio

async def print_with_delay(num):
    print(f'Coroutine {num} is done')
    await asyncio.sleep(1)

async def main():
    tasks = []
    for num in range(10):
        task = asyncio.create_task(print_with_delay(num))  # создаем 10 задач
        tasks.append(task)  # добавляем все задачи в список tasks
    await asyncio.gather(*tasks)  # запускаем все задачи из списка tasks

asyncio.run(main())



import asyncio


counters = {
    "Counter 1": 0,
    "Counter 2": 0
}

max_counts = {
    "Counter 1": 13,
    "Counter 2": 7
}

async def counter(counter_name, sec):
    while counters[counter_name] < max_counts[counter_name]:
        counters[counter_name] += sec
        await asyncio.sleep(sec)
        print(f'{counter_name}: {counters[counter_name]}')


async def main():
    task1 = asyncio.create_task(counter("Counter 1", 1))
    task2 = asyncio.create_task(counter("Counter 2", 1))
    await task1
    await task2

asyncio.run(main())

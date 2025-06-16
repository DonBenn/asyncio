import time
import asyncio


async def coro(num, seconds):
    print(f"coro{num} начала свое выполнение")
    await asyncio.sleep(seconds)
    print(f"coro{num} выполнена за {seconds} секунду(ы)")


async def main():
    # Создание объектов корутин путем вызова корутинной функции.
    coro1 = coro(1, 2)
    coro2 = coro(2, 1)
    # Запуск и ожидание выполнения объектов корутин.
    await coro2
    await coro1

start = time.time()
asyncio.run(main())
print(f'Программа выполнена за {time.time()-start:.3f} секунд(ы)')



import asyncio
import time


async def coro(num, seconds):
    print(f"Задача{num} начала свое выполнение")
    await asyncio.sleep(seconds)
    print(f"Задача{num} выполнена за {seconds} секунду(ы)")


async def main():
    # Создание задач из корутины.
    task1 = asyncio.create_task(coro(1, 2))
    task2 = asyncio.create_task(coro(2, 1))
    # Запуск и ожидание выполнения задач.
    await task2
    await task1

start = time.time()
asyncio.run(main())
print(f'Программа выполнена за {time.time()-start:.3f} секунд(ы)')
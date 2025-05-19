import asyncio


async def example_coroutine():
    print("Hello from coroutine!")



async def example_coroutine():
    await asyncio.sleep(1)  # запускаем внутри корутины асинхронную функцию sleep()
    print("Hello from coroutine!")



async def example_coroutine(number, *args, **kwargs):
    await asyncio.sleep(1)  # запускаем внутри корутины асинхронную функцию sleep()
    print(f"Hello from coroutine {number}!")
    return f"Корутина {number} завершила работу"



#НЕ ПРАВИЛЬНО
async def example_coroutine():
    print("Hello from coroutine!")

example_coroutine()  # создан объект корутины example_coroutine(), корутина не запущена!


#ПРАВИЛЬНО
async def example_coroutine():
    print("Hello from coroutine!")

asyncio.run(example_coroutine())  # корутина example_coroutine() запущена.



async def example_coroutine():
    await asyncio.sleep(1)
    print("Hello from coroutine!")

async def main():
    await example_coroutine() # запускаем example_coroutine() и ждем выполнения

asyncio.run(main())  # Точка входа



import asyncio
import time


async def example_coroutine(n):
    print(f"Hello from coroutine #{n}! {time.perf_counter() - start:.3f} секунды")
    await asyncio.sleep(1)
    print(f"Coroutine #{n} completed! {time.perf_counter() - start:.3f} секунды")


async def main():
    for num in range(1, 11):
        await example_coroutine(num)


start = time.perf_counter()
asyncio.run(main())
print(f"Программа выполнена за {time.perf_counter() - start:.3f} секунды")
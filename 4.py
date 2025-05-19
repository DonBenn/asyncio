import asyncio

async def main():
    print("Hello, Asyncio!")

asyncio.run(main())



import asyncio

async def coro_1():
    print('coro_1 says, hello coro_2!')

async def coro_2():
    print('coro_2 says, hello coro_1!')

async def main():
    await coro_1()
    await coro_2()

asyncio.run(main())
    # await asyncio.gather(coro_1(), coro_2())



import asyncio

async def generate(number):
    await asyncio.sleep(0.1)
    print(f"Корутина generate с аргументом {number}")
async def main():
    for i in range(10):
        await generate(i)

if __name__ == '__main__':
    asyncio.run(main())



import asyncio


async def coro_1():
    print("Вызываю корутину 0")


async def coro_5():
    print("Вызываю корутину 3")
    await coro_3()


async def coro_3():
    print("Вызываю корутину 2")
    await coro_2()


async def coro_4():
    print("Вызываю корутину 1")
    await coro_1()


async def coro_2():
    print("Вызываю корутину 4")
    await coro_4()


asyncio.run(coro_5())



import asyncio


async def example_coroutine():
    await asyncio.sleep(1)
    print("Hello from coroutine!")

async def main():
    task = asyncio.create_task(example_coroutine())  # создаем задачу из корутины example_coroutine()
    await task # ждем выполнения задачи
    print(type(asyncio.create_task(example_coroutine())))

asyncio.run(main())



import asyncio


async def example_coroutine():
    await asyncio.sleep(1)
    print("Hello from coroutine!")

async def main():
    tasks = []
    for _ in range(10):
        task = asyncio.create_task(example_coroutine())  # создаем 10 задач
        tasks.append(task)  # добавляем все задачи в список tasks
    await asyncio.gather(*tasks)  # запускаем все задачи из списка tasks

asyncio.run(main())



import asyncio

# Список поваров.
chef_list = ['', 'Франсуа', 'Жан', 'Марсель']


async def cook_order(order_number, dish):
    # Повар готовит блюдо
    print(
        f"Повар {chef_list[order_number]} начинает готовить заказ №{order_number}: {dish}")
    await asyncio.sleep(2)  # Имитация времени на готовку
    print(f"Заказ №{order_number}: {dish} готов!")


async def serve_order(order_number, dish):
    # Официант подает блюдо
    await cook_order(order_number, dish)
    print(f"Официант подает {dish}")


async def manager():
    # Менеджер (событийный цикл) назначает задачи
    orders = [(1, 'Салат'), (2, 'Стейк'), (3, 'Суп')]
    tasks = [asyncio.create_task(serve_order(order_number, dish)) for
             order_number, dish in orders]

    # Ожидаем завершения всех задач
    await asyncio.gather(*tasks)


# Запуск событийного цикла
asyncio.run(manager())
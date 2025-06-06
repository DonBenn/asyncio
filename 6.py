import asyncio


async def simulate_long_running_task(name, delay, future: asyncio.Future):
    print(f"Задача '{name}' началась, будет выполнена за {delay} секунд.")
    await asyncio.sleep(delay)
    result = f"Результат задачи '{name}'"
    print(f"Задача '{name}' завершена.")
    future.set_result(result)  # Устанавливаем результат для Future объекта


async def main():
    # Создаем объект Future
    future = asyncio.Future()

    # Запускаем корутину, передаем Future объект в функцию
    await simulate_long_running_task("Задача1", 3, future)

    # Получаем результат выполнения задачи
    result = future.result()
    print(f"Результат Future: {result}")


asyncio.run(main())



import asyncio


async def do_some_work_1(x, future: asyncio.Future):
    print(f"Выполняется работа 1: {x}")
    await asyncio.sleep(x)
    future.set_result(x * 2)


async def do_some_work_2(x, future: asyncio.Future):
    print(f"Выполняется работа 2: {x}")
    await asyncio.sleep(x)
    future.set_result(x + 2)


async def main():
    # Создаем объекты Future для каждой задачи
    future_1 = asyncio.Future()
    future_2 = asyncio.Future()

    # Запускаем первую задачу и передаем ей Future
    asyncio.create_task(do_some_work_1(2, future_1))

    # Дожидаемся завершения первой задачи
    await future_1
    result_1 = future_1.result()

    # Запускаем вторую задачу, передавая результат первой и объект Future
    asyncio.create_task(do_some_work_2(result_1, future_2))

    # Дожидаемся завершения второй задачи
    await future_2
    result_2 = future_2.result()

    print(f"Результат future_1: {result_1}")  # Выводим результат первой задачи
    print(f"Результат future_2: {result_2}")  # Выводим результат второй задачи


asyncio.run(main())



import asyncio

async def main():
    future = asyncio.Future()
    if not future.done():
        print("Состояние: Pending (ожидание)")
    try:
        result = future.result()
        print(result)
    except asyncio.InvalidStateError:
        print('Задача еще не выполнена. Доступа к результатам нет!')

asyncio.run(main())



import asyncio

async def main():
    future = asyncio.Future()
    future.set_result('Задача завершена')
    result = future.result()

    if future.done():
        print("Состояние: Completed (завершено)")
        print("Результат:", result)


asyncio.run(main())



import asyncio


async def main():
    future = asyncio.Future()
    future.cancel()
    if future.cancelled():
        print("Состояние: Cancelled (отменено)")
    try:
        result = future.result()
        print(result)
    except asyncio.CancelledError:
        print('Задача отменена. Доступа к результатам нет!')

asyncio.run(main())



import asyncio


async def my_coroutine():
    await asyncio.sleep(1)
    return 'Задача завершена'

async def main():
    task1 = asyncio.ensure_future(my_coroutine())
    task2 = asyncio.create_task(my_coroutine())
    print(f'Тип объекта, созданного методом ensure_future(): {type(task1)}')
    print(f'Тип объекта, созданного методом create_task(): {type(task2)}')
    await asyncio.gather(task1, task2)

asyncio.run(main())





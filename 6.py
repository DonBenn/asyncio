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



import asyncio

async def set_after(fut, delay, value):
    await asyncio.sleep(delay)
    fut.set_result(value)

async def main():
    future = asyncio.Future()
    asyncio.ensure_future(set_after(future, 1, 'done'))
    result = await future
    print(result)

asyncio.run(main())



import asyncio

async def set_future_result(value, delay):
    print(
        f"Задача начата. Установка результата '{value}' через {delay} секунд.")
    await asyncio.sleep(delay)
    print("Результат установлен.")
    return value

async def create_and_use_future():
    future = asyncio.Future()
    if not future.done():
        print("Состояние Task до выполнения: Ожидание")
    else:
        print("Состояние Task до выполнения: Завершено")
    print("Задача запущена, ожидаем завершения...")
    result = await asyncio.create_task(set_future_result('Успех', 2))

    if not future.done():
        print("Состояние Task после выполнения: Завершено")
    else:
        print("Состояние Task после выполнения: Ожидание")
    return result


async def main():
    result = await create_and_use_future()
    print("Результат из Task:", result)


asyncio.run(main())



import asyncio

async def set_future_result(value, delay):
    print(f"Задача начата. Установка результата '{value}' через {delay} секунд.")
    await asyncio.sleep(delay)
    print("Результат установлен.")
    return value

async def create_and_use_future():
    result = asyncio.ensure_future(set_future_result("Успех", 2))
    if not result.done():
        print("Состояние Task до выполнения: Ожидание")

    else:

        print("Состояние Task до выполнения: Завершено")
    print("Задача запущена, ожидаем завершения...")
    await result
    if not result.done():
        print("Состояние Task после выполнения: Ожидание")

    else:

        print("Состояние Task после выполнения: Завершено")

    print("Результат из Task:", result.result())
asyncio.run(create_and_use_future())



import asyncio

async def async_operation():
    print("Начало асинхронной операции.")
    await asyncio.sleep(2)
    future = asyncio.Future()
    if not future.cancelled():
        print("Асинхронная операция успешно завершилась.")
    try:
        result = future.result()
        print(result)
    except asyncio.CancelledError:
        print("Асинхронная операция была отменена в процессе выполнения.")
    raise



import asyncio


async def async_operation():
    print("Начало асинхронной операции.")
    try:
        await asyncio.sleep(2)
        print("Асинхронная операция успешно завершилась.")
    except asyncio.CancelledError:
        print("Асинхронная операция была отменена в процессе выполнения.")
        raise

async def main():
    print("Главная корутина запущена.")
    task = asyncio.create_task(async_operation())
    await asyncio.sleep(0.1)
    print("Попытка отмены Task.")
    task.cancel()
    try:
        result = await task
        print("Результат Task:", result)
    except asyncio.CancelledError:
        print("Обработка исключения: Task был отменен.")
    if task.cancelled():
        print("Проверка: Task был отменен.")
    else:
        print("Проверка: Task не был отменен.")
    print("Главная корутина завершена.")

asyncio.run(main())



import asyncio


async def first_function(x):
    print(f"Выполняется первая функция с аргументом {x}")
    await asyncio.sleep(1)
    result = x + 1
    print(f"Первая функция завершилась с результатом {result}")
    return result

async def second_function(x):
    print(f"Выполняется вторая функция с аргументом {x}")
    await asyncio.sleep(1)
    result = x * 2
    print(f"Вторая функция завершилась с результатом {result}")
    return result

async def third_function(x):
    print(f"Выполняется третья функция с аргументом {x}")
    await asyncio.sleep(1)
    result = x + 3
    print(f"Третья функция завершилась с результатом {result}")
    return result

async def fourth_function(x):
    print(f"Выполняется четвертая функция с аргументом {x}")
    await asyncio.sleep(1)
    result = x ** 2
    print(f"Четвертая функция завершилась с результатом {result}")
    return result

async def main():
    initial_value = 1
    print("Начало цепочки асинхронных вызовов")
    first_result = await asyncio.create_task(first_function(initial_value))
    second_result = await asyncio.create_task(second_function(first_result))
    third_result = await asyncio.create_task(third_function(second_result))
    final_result = await asyncio.create_task(fourth_function(third_result))
    print(f"Конечный результат цепочки вызовов: {final_result}")

asyncio.run(main())



import asyncio
import random


async def waiter(future):
    await future
    print(f"future выполнен, результат {future.result()}. Корутина waiter() может продолжить работу")

async def setter(future):
    await asyncio.sleep(random.randint(1,3))
    future.set_result(True)

async def main():
    future = asyncio.Future()
    await asyncio.gather(waiter(future), setter(future))

asyncio.run(main())

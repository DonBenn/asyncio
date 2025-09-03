import asyncio


async def some_coro(num):
    await asyncio.sleep(num)
    return num / 2


async def main():
    # Создаем группу задач.
    async with asyncio.TaskGroup() as tg:
        # Создаем в группе задачу.
        task = tg.create_task(some_coro(2))
    print(f"Задача выполнена с результатом: {task.result()}.")

asyncio.run(main())



import asyncio

async def coro():
    name = asyncio.current_task().get_name()
    print(f'{name} начала свою работу!')
    await asyncio.sleep(1)
    print(f'{name} завершена!')


async def main():
    # Создание группы задач
    async with asyncio.TaskGroup() as group:
        # Создание трех задач
        [group.create_task(coro(), name=f'Задача_0{i}') for i in range(1, 4)]

    # Ожидание, пока все задачи не будут завершены...
    print('Все задачи были выполнены!')


asyncio.run(main())



import asyncio


async def coro(value):
    await asyncio.sleep(1)
    return value * 100


async def main():
    # Создание группы задач
    async with asyncio.TaskGroup() as group:
        # Создание списка задач с передачей в них чисел из диапазона (1, 10)
        tasks = [group.create_task(coro(i)) for i in range(1, 11)]

    for task in tasks:
        print(task.result())


asyncio.run(main())



import asyncio


async def coro():
    name = asyncio.current_task().get_name()
    print(f'{name} начала свою работу!')
    await asyncio.sleep(1)
    print(f'{name} завершена!')


async def main():
    # Создание группы задач
    async with asyncio.TaskGroup() as group:
        # Создание трех задач
        tasks = [group.create_task(coro(), name=f'Задача_0{i}') for i in range(1, 4)]
        await asyncio.sleep(0.5)
        # Отмена второй задачи
        tasks[1].cancel()
    # Проверка состояния каждой задачи
    for task in tasks:
        print(f'{task.get_name()}: done={task.done()}, cancelled={task.cancelled()}')


asyncio.run(main())



import asyncio


async def coro():
    name = asyncio.current_task().get_name()
    print(f'{name} начала свою работу!')
    await asyncio.sleep(1)
    print(f'{name} завершена!')


# Корутина для подъема исключений
async def ex_coro():
    await asyncio.sleep(.5)
# 1) Поведение характерное для обработки KeyboardInterrupt и SystemExit
# Повторный вызов изначального исключения
#     print('ex_coro поднимает исключение KeyboardInterrupt')
#     raise KeyboardInterrupt
# 2) Поведение характерное для обработки других исключений (кроме asyncio.CancelledError)
# Исключения группируются в ExceptionGroup
    print('ex_coro поднимает исключение Exсeption')
    raise Exception('Что-то пошло не так!(((')


async def main():
    # Создание группы задач
    async with asyncio.TaskGroup() as group:
        # Создание трех задач
        tasks = [group.create_task(coro(), name=f'Задача_0{i}') for i in range(1, 4)]
        # Создание задачи, имитирующей возникновение исключения
        task_ex = group.create_task(ex_coro())


asyncio.run(main())



import asyncio


async def coro():
    name = asyncio.current_task().get_name()
    print(f'{name} начала свою работу!')
    await asyncio.sleep(1)
    print(f'{name} завершена!')


async def ex_coro():
    await asyncio.sleep(.5)
    # Вызываем исключение
    print('ex_coro поднимает исключение Exсeption')
    raise Exception('Что-то пошло не так!(((')


async def main():
    try:
        # Создание группы задач
        async with asyncio.TaskGroup() as group:
            # Создание трех задач
            tasks = [group.create_task(coro(), name=f'Задача_0{i}') for i in range(1, 4)]
            # Создание задачи, имитирующей возникновение исключения
            tasks.append(group.create_task(ex_coro(), name='Задача_ex'))
            # Создание четвертой "обычной" задачи
            tasks.append(group.create_task(coro(), name=f'Задача_0{4}'))
    except:
        pass

    # Проверка состояния каждой задачи
    for task in tasks:
        print(f'{task.get_name()}: done={task.done()}, cancelled={task.cancelled()}')
        if not task.cancelled():
            if eq := task.exception():
                print(f'{task.get_name()}: {eq}')


asyncio.run(main())



import asyncio


async def file_reader(filename: str) -> str:
    """Корутина для чтения файла"""
    with open(filename) as f:
        data: str = f.read()
    return data


async def get_data(data: int) -> dict:
    """Корутина, для возврата переданного числа в виде словаря вида {'data': data}"""
    if data == 0:
        raise Exception('Нет данных...')
    return {'data': data}


async def main():
    tasks = asyncio.gather(
        get_data(1),
        get_data(2),
        # Передаем имя несуществующего файла, чтобы вызвать ошибку
        file_reader('fake.png'),
        # Этот вызов тоже должен вызвать ошибку
        get_data(0),
        return_exceptions=True
    )
    result = await tasks
    print('Готово!!!', result)

asyncio.run(main())



import asyncio


async def file_reader(filename: str) -> str:
    """Корутина для чтения файла"""
    with open(filename) as f:
        data: str = f.read()
    return data


async def get_data(data: int) -> dict:
    """Корутина, для возврата переданного числа в виде словаря вида {'data': data}"""
    if data == 0:
        raise Exception('Нет данных...')
    return {'data': data}


async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(get_data(1))
        task2 = tg.create_task(get_data(2))
        task3 = tg.create_task(file_reader('fake.png'))
        task4 = tg.create_task(get_data(0))
    result = [task1.result(), task2.result(), task3.result(), task4.result()]
    print('Готово!!!', result)


asyncio.run(main())



import asyncio


async def file_reader(filename: str) -> str:
    """Корутина для чтения файла"""
    with open(filename) as f:
        data: str = f.read()
    return data


async def get_data(data: int) -> dict:
    """Корутина, для возврата переданного числа в виде словаря вида {'data': data}"""
    if data == 0:
        raise Exception('Нет данных...')
    return {'data': data}


async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            task1 = tg.create_task(get_data(1))
            task2 = tg.create_task(get_data(2))
            task3 = tg.create_task(get_data(0))
            task4 = tg.create_task(file_reader('fake.png'))
            task5 = tg.create_task(file_reader('new_fake.png'))
            task6 = tg.create_task(get_data(0))
        # Результат мы все равно не увидим, так как спровоцируем вызов исключений.
        result = [task1.result(), task2.result(), task3.result(), task4.result(), task5.result(), task6.result()]
        print('Готово!!!', result)
    # Добавляем обработчики, которые будут группировать ошибки одного типа.
    except* FileNotFoundError as e:
        for error in e.exceptions:
            print(error)
    except* Exception as e:
        for error in e.exceptions:
            print(error)


asyncio.run(main())



import asyncio


async def coro():
    await asyncio.sleep(1)

    # # Вариант 1. Без аргументов.
    # raise FileNotFoundError

    # Вариант 2. Самостоятельно определяем текст сообщения.
    # raise FileNotFoundError("Файл не найден")

    # Вариант 3. Exception выбрасывается самим интерпретатором.
    with open('bug.txt', 'r', encoding='utf-8') as file:
        ...


async def main():
    try:
        async with asyncio.TaskGroup() as group:
            # Создание группы задач
            [group.create_task(coro()) for _ in range(3)]
    except* FileNotFoundError as e:
        print("Исключения были перехвачены:")
        for error in e.exceptions:
            print(f"Тип ошибки: {type(error)}")
            print(f"Сообщение ошибки: {str(error)}")
            print(f"Аргументы ошибки: {error.args}")  # Аргументы исключения


asyncio.run(main())
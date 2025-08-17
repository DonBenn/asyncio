import asyncio
import time

async def coro(num):
    await asyncio.sleep(1/num)
    return f"Задача_{num} была выполнена за {time.perf_counter() - start:.4f} секунды"

async def main():
    future = asyncio.gather(*[coro(i) for i in range(1, 6)])
    print(type(future))
    results = await future
    print(results)


start = time.perf_counter()
asyncio.run(main())



import asyncio
import time

async def coro(num):
    print(f"Задача_{num} была запущена {time.perf_counter() - start:.4f} секунды")
    await asyncio.sleep(1/num)
    return f"Задача_{num} была выполнена за {time.perf_counter() - start:.4f} секунды"

async def main():
    # Проверка количества активных задач текущего цикла событий до asyncio.gather()
    tasks = asyncio.all_tasks()
    print(f"До asyncio.gather() в цикле событий {len(tasks)} задач: {[f'{task.get_name()}. Статус: {task._state}' for task in tasks]}")
    future = asyncio.gather(*[coro(i) for i in range(1, 6)])
    # Проверка количества активных задач текущего цикла событий после asyncio.gather()
    tasks = asyncio.all_tasks()
    print(f"После asyncio.gather() в цикле событий {len(tasks)} задач: {[f'{task.get_name()}. Статус: {task._state}' for task in tasks]}")
    print(f"Запланированные задачи еще не начали своего выполнения {time.perf_counter() - start:.4f} секунды")
    results = await future
    print(results)


start = time.perf_counter()
asyncio.run(main())



import asyncio
import random

async def my_coroutine(name):
    delay = random.random()
    await asyncio.sleep(delay)
    return f"Корутина {name}: {round(delay, 2)}"

async def main():
    results = await asyncio.gather(*[my_coroutine(i) for i in range(1, 6)])
    print(results)

asyncio.run(main())



import asyncio


async def my_coro(num):
    print(f"Корутина {num} началась")
    await asyncio.sleep(num)
    if num % 2 == 0:
        raise Exception(f"Ошибка в корутине {num}")
    print(f"Корутина {num} закончилась")
    return num


async def main():
    coros = [my_coro(i) for i in range(1, 6)]
    results = await asyncio.gather(*coros, return_exceptions=True)
    print(f'{results = }')


asyncio.run(main())



import asyncio

books_json = [
    {
        "Порядковый номер": 1,
        "Автор": "Rebecca Butler",
        "Название": "Three point south wear score organization.",
        "Год издания": "1985",
        "Наличие на полке": True
    },
    {
        "Порядковый номер": 2,
        "Автор": "Mark Cole",
        "Название": "Drive experience customer somebody pressure.",
        "Год издания": "1985",
        "Наличие на полке": True
    },
    {
        "Порядковый номер": 2,
        "Автор": "Mark Cole",
        "Название": "Drive experience customer somebody pressure.",
        "Год издания": "1985",
        "Наличие на полке": False
    },
    {
        "Порядковый номер": 1,
        "Автор": "Rebecca Butler",
        "Название": "Three point south wear score organization.",
        "Год издания": "1985",
        "Наличие на полке": False
    },
    ]

async def check_book(book):
    if book["Наличие на полке"] is not True:
        print(f'{book["Порядковый номер"]}: {book["Автор"]}: {book["Название"]} ({book["Год издания"]})')
        await asyncio.sleep(.1)

async def main():
    tasks = [asyncio.create_task(check_book(book)) for book in books_json]
    await asyncio.gather(*tasks)

# async def check_book(book):
#     return f'{book["Порядковый номер"]}: {book["Автор"]}: {book["Название"]} ({book["Год издания"]})'

# async def main():
#     tasks = []
#     for book in books_json:
#         if book["Наличие на полке"] is not True:
#             tasks.append(asyncio.create_task(check_book(book)))
#             await asyncio.sleep(.1)
#     result = await asyncio.gather(*tasks)
#     for element in result:
#         print(element)


asyncio.run(main())



import asyncio

equipment_list = ['#001 ps5f6537c5-506f-43c2-b095-1890ef579c52: 265 units',
                  '#002 ps5ec3020b-022f-466b-845a-a8f11161a6d1: 39 units',
                  '#003 psb5c6c090-4f1a-4741-936e-5fe2b3e8d181: 242 units',
                  '#004 ps10c90127-a4a5-4f85-b23f-66421ab04b09: 108 units',
                  '#005 psa8b77d97-ef82-4832-9601-36abfc399af2: 72 units']


async def equipment_request(request):
    await asyncio.sleep(1)
    # return f'{request.split()[0]} is Ok!'
    print(f'{request[-8:]} is Ok!')


async def send_requests():
    tasks = [asyncio.create_task(equipment_request(equipment)) for equipment in equipment_list]
    results = await asyncio.gather(*tasks)
    # waiting_time = query_time()
    # print(f'На отправку {len(results)} запросов потребовалось {waiting_time} секунд!')
    print(f'На отправку {len(results)} запросов потребовалось 1.00335 секунд!')

asyncio.run(send_requests())



import asyncio

tasks_dependencies = {
    "Подготовка_окружения": {
        "этапы": [
            {"название": "Настройка виртуального окружения", "время": 1},
            {"название": "Установка базовых зависимостей", "время": 2},
            {"название": "Настройка системы контроля версий", "время": 3},
            {"название": "Проверка сетевых настроек", "время": 4},
            {"название": "Клонирование основной ветки", "время": 4},
            {"название": "Проверка последних изменений", "время": 6},
            {"название": "Проверка локальных зависимостей", "время": 8}
        ]
    },
    "Проверка_зависимостей": {
        "этапы": [
            {"название": "Обновление устаревших зависимостей", "время": 1},
            {"название": "Установка новых зависимостей", "время": 3},
            {"название": "Предварительная очистка", "время": 6},
            {"название": "Компиляция исходного кода ядра", "время": 4},
            {"название": "Логирование результатов компиляции", "время": 7}
        ]
    },
    "Компиляция_модулей": {
        "этапы": [
            {"название": "Компиляция модуля A", "время": 3},
            {"название": "Компиляция модуля B", "время": 4},
            {"название": "Тестирование модулей на совместимость", "время": 1},
            {"название": "Инициализация тестового окружения", "время": 3},
            {"название": "Тестирование модуля A", "время": 1}
        ]
    },
    "Сборка_БД": {
        "этапы": [
            {"название": "Создание структуры БД", "время": 2},
            {"название": "Наполнение начальными данными", "время": 6},
            {"название": "Импорт данных пользователей", "время": 2},
            {"название": "Импорт транзакционных данных", "время": 1},
            {"название": "Подготовка пакетов для релиза", "время": 4}
        ]
    },
    "Развертывание_релиза": {
        "этапы": [
            {"название": "Создание инструкций для установки", "время": 7},
            {"название": "Финальное тестирование релиза", "время": 1},
            {"название": "Развертывание сборки", "время": 4},
            {"название": "Проверка работоспособности сервисов", "время": 6},
            {"название": "Подготовка релизных заметок", "время": 6},
            {"название": "Финализация документации", "время": 4},
            {"название": "Размещение релиза на сервере обновлений", "время": 1},
            {"название": "Подготовка мероприятия", "время": 3},
            {"название": "Объявление об успешном релизе", "время": 4}
        ]
    }
}

async def execute_subtask(task_name, duration):

    try:
        await asyncio.wait_for(asyncio.sleep(duration), 5)
        print(
            f'Подзадача: {task_name} успела выполниться в срок, за {duration} сек.')
    except asyncio.TimeoutError:
        print(
            f'Подзадача: {task_name} не успела выполниться в срок, за {duration} сек.')
        raise


async def execute_task(task_name, subtasks):

    all_tasks = [
        asyncio.create_task(
            execute_subtask(subtask["название"], subtask["время"])) for subtask in subtasks
    ]
    try:
        await asyncio.gather(*all_tasks)
        print(f"Задача: {task_name} = все подзадачи выполнены.")
    except asyncio.TimeoutError:
        print(
            f"Задача: {task_name} не выполнилась в срок, т.к. одна или несколько подзадач заняли слишком много времени.")


async def main():
    for task in tasks_dependencies:
        await asyncio.create_task(execute_task(task, tasks_dependencies[task]["этапы"]))


asyncio.run(main())



import asyncio


async def execute_subtask(task_name, duration):

    if duration > 5:
        await asyncio.sleep(5)
        print(f'Подзадача: {task_name} не успела выполниться в срок, за {duration} сек.')
        return f'Подзадача: {task_name} не успела выполниться в срок, за {duration} сек.'
    else:
        await asyncio.sleep(duration)
        print(f'Подзадача: {task_name} успела выполниться в срок, за {duration} сек.')
        return f'Подзадача: {task_name} успела выполниться в срок, за {duration} сек.'


async def execute_task(task_name, subtasks):
    mylist = []
    for subtask in subtasks:
        mylist.append(asyncio.create_task(execute_subtask(subtask["название"], subtask["время"])))
    result = await asyncio.gather(*mylist)

    count = 0
    for element in result:
        if "не успела" in element:
            print(f"Задача: {task_name} не выполнилась в срок, т.к. одна или несколько подзадач заняли слишком много времени.")
            break
        else:
            count += 1
            if len(result) == count:
                print(f"Задача: {task_name} = все подзадачи выполнены.")


async def main():
    for task in tasks_dependencies:
        await asyncio.create_task(execute_task(task, tasks_dependencies[task]["этапы"]))


asyncio.run(main())





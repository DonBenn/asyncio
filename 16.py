import asyncio


async def cook_dinner():
    print("Начинаем разогревать ужин...")
    # Представим, что ужин успеет разогреться за 5 секунд!
    await asyncio.sleep(5)
    print("Ужин готов!")


async def do_laundry():
    print("Начинаем стирку...")
    # Представим, что стирка занимает 7 секунд
    await asyncio.sleep(7)
    print("Стирка завершена!")


async def work_on_computer():
    print("Начинаем скачивать фильм на компьютере...")
    # Представим, что эта работа занимает 3 секунды
    await asyncio.sleep(3)
    print("Скачивание фильма завершено!")


async def main():
    dinner_task = asyncio.create_task(cook_dinner())
    laundry_task = asyncio.create_task(do_laundry())
    computer_task = asyncio.create_task(work_on_computer())

    await dinner_task
    await laundry_task
    await computer_task


asyncio.run(main())



import asyncio


async def task_func():
    print("Задача запустилась")
    await asyncio.sleep(1)
    print("Задача завершилась")
    return "Результат выполнения задачи"


async def main():
    task = asyncio.create_task(task_func())
    print('Первая проверка задачи -', task.done())       # Вывод статуса задачи до ее выполнения
    print("Задача создана и помещена в стек вызовов")
    await task
    print('Вторая проверка задачи -', task.done())       # Вывод статуса задачи после ее выполнения
    print("Проверка результата задачи", task.result())


asyncio.run(main())



import asyncio
import random


async def task_func(task_id):
    print(f"Старт задачи {task_id}, из корутины task_func")
    await asyncio.sleep(random.uniform(0, 2))
    print(f"Задача {task_id} выполнена в корутине task_func")


async def main():
    tasks = []
    for i in range(5):
        task = asyncio.create_task(task_func(i))
        tasks.append(task)
    print("Все задачи созданы")

    # Цикл, который выполняется, пока есть активные задачи
    while len(tasks) > 0:

        # Ожидание завершения задач
        done, tasks = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

        # Цикл для вывода сообщения о завершении каждой задачи
        for task in done:
            print(f"Задача выполнена- {task.get_name()} и имеет флаг- {task.done()}")


asyncio.run(main())



import asyncio

# Словарь файлов и их размеров
files = {
    "file1.mp4": 32,
    "image2.png": 24,
    "audio3.mp3": 16,
    "document4.pdf": 8,
    "archive5.zip": 40,
    "video6.mkv": 48,
    "presentation7.pptx": 12,
    "ebook8.pdf": 20,
    "music9.mp3": 5,
    "photo10.jpg": 7,
    "script11.py": 3,
    "database12.db": 36,
    "archive13.rar": 15,
    "document14.docx": 10,
    "spreadsheet15.xls": 25,
    "image16.gif": 2,
    "audioBook17.mp3": 60,
    "tutorial18.mp4": 45,
    "code19.zip": 22,
    "profile20.jpg": 9
}

async def download_file(file):
    x = files[file] / 8
    print(f'Начинается загрузка файла: {file}, его размер {files[file]} мб, время загрузки составит {x} сек')
    await asyncio.sleep(round(x, 3))
    print(f'Загрузка завершена: {file}')


async def monitor_tasks(tasks):
    while any(not task.done() for task in tasks):
        await asyncio.sleep(1)
        for task in tasks:
            print(f'Задача {task.get_name()}: {"в процессе" if not task.done() else "завершена"}, Статус задачи {task.done()}')


async def main():
    tasks = [asyncio.create_task(download_file(file), name=file) for file in files]
    await asyncio.gather(monitor_tasks(tasks), *tasks)
    print('Все файлы успешно загружены')

asyncio.run(main())



import asyncio


async def task_coroutine():
    print('Задача выполняется')
    await asyncio.sleep(1)
    return 99


async def main():
    print('Основная корутина начата')
    task = asyncio.create_task(task_coroutine())
    await task

    # Получение результата
    value = task.result()
    print(f'Результат: {value}')
    print('Основная корутина завершена')


asyncio.run(main())



import asyncio

async def perform_task():
    print("Выполнение задачи")
    await asyncio.sleep(1)
    return "Задача выполнена"

async def nested_coroutine():
    task = asyncio.create_task(perform_task())
    await task
    result = task.result()  # Получить результат задачи
    print(f"Результат во вложенной корутине: {result}")

async def main():
    await nested_coroutine()

asyncio.run(main())



import asyncio

async def task_coroutine():
    print("Задача начата")
    await asyncio.sleep(1)
    print("Задача завершена")

async def main():
    task = asyncio.create_task(task_coroutine())
    await task
    result = task.result()
    print(f"Результат задачи: {result}")


asyncio.run(main())



import asyncio


async def task_coroutine():
    print('Задача выполняется')
    await asyncio.sleep(1)

    # Возвращение значения (никогда не достигается)
    return 99


async def main():
    print('Основная корутина начата')
    task = asyncio.create_task(task_coroutine())
    await asyncio.sleep(0.1)
    try:
        value = task.result()
        print(f'Результат: {value}')
    except asyncio.InvalidStateError:
        print('Получено исключение InvalidStateError')
    print('Основная корутина завершена')


asyncio.run(main())



import asyncio


async def task_coroutine():
    print('Задача выполняется')
    await asyncio.sleep(1)
    return 99

async def main():
    print('Основная корутина начата')
    task = asyncio.create_task(task_coroutine())
    await asyncio.sleep(0.1)

    # Проверка, завершена ли задача
    if task.done():
        value = task.result()  # Получение результата завершённой задачи
        print(f'Результат: {value}')
    else:
        print('Задача еще не завершена')

    print('Основная корутина завершена')


asyncio.run(main())



import asyncio

async def task_coroutine():
    print('Задача выполняется')
    await asyncio.sleep(1)

    # Возвращение значения (никогда не достигается)
    return 99


async def main():
    print('Основная корутина начата')
    task = asyncio.create_task(task_coroutine())
    await asyncio.sleep(0.1)

    # Отмена задачи
    task.cancel()
    # Ожидание момента для отмены задачи
    await asyncio.sleep(0.1)
    try:
        # Получение результата
        value = await task
        print(f'Результат: {value}')
    except asyncio.CancelledError:
        print('Задача была отменена.')
    print('Основная корутина завершена')


asyncio.run(main())



import asyncio
import random


random.seed(0)

async def fetch_weather(source, city):
    await asyncio.sleep(random.randint(1, 5))
    temperature = random.randint(-10, 35)
    return f"Данные о погоде получены из источника {source} для города {city}: {temperature}°C"

async def main():
    city = "Москва"
    sources = [
        'http://api.weatherapi.com',
        'http://api.openweathermap.org',
        'http://api.weatherstack.com',
        'http://api.weatherbit.io',
        'http://api.meteostat.net',
        'http://api.climacell.co'
    ]
    tasks = [asyncio.create_task(fetch_weather(source, city)) for source in sources]
    done, pending = await asyncio.wait(tasks,
                                       return_when=asyncio.FIRST_COMPLETED)
    for task in done:
        print(task.result())
    for task in pending:
        task.cancel()

asyncio.run(main())



import asyncio


async def my_task(number):
    # Получение текущего объекта задачи asyncio.
    current_task = asyncio.current_task()

    # Вывод информации о старте задачи и объекте задачи.
    print(f"Текущий объект задачи: {current_task}")
    await asyncio.sleep(1)


async def main():
    task1 = asyncio.create_task(my_task(1))
    await asyncio.gather(task1)


asyncio.run(main())



import asyncio


async def my_task(number):
    # Получение текущего объекта задачи asyncio.
    current_task = asyncio.current_task()

    # Вывод информации о старте задачи и объекте задачи.
    print(f"Текущий объект задачи: {current_task}")
    await asyncio.sleep(1)


async def main():
    await my_task(1)


asyncio.run(main())



import asyncio


async def process_task():
    await asyncio.sleep(1)
    return id(asyncio.current_task())


async def main():
    tasks = [asyncio.create_task(process_task()) for _ in range(10)]
    result = await asyncio.gather(*tasks)
    return result


asyncio.run(main())



import asyncio

async def main():
    print('Основная корутина запущена')
    # Получение текущей задачи
    task = asyncio.current_task()
    # Задача пытается ожидать сама себя
    try:
        await task
    except RuntimeError as e:
        print(f'Ошибка: {e}')


asyncio.run(main())



import asyncio


async def my_task():
    current_task = asyncio.current_task()
    print(f"Текущий объект задачи: {current_task}")

    await asyncio.sleep(1)

    # Отмена текущей задачи
    current_task.cancel()

    # До этой строки мы дойдём, т.к. невозможно отменить активную в данный момент задачу.
    print(420)

async def main():
    task = asyncio.create_task(my_task())
    await task


asyncio.run(main())



import asyncio

async def my_task():
    current_task = asyncio.current_task()
    print(f"Текущий объект задачи: {current_task}")

    await asyncio.sleep(1)

    # Отмена текущей задачи
    current_task.cancel()

    # Попытка отмены задачи не останавливает выполнение немедленно, продолжаем выполнение
    print(420)

async def main():
    try:
        task = asyncio.create_task(my_task())
        await task  # Здесь возникнет CancelledError после попытки отмены
    except asyncio.CancelledError:
        print("Задача была отменена.")
    finally:
        print("Программа завершена без ошибок :)")

asyncio.run(main())



import asyncio

async def process_data():
    print("Обработка данных началась")
    await asyncio.sleep(1)
    print("Обработка данных продолжается")
    await asyncio.sleep(1)
    print("Обработка данных завершена")

async def main():
    task = asyncio.create_task(process_data())
    await asyncio.sleep(2)
    if not task.done():
        task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("Задача была отменена")

asyncio.run(main())



import asyncio

async def update_logs():
    try:
        print("Обновление логов")
        await asyncio.sleep(1)
        raise asyncio.CancelledError("Искусственная отмена")
    except asyncio.CancelledError:
        print("Обработка искусственной отмены")
    print("Логи обновлены")

async def main():
    task = asyncio.create_task(update_logs())
    await task

asyncio.run(main())



import asyncio

async def perform_task():
    current_task = asyncio.current_task()
    print(f"Текущая задача: {current_task}")
    await asyncio.sleep(1)
    current_task.cancel()

async def main():
    task = asyncio.create_task(perform_task())
    try:
        await task
    except asyncio.CancelledError:
        print("Задача отменена")

asyncio.run(main())



import asyncio

async def fetch_data():
    print("Начало загрузки данных")
    await asyncio.sleep(2)
    print("Загрузка данных завершена")

async def main():
    task = asyncio.create_task(fetch_data())
    await asyncio.sleep(1)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("Задача отменена")

asyncio.run(main())



import asyncio


reports = [
    {"name": "Алексей Иванов", "report": "Отчет о прибылях и убытках", "load_time": 5},
    {"name": "Мария Петрова", "report": "Прогнозирование движения денежных средств", "load_time": 4},
    {"name": "Иван Смирнов", "report": "Оценка инвестиционных рисков", "load_time": 3},
    {"name": "Елена Кузнецова", "report": "Обзор операционных расходов", "load_time": 2},
    {"name": "Дмитрий Орлов", "report": "Анализ доходности активов", "load_time": 10}
]

async def download_data(report):
    report_name = report["report"]
    name = report["name"]

    if report["name"] == "Дмитрий Орлов":
        await cancel_task(asyncio.current_task())
        print(f"Загрузка отчета {report_name} для пользователя {name} остановлена. Введите новые данные")

    await asyncio.sleep(report["load_time"])
    print(f"Отчет: {report_name} для пользователя {name} готов")


async def cancel_task(task):
    task.cancel()

async def main():
    tasks = [asyncio.create_task(download_data(report)) for report in reports]

    for task in tasks:
        try:
            await task
        except asyncio.CancelledError:
            pass

asyncio.run(main())
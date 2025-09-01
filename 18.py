import asyncio

async def foo():
    await asyncio.sleep(1)
    return "Завершено"

async def main():
    task = asyncio.create_task(foo())
    print("Корутина:", task.get_coro())

asyncio.run(main())



import asyncio


async def print_hello():
    current_task = asyncio.current_task()
    current_loop_from_task = current_task.get_loop()  # получаем цикл событий из задачи
    current_loop_from_asyncio = asyncio.get_running_loop()  # получаем цикл событий из контекста
    print("Событийный цикл:", current_loop_from_task)
    print(f'{current_loop_from_task is current_loop_from_asyncio = }')

async def main():
    await asyncio.create_task(print_hello())

asyncio.run(main())



import asyncio

async def foo():
    await asyncio.sleep(1)
    for stack in asyncio.current_task().get_stack():
        print(stack)

async def main():
    await asyncio.gather(foo(), foo())

asyncio.run(main())



import asyncio

async def foo():
    await asyncio.sleep(1)
    raise RuntimeError('Возникла ошибка')

async def main():
    await asyncio.gather(foo(), foo())

asyncio.run(main())



def greeting(name):  # Определение функции приветствия
    return f"Привет, {name}!"


def farewell(name):  # Определение функции прощания
    return f"Пока, {name}!"


def process_name(callback, name):
    return callback(name)


name = "Студент"

greeting_result = process_name(greeting, name)
print(greeting_result)

farewell_result = process_name(farewell, name)
print(farewell_result)



import asyncio


async def async_operation():
    print("Асинхронная операция началась...")
    await asyncio.sleep(2)
    print("Асинхронная операция завершена.")
    return "Результат асинхронной операции"


def on_completion(task):  # Callback-функция
    result = task.result()
    print(f"Callback функция вызвана. Получен результат: {result}")


async def main():
    task = asyncio.create_task(async_operation())
    task.add_done_callback(on_completion)  # Регистрация callback-функции
    await task


asyncio.run(main())



import asyncio


def notify_start_training(task):  # Callback-функция - начало тренировки
    print("Тренировка начинается, идите в спортзал.")


def cancel_training(task):  # Callback-функция - отмена тренировки
    print("Тренировка отменена.")


async def prepare_training():  # Асинхронная функция для ожидания тренировки
    await asyncio.sleep(3)


async def main(is_training_scheduled):
    task = asyncio.create_task(prepare_training())

    # Регистрация callback-функций
    task.add_done_callback(notify_start_training)
    task.add_done_callback(cancel_training)

    if is_training_scheduled:
        task.remove_done_callback(
            cancel_training)  # Тренировка назначена, удаляем callback-функцию cancel_training()
    else:
        task.remove_done_callback(
            notify_start_training)  # Тренировка отменена, удаляем callback-функцию notify_start_training()
    await task


# Флаг для определения состояния тренировки:
# True - тренировка назначена
# False - тренировка отменена
asyncio.run(main(False))



import asyncio
import random


async def prepare_pizza():
    print("Готовим пиццу...")
    await asyncio.sleep(5)
    return "Пицца готова!"


def notify_delivery(task):  # Callback-функция для уведомления о доставке пиццы
    print("Курьер: Ваш заказ доставлен!")


def cancel_notification(
        task):  # Callback-функция для отмены уведомления о доставке
    print("Курьер: Уведомление отменено, заберите пиццу самостоятельно.")


async def main():
    task = asyncio.create_task(prepare_pizza())

    # Регистрация callback-функций
    task.add_done_callback(notify_delivery)
    task.add_done_callback(cancel_notification)

    if random.choice([True, False]):
        print('Доставка подтверждена, везём пиццу')
        task.remove_done_callback(
            cancel_notification)  # Отмена уведомления об отмене доставки
    else:
        print('Доставка отменена, самовывоз')
        task.remove_done_callback(
            notify_delivery)  # Отмена уведомления о доставке

    await task


asyncio.run(main())



import asyncio


def callback1(task):
    print('Callback 1: Task completed!')
    print('Result:', task.result())


def callback2(task):
    print('Callback 2: Task completed!')
    print('Result:', task.result())


async def my_coro():
    return 42


async def main():
    task = asyncio.create_task(my_coro())

    # Добавление callback-ов к задаче
    task.add_done_callback(callback1)
    task.add_done_callback(callback2)

    await task


asyncio.run(main())



import asyncio

codes = ["56FF4D", "A3D2F7", "B1C94E", "F56A1D", "D4E6F1",
         "A1B2C3", "D4E5F6", "A7B8C9", "D0E1F2", "A3B4C5",
         "D6E7F8", "A9B0C1", "D2E3F4", "A5B6C7", "D8E9F0"]

messages = ["Привет, мир!", "Как дела?", "Что нового?", "Добрый день!", "Пока!",
            "Спокойной ночи!", "Удачного дня!", "Всего хорошего!", "До встречи!", "Счастливого пути!",
            "Успехов в работе!", "Приятного аппетита!", "Хорошего настроения!", "Спасибо за помощь!", "Всего наилучшего!"]


def func(task):
    result = task.result()
    index = messages.index(result)
    print(f"Код: {codes[index]}")

async def coroutine(message):
    await asyncio.sleep(1)
    print(f"Сообщение: {message}")
    return message

async def main():
    for message in messages:
        task = asyncio.create_task(coroutine(message))
        await task
        task.add_done_callback(func)

asyncio.run(main())



import asyncio

codes = ["56FF4D", "A3D2F7", "B1C94A", "F56A1D", "D4E6F1",
         "A1B2C3", "D4E5F6", "A7B8C9", "D0E1F2", "A3B4C5",
         "D6E7F8", "A9B0C1", "D2E3F4", "A5B6C7", "D8E9F2"]

messages = ["Привет, мир!", "Как дела?", "Что нового?", "Добрый день!", "Пока!",
            "Спокойной ночи!", "Удачного дня!", "Всего хорошего!", "До встречи!", "Счастливого пути!",
            "Успехов в работе!", "Приятного аппетита!", "Хорошего настроения!", "Спасибо за помощь!", "Всего наилучшего!"]


def func(task):
    result = task.result()
    index = messages.index(result)
    print(f"Код: {codes[index]}")

async def coroutine(message):
    await asyncio.sleep(1)
    print(f"Сообщение: {message}")
    return message

async def coroutine_2(message):
    await asyncio.sleep(1)
    print("Сообщение: Неверный код, сообщение скрыто")
    return message

async def main():
    tasks = []
    for code in codes:
        index = codes.index(code)
        # if ord(code[-1:]) % 2 == 0:
        if int(code[-1:], 16) % 2 == 0:
            task = asyncio.create_task(coroutine_2(messages[index]))
            await task
            task.add_done_callback(func)
            # tasks.append(task)
        else:
            task = asyncio.create_task(coroutine(messages[index]))
            await task
            task.add_done_callback(func)
            # tasks.append(task)
    # await asyncio.gather(*tasks)

asyncio.run(main())



import asyncio


codes = ["56FF4D", "A3D2F7", "B1C94A", "F56A1D", "D4E6F1",
         "A1B2C3", "D4E5F6", "A7B8C9", "D0E1F2", "A3B4C5",
         "D6E7F8", "A9B0C1", "D2E3F4", "A5B6C7", "D8E9F2"]
messages = ["Привет, мир!", "Как дела?", "Что нового?", "Добрый день!", "Пока!",
            "Спокойной ночи!", "Удачного дня!", "Всего хорошего!", "До встречи!", "Счастливого пути!",
            "Успехов в работе!", "Приятного аппетита!", "Хорошего настроения!", "Спасибо за помощь!", "Всего наилучшего!"]


async def courutine(n):
    await asyncio.sleep(0)
    return n


def print_code(task):
    result = task.result()
    code = codes[result]

    if int(code, 16) % 2 == 0:
        print(f"Сообщение: Неверный код, сообщение скрыто")
    else:
        print(f"Сообщение: {messages[result]}")

    print(f"Код: {code}")


async def main():
    for i in range(len(messages)):
        task = asyncio.create_task(courutine(i))
        task.add_done_callback(print_code)
        await task

asyncio.run(main())



import asyncio
import random

random.seed(5)

def on_data_parsed(task):
    result = task.result()
    print(f"Найдено {len(result)} файлов для скачивания: {result}")

async def parse_data(url):
    await asyncio.sleep(1)
    if random.choice([True, False]):
        file_urls = [f"{url}/example_file.zip"]
        asyncio.current_task().add_done_callback(on_data_parsed)
    else:
        file_urls = []
    return file_urls

async def main():
    urls = [
        "https://example.com/data1",
        "https://example.com/data2",
        "https://example.com/data3"
    ]
    tasks = [asyncio.create_task(parse_data(url)) for url in urls]
    await asyncio.gather(*tasks)

asyncio.run(main())



import asyncio


# Корутина для задачи, имитирующей выполнение критической задачи.
async def my_coroutine():
    print("Агент приступил к выполнению своего задания.")
    await asyncio.sleep(1)
    # Если задача не была отменена выведем это сообщение
    print("Злодей побежден! Миссия успешно завершена!")


# Корутина для попытки отмены выполнения защищенной задачи.
async def cancel_coroutine(future):
    await asyncio.sleep(0.5)
    future.cancel()
    print("Банг!!! Злодей стреляет в агента!")
    # Можно посмотреть состояние shield_obj после отмены.
    # print(f'shield_obj отменен: {future.cancelled()}')
    # print(f'shield_obj завершен: {future.done()}')


async def main():
    # Создаем защитный объект shield_obj.
    shield_obj = asyncio.shield(my_coroutine())
    # Можно посмотреть тип shield_obj
    # print(f'Тип защитного объекта shield: {type(shield_obj).__name__}') # Future
    print("Бронежилет надет на агента.")
    cancel_task = asyncio.create_task(cancel_coroutine(shield_obj))
    print("Пистолет злодея заряжен.")
    # В случае получения shield_obj asyncio.CancelledError выводим сообщение.
    try:
        await asyncio.gather(shield_obj, cancel_task)
    except asyncio.CancelledError:
        print("Внимание! Бронежилет разрушен!")
    await asyncio.sleep(1)


asyncio.run(main())



import asyncio
import aiohttp


async def fetch(url):
    asyncio.current_task().set_name(url)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return url, (await response.text())[:60]


async def main():
    urls = [
        'https://www.example.com/',
        'https://www.google.com/',
        'https://www.github.com/',
        'https://docs.python.org/3.12/',
        'https://docs.python.org/3.11/',
        'https://stepik.org/'
    ]

    # Создаем список задач, где часть защищена, часть - нет.
    shielded_and_usual_tasks = []
    for url in urls:
        if 'python' in url:
            task = asyncio.shield(fetch(url))
        else:
            task = asyncio.create_task(fetch(url))
        shielded_and_usual_tasks.append(task)

    # Получаем список всех задач в цикле событий кроме задачи, созданной из main()
    tasks = [task for task in asyncio.all_tasks() if task.get_name() != 'Task-1']

    # Получаем результат первого ответа, остальные попытаемся отменить
    done, pending = await asyncio.wait(shielded_and_usual_tasks, return_when=asyncio.FIRST_COMPLETED)
    print(*[f"Первая выполненная задача: {future.result()}" for future in done])
    [future.cancel() for future in pending]
    print(f'\nОтменяем: {len(pending)} задач')

    # Дожидаемся завершения всех задач.
    for task in tasks:
        try:
            result = await task
            print(f"Результат выполнения задачи {task.get_name()}: {result}")
        except asyncio.CancelledError as ex:
            print(f"Ошибка в задаче - задача {task.get_name()} отменена: {type(ex)}")


asyncio.run(main())

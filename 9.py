# Базовый цикл событий мог бы выглядеть следующим образом:
# Данный код — всего лишь условность, реальный цикл событий будет выглядеть куда длиннее и запутаннее.

class SimpleEventLoop:
    def __init__(self):
        self.tasks = []               # Очередь задач

    def add_task(self, task):
        self.tasks.append(task)       # Добавление задачи в очередь

    def run_forever(self):
        while self.tasks:             # Выполнять, пока есть задачи
            task = self.tasks.pop(0)  # Получить первую задачу
            task()                    # Выполнить задачу


def task1():
    print("Выполняется задача 1")

def task2():
    print("Выполняется задача 2")

loop = SimpleEventLoop()
loop.add_task(task1)  # Добавить задачу 1 в цикл событий
loop.add_task(task2)  # Добавить задачу 2 в цикл событий
loop.run_forever()    # Запустить цикл событий


import asyncio
import random

class Pizzeria:
    def __init__(self, name):
        self.name = name

    async def make_pizza(self, order_id):
        cook_time = random.randint(2, 5)      # случайное время готовки пиццы от 2 до 5 секунд
        print(f'Пиццерия {self.name} начала готовить пиццу для заказа {order_id}.')
        await asyncio.sleep(cook_time)        # ожидание пока пицца готовится
        print(f'Пиццерия {self.name} закончила готовить пиццу для заказа {order_id}.')

async def main():
    pizzeria = Pizzeria("Тесто & Сыр")

    # создание 5 заказов
    tasks = [pizzeria.make_pizza(i) for i in range(1, 6)]

    # запуск всех задач (заказов) в Event Loop
    await asyncio.gather(*tasks)

asyncio.run(main())



import asyncio

async def async_func():
    def sync_func():

        # тут может быть любой синхронный код

        return 42

    result = sync_func()
    print(result)

asyncio.run(async_func())



import asyncio


log_events = [
    {"event": "Запрос на вход", "delay": 0.5},
    {"event": "Запрос данных пользователя", "delay": 1.0},
    {"event": "Обновление данных пользователя", "delay": 1.5},
    {"event": "Обновление конфигурации сервера", "delay": 5.0}
    ]


async def fetch_log(event):

    await asyncio.sleep(event["delay"])
    print(f"Событие: '{event["event"]}' обработано с задержкой {event["delay"]} сек.")

async def main():
    tasks = []
    for event in log_events:
        task = asyncio.create_task(fetch_log(event))
        tasks.append(task)
    await asyncio.gather(*tasks)

asyncio.run(main())



import asyncio

async def coroutine_1():
    print("Первое сообщение от корутины 1")
    await asyncio.sleep(2)  # Подберите необходимую задержку
    print("Второе сообщение от корутины 1")

async def coroutine_2():
    print("Первое сообщение от корутины 2")
    await asyncio.sleep(1.5)  # Подберите необходимую задержку
    print("Второе сообщение от корутины 2")

async def coroutine_3():
    print("Первое сообщение от корутины 3")
    await asyncio.sleep(1)  # Подберите необходимую задержку
    print("Второе сообщение от корутины 3")

async def main():
    await asyncio.gather(
        coroutine_1(),
        coroutine_2(),
        coroutine_3(),
    )

asyncio.run(main())



import asyncio

async def coroutine_1(delay=0.1):
    print("Первое сообщение от корутины 1")
    await asyncio.sleep(0.4)  # Первая задержка

    print("Второе сообщение от корутины 1")
    await asyncio.sleep(0.7)  # Вторая задержка

    print("Третье сообщение от корутины 1")
    await asyncio.sleep(0.1)  # Третья задержка

    print("Четвертое сообщение от корутины 1")


async def coroutine_2(delay=0.1):
    print("Первое сообщение от корутины 2")
    await asyncio.sleep(0.3)  # Первая задержка

    print("Второе сообщение от корутины 2")
    await asyncio.sleep(0.4)  # Вторая задержка

    print("Третье сообщение от корутины 2")
    await asyncio.sleep(0.95)  # Третья задержка

    print("Четвертое сообщение от корутины 2")


async def coroutine_3(delay=0.1):
    print("Первое сообщение от корутины 3")
    await asyncio.sleep(0.2)  # Первая задержка

    print("Второе сообщение от корутины 3")
    await asyncio.sleep(0.6)  # Вторая задержка

    print("Третье сообщение от корутины 3")
    await asyncio.sleep(0.8)  # Третья задержка

    print("Четвертое сообщение от корутины 3")

async def main():
    await asyncio.gather(
        coroutine_1(),
        coroutine_2(),
        coroutine_3(),
    )

asyncio.run(main())



import asyncio

async def coroutine_1(delay=0.1):
    print("Первое сообщение от корутины 1")
    await asyncio.sleep(0.3)  # Первая задержка

    print("Второе сообщение от корутины 1")
    await asyncio.sleep(0.3)  # Вторая задержка

    print("Третье сообщение от корутины 1")
    await asyncio.sleep(0.1)  # Третья задержка

    print("Четвертое сообщение от корутины 1")


async def coroutine_2(delay=0.1):
    print("Первое сообщение от корутины 2")
    await asyncio.sleep(0.25)  # Первая задержка

    print("Второе сообщение от корутины 2")
    await asyncio.sleep(0.3)  # Вторая задержка

    print("Третье сообщение от корутины 2")
    await asyncio.sleep(0.3)  # Третья задержка

    print("Четвертое сообщение от корутины 2")


async def coroutine_3(delay=0.1):
    print("Первое сообщение от корутины 3")
    await asyncio.sleep(0.2)  # Первая задержка

    print("Второе сообщение от корутины 3")
    await asyncio.sleep(0.4)  # Вторая задержка

    print("Третье сообщение от корутины 3")
    await asyncio.sleep(0.2)  # Третья задержка

    print("Четвертое сообщение от корутины 3")

async def main():
    await asyncio.gather(
        coroutine_1(),
        coroutine_2(),
        coroutine_3(),
    )

asyncio.run(main())



import asyncio

async def coroutine_1():
    await asyncio.sleep(1.1)  # Задержка для первого сообщения
    print("Сообщение 1 от корутины 1")
    await asyncio.sleep(1.1)  # Задержка для второго сообщения
    print("Сообщение 2 от корутины 1")

async def coroutine_2():
    await asyncio.sleep(1.2)
    print("Сообщение 1 от корутины 2")
    await asyncio.sleep(1.8)
    print("Сообщение 2 от корутины 2")

async def coroutine_3():
    await asyncio.sleep(1.3)
    print("Сообщение 1 от корутины 3")
    await asyncio.sleep(1.9)
    print("Сообщение 2 от корутины 3")

async def coroutine_4():
    await asyncio.sleep(1.4)
    print("Сообщение 1 от корутины 4")
    await asyncio.sleep(2.0)
    print("Сообщение 2 от корутины 4")

async def coroutine_5():
    await asyncio.sleep(1.5)
    print("Сообщение 1 от корутины 5")
    await asyncio.sleep(2.1)
    print("Сообщение 2 от корутины 5")

async def coroutine_6():
    await asyncio.sleep(1.6)
    print("Сообщение 1 от корутины 6")
    await asyncio.sleep(2.2)
    print("Сообщение 2 от корутины 6")

async def main():
    await asyncio.gather(
        coroutine_1(),
        coroutine_2(),
        coroutine_3(),
        coroutine_4(),
        coroutine_5(),
        coroutine_6(),
    )

asyncio.run(main())



import asyncio
import random

random.seed(1)

class MailServer:
    def __init__(self):
        self.mailbox = ["Привет!", "Встреча в 15:00", "Важное уведомление", "Реклама"]

    async def check_for_new_mail(self):
        if random.random() < 0.1:
            return "Ошибка при проверке новых писем."
        return random.choice([True, False])

    async def fetch_new_mail(self):
        mail = random.choice(self.mailbox)
        return f"Новое письмо: {mail}"


async def check_mail(server):

    while True:
        await asyncio.sleep(1)
        check = await server.check_for_new_mail()
        if check == "Ошибка при проверке новых писем.":
            print("Ошибка при проверке новых писем.")
            break
        if check:
            print(await server.fetch_new_mail())
        else:
            print("Новых писем нет.")


async def main():
    await check_mail(MailServer())


asyncio.run(main())



import asyncio
import time


async def process_request(request_name, stages, status):
    for stage_name in stages:
        # await asyncio.sleep(0)
        time.sleep(1)  # Симулируем время выполнения этапа
        status[request_name] = stage_name
        await asyncio.sleep(0)


async def update_status(request_name, status):
    while True:
        # await asyncio.sleep(0)
        print(status)
        if status == {request_name: 'Отправка уведомлений'}:
            break
        await asyncio.sleep(0)


async def main():
    # Исходные данные по запросу и этапам его обработки
    request_name = 'Запрос 1'
    stages = ["Загрузка данных", "Проверка данных", "Анализ данных", "Сохранение результатов", "Отправка уведомлений"]

    status = {request_name: None}

    # Создание задач для каждой корутины
    process_task = asyncio.create_task(process_request(request_name, stages, status))
    updater_task = asyncio.create_task(update_status(request_name, status))

    await asyncio.gather(process_task, updater_task)


asyncio.run(main())
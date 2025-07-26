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
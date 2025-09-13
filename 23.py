import asyncio


lock = asyncio.Lock()

async def my_task(task_id):
    print(f"Задача {task_id} ожидает блокировки с помощью Lock")
    # Ожидание получения блокировки
    await lock.acquire()
    try:
        print(f"Задача {task_id} получила блокировку")
        await asyncio.sleep(2)

    finally:
        print(f"Задача {task_id} блокировка снята")
        # Освобождение блокировки
        lock.release()

async def main():
    tasks = [asyncio.create_task(my_task(i)) for i in range(3)]
    await asyncio.gather(*tasks)

asyncio.run(main())



import asyncio

counter = 0
lock = asyncio.Lock()


async def worker_1():
    global counter
    # Захватываем lock, чтобы исключить конкурентный доступ к counter
    async with lock:
        for i in range(10):
            counter += 1
            print(f"Переменная увеличена на 1 из корутины worker_1, counter = {counter}")
            await asyncio.sleep(1)


async def worker_2():
    global counter
    # Захватываем lock, чтобы исключить конкурентный доступ к counter
    async with lock:
        for i in range(10):
            counter += 1
            print(f"Переменная увеличена на 1 из корутины worker_2, counter = {counter}")
            await asyncio.sleep(1)


async def main():
    task1 = asyncio.create_task(worker_1())
    task2 = asyncio.create_task(worker_2())
    await task1
    await task2


asyncio.run(main())



import asyncio

counter = 0

async def worker_1():
    global counter
    for i in range(10):
        counter += 1
        print(f"Переменная увеличена на 1 из корутины worker_1, counter = {counter}")
        await asyncio.sleep(1)

async def worker_2():
    global counter
    for i in range(10):
        counter += 1
        print(f"Переменная увеличена на 1 из корутины worker_2, counter =  {counter}")
        await asyncio.sleep(1)

async def main():
    task1 = asyncio.create_task(worker_1())
    task2 = asyncio.create_task(worker_2())
    await task1
    await task2

asyncio.run(main())



import asyncio


balance = 100
lock = asyncio.Lock()


async def deposit(amount):
    global balance
    # Используем lock, чтобы защитить доступ к переменной balance
    async with lock:
        print(f"Баланс пополнен на {amount} у.е.")
        balance += amount
        print(f"Текущий баланс {balance}")


async def withdraw(amount):
    global balance
    # Используем lock, чтобы защитить доступ к переменной balance
    async with lock:
        if balance >= amount:
            print(f"Снятие {amount} у.е.")
            balance -= amount
            print(f"Текущий баланс {balance}")
        else:
            print(f"Попытка снять {amount}, недостаточно средств, текущий баланс {balance} у.е.")

async def main():
    task1 = asyncio.create_task(deposit(50))
    task2 = asyncio.create_task(withdraw(200))
    await task1
    await task2

asyncio.run(main())



import asyncio


location_counter = {"A": 0}
lock = asyncio.Lock()

robot_names = ['Электра', 'Механикс', 'Оптимус', 'Симулакр', 'Футуриус']

async def worker(name, location):
    global location_counter
    async with lock:
        print(f"Робот {name}({robot_names.index(name)}) передвигается к месту {location}")
        location_counter[location] += 1
        print(f"Робот {name}({robot_names.index(name)}) достиг места {location}. Место {location} посещено {location_counter[location]} раз")
        await asyncio.sleep(1)


async def main():
    tasks = [asyncio.create_task(worker(name, "A")) for name in robot_names]
    await asyncio.gather(*tasks)


asyncio.run(main())



import asyncio

# Создаем экземпляр события
event = asyncio.Event()

# Определяем корутину для ожидания события
async def wait_for_event():
    print('Ждём события')
    # Ожидаем событие
    await event.wait()
    print('Событие получено')

# Определяем корутину для установки события
async def set_event():
    print('Установка события')
    # Устанавливаем событие
    event.set()

async def main():
    task1 = asyncio.create_task(wait_for_event())
    task2 = asyncio.create_task(set_event())
    await asyncio.gather(task1, task2)

asyncio.run(main())


import asyncio
import random

# Создаем событие
event = asyncio.Event()


# Определяем корутину number_generator, которая генерирует случайные числа
async def number_generator():
    # Генерируем список из 5000 случайных чисел от 1 до 100
    lst = [random.randint(1, 100) for x in range(5000)]

    # Перебираем сгенерированный список
    for en, i in enumerate(lst):
        await asyncio.sleep(random.uniform(0, 0.1))
        if i == 33:
            event.set()

        print(f"Генерируем число: {i}")

        if event.is_set():
            print(f'Событие наступило, число {i} найдено, через {en} попыток')
            break


async def main():
    await asyncio.create_task(number_generator())


asyncio.run(main())



import asyncio
import random

# Создаем события для каждого источника данных
source_a_event = asyncio.Event()
source_b_event = asyncio.Event()
source_c_event = asyncio.Event()


async def fetch_data(source_name, event):
    print(f"{source_name}: Скачивание данных...")
    await asyncio.sleep(random.randint(1, 3))
    print(f"{source_name}: Данные получены.")
    event.set()  # Сигнализируем, что данные готовы


async def analyze_data():
    # ожидаем получения нужных данных
    await source_a_event.wait()
    await source_b_event.wait()
    await source_c_event.wait()
    print("Все данные получены. Начало анализа...")
    await asyncio.sleep(2)  # тут может быть анализ данных/отправка их в БД/...
    print("Анализ завершен.")


async def main():
    # Запускаем задачи для получения данных от различных источников
    asyncio.create_task(fetch_data("Источник A", source_a_event))
    asyncio.create_task(fetch_data("Источник B", source_b_event))
    asyncio.create_task(fetch_data("Источник C", source_c_event))

    await analyze_data()


asyncio.run(main())



import asyncio

alarm = asyncio.Event()

async def sensor(sensor_id, sensor_name):
    print(f'Датчик {sensor_id} IP-адрес {sensor_name} настроен и ожидает срабатывания')
    await alarm.wait()
    print(f'Датчик {sensor_id} IP-адрес {sensor_name} активирован, "Wee-wee-wee-wee"')

async def activate_alarm():
    await asyncio.sleep(5)
    alarm.set()
    print("Датчики зафиксировали движение")

async def main():
    ip = ["192.168.0.3", "192.168.0.1", "192.168.0.2", "192.168.0.4", "192.168.0.5"]
    await asyncio.gather(*(sensor(i, ip[i]) for i in range(5)), activate_alarm())

asyncio.run(main())



import asyncio

# Корутина для демонстрации реакции ботов.
async def robot_reaction(event, bot, message):
    await event.wait()
    await speech_synt(bot, message)

# Корутина проверки id от датчика персонала
async def _event(id, id_sm, event):
    if id == id_sm:
        await asyncio.sleep(2)
        event.set()
    else:
        print('Спокойно, ждем сержанта!')

# Корутина для настройки ботов
async def birthday():
    id_sm = 'sms_62933d018e09401bb61c3e823bdb4477'
    id_bots = ["d234", "d235", "d236", "d237", "d238", "d239", "d240", "d241"]
    message = "Повелитель механизмов! Долгих лет! Ты ведешь нас! Слава сержанту! Ура!"
    # Создаем событие
    happy_event = asyncio.Event()
    # Создаем задачи для демонстрации реакции ботов
    bots_tasks = [asyncio.create_task(robot_reaction(happy_event, bot, message)) for bot in id_bots]
    # Подключение корутины _event к датчику в системе контроля экипажа
    await sensor_id_124(_event, id_sm, happy_event)



import asyncio

# Создаем экземпляр Semaphore максимум c двумя разрешениями

semaphore = asyncio.Semaphore(2)
# semaphore = asyncio.BoundedSemaphore(2)


async def my_coroutine(id):
    print(f'Корутина {id} хочет получить семафор')
    await semaphore.acquire()
    print(f'Корутина {id} получила семафор')
    await asyncio.sleep(1)
    semaphore.release()
    print(f'Корутина {id} отпустила семафор')
    semaphore.release()
    print(f'Корутина {id} отпустила семафор еще раз')


async def main():
    await asyncio.gather(my_coroutine(1), my_coroutine(2), my_coroutine(3))


asyncio.run(main())

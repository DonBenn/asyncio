import asyncio


sem = asyncio.Semaphore(3) # Создаем сефамор с начальным значением счетчика 3.

async def task(id):
    async with sem:  # Семафор захватывается и освобождается с помощью менеджера контекста
        print(f'Задача {id} начала выполнение')
        await asyncio.sleep(1)
        print(f'Задача {id} завершила выполнение')


async def main():
    tasks = [task(i) for i in range(50)]
    await asyncio.gather(*tasks)

asyncio.run(main())



from random import random
import asyncio


async def task(semaphore, number):
    async with semaphore:
        value = random()
        await asyncio.sleep(value)
        print(f'Задача {number} получила {value}')


async def main():
    semaphore = asyncio.Semaphore(2)
    tasks = [asyncio.create_task(task(semaphore, i)) for i in range(10)]
    await asyncio.wait(tasks)


asyncio.run(main())



import asyncio

semaphore = asyncio.Semaphore(1)  # Создаем семафор


async def write_to_file(text):
    async with semaphore:  # Используем семафор для ограничения доступа к файлу
        with open("file.txt", "a") as file:
            file.write(text)


async def main():
    # Создаем список задач
    tasks = [write_to_file("строка 1\n"), write_to_file("строка 2\n"),
             write_to_file("строка 3\n")]
    await asyncio.gather(*tasks)


asyncio.run(main())



import asyncio

# Создаем два семафора с максимальным количеством зеленых светофоров равным 2
sem1 = asyncio.Semaphore(2)
sem2 = asyncio.Semaphore(2)

async def task(id):
    async with sem1, sem2:
        print(f'Задача {id} начала выполнение')
        await asyncio.sleep(1)
        print(f'Задача {id} завершила выполнение')

async def main():
    tasks = [task(i) for i in range(5)]
    await asyncio.gather(*tasks)

asyncio.run(main())



import asyncio


sem = asyncio.Semaphore(2)

async def task(id):
    try:
        async with sem:
            print(f'Задача {id} начала выполнение')
            await asyncio.sleep(1)
            if id == 2:  # Для задачи с id 2 искусственно создаем исключение
                raise Exception('Ошибка в задаче')
            print(f'Задача {id} завершила выполнение')
    except Exception as e:
        print(f'В задаче {id} произошла ошибка: {e}')


async def main():
    tasks = [task(i) for i in range(5)]
    await asyncio.gather(*tasks)

asyncio.run(main())



import asyncio


users = ["sasha", "petya", "masha", "katya", "dima", "olya", "igor", "sveta", "nikita", "lena",
         "vova", "yana", "kolya", "anya", "roma", "nastya", "artem", "vera", "misha", "liza"]

semaphore = asyncio.Semaphore(3)
counter = 0

async def task(user):
    global counter
    async with semaphore:
        print(f'Пользователь {user} делает запрос')
        await asyncio.sleep(1)
        print(f'Запрос от пользователя {user} завершен')
        counter += 1
        print(f'Всего запросов: {counter}')
        # print(f'Всего запросов: {(len(users)-len(semaphore._waiters))}')


async def main():
    tasks = [asyncio.create_task(task(user)) for user in users]
    await asyncio.gather(*tasks)


asyncio.run(main())



import asyncio


# semaphore = asyncio.Semaphore(2)
semaphore = asyncio.BoundedSemaphore(2)

print(f'Исходный лимит для {type(semaphore).__name__}: {semaphore._value}')


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
    try:
        await asyncio.gather(my_coroutine(1), my_coroutine(2), my_coroutine(3))
    # Перехват исключения для ситуации, когда слишком много release()
    except ValueError:
        print(f'Попытка несанкционированного release().\n'
              f'Количество попыток освободить семафор превышает количество его захватов')
    finally:
        print(f'Лимит {type(semaphore).__name__}: {semaphore._value} ', end='/')
        print(f'(Лимит был увеличен)' if semaphore._value > 2 else f'(Увеличения лимита не произошло)')


asyncio.run(main())



import asyncio


apartments_data = [
    {"id": "apt_1_1", "price": 45000, "rooms": 2, "address": "ул. Ленина, д. 10", "area": 50},
    {"id": "apt_1_2", "price": 55000, "rooms": 3, "address": "ул. Пушкина, д. 15", "area": 75},
    {"id": "apt_1_3", "price": 50000, "rooms": 2, "address": "ул. Суворова, д. 8", "area": 55},
    {"id": "apt_1_4", "price": 65000, "rooms": 3, "address": "ул. Чехова, д. 22", "area": 80},
    {"id": "apt_1_5", "price": 48000, "rooms": 2, "address": "ул. Горького, д. 12", "area": 52},
    {"id": "apt_2_2", "price": 60000, "rooms": 4, "address": "ул. Чайковского, д. 20", "area": 90},
    {"id": "apt_2_3", "price": 37000, "rooms": 1, "address": "ул. Тургенева, д. 9", "area": 42},
    {"id": "apt_2_4", "price": 62000, "rooms": 3, "address": "ул. Арбат, д. 25", "area": 85},
    {"id": "apt_2_5", "price": 33000, "rooms": 1, "address": "ул. Шолохова, д. 7", "area": 38},
    {"id": "apt_3_1", "price": 70000, "rooms": 4, "address": "ул. Тверская, д. 3", "area": 95},
    {"id": "apt_3_2", "price": 72000, "rooms": 3, "address": "ул. Кутузовский проспект, д. 21", "area": 100},
    {"id": "apt_3_3", "price": 75000, "rooms": 4, "address": "ул. Неглинная, д. 11", "area": 110},
    {"id": "apt_3_4", "price": 69000, "rooms": 3, "address": "ул. Новослободская, д. 14", "area": 90},
    {"id": "apt_3_5", "price": 71000, "rooms": 3, "address": "ул. Большая Дмитровка, д. 17", "area": 95},
    {"id": "apt_4_1", "price": 40000, "rooms": 2, "address": "ул. Ярославская, д. 30", "area": 50},
    {"id": "apt_4_2", "price": 42000, "rooms": 2, "address": "ул. Лескова, д. 6", "area": 52},
    {"id": "apt_4_3", "price": 43000, "rooms": 2, "address": "ул. Синельникова, д. 5", "area": 54},
    {"id": "apt_4_4", "price": 44000, "rooms": 2, "address": "ул. Петровка, д. 28", "area": 56},
    {"id": "apt_4_5", "price": 41000, "rooms": 2, "address": "ул. Колобова, д. 4", "area": 51},
    {"id": "apt_5_1", "price": 55000, "rooms": 3, "address": "ул. Авиамоторная, д. 12", "area": 70},
    {"id": "apt_5_2", "price": 56000, "rooms": 3, "address": "ул. Вавилова, д. 19", "area": 72},
    {"id": "apt_5_3", "price": 57000, "rooms": 3, "address": "ул. Керченская, д. 8", "area": 74},
    {"id": "apt_5_4", "price": 58000, "rooms": 3, "address": "ул. Профсоюзная, д. 16", "area": 76},
    {"id": "apt_5_5", "price": 59000, "rooms": 3, "address": "ул. Синельникова, д. 10", "area": 78},
    {"id": "apt_2_1", "price": 35000, "rooms": 1, "address": "ул. Гагарина, д. 5", "area": 40},
]

semaphore = asyncio.BoundedSemaphore(5)

async def fetch_apartment_data(apartment):
    async with semaphore:
        await asyncio.sleep(1)
        if min_price <= apartment["price"] <= max_price and apartment['rooms'] == rooms:
            print(apartment)

async def main():
    tasks = [asyncio.create_task(fetch_apartment_data(apartment)) for apartment in apartments_data]
    await asyncio.gather(*tasks)


min_price, max_price, rooms = map(int, input().split())
asyncio.run(main())



import asyncio

names = input().split()
account = input()

async def convert_file(file_name, semaphore):
    async with semaphore:
        await asyncio.sleep(1)
        return f"Файл {file_name} обработан"


async def main():
    free = asyncio.BoundedSemaphore(2)
    premium = asyncio.BoundedSemaphore(10)
    if account== 'free':
        tasks = [asyncio.create_task(convert_file(name, free)) for name in names]
    if account == 'premium':
        tasks = [asyncio.create_task(convert_file(name, premium)) for name in names]
    result = await asyncio.gather(*tasks)
    for res in result:
        print(res)


asyncio.run(main())



import asyncio


# Корутина worker, принимающая объект asyncio.Barrier.
async def worker(barrier: asyncio.Barrier, num):
    print(f"worker_{num} ждет на барьере")

    # В этой точке задача приостанавливается до накопления на барьере заданного количества задач.
    await barrier.wait()
    # После преодоления барьера работа задачи возобновляется.

    await asyncio.sleep(0.5)
    print(f"worker_{num} прошел барьер")


async def main():
    # Создание объекта asyncio.Barrier (для разблокировки ожидаем 4 задачи).
    barrier = asyncio.Barrier(4)
    tasks = [asyncio.create_task(worker(barrier, num)) for num in range(3)]

    print(f'Состояние {barrier=}')
    print("Ждем, пока worker's пройдут барьер")
    await asyncio.sleep(0)
    print(f'Состояние {barrier=}')

    # Регистрируем на нашем барьере последнюю, 4-ю задачу для преодоления барьера.
    await barrier.wait()

    # Часть кода которая может быть выполнена только после преодоления барьера.
    await asyncio.sleep(1)
    print("Все задачи успешно прошли барьер")
    print(f'Состояние {barrier=}')


asyncio.run(main())



import asyncio


# Корутина для задачи прохождения барьера.
async def task(name, num, barrier):
    await asyncio.sleep(num / 10)
    print(f'{name} начинает и ожидает у барьера.')
    if not barrier.broken:
        print(f'    На барьере ожидает задач: {barrier.n_waiting + 1}')
        print(
            f'    Для прохождения нужно еще задач: {barrier.parties - (barrier.n_waiting + 1)}')

    try:
        async with barrier:
            print(f'{name} прошла через барьер.')

    except asyncio.BrokenBarrierError:
        print(
            f'{name} обнаружила, что барьер {["сброшен", "сломан"][barrier.broken]}.')


async def aborting_task(name, barrier):
    await asyncio.sleep(1)
    print(f'--{name} сбрасывает/ломает барьер.')

    # Вариант 1. Прерываем работу барьера.
    await barrier.abort()
    # Вариант 2. Сбрасываем барьер в исходное состояние.
    # await barrier.reset()


async def main():
    # Создаем барьер на 2 задачи
    barrier = asyncio.Barrier(2)
    tasks1 = [asyncio.create_task(task(f'Задача {i}', i, barrier)) for i in
              range(1, 4)
              ] + [asyncio.create_task(
        aborting_task('Сбрасывающая задача', barrier))]

    await asyncio.gather(*tasks1)
    # Создаем новый список задач.
    tasks2 = [asyncio.create_task(task(f'Задача {i}_new', i, barrier)) for i in
              range(1, 7)]

    # Проверяем состояние барьера
    print(f'--Барьер разрушен: {(state := barrier.broken)}')
    if not state:
        # Если барьер цел запускаем на него вторую партию задач
        print('--Барьер сброшен,продолжаем использовать барьер.')
    else:
        print('--Барьер сломан, все новые задачи получат BrokenBarrierError.')
        # Это для эксперимента со сломанным барьером:
        # await barrier.reset()
        # У меня барьер успешно перезапускается, но в доках написано:
        # Если барьер разрушен, возможно, лучше просто оставить его и создать новый.

    await asyncio.gather(*tasks2)


asyncio.run(main())



import asyncio

players = {
    'DragonSlayer': 0.2,
    'ShadowHunter': 0.6,
    'MagicWizard': 0.8,
    'KnightRider': 0.3,
    'ElfArcher': 2.0,
    'DarkMage': 1.4,
    'SteelWarrior': 1.6,
    'ThunderBolt': 3.0,
    'SilentAssassin': 1.1,
    'FireSorcerer': 2.6,
    'MysticHealer': 1.5,
    'IceQueen': 1.7,
    'BladeMaster': 2.9,
    'StormBringer': 1.2,
    'ShadowKnight': 0.9,
    'GhostRogue': 1.8,
    'FlameWielder': 0.7,
    'ForestGuardian': 0.4,
    'BattlePriest': 1.9,
    'EarthShaker': 2.8
}
barrier = asyncio.Barrier(5)

async def enter_dungeon(player, time):
    await asyncio.sleep(time)
    print(f"{player} готов войти в подземелье")
    await barrier.wait()
    print(f"{player} вошел в подземелье")

async def main():
    tasks = [asyncio.create_task(enter_dungeon(key, value)) for key, value in players.items()]
    await asyncio.gather(*tasks)

asyncio.run(main())



import asyncio

players = {
    'DragonSlayer': 0.2,
    'ShadowHunter': 0.6,
    'MagicWizard': 0.8,
    'ElfArcher': 2.0,
    'DarkMage': 1.4,
    'SteelWarrior': 1.6,
    'ThunderBolt': 3.0
}

async def enter_dungeon(barrier, player, delay):
    try:
        print(await asyncio.sleep(delay, f"{player} готов войти в подземелье"))
        async with barrier:
            print(f"{player} вошел в подземелье")
    except asyncio.BrokenBarrierError:
        print(f"{player} не смог попасть в подземелье. Группа не собрана")


async def main():
    barrier = asyncio.Barrier(5)
    tasks = [asyncio.create_task(enter_dungeon(barrier, name, delay)) for name, delay in players.items()]
    done, pending = await asyncio.wait(tasks, timeout=5)
    await barrier.reset() if pending else ...


asyncio.run(main())
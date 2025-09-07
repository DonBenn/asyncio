import asyncio

# Инициализация банковского счета
bank_account = 1000


# Асинхронная функция для снятия денег
async def withdraw_money(amount):
    global bank_account
    # Проверка наличия достаточных средств на счете
    if bank_account >= amount:
        print(f"Снятие {amount} р. успешно")
        await asyncio.sleep(1)

        # Вычитание суммы снятия из общего банковского счета
        bank_account -= amount


async def main():
    task1 = asyncio.create_task(withdraw_money(900))
    task2 = asyncio.create_task(withdraw_money(900))
    await asyncio.gather(task1, task2)

    print(f'Остаток средств {bank_account} р.')


asyncio.run(main())



import asyncio

# Библиотечный каталог
library_catalog = {
    "Мастер и Маргарита": 3,
    "Война и мир": 2,
    "Преступление и наказание": 1,
}

# Резервирование книг для пользователей
reservation_tasks = {
    "Алексей": "Мастер и Маргарита",
    "Ирина": "Мастер и Маргарита",
    "Сергей": "Война и мир",
    "Елена": "Преступление и наказание",
    "Анна": "Мастер и Маргарита",
    "Игорь": "Война и мир",
    "Мария": "Преступление и наказание",
}

async def reserve_book(name, book):
    if book in library_catalog:
        library_catalog[book] -= 1
        await asyncio.sleep(1)
        print("Книга успешно зарезервирована.")
    else:
        print("Книга отсутствует. Резервирование отменено.")


async def main():
    tasks = [asyncio.create_task(reserve_book(name, book)) for name, book in reservation_tasks.items()]
    await asyncio.gather(*tasks)
    for key, value in library_catalog.items():
        print(f"{key}: {value}")


asyncio.run(main())



import asyncio

# Общий ресурс, который будет обновляться
shared_resource = 0


async def update_resource():

    # Используем глобальную переменную shared_resource
    global shared_resource
    print('Начинаем обновление shared_resource')

    # Сохраняем текущее значение shared_resource во временную переменную
    temp = shared_resource

    # Имитация операции ввода-вывода
    await asyncio.sleep(1)

    # Увеличиваем значение shared_resource на 1
    shared_resource = temp + 1
    print('Обновление shared_resource завершено')


async def main():
    await asyncio.gather(update_resource(), update_resource())
    print(f'shared_resource: {shared_resource}')

asyncio.run(main())



import asyncio

# Эмуляция комнаты с замком
class Room:
    def __init__(self):
        self.lock = asyncio.Lock()

    async def use(self, name):
        # Захват мьютекса
        await self.lock.acquire()
        try:
            print(f"{name} вошел в комнату.")
            # Имитация выполнения работы внутри комнаты
            await asyncio.sleep(1)
            print(f"{name} вышел из комнаты.")
        finally:
            # Освобождение мьютекса
            self.lock.release()

async def person(name, room):
    # Человек (задача) пытается использовать комнату
    print(f"{name} хочет войти в комнату.")
    await room.use(name)

async def main():
    room = Room()  # Инициализация комнаты с замком

    # Создание задач для нескольких людей, пытающихся войти в комнату
    await asyncio.gather(
        person("Алексей", room),
        person("Мария", room),
        person("Иван", room)
    )

asyncio.run(main())



import asyncio

class Room:
    def __init__(self):
        self.lock = asyncio.Lock()

    async def use(self, name):
        # Использование менеджера контекста для работы с замком
        async with self.lock:
            print(f"{name} вошел в комнату.")
            # Имитация выполнения работы внутри комнаты
            await asyncio.sleep(1)
            print(f"{name} вышел из комнаты.")

async def person(name, room):
    # Человек (задача) пытается использовать комнату
    print(f"{name} хочет войти в комнату.")
    await room.use(name)

async def main():
    room = Room()  # Инициализация комнаты с замком

    # Создание задач для нескольких людей, пытающихся войти в комнату
    await asyncio.gather(
        person("Алексей", room),
        person("Мария", room),
        person("Иван", room)
    )

asyncio.run(main())



import asyncio

bank_account = 1000


# Принимает сумму для снятия и блокировку для безопасного доступа к банковскому счету
async def withdraw_money(amount, lock):
    global bank_account

    # Используем асинхронную блокировку для безопасного доступа к банковскому счету
    async with lock:
        if bank_account >= amount:
            print(f"Снятие {amount} р. успешно")
            await asyncio.sleep(1)
            bank_account -= amount


async def main():
    lock = asyncio.Lock()
    task1 = asyncio.create_task(withdraw_money(900, lock))
    task2 = asyncio.create_task(withdraw_money(900, lock))


    await asyncio.gather(task1, task2)
    print(f'Остаток средств {bank_account} р.')


asyncio.run(main())



import asyncio

# Общий ресурс, который будет обновляться
shared_resource = 0

# Создаем асинхронный замок для обеспечения безопасности при обновлении shared_resource
lock = asyncio.Lock()


async def update_resource():

    # Используем глобальную переменную shared_resource
    global shared_resource
    print('Начинаем обновление shared_resource')

    # Используем асинхронный замок для обеспечения безопасности при обновлении shared_resource
    async with lock:

        # Сохраняем текущее значение shared_resource во временную переменную
        temp = shared_resource
        await asyncio.sleep(1)

        # Увеличиваем значение shared_resource на 1
        shared_resource = temp + 1
    print('Обновление shared_resource завершено')

async def main():
    await asyncio.gather(update_resource(), update_resource())
    print(f'shared_resource: {shared_resource}')

asyncio.run(main())



import asyncio

# Инициализация банковского счета
bank_account = 10000
print(f"Исходный баланс: {bank_account}р")

lock = asyncio.Lock()

async def withdraw_money(amount):
    global bank_account
    # Проверка наличия достаточных средств на счете
    async with lock:
        print(f"Попытка снять {amount}р. Доступный баланс: {bank_account}р")
        if bank_account >= amount:
            await asyncio.sleep(0.01)  # Имитация долгой операции
            bank_account -= amount
            print(f"Снятие {amount}р успешно. Оставшийся баланс: {bank_account}р")
        else:
            print(f"Снятие {amount}р не удалось. Недостаточно средств. Оставшийся баланс: {bank_account}р")


async def main():
    tasks = [asyncio.create_task(withdraw_money(1200)) for x in range(9)]
    await asyncio.gather(*tasks)
    print(f'Конечный остаток средств: {bank_account}р')

asyncio.run(main())



import asyncio

# Библиотечный каталог
library_catalog = {
    "Мастер и Маргарита": 5,
    "Война и мир": 3,
    "Преступление и наказание": 2,
    "Анна Каренина": 4,
    "Отцы и дети": 2,
    "Белые ночи": 1,
    "Кому на Руси жить хорошо": 1,
}

# Резервирование книг для пользователей
reservation_tasks = {
    "Алексей": "Мастер и Маргарита",
    "Ирина": "Мастер и Маргарита",
    "Сергей": "Война и мир",
    "Елена": "Преступление и наказание",
    "Анна": "Мастер и Маргарита",
    "Игорь": "Война и мир",
    "Мария": "Преступление и наказание",
    "Олег": "Анна Каренина",
    "Юлия": "Белые ночи",
    "Дмитрий": "Отцы и дети",
    "Татьяна": "Кому на Руси жить хорошо",
    "Светлана": "Анна Каренина",
    "Владимир": "Белые ночи",
    "Марина": "Кому на Руси жить хорошо",
    "Иван": "Анна Каренина",
}

lock = asyncio.Lock()

async def reserve_book(user_name, book_title):
    async with lock:
        if book_title in library_catalog:
            if library_catalog[book_title] > 0:
                library_catalog[book_title] -= 1
                await asyncio.sleep(0.1)
                print(f"Пользователь {user_name} успешно зарезервировал книгу '{book_title}'.")
            else:
                print(f"Книга '{book_title}' отсутствует на складе. Резервирование для пользователя {user_name} отменено.")

async def main():
    tasks = [asyncio.create_task(reserve_book(user_name, book_title)) for user_name, book_title in reservation_tasks.items()]
    await asyncio.gather(*tasks)

asyncio.run(main())



import asyncio


async def car(lock1, lock2, name):
    print(f'Автомобиль {name} приближается к перекрестку.')
    await asyncio.sleep(1)  # Имитация времени приближения к перекрестку

    async with lock1:
        print(f'Автомобиль {name} ожидает на перекрестке.')
        await asyncio.sleep(1)  # Имитация времени ожидания на перекрестке

        async with lock2:
            # В реальной ситуации этот код никогда не выполнится из-за deadlock
            print(f'Автомобиль {name} покидает перекресток.')


async def main():
    # Инициализация замков для каждого "направления" движения
    north_south = asyncio.Lock()
    east_west = asyncio.Lock()

    # Запуск асинхронных задач для каждого автомобиля
    await asyncio.gather(
        car(north_south, east_west, 'Север-Юг'),
        car(east_west, north_south, 'Восток-Запад'),
        car(north_south, east_west, 'Юг-Север'),
        car(east_west, north_south, 'Запад-Восток')
    )


asyncio.run(main())



import asyncio

# Корутина, которая ждет сама себя
async def coro():
    print("Ожидает сама себя")
    await asyncio.sleep(1)
    await coro()

asyncio.run(coro())



import asyncio


# Корутина, которая дважды получает замок
async def task(lock):
    print('Задача пытается захватить замок...')

    # Захватываем замок
    async with lock:
        print('Задача снова пытается захватить замок...')

        # Снова захватываем замок
        async with lock:
            pass


async def main():
    lock = asyncio.Lock()
    await task(lock)


asyncio.run(main())



import asyncio


async def coro(num):
    await asyncio.sleep(num * 0.1)
    print(f'Задача {num} выполнена')


async def main():
    tasks = []
    for i in range(5):
        # asyncio.create_task(coro(i))
        tasks.append(asyncio.create_task(coro(i)))
    # tasks = asyncio.all_tasks()
    await asyncio.gather(*tasks)
    print('Работа программы завершена')


asyncio.run(main())



import asyncio

async def coroutine_a(event_a, event_b):
    print("Корутина A: начата")
    await event_b.wait()  # ожидает установки события в корутине B
    print("Корутина A: ожидает корутину B")
    event_a.set()

async def coroutine_b(event_b, event_c):
    print("Корутина B: начата")
    await event_c.wait()  # ожидает установки события в корутине C
    print("Корутина B: ожидает корутину C")
    event_b.set()

async def coroutine_c(event_c, event_a):
    print("Корутина C: начата")
    await event_a.wait()  # ожидает установки события в корутине A
    print("Корутина C: ожидает корутину A")
    event_c.set()

async def main():
    # Создание событий для каждой корутины
    event_a = asyncio.Event()
    event_b = asyncio.Event()
    event_c = asyncio.Event()

    # Запуск корутин
    await asyncio.gather(
        coroutine_a(event_a, event_b),
        coroutine_b(event_b, event_c),
        coroutine_c(event_c, event_a),
    )

asyncio.run(main())



import asyncio

async def coroutine_a(b_event, c_event):
    print('Корутина A ожидает B')
    try:
        await asyncio.wait_for(b_event.wait(), timeout=2)
    except asyncio.TimeoutError:
        print('Корутина A прекратила ожидание B из-за таймаута')
    c_event.set()  # Сообщаем C, что A завершила ожидание
    print('Корутина A завершила выполнение')

async def coroutine_b(a_event, c_event):
    print('Корутина B ожидает C')
    try:
        await asyncio.wait_for(c_event.wait(), timeout=2)
    except asyncio.TimeoutError:
        print('Корутина B прекратила ожидание C из-за таймаута')
    a_event.set()  # Сообщаем A, что B завершила ожидание
    print('Корутина B завершила выполнение')

async def coroutine_c(b_event, a_event):
    print('Корутина C ожидает A')
    try:
        await asyncio.wait_for(a_event.wait(), timeout=2)
    except asyncio.TimeoutError:
        print('Корутина C прекратила ожидание A из-за таймаута')
    b_event.set()  # Сообщаем B, что C завершила ожидание
    print('Корутина C завершила выполнение')

async def main():
    # Инициализируем события для управления ожиданием корутин
    a_event = asyncio.Event()
    b_event = asyncio.Event()
    c_event = asyncio.Event()

    # Запускаем корутины
    await asyncio.gather(
        coroutine_a(b_event, c_event),
        coroutine_b(a_event, c_event),
        coroutine_c(b_event, a_event),
    )

asyncio.run(main())



import asyncio


async def task(number, first_lock, second_lock):
    print(f"Задача {number}: пытается захватить первую блокировку")
    async with first_lock:
        print(f"Задача {number}: захватила первую блокировку")
        await asyncio.sleep(1)  # Имитация работы в критическом участке
        print(f"Задача {number}: пытается захватить вторую блокировку")

        async with second_lock:
            print(f"Задача {number}: захватила вторую блокировку")
            await asyncio.sleep(
                1)  # Дополнительная работа в критическом участке
    print(f"Задача {number}: завершила выполнение")


async def main():
    # Инициализация двух асинхронных блокировок
    lock1 = asyncio.Lock()
    lock2 = asyncio.Lock()

    # Запуск корутин с блокировками в разном порядке
    await asyncio.gather(
        task(1, lock1, lock2),
        task(2, lock2, lock1),
    )


asyncio.run(main())



import asyncio


async def task(lock):
    print('Задача приобретает блокировку...')
    # Приобретаем блокировку
    await lock.acquire()

    # Генерируем исключение, симулируя ошибку
    raise Exception('Произошло что-то плохое')

    # этот код никогда не будет выполнен
    print('Задача освобождает блокировку...')
    lock.release()


async def main():
    lock = asyncio.Lock()
    asyncio.create_task(task(lock))
    await asyncio.sleep(1)
    print('Основная функция приобретает блокировку...')
    # Используем метод acquire() для асинхронного приобретения блокировки
    await lock.acquire()

    # этот код не будет выполнен
    lock.release()


asyncio.run(main())



import asyncio


number_facts_database = {
    1: "Один — это единственное число, которое не является ни простым, ни составным.",
    2: "Два — это единственное чётное простое число.",
    3: "Три — это количество пространственных измерений, в которых мы живём (длина, ширина, высота).",
    4: "Четыре — это количество нуклеотидов в ДНК (аденин, тимин, гуанин, цитозин).",
    5: "Пять — это количество человеческих чувств (зрение, слух, обоняние, вкус, осязание).",
    6: "Шесть — это первое совершенное число (его делители (1, 2 и 3) в сумме дают само число).",
    7: "Семь — это число дней в неделе и цветов радуги.",
    8: "Восемь — это символ бесконечности (если повернуть его горизонтально).",
    9: "Девять — это количество планет в Солнечной системе до исключения Плутона из их числа.",
    10: "Десять — это база десятичной системы счисления, которую мы используем ежедневно."
}

async def get_fact_from_db(lock, number):
    await asyncio.sleep(number * 0.1)
    global number_facts_database
    # await lock.acquire()
    print(f'{number}: {number_facts_database[number]}')


async def main():
    lock = asyncio.Lock()
    tasks = [asyncio.create_task(get_fact_from_db(lock, i)) for i in range(1, 11)]
    await asyncio.gather(*tasks)


asyncio.run(main())



import asyncio

global_counter = 0
lock = asyncio.Lock()

async def increment():
    async with lock:
        global global_counter
        temp = global_counter
        await asyncio.sleep(.01)
        global_counter = temp + 2.39

async def main():
    await asyncio.gather(*[asyncio.create_task(increment()) for x in range(99)])

asyncio.run(main())
print(f"global_counter: {round(global_counter,2)}")
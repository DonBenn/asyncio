import asyncio

async def task_func(task_id):
    print(f"Задача {task_id} выполнена")
    return task_id

async def main():
    # Создаем несколько задач
    tasks = [asyncio.create_task(task_func(i), name=f'Task-{i}') for i in range(5)]

    # Ожидаем завершения всех задач
    _, pending = await asyncio.wait(tasks)

    # Проверяем, что все задачи завершены
    assert not pending, f"{len(pending)} ожидающих задач"
    for task in tasks:
        print(f"Результат задачи {task.get_name()}:", task.result())


asyncio.run(main())



import asyncio


async def my_coro(delay):
    """Асинхронная задача, которая просто ждет указанное время."""
    task_name = asyncio.current_task().get_name()
    print(f'{task_name} началась, будет выполняться {delay} секунд(ы).')
    await asyncio.sleep(delay)
    print(f'{task_name} завершена.')
    return f'{task_name}: результат'


async def main():
    tasks = [asyncio.create_task(my_coro(i), name=f'Задача_{i}') for i in range(1, 4)]
    print("Запуск задач...")
    done, pending = await asyncio.wait(tasks, timeout=2)

    # Проверяем, какие задачи выполнены, а какие еще в ожидании
    print(f"\nРезультаты завершенных задач: {[d.result() for d in done]}")
    if pending:
        print(f"Ожидающие задачи: {[x.get_name() for x in pending]}")
        # Опционально: Можно отменить оставшиеся задачи, если это необходимо
        print(f"Отмена задач...")
        for task in pending:
            print(f"{task.get_name()}: Отмена ")
            task.cancel()
    else:
        print(f"Все задачи завершены.")


asyncio.run(main())



import asyncio


async def foo():
    print("Запущена корутина foo")
    await asyncio.sleep(5)


async def bar():
    print("Запущена корутина bar")
    await asyncio.sleep(3)


async def main():
    tasks = [asyncio.create_task(foo(), name='foo'), asyncio.create_task(bar(), name='bar')]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    for task in done:
        print("Задание завершено:", task.get_name())
    for task in pending:
        print("Задание ожидает выполнения:", task.get_name())


asyncio.run(main())



import asyncio


async def foo():
    print("Запущена корутина foo")
    await asyncio.sleep(5)


async def bar():
    print("Запущена корутина bar")
    await asyncio.sleep(3)


async def main():
    tasks = [asyncio.create_task(foo(), name='foo'), asyncio.create_task(bar(), name='bar')]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)

    for task in done:
        print("Задание завершено:", task.get_name())


asyncio.run(main())



import asyncio

async def foo():
    print("Запущена корутина foo")
    await asyncio.sleep(5)
    raise Exception("Ошибка в foo")

async def bar():
    print("Запущена корутина bar")
    await asyncio.sleep(3)
    raise Exception("Ошибка в bar")

async def main():
    tasks = [asyncio.create_task(foo(), name="foo"), asyncio.create_task(bar(), name="bar")]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_EXCEPTION)

    for task in done:
        print("Задание завершено:", task.get_name())
        if task.exception() is not None:
            print("Исключение задачи:", task.exception())
    for task in pending:
        print("Задача в ожидании:", task.get_name())

asyncio.run(main())



import asyncio

processor_delays = {
    'Intel Core i9-11900K': 7.01,
    'Intel Core i7-11700K': 4.32,
    'Intel Core i5-11600K': 8.59,
    'AMD Ryzen 9 5950X': 2.53,
}

async def simulate_processing(delay):
    await asyncio.sleep(delay)


async def main():
    tasks = [asyncio.create_task(simulate_processing(value), name=key) for key, value in processor_delays.items()]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    for task in done:
        print(f"Первый завершенный процесс: {task.get_name()}")


asyncio.run(main())



import asyncio

dishes = {'Куриный суп': 118, 'Бефстроганов': 13, 'Рататуй': 49, 'Лазанья': 108, 'Паэлья': 51, 'Утка по-пекински': 41,
          'Суши': 116, 'Цезарь с курицей': 106, 'Маргарита пицца': 23, 'Шпинатный пирог': 29, 'Карри с курицей': 88,
          'Тирамису': 10, 'Греческий салат': 18, 'Фалафель': 102, 'Буррито': 90, 'Карбонара': 111,
          'Ризотто с грибами': 79, 'Фокачча': 38, 'Шашлык': 121, 'Газпачо': 95, 'Блинчики': 118, 'Сэндвич с авокадо': 67,
          'Кимчи': 80, 'Табуле': 68, 'Паста алла норма': 32, 'Жареный рис': 47, 'Том Ям': 19, 'Веганский бургер': 43,
          'Киш с луком': 61, 'Салат Нисуаз': 97}

async def cook_dish(name, duration):
    print(f"Приготовление {name} начато.")
    await asyncio.sleep(duration/10)
    print(f"Приготовление {name} завершено за {duration / 10} секунды.")


async def main():
    tasks = [asyncio.create_task(cook_dish(key, value), name=key) for
             key, value in dishes.items()]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED, timeout=10)
    for task in pending:
        print(
            f"{task.get_name()} не успел(а,о) приготовиться и будет отменено.")
        task.cancel()
    print(
        f"\nПриготовлено блюд: {len(done)}. Не успели приготовиться: {len(pending)}.")

asyncio.run(main())



import asyncio

data = [
    {
        "Имя": "Sarah",
        "Фамилия": "Lewis",
        "Возраст": 54,
        "Навыки": 10,
        "Страна проживания": "Tuvalu",
        "Город проживания": "North Heathertown",
        "Уровень секретности": 1,
        "Псевдоним": "michelestanton",
        "Профессия": "Консультант по безопасности",
        "Владение иностранными языками": {
            "Английский": "Свободно"
        },
        "Специализированные навыки": "Взлом, слежка",
        "Образование": "Военная академия",
        "Предыдущие места работы": "Неизвестно",
        "Хобби и интересы": "Фотография, путешествия",
        "Членство в организациях": "Неизвестно",
        "История путешествий": "Многочисленные страны",
        "Наличие дипломатического паспорта": True,
        "Биометрические данные": "Доступны",
        "Семейное положение": "Неизвестно",
        "Наличие специализированного оборудования": "Есть",
        "Срок доступа": "5857 часов",
        "Тайные операции": [
            "Операция 'Кондор'",
            "Операция 'Снег'"
        ],
        "Скрытые навыки": [
            "Мастер перевоплощений",
            "Эксперт по криптографии"
        ],
        "Контакты в иностранных спецслужбах": "Turner, Craig and Ortiz",
        "Специализация": "Контрразведка"
    },

]

async def check_access(data_elem):
    try:
        await asyncio.sleep(data_elem["Уровень секретности"])
        if data_elem["Срок доступа"] is None:
            raise ValueError(
                f'Ошибка доступа: У участника {data_elem["Имя"]} {data_elem["Фамилия"]} срок доступа истек или не указан.')

        print(
            f'Участник {data_elem["Имя"]} {data_elem["Фамилия"]} имеет действующий доступ. Продолжительность доступа: {data_elem["Срок доступа"]}')
    except Exception as e:
        raise ValueError(str(e))

async def main():
    tasks = [asyncio.create_task(check_access(participant), name=f'{participant["Имя"]} {participant["Фамилия"]}') for participant in data]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_EXCEPTION)
    for task in done:
        if task.exception() is not None:
            print(task.exception())

    for task in pending:
        task.cancel()
        print(
            f'Доступ участника {task.get_name()} отменен из-за критической ошибки.')

asyncio.run(main())



import asyncio
import random


async def task(num):
    await asyncio.sleep(delay := random.random())
    return f'Task {num} completed, {delay=:.3f}'


async def main():
    tasks = [asyncio.create_task(task(i)) for i in range(5)]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    while done:
        for completed_task in done:
            result = await completed_task
            print(result)
        if pending:
            done, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)
        else:
            break

asyncio.run(main())



import asyncio
import random


async def task(num):
    await asyncio.sleep(delay := random.random())
    return f'Task {num} completed, {delay=:.3f}'


async def main():
    tasks = [asyncio.create_task(task(i)) for i in range(5)]

    for completed_task in asyncio.as_completed(tasks):
        # completed_task - объект корутины, создаваемый функцией as_completed(), возвращающий результат завершенной задачи.
        result = await completed_task
        print(result)


asyncio.run(main())



import asyncio


async def upload_file(filename: str, delay: float) -> str:
    await asyncio.sleep(delay)
    return filename

async def main():
    files = {
        "Начало": 4.2,
        "Матрица": 3.8,
        "Аватар": 5.1,
        "Интерстеллар": 2.6,
        "Паразиты": 6.0,
        "Джокер": 4.5,
        "Довод": 3.3,
        "Побег из Шоушенка": 5.4,
        "Криминальное чтиво": 2.9,
        "Форрест Гамп": 5.8
    }
    tasks = [asyncio.create_task(upload_file(key, value)) for key, value in files.items()]
    for completed_task in asyncio.as_completed(tasks):
        filename = await completed_task
        print(f"{filename}: фильм загружен на сервер")

asyncio.run(main())



import asyncio
import random

# Не менять!
random.seed(1)

async def collect_gold():
    await asyncio.sleep(random.randint(1, 5))
    return random.randint(10, 50)


async def main():
    total = 0
    tasks = [asyncio.create_task(collect_gold()) for _ in range(10)]
    for completed_task in asyncio.as_completed(tasks):
        amount = await completed_task
        total += amount
        print(f"Собрано {amount} единиц золота.")
        print(f"Общее количество золота: {total} единиц.")
        print()

asyncio.run(main())
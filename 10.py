import asyncio


async def my_coroutine():
    # Получаем имя текущей задачи.
    task = asyncio.current_task()
    task_name = task.get_name()

    print(f'Задача {task_name} запущена.')
    await asyncio.sleep(1)
    print(f'Задача {task_name} была выполнена.')


async def main():
    task = asyncio.create_task(my_coroutine(), name='my_task')
    print(f"Задача {task.get_name()} создана, но еще не запущена")
    await task
    print('Ожидание выполнения my_task окончено, управление было возвращено в main().\nmain() завершает свою работу.')


asyncio.run(main())



import asyncio

async def my_coroutine():
    print(f"Корутина запустилась")
    await asyncio.sleep(2)
    print(f"Корутина завершена")  # данное сообщение выведено не будет!

async def main():
    task = asyncio.create_task(my_coroutine())
    await asyncio.sleep(1)

asyncio.run(main())



import asyncio


async def my_coroutine(i, delay):
    print(f"Корутина {i} запустилась")
    await asyncio.sleep(delay)
    print(f"Корутина {i} завершена")


async def main():
    task1 = asyncio.create_task(my_coroutine(1, 2))
    task2 = asyncio.create_task(my_coroutine(2, 1))
    await asyncio.gather(task1, task2)

asyncio.run(main())



import asyncio
places = [
   "начинает путешествие",
   "находит загадочный лес",
   "переправляется через реку",
   "встречает дружелюбного дракона",
   "находит сокровище"]

roles = ["Искатель приключений", "Храбрый рыцарь", "Отважный пират"]

async def counter(name, delay=.1):
    for place in places:
        print(f"{name} {place}...")
        await asyncio.sleep(delay)

async def main():
    task1 = asyncio.create_task(counter(name=roles[0], delay=.1))
    task2 = asyncio.create_task(counter(name=roles[1], delay=.1))
    task3 = asyncio.create_task(counter(name=roles[2], delay=.1))

    #Дождитесь выполнения всех созданных задач в главной корутине с помощью await.
    await asyncio.gather(task1, task2, task3)

asyncio.run(main())



import asyncio


async def countdown(name, seconds):
    i = seconds
    while i > 0:

        if name == "Квест на поиск сокровищ":
            print(f"{name}: Осталось {i} сек. Найди скрытые сокровища!")

        else:
            print(f"{name}: Осталось {i} сек. Беги быстрее, дракон на хвосте!")

        i -= 1
        await asyncio.sleep(0.2)
    print(f"{name}: Задание выполнено! Что дальше?")


async def main():
    treasure_hunt = "Квест на поиск сокровищ"
    dragon_escape = "Побег от дракона"
    task1 = asyncio.create_task(countdown(treasure_hunt, 10))
    task2 = asyncio.create_task(countdown(dragon_escape, 5))
    await asyncio.gather(task1, task2)


asyncio.run(main())



import asyncio

async def countdown(name, seconds):
    for i in range(seconds, 0, -1):
        if name == "Квест на поиск сокровищ":
            print(f"{name}: Осталось {i} сек. Найди скрытые сокровища!")
        elif name == "Побег от дракона":
            print(f"{name}: Осталось {i} сек. Беги быстрее, дракон на хвосте!")
        await asyncio.sleep(1)
    print(f"{name}: Задание выполнено! Что дальше?")

async def main():
    treasure_hunt = asyncio.create_task(countdown("Квест на поиск сокровищ", 10))
    dragon_escape = asyncio.create_task(countdown("Побег от дракона", 5))

    await asyncio.gather(treasure_hunt, dragon_escape)

asyncio.run(main())



import asyncio

news_list = [
    "Новая волна COVID-19 обрушилась на Европу",
    "Рынки акций растут на фоне новостей о вакцине",
    "обнаружен новый вид этого",
    "олимпийских игр не будет в этом году",
]

async def analyze_news(keyword, news_list, delay):
    for news in news_list:
        if keyword in news:
            print(f"Найдено соответствие для '{keyword}': {news}")
            await asyncio.sleep(delay)


async def main():
    # Создаем асинхронные задачи для каждой корутины с разными ключевыми словами и задержками
    task1 = asyncio.create_task(analyze_news("COVID-19", news_list, 0.1))
    task2 = asyncio.create_task(analyze_news("игр", news_list, 0.1))
    task3 = asyncio.create_task(analyze_news("новый вид", news_list, 0.1))

    await asyncio.gather(task1, task2, task3)
    # Ожидаем выполнения всех задач


asyncio.run(main())



import asyncio


async def monitor_cpu(status_list):
    task_name = asyncio.current_task().get_name()
    for status in status_list:
        print(f"[{task_name}] Статус проверки: {status}")
        if status == "Катастрофически":
            print(
                f"[{task_name}] Критическое состояние достигнуто. Инициируется остановка...")
        await asyncio.sleep(0.1)


async def monitor_memory(status_list):
    task_name = asyncio.current_task().get_name()
    for status in status_list:
        print(f"[{task_name}] Статус проверки: {status}")
        if status == "Катастрофически":
            print(
                f"[{task_name}] Критическое состояние достигнуто. Инициируется остановка...")
        await asyncio.sleep(0.1)


async def monitor_disk_space(status_list):
    task_name = asyncio.current_task().get_name()
    for status in status_list:
        print(f"[{task_name}] Статус проверки: {status}")
        if status == "Катастрофически":
            print(
                f"[{task_name}] Критическое состояние достигнуто. Инициируется остановка...")
        await asyncio.sleep(0.1)



async def main():
    status_list = [
        "Отлично", "Хорошо", "Удовлетворительно", "Средне",
        "Пониженное", "Ниже среднего", "Плохо", "Очень плохо",
        "Критично", "Катастрофически"
    ]
    task1 = asyncio.create_task(monitor_cpu(status_list), name="CPU")
    task2 = asyncio.create_task(monitor_memory(status_list), name="Память")
    task3 = asyncio.create_task(monitor_disk_space(status_list), name="Дисковое пространство")
    await asyncio.gather(task1, task2, task3)

asyncio.run(main())



import asyncio


async def activate_portal(x):
    print(f'Активация портала в процессе, требуется времени: {x} единиц')
    await asyncio.sleep(x)
    return x*2

async def perform_teleportation(x):
    print(f'Телепортация в процессе, требуется времени: {x} единиц')
    await asyncio.sleep(x)
    time = x+2
    return time

async def portal_operator():
    task = asyncio.create_task(activate_portal(2))
    result = await task
    if result > 4:
        task2 = asyncio.create_task(perform_teleportation(1))
        await task2
    else:
        task2 = asyncio.create_task(perform_teleportation(result))
        result2 = await task2


    print(f'Результат активации портала: {result} единиц энергии')
    print(f'Результат телепортации: {result2} единиц времени')


asyncio.run(portal_operator())



import asyncio


async def activate_portal(x):
    print(f'Активация портала в процессе, требуется времени: {x} единиц')
    await asyncio.sleep(x)
    return x*2

async def perform_teleportation(x):
    print(f'Телепортация в процессе, требуется времени: {x} единиц')
    await asyncio.sleep(x)
    return x+2

async def recharge_portal(x):
    print(f'Подзарядка портала, требуется времени: {x} единиц')
    await asyncio.sleep(x)
    return x*3


async def check_portal_stability(x):
    print(f'Проверка стабильности портала, требуется времени: {x} единиц')
    await asyncio.sleep(x)
    return x+4

async def restore_portal(x):
    print(f'Восстановление портала, требуется времени: {x} единиц')
    await asyncio.sleep(x)
    return x*5

async def close_portal(x):
    print(f'Закрытие портала, требуется времени: {x} единиц')
    await asyncio.sleep(x)
    return x-1


async def portal_operator():
    task_1 = asyncio.create_task(activate_portal(2))
    task_2 = asyncio.create_task(perform_teleportation(3))
    task_3 = asyncio.create_task(recharge_portal(4))
    task_4 = asyncio.create_task(check_portal_stability(5))
    task_5 = asyncio.create_task(restore_portal(6))
    task_6 = asyncio.create_task(close_portal(7))
    results = await asyncio.gather(task_1, task_2, task_3, task_4, task_5, task_6)

    print(f'Результат активации портала: {results[0]} единиц энергии')
    print(f'Результат телепортации: {results[1]} единиц времени')
    print(f'Результат подзарядки портала: {results[2]} единиц энергии')
    print(f'Результат проверки стабильности: {results[3]} единиц времени')
    print(f'Результат восстановления портала: {results[4]} единиц энергии')
    print(f'Результат закрытия портала: {results[5]} единиц времени')


asyncio.run(portal_operator())
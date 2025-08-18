import asyncio


async def my_coro():
    await asyncio.sleep(5)
    return 'Привет мир!'


async def main():
    await asyncio.wait_for(my_coro(), timeout=3)


asyncio.run(main())



import asyncio


async def my_coro():
    await asyncio.sleep(1)
    return 'Привет мир!'


async def main():
    result = await asyncio.wait_for(my_coro(), timeout=3)
    print(result)


asyncio.run(main())



import asyncio

async def long_running_task():
    # Эмуляция долгой задачи
    await asyncio.sleep(10)
    print("Задача завершена")

async def main():
    # Создаем задачу
    task = asyncio.create_task(long_running_task())

    try:
        # Ожидаем завершения задачи в течение 5 секунд
        await asyncio.wait_for(task, timeout=5)
    except TimeoutError:
        print("Задача не была завершена в установленное время")

asyncio.run(main())



import asyncio
import time

async def coro(delay):
    start = time.time()
    print(f'Задача получила delay: {delay}')
    await asyncio.sleep(delay)
    print(f'Задача выполнена за {time.time()-start:.3f}')

async def main():
    # Создаем задачу со временем выполнения 3 секунды
    task = asyncio.create_task(coro(3))
    await asyncio.sleep(2.1)
    # Ожидаем выполнения task 1 секунду
    await asyncio.wait_for(task, timeout=1)

asyncio.run(main())



import asyncio


async def long_running_task():
    await asyncio.sleep(10)
    return "Завершение работы защищенной корутины long_running_task() после timeout"


async def main():
    task = asyncio.create_task(long_running_task())
    try:
        # Используем shield для защиты задачи от отмены
        await asyncio.wait_for(asyncio.shield(task), timeout=5)

    except TimeoutError:
        print("Задача не была завершена в установленное время")
        result = await task
        print(result)


asyncio.run(main())



import asyncio

runners = {
    "Молния Марк": 12.8,
    "Ветреный Виктор": 13.5,
    "Скоростной Степан": 11.1,
    "Быстрая Белла": 10.8,
    "Легкая Лиза": 11.3,
    "Ракетный Роман": 15.5,
    "Турбо Таня": 13.7,
    "Живчик Женя": 12.5,
    "Вихревой Валерий": 14.5,
    "Газель Галина": 13.4,
    "Непобедимый Никита": 11.7,
    "Прыгун Павел": 10.9,
    "Зефирный Захар": 11.2,
    "Метеор Марина": 9.3,
    "Экспресс Елена": 9.1,
    "Флеш Филипп": 10.2,
    "Аэродинамичная Алина": 8.6,
    "Бриз Борис": 9.4,
    "Ветерок Василий": 13.1,
    "Стрела Станислав": 12.9
}


async def run_lap(name, speed):
    distance = 100
    time_needed  = round(distance / speed, 2)
    await asyncio.sleep(time_needed)
    return print(f"{name} завершил круг за {time_needed} секунд")


async def main(max_time=10):  # Максимальное время для завершения круга 10 сек
    tasks = [asyncio.create_task(run_lap(key, value)) for key, value in runners.items()]

    try:
        await asyncio.wait_for(asyncio.gather(*tasks), max_time)
    except asyncio.TimeoutError:
        pass

asyncio.run(main())



import asyncio

spells = {
    "Огненный шар": 3,
    "Ледяная стрела": 2,
    "Щит молний": 4,
    "Телепортация": 7
}

# Максимальное время для каста заклинания
max_cast_time = 5  # Секунды

# Ученики мага
students = ["Алара", "Бренн", "Сирил", "Дариа", "Элвин"]


async def cast_spell(student, spell, cast_time):
    try:
        await asyncio.wait_for(asyncio.shield(asyncio.sleep(cast_time)), max_cast_time)
        print(f"{student} успешно кастует {spell} за {cast_time} сек.")
    except asyncio.TimeoutError:
        await asyncio.sleep(cast_time)
        print(f"Ученик {student} не справился с заклинанием {spell}, и учитель применил щит. "
              f"{student} успешно завершает заклинание с помощью shield.")

async def main():
    tasks = [
        asyncio.create_task(
            cast_spell(student, spell, cast_time)) for student in students for spell, cast_time in spells.items()
    ]
    await asyncio.gather(*tasks)


asyncio.run(main())


import asyncio


async def cast_spell(student, spell, cast_time):

    await asyncio.sleep(cast_time)
    if cast_time <= max_cast_time:
        print(f"{student} успешно кастует {spell} за {cast_time} сек.")
    else:
        print(
            f"Ученик {student} не справился с заклинанием {spell}, и учитель применил щит. "
            f"{student} успешно завершает заклинание с помощью shield.")

async def main():
    tasks = []
    for student in students:
        for spell, cast_time in spells.items():
            task = asyncio.create_task(cast_spell(student, spell, cast_time))
            tasks.append(task)

    for task in tasks:
        try:
            # Обернуть каждую задачу в shield и установить таймаут
            await asyncio.wait_for(asyncio.shield(task), timeout=max_cast_time)
        except asyncio.TimeoutError:
            print(f"Заклинание не было завершено вовремя.")


asyncio.run(main())
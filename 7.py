import time
import asyncio


async def coro(num, seconds):
    print(f"coro{num} начала свое выполнение")
    await asyncio.sleep(seconds)
    print(f"coro{num} выполнена за {seconds} секунду(ы)")


async def main():
    # Создание объектов корутин путем вызова корутинной функции.
    coro1 = coro(1, 2)
    coro2 = coro(2, 1)
    # Запуск и ожидание выполнения объектов корутин.
    await coro2
    await coro1

start = time.time()
asyncio.run(main())
print(f'Программа выполнена за {time.time()-start:.3f} секунд(ы)')



import asyncio
import time


async def coro(num, seconds):
    print(f"Задача{num} начала свое выполнение")
    await asyncio.sleep(seconds)
    print(f"Задача{num} выполнена за {seconds} секунду(ы)")


async def main():
    # Создание задач из корутины.
    task1 = asyncio.create_task(coro(1, 2))
    task2 = asyncio.create_task(coro(2, 1))
    # Запуск и ожидание выполнения задач.
    await task2
    await task1

start = time.time()
asyncio.run(main())
print(f'Программа выполнена за {time.time()-start:.3f} секунд(ы)')



import asyncio

async def read_book(student, time):
    print(f"{student} начал читать книгу.")
    await asyncio.sleep(time)
    print(f"{student} закончил читать книгу за {time} секунд.")


async def main():
    task1 = asyncio.create_task(read_book("Алекс", 5))
    task2 = asyncio.create_task(read_book("Мария", 3))
    task3 = asyncio.create_task(read_book("Иван", 4))
    await asyncio.gather(task1, task2, task3)

asyncio.run(main())



import asyncio

students = {
    "Алекс": {"course": "Асинхронный Python", "steps": 515, "speed": 78},
    "Мария": {"course": "Многопоточный Python", "steps": 431, "speed": 62},
    "Иван": {"course": "WEB Парсинг на Python", "steps": 491, "speed": 57}
}

async def study_course(student, course, steps, speed):
    print(f'{student} начал проходить курс {course}.')
    result = round(steps / speed, 2)
    await asyncio.sleep(result)
    print(f'{student} прошел курс {course} за {result} ч.')


async def main():
    student_items = [
        asyncio.create_task(study_course(
            student, value['course'], value['steps'], value['speed']))
        for student, value in students.items()
    ]

    await asyncio.gather(*student_items)

asyncio.run(main())


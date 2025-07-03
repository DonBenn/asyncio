import asyncio

async def my_coroutine(num):
    print(f'Начинаем выполнение корутины {num}')
    await asyncio.sleep(1)  # в этот момент данная корутина передает управление в цикл событий
    print(f'Закончили выполнение корутины {num}')

async def main():
    tasks = [asyncio.create_task(my_coroutine(i)) for i in range(1, 6)]
    await asyncio.gather(*tasks)

asyncio.run(main())



# НЕЛЬЗЯ
import asyncio

async def main():
    await None  # или await "Hello, World!" и др. не awaitable объекты

asyncio.run(main())  # ошибка TypeError!



# НЕЛЬЗЯ
import asyncio

def main():
    await asyncio.sleep(1)

asyncio.run(main())  # ошибка SyntaxError!



import asyncio

async def my_coroutine():
    print(f'Начинаем')
    await asyncio.sleep(1)  # Тут блокируется корутина my_coroutine() до завершения asyncio.sleep().
    print(f'Закончили')

async def main():
    await my_coroutine()  #  Тут блокируется main() до завершения my_coroutine().
    print('выполнение корутины завершено')


asyncio.run(main())



import asyncio

async def my_coroutine():
    await asyncio.sleep(1)
    return "Задача завершена"

async def main():
    result = await my_coroutine()  # сохраняем в переменную результат выполнения my_coroutine()
    print(result)


asyncio.run(main())



import asyncio

async def my_coroutine(num):
    await asyncio.sleep(1)
    return f"Задача {num} завершена"

async def main():
    tasks = [asyncio.create_task(my_coroutine(i)) for i in range(1, 4)]
    result = await asyncio.gather(*tasks)
    print(result)

asyncio.run(main())



import asyncio
import time

async def my_coroutine_without_await(num):
    print(f'Начинаем выполнение корутины {num}')
    time.sleep(1)
    print(f'Закончили выполнение корутины {num}')

async def main():
    tasks = [asyncio.create_task(my_coroutine_without_await(i)) for i in range(1, 6)]
    await asyncio.gather(*tasks)

asyncio.run(main())



import asyncio

# Асинхронная функция, имитирующая чтение данных из файла
async def read_data_from_file(filename):
    print(f"Начинаем чтение из файла {filename}")
    await asyncio.sleep(2)  # # Имитация задержки для чтения файла
    print(f"Чтение из файла {filename} завершено")
    return f"данные из {filename}"

# Асинхронная функция, имитирующая отправку данных в интернет
async def send_data_to_internet(data):
    print("Начинаем отправку данных в интернет")
    await asyncio.sleep(3)  # Имитация задержки для отправки данных
    print("Отправка данных в интернет завершена")

# Главная асинхронная функция, которая управляет выполнением программы
async def main():
    filename = "example.txt"
    # Чтение данных из файла
    file_data = await read_data_from_file(filename)
    # Отправка прочитанных данных в интернет
    await send_data_to_internet(file_data)

asyncio.run(main())



import asyncio

async def task1():
    await asyncio.sleep(1)
    print("Привет из корутины task1")

async def task2():
    await asyncio.sleep(1)
    print("Привет из корутины task2")

async def main():
    await asyncio.create_task(task1())
    await asyncio.create_task(task2())

asyncio.run(main())



import asyncio

async def task1():
    print("Начинаем задачу 1")
    await asyncio.sleep(1)
    print("Привет из корутины task1")
    await asyncio.sleep(1)
    print("Задача 1 завершилась")

async def task2():
    print("Начинаем задачу 2")
    await asyncio.sleep(2)
    print("Привет из корутины task2")
    await asyncio.sleep(2)
    print("Задача 2 завершилась")

async def task3():
    print("Начинаем задачу 3")
    await asyncio.sleep(3)
    print("Привет из корутины task3")
    await asyncio.sleep(3)
    print("Задача 3 завершилась")

async def main():
    task_1 = asyncio.create_task(task1())
    task_2 = asyncio.create_task(task2())
    task_3 = asyncio.create_task(task3())

    await task_1
    await task_2
    await task_3

asyncio.run(main())



import asyncio

async def compute_square(x):
    print(f"Вычисляем квадрат числа: {x}")
    await asyncio.sleep(1)  # Имитация длительной операции
    return x * x

async def main():
    # Создаём и запускаем задачи
    tasks = [asyncio.create_task(compute_square(i)) for i in range(10)]
    # Ожидаем завершения всех задач и собираем результаты
    results = await asyncio.gather(*tasks)

    for result in results:
        print(f"Результат: {result}")

asyncio.run(main())
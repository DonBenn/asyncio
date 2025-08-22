import asyncio

async def main():
    print("Hello, World!")


loop = asyncio.new_event_loop()
# asyncio.set_event_loop(loop)

loop.run_until_complete(main())
loop.close()



import asyncio
import threading


# Корутина, которая будет выполнена в каждом из независимых потоков.
async def task(loop, num):
    # Получаем id потока в котором выполняется задача.
    thread_id = threading.current_thread().ident
    # Получаем текущий цикл событий.
    e_loop_id = asyncio.get_running_loop()
    print(
        f"Задача task_{num} запущена в потоке id: {thread_id}, "
        f"текущий event loop id: {id(e_loop_id)}, "
        f"переданный event loop id: {id(loop)}")
    await asyncio.sleep(num)
    print(f"Задача task_{num} завершена!")


# Функция для запуска асинхронного цикла событий в отдельном потоке.
def start_loop(loop, coro, num):
    # Установка переданного цикла событий в качестве текущего для этого потока.
    asyncio.set_event_loop(loop)
    # Запуск задачи в установленном цикле событий, ожидание ее результата.
    loop.run_until_complete(coro(loop, num))
    # Закрываем цикл событий
    loop.close()


# Основная асинхронная функция, управляющая созданием циклов событий и потоков.
async def main():

    print(f'main()\nТекущий поток id: {threading.current_thread().ident}\n'
          f'Текущий цикл событий id: {id(asyncio.get_running_loop())}\n{"-" * 50}')
    loop1 = asyncio.new_event_loop()  # Создание нового цикла событий.
    print(f'Создан новый цикл событий id: {id(loop1)}')
    loop2 = asyncio.new_event_loop()  # Создание еще одного нового цикла событий.
    print(f'Создан новый цикл событий id: {id(loop2)}\n{"-" * 50}')

    # Создание и запуск независимых потоков для каждого цикла событий и корутины.
    thread1 = threading.Thread(target=start_loop, args=(loop1, task, 1,))
    thread2 = threading.Thread(target=start_loop, args=(loop2, task, 2))

    # Запуск потоков.
    thread1.start()
    thread2.start()

    # Ожидание завершения потоков.
    thread1.join()
    thread2.join()


asyncio.run(main())



import asyncio

async def main():
    print("Корутина завершена")


loop = asyncio.new_event_loop()

loop.run_until_complete(main())
loop.close()



import asyncio

def check_loop_status(loop):
    return f'Цикл событий активен: {loop.is_running()}, Цикл событий закрыт: {loop.is_closed()}.'

async def main():
    print(check_loop_status(loop))
    print("Корутина завершена")


loop = asyncio.new_event_loop()
print(check_loop_status(loop))
loop.run_until_complete(main())
loop.close()
print(check_loop_status(loop))



import asyncio


async def my_task(idx):
    print(f"Задача {idx} выполняется")
    print(f'Идентификатор цикла задачи: {id(asyncio.get_running_loop())}')
    await asyncio.sleep(1)
    print(f"Задача {idx} завершена")


async def main():
    print(f'Исходный идентификатор цикла: {id(asyncio.get_running_loop())}')

    # Создаем новый цикл выполнения задач
    loop = asyncio.new_event_loop()

    # Выводим идентификатор нового цикла выполнения
    print(f'Идентификатор нового цикла: {id(loop)}')

    # Устанавливаем новый цикл выполнения как текущий
    asyncio.set_event_loop(loop)

    # Выводим идентификатор текущего цикла выполнения после установки нового
    print(f'Текущий идентификатор цикла: {id(asyncio.get_running_loop())}')

    tasks = [asyncio.ensure_future(my_task(i)) for i in range(5)]
    await asyncio.gather(*tasks)
    loop.close()


asyncio.run(main())



import asyncio
import threading


# Выводит сообщения о начале и завершении выполнения, а также идентификатор текущего цикла событий.
async def task1(task_id, loop):
    print(f"Задача {task_id} начинается, цикл = {loop}")
    print(
        f'Идентификатор цикла в задаче {task_id}: {id(asyncio.get_running_loop())}')
    await asyncio.sleep(2)
    print(f"Задача {task_id} завершена")


async def task2(task_id, loop):
    # Аналогично task1, но с другой задержкой.
    print(f"Задача {task_id} начинается, цикл = {loop}")
    print(
        f'Идентификатор цикла в задаче {task_id}: {id(asyncio.get_running_loop())}')
    await asyncio.sleep(3)
    print(f"Задача {task_id} завершена")


# Функция для запуска асинхронной задачи в отдельном цикле событий в новом потоке.
def start_loop(loop, coroutine):
    # Установка переданного цикла событий как текущего для потока.
    asyncio.set_event_loop(loop)

    # Запуск переданной корутины до её полного выполнения.
    loop.run_until_complete(coroutine)


# Главная асинхронная функция, координирующая создание циклов событий и запуск задач.
async def main():
    # Вывод идентификатора исходного (оригинального) цикла событий.
    print(
        f'Идентификатор оригинального цикла: {id(asyncio.get_running_loop())}')

    # Создание и вывод идентификаторов новых циклов событий для демонстрации их уникальности.
    loop1 = asyncio.new_event_loop()
    print(f'Идентификатор первого нового цикла: {id(loop1)}')
    loop2 = asyncio.new_event_loop()
    print(f'Идентификатор второго нового цикла: {id(loop2)}')

    # Подготовка асинхронных задач для запуска в отдельных циклах и потоках.
    coroutine1 = task1(1, loop1)
    coroutine2 = task2(2, loop2)

    # Создание и запуск отдельных потоков для выполнения асинхронных задач в разных циклах событий.
    thread1 = threading.Thread(target=start_loop, args=(loop1, coroutine1,))
    thread2 = threading.Thread(target=start_loop, args=(loop2, coroutine2,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


asyncio.run(main())



import asyncio

async def my_task(n):
    print(f"Task {n} starting")
    await asyncio.sleep(1)
    print(f"Task {n} finished")

async def main():
    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(my_task(i)) for i in range(5)]
    await asyncio.gather(*tasks)
    # loop.close() # Эта строка не рекомендуется и не требуется при использовании asyncio.run()


asyncio.run(main())



import asyncio

async def my_task(n, loop):
    print(f"Задача {n} с идентификатором цикла {id(loop)} начинается")
    await asyncio.sleep(1)
    print(f"Задача {n} завершена")

async def main(loop):
    tasks = [my_task(i, loop) for i in range(5)]
    await asyncio.gather(*tasks)


loop = asyncio.get_event_loop()
try:
    # Передача цикла событий в функцию main
    loop.run_until_complete(main(loop))
finally:
    loop.close()



import asyncio

async def my_task(n):
    loop = asyncio.get_running_loop()  # Получение текущего цикла событий
    print(f"Задача {n} с идентификатором цикла {id(loop)} начинается")
    await asyncio.sleep(1)
    print(f"Задача {n} завершена")

async def main():
    tasks = [my_task(i) for i in range(5)]
    await asyncio.gather(*tasks)

asyncio.run(main())



import asyncio

async def my_task():
    print("Running my task")

async def main():
    loop = asyncio.get_running_loop()
    print(type(loop))
    print(loop)
    loop.create_task(my_task())
    await asyncio.sleep(1)

asyncio.run(main())



import asyncio

articles = [
    {'title': 'Методы картирования генома', 'length': 3.2},
    {'title': 'Гормоны растений и их рост', 'length': 4.5},
    {'title': 'Применение CRISPR', 'length': 2.1},
    {'title': 'Микробное разнообразие', 'length': 1.5},
    {'title': 'Механика деления клеток', 'length': 4.1},
    {'title': 'Эпигенетическая регуляция', 'length': 3.8},
    {'title': 'Динамика сворачивания белков', 'length': 4.0},
    {'title': 'Экологические взаимодействия', 'length': 0.7},
    {'title': 'Модели нейронных сетей', 'length': 4.3},
    {'title': 'Пути биолюминесценции', 'length': 2.9}
]

async def upload_article(article):
    await asyncio.sleep(article['length'])
    loop = asyncio.get_running_loop()
    article['loop'] = loop
    return article

async def main():
    tasks = [asyncio.create_task(upload_article(article)) for article in articles]
    await asyncio.gather(*tasks)

asyncio.run(main())



import asyncio


async def send_message(message):
    print(f"Отправка сообщения: {message}")
    await asyncio.sleep(1)  # Имитация задержки отправки сообщения
    print(f"Сообщение отправлено: {message}")


async def receive_message():
    await asyncio.sleep(2)  # Имитация задержки получения сообщения
    message = "И тебе привет!"
    print(f"Сообщение получено: {message}")
    return message


async def main():
    send_task = asyncio.create_task(send_message("Привет"))
    receive_task = asyncio.create_task(receive_message())
    await asyncio.gather(send_task, receive_task)
    event_loop = asyncio.get_running_loop()
    print(f'Цикл событий активен: {event_loop.is_running()}')


asyncio.run(main())

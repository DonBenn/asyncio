from random import random
import asyncio


async def producer(queue):
    print('Производитель: Запущен')
    for i in range(10):
        value = random()
        await asyncio.sleep(value)
        await queue.put(value)
    await queue.put(None)
    print('Производитель: Done')


async def consumer(queue):
    print('Потребитель: Запущен')
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f'>Потребитель получил: {item}')
    print('Потребитель: Done')


async def main():
    queue = asyncio.Queue()
    await asyncio.gather(producer(queue), consumer(queue))



asyncio.run(main())



import asyncio


async def read_queue(queue):
    while True:                                     # запускаем бесконечный цикл для чтения элементов из очереди
        item = await queue.get()                    # получаем элемент из очереди
        print("Получен элемент из очереди:", item)  # выводим полученный элемент


async def main():
    queue = asyncio.Queue()                         # создаем очередь
    asyncio.create_task(read_queue(queue))          # создаем задачу для корутины read_queue
    await queue.put("Первый элемент")               # добавляем первый элемент в очередь
    await queue.put("Второй элемент")               # добавляем второй элемент в очередь


asyncio.run(main())



import asyncio


# объявление асинхронной функции producer, принимающей аргумент queue
async def producer(n, queue, prod_range):
    for i in range(*prod_range):
        item = f'Элемент {i}'  # создание строки с элементом и его номером
        await queue.put(item)  # добавление элемента в очередь
        print(f'producer {n} добавил в очередь элемент: {item}')
        # переключение контекста, позволяющее работать задачам асинхронно
        await asyncio.sleep(0)


# объявление асинхронной функции consumer, принимающей аргумент queue
async def consumer(queue):
    while True:
        item = await queue.get()  # получение элемента из очереди
        if item is None:  # если элемент равен None - выход из цикла
            break
        print(f'consumer получил из очереди элемент: {item}')
        # переключение контекста, позволяющее работать задачам асинхронно
        await asyncio.sleep(0)


async def main():
    queue = asyncio.Queue()  # создание очереди

    # создание задач для функции producer и consumer
    prod_task_1 = asyncio.create_task(producer(1, queue, (0, 10, 2)))
    prod_task_2 = asyncio.create_task(producer(2, queue, (1, 10, 2)))
    cons_task = asyncio.create_task(consumer(queue))
    await prod_task_1
    await prod_task_2
    await queue.put(None)  # добавление элемента None в очередь для выхода из цикла
    await cons_task


asyncio.run(main())



import asyncio


# объявление асинхронной функции producer, принимающей аргумент queue
async def producer(queue, prod_range):
    for i in range(*prod_range):
        item = f'Элемент {i}'  # создание строки с элементом и его номером
        await queue.put(item)  # добавление элемента в очередь
        print(f'{asyncio.current_task().get_name()} добавил в очередь элемент: {item}')
        # переключение контекста, позволяющее работать задачам асинхронно
        await asyncio.sleep(0)


# объявление асинхронной функции consumer, принимающей аргумент queue
async def consumer(queue):
    while True:
        item = await queue.get()  # получение элемента из очереди
        print(f'{asyncio.current_task().get_name()} получил из очереди элемент: {item}')
        # указание, что ранее поставленная в очередь задача завершена
        queue.task_done()
        # переключение контекста, позволяющее работать задачам асинхронно
        await asyncio.sleep(0)


async def main():
    queue = asyncio.Queue()  # создание очереди

    # создание задач для функции producer и consumer
    prod_task_1 = asyncio.create_task(producer(queue, (0, 10, 2)), name='Производитель_1')
    prod_task_2 = asyncio.create_task(producer(queue, (1, 10, 2)), name='Производитель_2')
    cons_task = asyncio.create_task(consumer(queue), name='Потребитель')
    # Список имен незавершенных задач
    print([task.get_name() for task in
           asyncio.all_tasks()])  # ['Task-1', 'Производитель_1', 'Производитель_2', 'Потребитель']
    # Запуск созданных задач на await (переключение контекста)
    await asyncio.sleep(0)

    # Выполнение Task-1 блокируется до "истощения" очереди
    await queue.join()
    print([task.get_name() for task in asyncio.all_tasks()])  # ['Task-1', 'Потребитель']
    # Отмена cons_task ('Потребитель'), из-за бесконечного цикла она не завершится сама.
    cons_task.cancel()
    await asyncio.sleep(0)  # Переключение контекста для выполнения запроса на отмену задачи
    print([task.get_name() for task in asyncio.all_tasks()])  # ['Task-1']


asyncio.run(main())



import asyncio

async def producer(queue):
    patient_info = [
        "Алексей Иванов: Прием для общего осмотра",
        "Мария Петрова: Чистка зубов",
        "Ирина Сидорова: Анализ крови",
        "Владимир Кузнецов: Рентгеновское исследование",
        "Елена Васильева: Вакцинация",
        "Дмитрий Николаев: Выписка рецепта",
        "Светлана Михайлова: Осмотр офтальмолога",
        "Никита Алексеев: Сеанс физиотерапии",
        "Ольга Сергеева: Срочный прием",
        "Анна Жукова: Регулярный контрольный осмотр"
    ]
    for patient in patient_info:
        await asyncio.sleep(0.5)
        await queue.put(patient)
        print(f"Регистратор добавил в очередь: {patient}")
    await queue.put(None)

async def consumer(queue):
    while True:
        patient = await queue.get()
        if patient is None:
            break
        print(f"Врач принял пациента: {patient}")
        await asyncio.sleep(0.5)


async def main():
    queue = asyncio.Queue()
    await asyncio.gather(producer(queue), consumer(queue))

asyncio.run(main())



import asyncio

async def producer(queues, patient_info):
    await asyncio.sleep(0.5)
    for patient in patient_info:
        if patient['direction'] == 'Терапевт':
            await queues["therapist"].put(patient)
            await consumer(queues["therapist"], patient['direction'])
        if patient['direction'] == 'Хирург':
            await queues["surgeon"].put(patient)
            await consumer(queues["surgeon"], patient['direction'])
        if patient['direction'] == 'ЛОР':
            await queues["ent"].put(patient)
            await consumer(queues["ent"], patient['direction'])
        print(f"Регистратор добавил в очередь: {patient['name']}, направление: {patient['direction']}, процедура: {patient['procedure']}")


async def consumer(queue, doctor_type):
    await asyncio.sleep(0.5)
    patient = await queue.get()
    print(
        f"{doctor_type} принял пациента: {patient['name']}, процедура: {patient['procedure']}")


async def main():
    patient_info = [
        {'name': 'Алексей Иванов', 'direction': 'Терапевт',
         'procedure': 'Прием для общего осмотра'},
        {'name': 'Мария Петрова', 'direction': 'Хирург',
         'procedure': 'Малая операция'},
        {'name': 'Ирина Сидорова', 'direction': 'ЛОР',
         'procedure': 'Осмотр уха'},
        {'name': 'Владимир Кузнецов', 'direction': 'Терапевт',
         'procedure': 'Консультация'},
        {'name': 'Елена Васильева', 'direction': 'Хирург',
         'procedure': 'Хирургическая процедура'},
        {'name': 'Дмитрий Николаев', 'direction': 'ЛОР',
         'procedure': 'Промывание носа'},
        {'name': 'Светлана Михайлова', 'direction': 'Терапевт',
         'procedure': 'Рутинный осмотр'},
        {'name': 'Никита Алексеев', 'direction': 'Хирург',
         'procedure': 'Операция на колене'},
        {'name': 'Ольга Сергеева', 'direction': 'ЛОР',
         'procedure': 'Лечение ангины'},
        {'name': 'Анна Жукова', 'direction': 'Терапевт',
         'procedure': 'Вакцинация'}
    ]

    queues = {
        'therapist': asyncio.Queue(),
        'surgeon': asyncio.Queue(),
        'ent': asyncio.Queue()
    }

    await asyncio.gather(producer(queues, patient_info))

asyncio.run(main())



import asyncio


async def lifoqueue_example():
    # создание LifoQueue с максимальным количеством элементов 3
    lifo_queue = asyncio.LifoQueue(maxsize=3)

    # добавление элементов в очередь
    await lifo_queue.put("Первый элемент")
    await lifo_queue.put("Второй элемент")
    await lifo_queue.put("Третий элемент")

    # получение последнего элемента из очереди
    last_item = await lifo_queue.get()
    print(last_item)

    # получение второго с конца элемента из очереди
    second_last_item = await lifo_queue.get()
    print(second_last_item)

    # получение первого элемента из очереди
    first_item = await lifo_queue.get()
    print(first_item)


asyncio.run(lifoqueue_example())



import asyncio


async def worker(name, lifo_queue):
    while True:
        task = await lifo_queue.get()  # Получаем задание из очереди
        print(f"Рабочий_{name}. Получил задачу: {task}")
        await asyncio.sleep(0.5)  # Обрабатываем задание
        lifo_queue.task_done()  # Отправляем сигнал, что задание выполнено


async def main():
    lifo_queue = asyncio.LifoQueue()  # Создаем очередь
    for i in range(10):
        await lifo_queue.put(i)  # Заполняем очередь заданиями

    # Создаем несколько задач-рабочих
    workers = [asyncio.create_task(worker(f"{i}", lifo_queue)) for i in
               range(3)]
    await lifo_queue.join()  # Ждем, пока все задания не будут выполнены
    for w in workers:  # Останавливаем задачи-рабочие
        w.cancel()


if __name__ == "__main__":
    asyncio.run(main())



import asyncio

# При выводе в консоль можно использовать ANSI коды
RED = '\033[31m'
YELLOW = '\033[33m'
GREEN = '\033[32m'
END = '\033[0m'  # Возврат к настройкам


async def customer(queue):
    # Цикл работает до опустошения очереди
    while not queue.empty():
        await asyncio.sleep(.5)
        elem = queue.get_nowait()
        print(f'Из очереди получен элемент_{elem}')

    print(f'{YELLOW}Очередь опустошена{END}')
    # Применяем метод get_nowait() для вызова исключения asyncio.QueueEmpty
    try:
        elem = queue.get_nowait()
        print(f'Из очереди получен элемент_{elem}')  # Принт не сработает
    except asyncio.QueueEmpty:
        print(f'{RED}Попытка получить элемент из пустой очереди методом get_nowait() вызвала asyncio.QueueEmpty{END}')


async def producer(queue):
    for i in range(5):
        await asyncio.sleep(.5)
        queue.put_nowait(i)
        print(f'В очередь поставлен элемент_{i}')
        if queue.full():  # Если очередь заполнена
            print(f'{YELLOW}Очередь заполнена{END}')
            try:
                # Применяем метод put_nowait() для вызова исключения asyncio.QueueFull
                queue.put_nowait(i + 1)
                print(f'В очередь поставлен элемент_{i}')  # Принт не сработает
            except asyncio.QueueFull:
                print(
                    f'{RED}Попытка поместить элемент в заполненную очередь методом put_nowait() вызвала asyncio.QueueFull{END}')
                print(f'{GREEN}Запускаем процесс получения элементов из очереди{END}')
                # Приостанавливаем producer() и ожидаем выполнения customer()
                await customer(queue)


async def main():
    # Создаем очередь с maxsize == 5
    queue = asyncio.LifoQueue(5)
    print(f'{GREEN}Емкость созданной очереди: {queue.maxsize} элементов{END}')
    prod = asyncio.create_task(producer(queue))
    # Приостанавливаем текущую задачу и ожидаем выполнения prod
    await prod
    print('End')


asyncio.run(main())



import asyncio


flights = [
    ("Delta Air Lines DL758", 1.0),
    ("United Airlines UA1189", 2.1),
    ("Southwest Airlines WN3920", 1.2),
    ("American Airlines AA2401", 2.7),
    ("Spirit Airlines NK301", 3.1),
    ("Alaska Airlines AS621", 1.4),
    ("JetBlue Airways B61883", 1.8),
    ("Frontier Airlines F91514", 3.0),
    ("Hawaiian Airlines HA22", 2.4),
    ("Allegiant Air G4159", 1.1),
    ("Air Canada AC758", 2.9),
    ("Lufthansa LH447", 3.3),
    ("British Airways BA183", 2.3),
    ("Qantas QF12", 1.3),
    ("Emirates EK231", 1.5)
]


async def process_flights(queue):
    priority, flight = await queue.get()
    print(f"Посадка самолёта: {flight} с приоритетом {priority}")
    await asyncio.sleep(1)
    queue.task_done()


async def main():
    queue = asyncio.PriorityQueue()
    tasks = []
    for flight in flights:
        await queue.put((flight[1], flight[0]))
        tasks.append(asyncio.create_task(process_flights(queue)))
    await asyncio.gather(*tasks)
    await queue.join()

asyncio.run(main())
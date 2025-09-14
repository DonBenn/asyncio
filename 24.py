import asyncio
import time

# Глобальная переменная, которую будем изменять
shared_data = 0


# Корутина, ожидающая изменения переменной
async def waiting_coro(condition, task_id):
    async with condition:
        print(f'Задача {task_id} ожидает, пока shared_data >= 3')
        await condition.wait_for(lambda: shared_data >= 3)
        print(
            f'Задача {task_id} обнаружила, что shared_data = {shared_data}, '
            f'продолжает работу {time.perf_counter() - start:.4f}')
        await asyncio.sleep(0.2)
        print(f'Задача {task_id} завершила работу {time.perf_counter() - start:.4f}')


# Корутина, изменяющая состояние переменной
async def modifying_coro(condition):
    global shared_data
    for i in range(1, 5):
        await asyncio.sleep(1)
        shared_data += 1
        print(f'Изменено shared_data {shared_data}: {time.perf_counter() - start:.4f}')
        async with condition:
            print(f'Отправлено оповещение notify_all() {i}: {time.perf_counter() - start:.4f}')
            condition.notify_all()


async def main():
    condition = asyncio.Condition()

    # Создаем задачи
    waiting_tasks = [asyncio.create_task(waiting_coro(condition, f'task{i}')) for i in range(1, 4)]
    modifying_task = asyncio.create_task(modifying_coro(condition))

    # Ожидаем завершения всех задач
    await asyncio.gather(*waiting_tasks, modifying_task)


start = time.perf_counter()
asyncio.run(main())



import asyncio


# корутина, ожидающая наступление условия
async def waiting_coro(condition, task_id):
    async with condition:
        print(f'Задача {task_id} освобождает блокировку и встает в очередь, ожидая уведомления')
        await condition.wait()
        print(f'Задача {task_id} снова захватывает блокировку и продолжает работу')
        await asyncio.sleep(1)  # Тут любая работа с данными, требующими синхронизации доступа
        print(f'Задача {task_id} завершила работу, блокировка свободна')


# корутина, отправляющая уведомление
async def notifying_coro(condition):
    async with condition:
        await asyncio.sleep(1)
        print(f'Отправлены уведомления всем ожидающим задачам')
        condition.notify_all()


async def main():
    condition = asyncio.Condition()
    waiting_tasks = [asyncio.create_task(waiting_coro(condition, f'task{i}')) for i in range(1, 4)]
    notifying_task = asyncio.create_task(notifying_coro(condition))
    await asyncio.gather(*waiting_tasks)

asyncio.run(main())



import asyncio

async def worker(condition, msg):

    # Захватываем блокировку
    async with condition:
        print(f"worker() получил блокировку, сообщение {msg}")
        await condition.wait() # тут блокировка снимается на время ожидания корутины
        print('В worker() сработал await condition.wait() и она продолжает выполнять любую логику')
        print(f"worker() разблокирована, сообщение {msg}")

async def main():
    # Создаем условие
    condition = asyncio.Condition()
    task1 = asyncio.create_task(worker(condition, 'task1'))
    task2 = asyncio.create_task(worker(condition, 'task2'))
    await asyncio.sleep(1)
    # Захватываем блокировку
    async with condition:
        print("Корутина main получила блокировку")
        print("Корутина main реализует любую логику приложения")
        condition.notify_all()

        print('main() оповещает все корутины с помощью -  condition.notify_all(), и передаёт управление в цикл событий')
        print("Корутина main разблокирована")

    await task1
    await task2

asyncio.run(main())



import asyncio


async def auto_write_data(condition, name):
    # Блокировка условия
    async with condition:
        print(f'Ожидает получения данных: {name}')
        await condition.wait()
        print(f'{name} добавляются в БД')
        await asyncio.sleep(0.5)
        print(f'Скачанные {name} автоматически записаны в БД')


async def download_data(condition):
    for i in range(3):
        async with condition:
            await asyncio.sleep(0.5) # скачивание данных
            print(f'Данные {i} готовы для записи в БД')
            condition.notify()


async def manual_write_data(lock, data):
    async with lock:
        print(f'{data} добавляются в БД')
        await asyncio.sleep(0.5)
        print(f'{data} добавлены в БД')


async def main():
    lock = asyncio.Lock() # создаем замок
    condition = asyncio.Condition(lock) # используем данный замок при создании объекта Condition
    tasks = [asyncio.create_task(auto_write_data(condition, f'данные {i}')) for i in range(3)]
    manual_task = asyncio.create_task(manual_write_data(lock, f'данные из другого источника'))
    await asyncio.gather(download_data(condition), *tasks, manual_task)


asyncio.run(main())



import asyncio

users = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eva', 'Frank', 'George', 'Helen', 'Ivan', 'Julia']

async def access_db(condition, name):
    async with condition:
        print(f'Пользователь {name} ожидает доступа к базе данных')
        await condition.wait()
        print(f'Пользователь {name} подключился к БД')
        await asyncio.sleep(0.5)
        print(f'Пользователь {name} отключается от БД')
        condition.notify()


async def controller(condition):
    async with condition:
        await asyncio.sleep(0.5)
        condition.notify()
        # condition.notify_all()


async def main():
    lock = asyncio.Lock()
    condition = asyncio.Condition(lock)
    tasks = [asyncio.create_task(access_db(condition, user)) for user in users]
    await asyncio.gather(controller(condition), *tasks, )

asyncio.run(main())



import asyncio

wood_resources_dict = {
    'Деревянный меч': 6,
    'Деревянный щит': 12,
    'Деревянный стул': 24,
}

storage = 0

async def gather_wood(condition, wood_resources_dict):
    global storage
    while True:
        await asyncio.sleep(0.1)
        storage += 2
        print(f"Добыто 2 ед. дерева. На складе {storage} ед.")

        keys_to_remove = []
        for key, value in wood_resources_dict.items():
            if storage == value:
                async with condition:
                    condition.notify()
                keys_to_remove.append(key)
                storage = 0

        for key in keys_to_remove:
            del wood_resources_dict[key]

        if not wood_resources_dict:
            break


async def craft_item(condition, item):
    async with condition:
        await condition.wait()
        print(f"Изготовлен {item}.")


async def main():

    lock = asyncio.Lock()
    condition = asyncio.Condition(lock)
    tasks = [asyncio.create_task(craft_item(condition, item)) for item in wood_resources_dict]
    await asyncio.gather(*tasks, gather_wood(condition, wood_resources_dict))

asyncio.run(main())

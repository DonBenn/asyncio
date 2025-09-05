import aiofiles
import asyncio

async def read_file(file_name):
    # Используем async with для открытия файла асинхронно
    async with aiofiles.open(file_name, 'r') as file:
        contents = await file.read()
        print(contents)

asyncio.run(read_file('example.txt'))



import aiohttp
import asyncio

async def fetch_url(url):
    # Используем async with для создания асинхронной сессии aiohttp
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            content = await response.text()
            print(content)

asyncio.run(fetch_url('https://example.com'))



import asyncio

async def protected_section(lock, task_id):
    # Используем async with для корректного захвата и освобождения блокировки
    async with lock:
        print(f'Task {task_id} has entered the protected section')
        await asyncio.sleep(1)
        print(f'Task {task_id} has left the protected section')

async def main():
    lock = asyncio.Lock()
    tasks = [protected_section(lock, i) for i in range(3)]
    await asyncio.gather(*tasks)


asyncio.run(main())



import asyncio


class AsyncTransaction:
    # Метод для выполнения асинхронной операции перед началом контекста
    async def __aenter__(self):
        print("Starting transaction")
        await asyncio.sleep(0.5)

    # Метод для выполнения асинхронной операции после завершения контекста
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Ending transaction")
        await asyncio.sleep(0.5)


async def perform_transaction():
    # Используем async with для корректного выполнения асинхронных операций перед началом и после завершения контекста
    async with AsyncTransaction():
        print("Performing transaction operations")
        await asyncio.sleep(1)


asyncio.run(perform_transaction())



import asyncio


database = [
    {"название": "Разработать API", "статус": "Завершена"},
    {"название": "Написать документацию", "статус": "Ожидает"},
    {"название": "Провести код-ревью", "статус": "Ожидает"}
]


class AsyncListManager:
    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.disconnect()

    async def connect(self):
        print("Начало работы с базой данных")
        await asyncio.sleep(0.5)

    async def disconnect(self):
        print("Завершение работы с базой данных")
        await asyncio.sleep(0.5)

    async def stage_append(self, value):
        await asyncio.sleep(1)
        database.append(value)
        print('Новые данные добавлены')


async def main():
    async with AsyncListManager() as manager:
        # value = "Настроить CI/CD, В процессе"
        # res = value.split(", ")
        # dictionary = {"название": res[0], "статус": res[1]}
        name, status = input().split(', ')
        dictionary = {"название": name, "статус": status}
        await manager.stage_append(dictionary)
        for dic in database:
            print(dic)


asyncio.run(main())



import asyncio

# Асинхронный генератор
async def async_gen():
    for i in range(5):  # Итерируемся по диапазону чисел от 0 до 4
        await asyncio.sleep(.5)
        yield i  # Возвращаем текущее число


async def main():
    async for number in async_gen():  # Используем асинхронный цикл for для итерации
        print(number)


asyncio.run(main())



import aiohttp
import asyncio


# Асинхронный генератор
async def async_url_generator(urls):
    for url in urls:
        yield url


# Асинхронная функция для асинхронных HTTP-запросов, возвращает текст ответа
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    urls = [
        'https://example.com',
        'https://example.org',
        'https://example.net',
    ]

    # Создаем асинхронный контекстный менеджер сессии для выполнения HTTP-запросов
    async with aiohttp.ClientSession() as session:
        # Итерируемся по URL-адресам с помощью асинхронного генератора async_url_generator
        async for url in async_url_generator(urls):
            content = await fetch(session, url)
            print(f'Fetched content from {url}: {content[:100]}')


asyncio.run(main())



import aiofiles
import asyncio


# Асинхронная функция для чтения файлов
async def read_file_line_by_line(file_path):
    async with aiofiles.open(file_path, mode='r') as file:  # асинхронное открытие файла
        async for line in file:  # итерация по строкам файла
            print(line.strip())


async def main():
    file_path = 'example.txt'
    await read_file_line_by_line(file_path)


asyncio.run(main())



import asyncio
import random

users = ['user1', 'user2', 'user3']
products = ['iPhone 14', 'Samsung Galaxy S23', 'MacBook Pro', 'Dell XPS 13', 'Sony WH-1000XM5', 'Apple Watch Series 8', 'Kindle Paperwhite', 'GoPro Hero 11', 'Nintendo Switch', 'Oculus Quest 2']
actions = ['просмотр', 'покупка', 'добавление в избранное']

async def user_action_generator():
    while True:
        user = random.choice(users)
        product = random.choice(products)
        action = random.choice(actions)
        yield {
            'user_id': user,
            'action': action,
            'product_id': product
        }

asyncio.run(user_action_generator())



import asyncio
import random

random.seed(1)

SERVERS = [
    "api.database.local",
    "auth.backend.local",
    "web.frontend.local",
    "cache.redis.local",
    "analytics.bigdata.local"
]

STATUSES = ["Online", "Offline", "Maintenance", "Error"]

async def monitor_servers(servers):
    for server in servers:
        status = random.choice(STATUSES)
        await asyncio.sleep(0.1)
        yield server, status

async def main():
    async for server, status in monitor_servers(SERVERS):
        print(f'{server}: состояние {status}')

asyncio.run(main())
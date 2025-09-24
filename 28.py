import aiohttp
import asyncio

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://python.org') as response:
            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])
            html = await response.text()
            print("Body:", html[:15], "...")

asyncio.run(main())



from aiohttp import web

# Асинхронный обработчик для обработки входящих HTTP-запросов
async def handle(request):
    # Извлечение параметра 'name' из URL или использование значения "Anonymous", если параметр отсутствует
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    # Возвращение HTTP-ответа с сформированным текстом
    return web.Response(text=text)

# Создание экземпляра веб-приложения
app = web.Application()
# Добавление маршрутов для обработки корневого URL и URL с параметром 'name'
app.add_routes([web.get('/', handle), web.get('/{name}', handle)])

# Запуск веб-приложения на IP-адресе 192.168.1.100
# web.run_app(app, host='192.168.1.100')
web.run_app(app, host="localhost")



import asyncio
from aiohttp import ClientSession


async def hello(url: str):
    async with ClientSession() as session:
        async with session.get(url) as response:
            text_response = await response.text()
            print(text_response[:100])


async def main():
    tasks = []
    url = "https://example.com/"
    for i in range(10):
        task = asyncio.create_task(hello(f'{url}{i}'))  # Создание 10 задач с разными URL
        tasks.append(task)

    await asyncio.gather(*tasks)


asyncio.run(main())



import aiohttp
import asyncio
import time
async def fetch(session, url):
    async with session.get(url) as response:
        text = await response.text()
        print(f"Отправлен запрос на {url}, первые 10 символов ответа {text[:10]}")


async def main():
    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in range(100):
            task = asyncio.ensure_future(fetch(session, f"http://example.com/{i}"))
            tasks.append(task)
        responses = await asyncio.gather(*tasks)

start_time = time.time()
asyncio.run(main())
end_time = time.time()
print(f"Асинхронный клиент завершил работу за {end_time - start_time:.2f} секунд.")



import aiohttp
import asyncio

async def fetch_url(url, semaphore: asyncio.Semaphore):
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                r = await response.text()
                print(r[:15])
                # return await response.text()

async def main():
    semaphore = asyncio.Semaphore(10)  # Ограничиваем количество одновременных запросов до 10
    urls = ["http://example.com"] * 100
    tasks = [fetch_url(url, semaphore) for url in urls]
    await asyncio.gather(*tasks)

asyncio.run(main())



import asyncio
import time
from aiohttp import ClientSession


async def fetch(url, session):
    async with session.get(url) as response:
        data = await response.text()
        print(data[:5], response.url)


async def run():
    url = "http://asyncio.ru/example/index.html"
    tasks = []
    async with ClientSession() as session:
        for i in range(30000):
            task = asyncio.create_task(fetch(url, session))
            tasks.append(task)

        responses = asyncio.gather(*tasks)
        await responses

start_time = time.time()
asyncio.run(run())
end_time = time.time()
print(f"Асинхронный клиент завершил работу за {end_time - start_time:.2f} секунд.")



import asyncio
import time
from aiohttp import ClientSession

async def fetch(url, session):
    async with session.get(url) as response:

        data = await response.text()
        print(data[:5], response.url)


async def bound_fetch(sem, url, session):
    async with sem:
        await fetch(url, session)


async def run():
    url = "http://asyncio.ru/example/index.html"
    tasks = []
    sem = asyncio.Semaphore(5000)
    async with ClientSession() as session:
        for i in range(100000):
            task = asyncio.ensure_future(bound_fetch(sem, url, session))
            tasks.append(task)

        responses = asyncio.gather(*tasks)
        await responses

start_time = time.time()
asyncio.run(run())
end_time = time.time()
print(f"Асинхронный клиент завершил работу за {end_time - start_time:.2f} секунд.")



import asyncio
import time

import aiohttp
from aiohttp import ClientSession

async def fetch(url, session):
    async with session.get(url) as response:
        data = await response.text()
        print(data[:5], response.url)


async def bound_fetch(url, session):
    await fetch(url, session)


async def run():
    url = "http://asyncio.ru/example/index.html"
    tasks = []
    connector = aiohttp.TCPConnector(limit=50)
    async with ClientSession(connector=connector) as session:
        for i in range(100000):
            task = asyncio.ensure_future(bound_fetch(url, session))
            tasks.append(task)

        responses = asyncio.gather(*tasks)
        await responses


start_time = time.time()
asyncio.run(run())
end_time = time.time()
print(f"Асинхронный клиент завершил работу за {end_time - start_time:.2f} секунд.")



import aiohttp
import asyncio


async def fetch_status(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                status_code = response.status
                if status_code == 200:
                    print(f"Успешный запрос к {url}")
                elif status_code == 404:
                    print(f"Ресурс {url} не найден")
                elif status_code >= 500:
                    print(f"Ошибка на стороне сервера {url}")
                print(f"Статус-код: {status_code}")
                return status_code

    except aiohttp.ClientConnectorError as e:
        print(f"Не удалось подключиться к {url}. Ошибка: {e}")
        return None


async def main():
    urls = ["https://www.example.com", "https://www.nonexistentwebsite.com"]
    tasks = [fetch_status(url) for url in urls]
    await asyncio.gather(*tasks)


asyncio.run(main())



import aiohttp
import asyncio


async def main():
    session = aiohttp.ClientSession()

    async with session.get('https://www.example.com') as response:
        print(f"Статус код: {response.status}")
        print((await response.text())[:15])
    await session.close()

    if session.closed:
        print(f"Cостояние сессии: {session.closed=}")
        print("Сессия закрыта и все ресурсы освобождены.")

asyncio.run(main())



import aiohttp
import asyncio

async def fetch_with_params(session, url, params=None):
    async with session.get(url, params=params) as response:
        return await response.text()

async def main():
    params = {
        'param1': 'value1',
        'param2': 'value2'
    }
    async with aiohttp.ClientSession() as session:
        response = await fetch_with_params(session, 'http://example.com/page', params)
        print(response)

asyncio.run(main())



import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'http://example.com')
        print(html)

asyncio.run(main())



import aiohttp
import asyncio
from aiocache import cached, caches, Cache
import time

default_cache = caches.get('default')
# # **Использование кеша без декоратора
# async def fetch(url):
#     cached_response = await default_cache.get(url)
#     if cached_response is not None:
#         return cached_response  # Возвращаем кешированный ответ, если он есть
#     else:
#         async with aiohttp.ClientSession() as session:
#             async with session.get(url) as response:
#                 text = await response.text()
#                 await default_cache.set(url, text, ttl=20)  # Сохраняем ответ в кеш
#                 return text

# Декоратор для кеширования асинхронной функции
@cached(ttl=20, cache=Cache.MEMORY)  # ttl - время жизни кеша в секундах
async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def main():
    url = 'https://httpbin.org/delay/2'  # задержка ответа в 2 секунды

    # При первом вызове данные будут получены и сохранены в кеше.
    start_time = time.time()
    response = await fetch(url)
    end_time = time.time()
    print(f"First request duration: {end_time - start_time:.2f} seconds")
    print(f"First request content: {response[:100]}...")

    # Второй запрос (должен идти из кеша)
    start_time = time.time()
    response = await fetch(url)
    end_time = time.time()
    print(f"Second request duration (from cache): {end_time - start_time:.2f} seconds")
    print(f"Second request content (from cache): {response[:100]}...")

asyncio.run(main())



import aiohttp
import asyncio

async def send_post_request():
    headers = {'Content-Type': 'application/json', 'User-Agent': 'my-app/0.0.1'}

    async with aiohttp.ClientSession() as session:
        response = await session.post('https://httpbin.org/post', json={'key': 'value'}, headers=headers)

        text_response = await response.text()
        print("Text Response:", text_response)

        json_response = await response.json()
        print("JSON Response:", json_response)

asyncio.run(send_post_request())



import aiohttp
import asyncio

async def send_file():
    async with aiohttp.ClientSession() as session:
        with open('path_to_file.jpg', 'rb') as file:
            file_data = {'file': file}
            response = await session.post('https://httpbin.org/post', data=file_data)
            print(await response.text())

asyncio.run(send_file())



import aiohttp
import asyncio


async def send_file():
    async with aiohttp.ClientSession() as session:
        data = aiohttp.FormData()
        with open('path_to_file.jpg', 'rb') as file:
            data.add_field('file', file, filename='path_to_file.jpg',
                           content_type='image/jpeg')

            response = await session.post('https://httpbin.org/post',
                                          data=data)
            print(await response.text())


asyncio.run(send_file())



import asyncio
import aiohttp


async def send_option_request():
    async with aiohttp.ClientSession() as session:
        response = await session.options('https://jsonplaceholder.typicode.com/posts')
        print(response.headers)
        print("Allow:", response.headers.get("Access-Control-Allow-Methods"))

asyncio.run(send_option_request())



import aiohttp
import asyncio


async def fetch_options(url):
    async with aiohttp.ClientSession() as session:
        async with session.options(url) as response:
            allowed_methods = response.headers.get('Allow')
            print(f"Разрешенные методы для {url}: {allowed_methods}")
            if 'GET' in allowed_methods:
                async with session.get(url) as get_response:
                    content = await get_response.text()
                    print(
                        f"Контент от {url}:\n{content[:100]}...")
            return allowed_methods


url_to_check = 'https://example.com/'
asyncio.run(fetch_options(url_to_check))



import aiohttp
import asyncio

async def fetch_head(url):
    async with aiohttp.ClientSession() as session:
        async with session.head(url, allow_redirects=True) as response:
            print(response.status)
            print(response.headers)

asyncio.run(fetch_head("https://example.com"))



import aiohttp
import asyncio


async def main():
    async with aiohttp.ClientSession() as session:
        data = {'key': 'value'}
        async with session.put('http://httpbin.org/put',
                               json=data) as response:
            print("Status:", response.status)
            print("Content-Type:", response.headers.get('content-type'))
            text = await response.text()
            print("Body:", text)

asyncio.run(main())



import aiohttp
import asyncio
import json


async def update_task(session, task_id, new_status, new_description):
    url = f'http://httpbin.org/put/{task_id}'
    payload = {
        'status': new_status,
        'description': new_description
    }
    async with session.put(url, json=payload) as response:
        if response.status == 200:
            updated_task = await response.json()
            print(f"Successfully updated task: {updated_task}")
        elif response.status == 204:
            print("Task updated successfully, but no content returned.")
        else:
            print(f"Failed to update task. Status code: {response.status}")


async def main():
    task_id = 1
    new_status = 'Завершено'
    new_description = 'Задача успешно завершена.'

    async with aiohttp.ClientSession() as session:
        await update_task(session, task_id, new_status, new_description)


asyncio.run(main())



import aiohttp
import asyncio
import os


async def upload_large_file(session, url, file_path, chunk_size=1024 * 1024):
    file_size = os.path.getsize(file_path)

    with open(file_path, 'rb') as f:
        for offset in range(0, file_size, chunk_size):
            f.seek(offset)
            chunk = f.read(chunk_size)
            chunk_headers = {
                'Content-Range': f'bytes {offset}-{offset + len(chunk) - 1}/{file_size}'
            }

            async with session.put(url, data=chunk, headers=chunk_headers) as response:
                if response.status != 200 and response.status != 201:
                    print(f"Failed to upload chunk at offset {offset}")
                    return
                else:
                    print(f"Successfully uploaded chunk at offset {offset}")

async def main():
    url = 'http://httpbin.org/put/large-file'
    file_path = '/path/to/large/file'

    async with aiohttp.ClientSession() as session:
        await upload_large_file(session, url, file_path)


asyncio.run(main())



import aiohttp
import asyncio
import json

async def main():
    async with aiohttp.ClientSession() as session:
        payload = {
            "json": {'key_111': 'value_111'},
            "data": {"key_777": "value_777"},
            "headers": {"Content-Type": "application/json"}
        }
        async with session.patch('https://httpbin.org/patch', data=payload) as resp:
            print(await resp.text())

asyncio.run(main())



import aiohttp
import asyncio
import json
import logging


user_db = {
    1: {"name": "Alice", "age": 30},
    2: {"name": "Bob", "age": 40},
    3: {"name": "Charlie", "age": 50},
}


async def update_user(user_id, new_data):
    url = f"https://api.example.com/users/{user_id}"

    async with aiohttp.ClientSession() as session:
        headers = {"Content-Type": "application/json"}
        payload = json.dumps(new_data)

        try:
            async with session.patch(url, data=payload, headers=headers) as resp:
                if resp.status == 200:
                    logging.info(f"Successfully updated user {user_id}")
                else:
                    logging.error(f"Failed to update user {user_id}. Status code: {resp.status}")

                return await resp.json()

        except aiohttp.ClientError as e:
            logging.error(f"Network error: {e}")
            return None


async def main():
    tasks = []
    new_data = {"age": 35}

    for user_id in user_db.keys():
        task = update_user(user_id, new_data)
        tasks.append(task)

    await asyncio.gather(*tasks)


asyncio.run(main())




import aiohttp
import asyncio

async def delete_record(record_id):
    url = f"https://api.example.com/records/{record_id}"
    async with aiohttp.ClientSession() as session:
        async with session.delete(url) as response:
            if response.status == 200:
                print(f"Successfully deleted record with ID {record_id}")
            else:
                print(f"Failed to delete record with ID {record_id}. Status code: {response.status}")

async def main():
    await delete_record(1)  # Удаление записи с ID 1

asyncio.run(main())



import aiohttp
import asyncio


async def update_and_clear_cache(record_id, new_data):
    data_url = f"https://api.example.com/data/{record_id}"
    cache_url = f"https://api.example.com/cache/{record_id}"

    async with aiohttp.ClientSession() as session:
        async with session.put(data_url, json=new_data) as response:
            if response.status == 200:
                async with session.delete(cache_url) as delete_response:
                    if delete_response.status == 200:
                        print(
                            f"Successfully updated and cleared cache for data with ID {record_id}")
                    else:
                        print(
                            f"Failed to clear cache. Status code: {delete_response.status}")
            else:
                print(f"Failed to update data. Status code: {response.status}")

async def main():
    new_data = {"key": "new_value"}
    await update_and_clear_cache(1, new_data)


asyncio.run(main())



import asyncio
import aiohttp


async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    urls = [
        'https://example.com/page1',
        'https://example.com/page2',
        'https://example.com/page3'
    ]

    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            task = asyncio.ensure_future(fetch_url(session, url))
            tasks.append(task)

        responses = await asyncio.gather(*tasks)

        for i, response in enumerate(responses):
            print(f"Response from {urls[i]}: {response[:100]}...")


if __name__ == '__main__':
    asyncio.run(main())
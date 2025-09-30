from aiohttp import ClientSession, CookieJar
from http.cookies import SimpleCookie
import asyncio


async def main():
    # Создаем асинхронную сессию с использованием CookieJar для хранения кук
    async with ClientSession(cookie_jar=CookieJar(unsafe=True)) as session:
        # Создаем объект SimpleCookie для управления куками
        cookie = SimpleCookie()
        # Устанавливаем значение для кука с именем "my_cookie_name"
        cookie["my_cookie_name"] = "my_cookie_value"
        # Получаем объект Morsel для дальнейшей настройки кука
        morsel = cookie["my_cookie_name"]

        # Настраиваем различные атрибуты кука
        morsel['path'] = '/'
        morsel['domain'] = '.httpbin.org'
        morsel['expires'] = 'Tue, 01-Sep-2026 10:50:22 GMT'
        morsel['max-age'] = 31536000
        morsel['secure'] = True
        morsel['httponly'] = True
        morsel['samesite'] = 'Strict'

        # Добавляем настроенный кук в CookieJar сессии
        session.cookie_jar.update_cookies(cookie)

        async with session.get('https://httpbin.org/cookies') as response:
            print(await response.text())


asyncio.run(main())



import aiohttp
import asyncio
from http.cookies import SimpleCookie


async def make_request(session, url, cookie_data):
    # Преобразование данных cookie в правильный формат
    cookie = SimpleCookie()
    cookie[cookie_data["Name"]] = cookie_data["Value"]

    for key, value in cookie_data.items():
        if key not in ["Name", "Value"]:
            cookie[cookie_data["Name"]][key] = value

    # Добавление cookie в сессию
    session.cookie_jar.update_cookies(cookie)

    async with session.get(url) as response:
        print(f"Response from {url}: {await response.text()}")


async def main():
    urls = ['https://example.com/page1', 'https://example.com/page2',
            'https://example.com/page3']

    # Три разных набора cookies
    cookies_list = [
        {
            'Name': 'cookie1',
            'Value': 'value1',
            'Secure': 'Secure',
            'HttpOnly': 'HttpOnly',
            'SameSite': 'Strict'
        },
        {
            'Name': 'cookie2',
            'Value': 'value2',
            'Path': '/',
            'Domain': '.example.com',
            'Expires': 'Tue, 01-Sep-2026 10:50:22 GMT'
        },
        {
            'Name': 'cookie3',
            'Value': 'value3',
            'Max-Age': '31536000'
        }
    ]

    async with aiohttp.ClientSession() as session:
        tasks = []

        # Создание списка задач для выполнения
        for url, cookie_data in zip(urls, cookies_list):
            task = make_request(session, url, cookie_data)
            tasks.append(task)

        await asyncio.gather(*tasks)


asyncio.run(main())



import aiohttp
import asyncio


async def main():
    async with aiohttp.ClientSession(cookie_jar=aiohttp.CookieJar()) as session:
        async with session.get('http://example.com/') as response:
            print(await response.text())

        # После первого запроса все куки, установленные сервером,
        # сохраняются в CookieJar. При следующем запросе к тому же серверу
        # куки автоматически будут включены в заголовки.

        async with session.get('http://example.com/some_page') as response:
            print(await response.text())


asyncio.run(main())



import aiohttp
import asyncio
from http.cookies import SimpleCookie
from yarl import URL


async def main():
    async with aiohttp.ClientSession(cookie_jar=aiohttp.CookieJar()) as session:
        # Добавляем некоторые куки в CookieJar
        cookies = SimpleCookie('sessionid=12345; username=user')
        session.cookie_jar.update_cookies(cookies, response_url=URL('http://example.com'))

        # Добавляем куки для другого домена
        other_cookies = SimpleCookie('id=6789')
        session.cookie_jar.update_cookies(other_cookies, response_url=URL('http://another-example.com'))

        # Фильтруем куки, которые подходят для http://example.com
        filtered_cookies = session.cookie_jar.filter_cookies(URL('http://example.com'))

        print("Filtered cookies for http://example.com:")
        for key, morsel in filtered_cookies.items():
            print(f"{key}: {morsel.value}")


asyncio.run(main())



import asyncio
import aiohttp
from aiohttp_socks import ProxyType, ProxyConnector

async def fetch(url, proxy_type, host, port):
    connector = ProxyConnector(proxy_type=proxy_type, host=host, port=port)
    async with aiohttp.ClientSession(connector=connector) as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    url = "https://httpbin.org/ip"

    # Пример с SOCKS4 прокси
    html = await fetch(url, ProxyType.SOCKS4, "196.17.0.29", 8001)
    print("Response with SOCKS4 proxy:")
    print(html)

    # Пример с SOCKS5 прокси
    html = await fetch(url, ProxyType.SOCKS5, "196.17.0.29", 8001)
    print("Response with SOCKS5 proxy:")
    print(html)

    # Пример с HTTP прокси
    html = await fetch(url, ProxyType.HTTP, "196.17.0.29", 8001)
    print("Response with HTTP proxy:")
    print(html)

asyncio.run(main())



import aiohttp
import asyncio
from aiohttp_socks import ProxyType, ProxyConnector, ChainProxyConnector
import random


async def fetch(url, proxy_type, host, port):
    # Создание экземпляра ProxyConnector с указанным типом прокси, хостом и портом
    connector = ProxyConnector(proxy_type=proxy_type, host=host, port=port)

    # Инициализация сессии с использованием ProxyConnector
    async with aiohttp.ClientSession(connector=connector) as session:
        async with session.get(url) as response:
            return await response.text()


async def main():
    url = "https://httpbin.org/ip"

    # Список возможных типов прокси и их параметров
    proxy_list = [
        {'type': ProxyType.HTTP, 'host': '196.17.*.*', 'port': 8001},
        {'type': ProxyType.SOCKS4, 'host': '196.17.*.*', 'port': 8001},
        {'type': ProxyType.SOCKS5, 'host': '196.17.*.*', 'port': 8001},

    ]

    # Случайный выбор типа прокси из списка
    while True:
        chosen_proxy = random.choice(proxy_list)

        print(f"Используемый тип прокси: {chosen_proxy['type']}")
        try:
            # Выполнение HTTP-запроса с использованием выбранного прокси
            html = await fetch(url, chosen_proxy['type'], chosen_proxy['host'],
                               chosen_proxy['port'])

            print("Успешный запрос:")
            print(html)
        except Exception as e:
            print(f"Ошибка при выполнении запроса: {e}")


asyncio.run(main())



import asyncio
import aiohttp
from aiohttp_socks import ProxyType, ProxyConnector

async def fetch():
    url = 'https://httpbin.org/ip'

    # Создание экземпляра ProxyConnector с параметрами прокси
    connector = ProxyConnector(
        proxy_type=ProxyType.SOCKS5,  # Тип прокси (SOCKS5)
        host='196.17.*.*',         # IP-адрес прокси-сервера
        port=8001,                    # Порт прокси-сервера
        username='***',            # Имя пользователя для аутентификации
        password='***',            # Пароль для аутентификации
        rdns=True                     # Использование обратного DNS-разрешения
    )

    # Инициализация сессии с использованием ProxyConnector
    async with aiohttp.ClientSession(connector=connector) as session:
        async with session.get(url) as response:
            print(await response.text())

asyncio.run(fetch())



import aiohttp
from aiohttp_socks import ProxyConnector, ProxyType
import asyncio


async def fetch(url, session):
    async with session.get(url) as response:
        return await response.text()


async def main():
    with open('proxy.txt', 'r') as f:
        proxies = f.readlines()

    for proxy in proxies:
        username, password_host_port = proxy.strip().split(":", 1)

        password, host_port = password_host_port.split("@")
        host, port = host_port.split(":")

        # Создание коннектора с прокси
        connector = ProxyConnector(
            proxy_type=ProxyType.SOCKS5,
            host=host,
            port=int(port),
            username=username,
            password=password,
            rdns=True
        )

        async with aiohttp.ClientSession(connector=connector) as session:
            url = "http://example.com"
            html = await fetch(url, session)
            print(f"Полученный HTML через прокси {host}:{port} - {html[:50]}...")


asyncio.run(main())



import aiohttp
from aiohttp_socks import ChainProxyConnector
import asyncio

async def fetch(url):
    # Создание цепочки прокси (proxy chaining)
    connector = ChainProxyConnector.from_urls([
        'socks5://user:password@127.0.0.1:1080',
        'socks4://127.0.0.1:1081',
        'http://user:password@127.0.0.1:3128',
    ])

    async with aiohttp.ClientSession(connector=connector) as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    url = 'https://httpbin.org/ip'
    result = await fetch(url)
    print(result)

if __name__ == "__main__":
    asyncio.run(main())



import asyncio
import aiohttp

count = 0

async def task(semaphore, url, session):
    global count
    async with semaphore:
        await asyncio.sleep(0.1)
        async with session.get(url) as response:
            print(f"Статус код: {response.status}")
            count += response.status

async def main():
    semaphore = asyncio.Semaphore(10)
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(1, 1001):
            url = f"https://asyncio.ru/zadachi/5/{i}.html"
            tasks.append(asyncio.create_task(task(semaphore, url, session)))
        await asyncio.gather(*tasks)

asyncio.run(main())
print(count)



import asyncio
import aiohttp
from bs4 import BeautifulSoup

code_dict = {
    0: 'F',
    1: 'B',
    2: 'D',
    3: 'J',
    4: 'E',
    5: 'C',
    6: 'H',
    7: 'G',
    8: 'A',
    9: 'I'
}

async def task(url, session):
    letters = ''
    async with session.get(url) as response:
        html_content = await response.text()
        soup = BeautifulSoup(html_content, 'html.parser')
        p_text = soup.find('p').text.strip()
        for element in p_text:
            letters += code_dict[int(element)]
    print(letters)

async def main():
    async with aiohttp.ClientSession() as session:
        url = f"https://asyncio.ru/zadachi/1/index.html"
        tas = asyncio.create_task(task(url, session))
        await asyncio.gather(tas)

asyncio.run(main())



import asyncio
import aiohttp
from bs4 import BeautifulSoup
import aiofiles

numbers = []

async def get_number(url, semaphore, session):
    async with semaphore:
        async with session.get(url) as response:
            html_content = await response.text()
            soup = BeautifulSoup(html_content, 'html.parser')
            p_tags = soup.find('p', id='number').text
            numbers.append(int(p_tags))


async def main():
    semaphore = asyncio.Semaphore(12)
    async with aiohttp.ClientSession() as session:
        tasks = []
        async with aiofiles.open('problem_pages.txt', 'r') as file:
            async for line in file:
                url = f'https://asyncio.ru/zadachi/2/html/{line.strip()}.html'
                task = asyncio.create_task(get_number(url, semaphore, session))
                tasks.append(task)
        await asyncio.gather(*tasks)


asyncio.run(main())
print(sum(numbers))



import os
import asyncio
import aiohttp
from bs4 import BeautifulSoup
import aiofiles
from urllib.parse import urljoin


async def download_image(session, url, folder):
    async with session.get(url) as response:
        if response.status == 200:
            img_data = await response.read()
            img_name = url.split('/')[-1]
            with open(os.path.join(folder, img_name), 'wb') as f:
                f.write(img_data)
        else:
            print(f"Failed to download {url}")

async def fetch_page(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    semaphore = asyncio.Semaphore(12)
    folder = "downloaded_images"
    os.makedirs(folder, exist_ok=True)
    url = 'https://asyncio.ru/zadachi/4/index.html'

    async with aiohttp.ClientSession() as session:
        html_content = await fetch_page(session, url)
        soup = BeautifulSoup(html_content, 'html.parser')
        img_tags = soup.find_all('img')

        tasks = []
        for img_tag in img_tags:
            img_url = img_tag.get('src')
            if img_url:
                full_img_url = urljoin(url, img_url)
                tasks.append(download_image(session, full_img_url, folder))

        await asyncio.gather(*tasks)

asyncio.run(main())

def get_folder_size(folder_path):
    total_size = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            total_size += os.path.getsize(file_path)
    return total_size


folder_path = r"D:\Dev\asyncio\downloaded_images"
print(get_folder_size(folder_path))



from aiofiles import os
import aiofiles
import asyncio

async def main():
    semaphore = asyncio.Semaphore(12)
    numbers = []
    contents = await os.listdir('D:/Dev/asyncio/files')
    for content in contents:
        async with aiofiles.open('D:/Dev/asyncio/files/'+content, 'r') as f:
            content = await f.read()
            if int(content.strip()) % 2 == 0:
                numbers.append(int(content.strip()))
    print(sum(numbers))


asyncio.run(main())
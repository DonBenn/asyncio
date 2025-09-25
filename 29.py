import aiohttp
import asyncio

async def fetch_url(session, url,connector):
    async with session.get(url) as response:

        print(f"Текущее количество используемых соединений: {len(connector._acquired)}")
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        connector = session.connector

        print(f"Тип коннектора: {type(connector)}")
        print(f"Максимальное количество соединений: {connector.limit}")

        tasks = [fetch_url(session, 'https://www.example.com', connector) for _ in range(5)]

        await asyncio.gather(*tasks)


asyncio.run(main())



import aiohttp
import asyncio


async def main():
    # Создание сессии, коннектор будет создан автоматически
    session = aiohttp.ClientSession()
    print('____session')
    # Сохраняем ссылку на коннектор, чтобы в дальнейшем получить доступ к нему
    connect = session.connector

    async with session.get('https://www.example.com') as response:
        print(f"Статус код: {response.status}")
    print(f"Cостояние сессии: {session.closed=}\nСостояние коннектора: {connect.closed=}")
    print('И сессия и коннектор открыты')
    # Отсоединение коннектора от сессии
    session.detach()
    print('____session.detach()')
    print(f"Cостояние сессии : {session.closed=}\nСостояние коннектора: {connect.closed=}")
    print('Сессия закрыта, но коннектор остается доступным')

    # Использование отсоединенного коннектора для новой сессии
    new_session = aiohttp.ClientSession(connector=connect)
    print('____new_session')

    # Отправка GET-запроса с новой сессией
    async with new_session.get('https://www.example.org') as response:
        print(f"Статус код: {response.status}")
        print(f"Cостояние сессии : {new_session.closed=}\n"
              f"Состояние коннектора: {connect.closed=}")

    # Закрытие новой сессии и коннектора
    await new_session.close()
    print('____new_session.close()')
    print(f"Cостояние сессии : {new_session.closed=}\n"
          f"Состояние коннектора: {connect.closed=}")
    print('И сессия и коннектор закрыты')


asyncio.run(main())



import aiohttp
import asyncio


async def main():
    # Создание сессии с trust_env установленным в True
    session = aiohttp.ClientSession(trust_env=True)

    async with session.get('https://www.example.com') as response:
        print(f"Статус код: {response.status}")
        print(await response.text())

    await session.close()


asyncio.run(main())



import aiohttp
import asyncio


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://ya.ru/') as response:
            print(f"Статус код: {response.status}")

        # Доступ к куки после запроса
        cookie_jar = session.cookie_jar
        cookies = cookie_jar.filter_cookies('https://ya.ru/')
        print(f"Куки для домена ya.ru: {cookies}")
        # Отправка еще одного запроса с использованием сохраненных куки
        async with session.get('https://ya.ru/') as response:
            print(f"Статус код: {response.status}")
            print(await response.text())


asyncio.run(main())



import aiohttp
import asyncio


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://www.example.com') as response:
            print(f"Статус код: {response.status}")

            # Получение версии протокола HTTP для этого ответа
            http_version = response.version
            print(f"Версия протокола HTTP: HTTP/{http_version.major}.{http_version.minor}")


asyncio.run(main())



import aiohttp
import asyncio


async def some_async_task(loop):
    print("Запуск асинхронной задачи")
    await asyncio.sleep(2)
    print(f"Задача выполняется в loop = {loop}")


async def main():
    async with aiohttp.ClientSession() as session:
        # Получение текущего цикла событий сессии
        loop = session.loop
        async with session.get('https://www.example.com') as response:
            print(f"Статус код: {response.status}")

        # Запуск асинхронной задачи в том же цикле событий
        await some_async_task(loop)

asyncio.run(main())



import aiohttp
import asyncio
from aiohttp import ClientTimeout


async def main():
    timeout = ClientTimeout(total=5)

    async with aiohttp.ClientSession(timeout=timeout) as session:

        try:
            async with session.get('https://www.example.com') as response:
                print(f"Статус код: {response.status}")
                print(await response.text())
        except asyncio.TimeoutError:
            print(
                "Таймаут: не удалось получить ответ от сервера в течение 5 секунд.")

        current_timeout = session.timeout.total if session.timeout else None
        print(f"Текущий таймаут сессии: {current_timeout} секунд")


asyncio.run(main())



import aiohttp
import asyncio


async def main():
    headers = {'User-Agent': 'MyApp/1.0'}
    async with aiohttp.ClientSession(headers=headers) as session:
        print(f"Текущие заголовки сессии: {session.headers}")

        async with session.get('https://www.example.com') as response:
            print(f"Статус код: {response.status}")
            print(await response.text())


asyncio.run(main())



import aiohttp
import asyncio
from aiohttp import BasicAuth


async def main():
    auth = BasicAuth('username', 'password')

    async with aiohttp.ClientSession(auth=auth) as session:
        print(f"Объект аутентификации: {session.auth}")

        async with session.get('https://www.example.com/secure') as response:
            print(f"Статус код: {response.status}")
            print(await response.text())


asyncio.run(main())



import aiohttp
import asyncio


# Колбэк-функции для обработчиков
async def on_request_start(session, trace_config_ctx, params):
    print("Запрос начат:", params.url)

async def on_request_end(session, trace_config_ctx, params):
    print("Запрос завершён:", params.url, params.response.status)


async def main():
    # Этот класс позволяет настроить обработчики для различных этапов HTTP-запроса
    trace_config = aiohttp.TraceConfig()

    # Добавляем обработчик для события "начало запроса".
    # Функция on_request_start() будет вызвана, когда начнется выполнение HTTP-запроса
    trace_config.on_request_start.append(on_request_start)

    # Добавляем обработчик для события "завершение запроса".
    # Функция on_request_end() будет вызвана после завершения HTTP-запроса
    trace_config.on_request_end.append(on_request_end)

    async with aiohttp.ClientSession(trace_configs=[trace_config]) as session:
        async with session.get('http://www.google.com') as response:
            print("Статус код:", response.status)


asyncio.run(main())



import aiohttp
import asyncio


# Обработчик для события начала запроса
async def on_request_start(session, trace_config_ctx, params):
    print(f"Начало запроса: {params.url}")

# Обработчик для события завершения разрешения DNS
async def on_dns_resolvehost_end(session, trace_config_ctx, params):
    print(f"Завершено разрешение DNS")

# Обработчик для события начала соединения
async def on_connection_create_start(session, trace_config_ctx, params):
    print(f"Начало соединения")

# Обработчик для события завершения запроса
async def on_request_end(session, trace_config_ctx, params):
    print(f"Завершение запроса: {params.url}, Код статуса: {params.response.status}")

async def main():
    # Создаем экземпляр класса TraceConfig из библиотеки aiohttp.
    # Этот класс позволяет настроить обработчики для различных этапов HTTP-запроса.
    trace_config = aiohttp.TraceConfig()

    # Добавляем обработчик для события "начало запроса".
    # Функция on_request_start будет вызвана, когда начнется выполнение HTTP-запроса.
    trace_config.on_request_start.append(on_request_start)

    # Добавляем обработчик для события "завершение разрешения DNS".
    # Функция on_dns_resolvehost_end будет вызвана после успешного разрешения DNS.
    trace_config.on_dns_resolvehost_end.append(on_dns_resolvehost_end)

    # Добавляем обработчик для события "начало создания соединения".
    # Функция on_connection_create_start будет вызвана при начале установки соединения с сервером.
    trace_config.on_connection_create_start.append(on_connection_create_start)

    # Добавляем обработчик для события "завершение запроса".
    # Функция on_request_end будет вызвана после завершения HTTP-запроса и получения ответа.
    trace_config.on_request_end.append(on_request_end)

    # Выполняем HTTP-запрос, используя TraceConfig
    async with aiohttp.ClientSession(trace_configs=[trace_config]) as session:
        async with session.get('http://www.google.com') as response:
            print(f"Итоговый код статуса: {response.status}")


asyncio.run(main())



import aiohttp
import asyncio
from datetime import datetime


# Обработчик для события начала запроса
async def on_request_start(session, trace_config_ctx, params):
    trace_config_ctx.start_time = datetime.now()  # Сохраняем время начала запроса в контексте трассировки
    print(f"Начало запроса: {params.url}")

# Обработчик для события завершения запроса
async def on_request_end(session, trace_config_ctx, params):
    end_time = datetime.now()  # Получаем время завершения запроса
    elapsed_time = (end_time - trace_config_ctx.start_time).total_seconds()  # Вычисляем затраченное время
    print(f"Завершение запроса: {params.url}, Код статуса: {params.response.status}")
    print(f"Время выполнения: {elapsed_time} секунд")  # Выводим затраченное время


async def main():
    # Создаем экземпляр TraceConfig и добавляем в него обработчики
    trace_config = aiohttp.TraceConfig()
    trace_config.on_request_start.append(on_request_start)
    trace_config.on_request_end.append(on_request_end)

    # Инициируем асинхронную сессию HTTP-клиента с настроенным TraceConfig
    async with aiohttp.ClientSession(trace_configs=[trace_config]) as session:
        async with session.get('http://www.google.com') as response:
            print(f"Итоговый код статуса: {response.status}")


asyncio.run(main())



import aiohttp
import asyncio


# Обработчик для события начала запроса
async def on_request_start(session, trace_config_ctx, params):
    print(f"Начало запроса: {params.url}, Метод: {params.method}")

    # Добавление пользовательского заголовка в запрос
    params.headers["Custom-Header"] = "Custom-Value"

async def main():
    # Создаем экземпляр TraceConfig и добавляем в него обработчик
    trace_config = aiohttp.TraceConfig()
    trace_config.on_request_start.append(on_request_start)

    # Инициируем асинхронную сессию HTTP-клиента с настроенным TraceConfig
    async with aiohttp.ClientSession(trace_configs=[trace_config]) as session:
        async with session.get('http://www.google.com') as response:
            # проверяем заголовки запроса
            print(response.request_info.headers)
            print(f"Итоговый код статуса: {response.status}")


asyncio.run(main())



import aiohttp
import asyncio


# Обработчик для события перенаправления
async def on_request_redirect(session, trace_config_ctx, params):
    print(f"Перенаправление: {params.url} -> {params.response.headers['Location']}, Код статуса: {params.response.status}")


async def main():
    trace_config = aiohttp.TraceConfig()
    trace_config.on_request_redirect.append(on_request_redirect)

    async with aiohttp.ClientSession(trace_configs=[trace_config]) as session:
        async with session.get(
                'https://httpbin.org/redirect-to?url=https%3A%2F%2Fwww.google.com%2F') as response:  # Здесь пример URL, который перенаправляет на другой URL
            print(f"Итоговый код статуса: {response.status}")


asyncio.run(main())



import aiohttp
import asyncio
from datetime import datetime


# Обработчик для события начала установки соединения
async def acquire_connection(session, trace_config_ctx, params):
    trace_config_ctx.acquire_start_time = datetime.now()  # Сохраняем время начала установки соединения
    print("Начало установки соединения")


# Обработчик для события завершения установки соединения
async def connection_create_end(session, trace_config_ctx, params):
    end_time = datetime.now()  # Получаем время завершения установки соединения
    elapsed_time = (end_time - trace_config_ctx.acquire_start_time).total_seconds()  # Вычисляем затраченное время
    print("Соединение установлено")
    print(f"Время на установку соединения: {elapsed_time} секунд")


async def main():
    trace_config = aiohttp.TraceConfig()
    trace_config.on_connection_create_start.append(acquire_connection)
    trace_config.on_connection_create_end.append(connection_create_end)

    async with aiohttp.ClientSession(trace_configs=[trace_config]) as session:
        async with session.get('http://www.google.com') as response:
            print(f"Итоговый код статуса: {response.status}")


asyncio.run(main())



import aiohttp
import asyncio


# Обработчик для события исключения в запросе
async def on_request_exception(session, trace_config_ctx, params):
    print(f"Исключение в запросе: {params.url}")
    print(f"Тип исключения: {params.exception}")
    print(f"Детали исключения: {params.exception.args}")


async def main():
    trace_config = aiohttp.TraceConfig()
    trace_config.on_request_exception.append(on_request_exception)

    async with aiohttp.ClientSession(trace_configs=[trace_config]) as session:
        try:
            async with session.get('http://nonexistent.url') as response:  # Выполняем HTTP-запрос к несуществующему URL
                print(f"Итоговый код статуса: {response.status}")
        except:
            print("Обработка исключения на уровне приложения")


asyncio.run(main())
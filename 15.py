import asyncio
import time


# Блокирующая функция
def blocking_fn():
    print(f"Старт blocking_fn(): {time.strftime('%X')}")
    # Обратите внимание, что time.sleep() может быть заменен любой блокирующей
    # IO-bound операцией, например операцией с файлами.
    time.sleep(1)  # Имитация выполнения длительной операции.
    print(f"Завершение blocking_fn() {time.strftime('%X')}")


# Вызов блокирующей функции
async def fn():
    return blocking_fn()


# Функция асинхронного sleep()
async def sleep_fn():
    print(f"Старт sleep_fn(): {time.strftime('%X')}")
    await asyncio.sleep(1)
    print(f"Завершение sleep_fn() {time.strftime('%X')}")


async def main():
    print(f"Старт main в {time.strftime('%X')}")
    await asyncio.gather(fn(), sleep_fn(), sleep_fn())
    print(f"Завершение main в {time.strftime('%X')}")


start = time.time()
asyncio.run(main())
print(f'Время выполнения программы: {(time.time() - start)}')



import asyncio
import threading
import time


# Блокирующая функция
def blocking_fn():
    print(f"Старт blocking_fn() в потоке c id {threading.current_thread().ident} в {time.strftime('%X')}")
    # Обратите внимание, что time.sleep() может быть заменен любой блокирующей
    # IO-bound операцией, например операцией с файлами.
    time.sleep(1)  # Имитация выполнения длительной операции.
    print(f"Завершение blocking_fn() в {time.strftime('%X')}")



# Функция асинхронного sleep()
async def sleep_fn():
    print(f"Старт sleep_fn() в потоке c id {threading.current_thread().ident} в {time.strftime('%X')}")
    await asyncio.sleep(1)
    print(f"Завершение sleep_fn() в {time.strftime('%X')}")


async def main():
    print(f"Старт main в потоке c id {threading.current_thread().ident} в {time.strftime('%X')}")

    # Создание корутины, для запуска в независимом потоке
    coro = asyncio.to_thread(blocking_fn)
    print(f'Тип объекта coro: {type(coro)}')

    # Асинхронный запуск задач.
    await asyncio.gather(coro, sleep_fn(), sleep_fn())
    print(f"Завершение main в {time.strftime('%X')}")


start = time.time()
asyncio.run(main())
print(f'Время выполнения программы: {(time.time() - start)}')



import asyncio
import threading
import time


# Блокирующая функция
def blocking_fn(arg1, arg2):
    # Печать сообщения о старте и номере используемого потока.
    print(f"Старт blocking_fn() в потоке c id {threading.current_thread().ident} в {time.strftime('%X')}")

    # Обратите внимание, что time.sleep() может быть заменен любой блокирующей
    # IO-bound операцией, например операцией с файлами.
    time.sleep(arg1)  # Имитация выполнения длительной операции используем arg1.
    print(f"Завершение blocking_fn() в {time.strftime('%X')}")
    return f'В blocking_fn() были переданы два аргумента arg1: {arg1} и arg2: {arg2}'


# Функция асинхронного sleep()
async def sleep_fn():
    # Печать сообщения о старте и номере используемого потока.
    print(f"Старт sleep_fn() в потоке c id {threading.current_thread().ident} в {time.strftime('%X')}")
    await asyncio.sleep(1)
    print(f"Завершение sleep_fn() в {time.strftime('%X')}")


async def main():
    # Печать сообщения о старте и номере используемого потока
    print(f"Старт main в потоке c id {threading.current_thread().ident} в {time.strftime('%X')}")

    # Создание корутины, для запуска в независимом потоке, передача аргументов.
    coro = asyncio.to_thread(blocking_fn, 1, 'Привет')

    # Проверка типа объекта для coro
    print(f'Тип объекта coro: {type(coro)}')
    result = await asyncio.gather(coro, sleep_fn(), sleep_fn())
    print(result[0])
    print(f"Завершение main в {time.strftime('%X')}")


start = time.time()
asyncio.run(main())
print(f'Время выполнения программы: {(time.time() - start)}')



import asyncio

async def coro():
    print("Вы ошиблись! Я работаю!")
    await asyncio.sleep(1)
    print("Моя работа завершилась!")

async def main():
    # Попытка передать корутину для выполнения в отдельном потоке.
    await asyncio.to_thread(coro)

asyncio.run(main())



import time
import asyncio
import threading

base_thread_id = 0
new_thread_id = 0


# Блокирующая функция
def blocking_func():
    global new_thread_id
    # Получите идентификатор текущего потока!!!
    new_thread_id = threading.current_thread().ident
    # Печать сообщения о старте и номере используемого потока.
    print(f"Старт blocking_func() в потоке c id {new_thread_id}")
    # Имитация выполнения долгой блокирующей IO-bound операции
    time.sleep(3)
    # Печать сообщения о завершении работы
    print("blocking_func() успешно выполнена!")


# Первая корутина
async def coro1():
    # Имитация выполнения IO-bound операции
    await asyncio.sleep(1)
    print("Выполнение coro1 завершено!")


# Вторая корутина
async def coro2():
    # Имитация выполнения IO-bound операции
    await asyncio.sleep(2)
    print("Выполнение coro2 завершено!")


async def main():
    global base_thread_id
    # Получите идентификатор текущего потока!!!
    base_thread_id = threading.current_thread().ident
    # Печать сообщения о старте и номере используемого потока
    print(f"Идентификатор основного потока {base_thread_id}")
    # Создайте корутину для запуска blocking_func() в независимом потоке:
    new_coro = asyncio.to_thread(blocking_func)
    # Асинхронный запуск задач.
    await asyncio.gather(new_coro, coro1(), coro2())


asyncio.run(main())



import asyncio
import random

articles = [
    {
        "id": 1,
        "title": "Основы Python",
        "content": "Python – язык программирования, который подходит для решения широкого спектра задач, от веб-разработки до анализа данных и машинного обучения. Благодаря своей простоте Python часто используется в начале обучения программированию. Python поддерживает множество библиотек, фреймворков, таких как Django для веб-разработки и Pandas для работы с данными. Выбирайте Python !"
    },
    {
        "id": 2,
        "title": "Введение в JavaScript",
        "content": "JavaScript – это язык программирования, который выполняется в браузере и позволяет создавать динамичные, интерактивные веб-страницы. JavaScript поддерживает функциональное, а также объектно-ориентированное программирование, асинхронное программирование. JavaScript является основным языком для фронтенд-разработки, часто используется вместе с HTML и CSS."
    },
    {
        "id": 3,
        "title": "Системное программирование на C++",
        "content": "C++ – язык программирования, который позволяет разработчикам создавать эффективные и производительные приложения. C++ расширяет язык C, добавляя объектно-ориентированное программирование, поддержку шаблонов. C++ используется в системном программировании, разработке игр, в высокопроизводительных вычислениях благодаря своей способности работать с низкоуровневыми данными и управлять памятью."
    },
    {
        "id": 4,
        "title": "Что такое SQL?",
        "content": "SQL (Structured Query Language) – это язык запросов, используемый для управления реляционными базами данных. SQL позволяет пользователям выполнять операции по созданию, чтению, обновлению и удалению данных. SQL запросы могут извлекать данные из одной или нескольких таблиц, фильтровать их, сортировать и агрегировать, что делает его мощным инструментом для работы с большими объемами информации."
    },
    {
        "id": 5,
        "title": "Основы HTML и CSS",
        "content": "HTML (HyperText Markup Language), CSS (Cascading Style Sheets) являются основными технологиями при создании веб-страниц. HTML задает структуру контента на странице с помощью различных HTML тегов, таких как заголовки, параграфы и изображения. CSS используется при определении визуального оформления этих элементов, включая цвета, шрифты, макеты. HTML и CSS часто используются вместе для создания современных веб-сайтов."
    },
    {
        "id": 6,
        "title": "Преимущества использования Git",
        "content": "Git – это система управления версиями, которая позволяет отслеживать изменения в коде, сотрудничать с другими разработчиками. Git обеспечивает распределенное управление версиями, что позволяет каждому разработчику работать из локальной копии репозитория и синхронизировать изменения с центральным репозиторием. Git упрощает управление проектами и упрощает откат к предыдущим версиям кода."
    },
    {
        "id": 7,
        "title": "Основы машинного обучения с Python",
        "content": "Машинное обучение – это область искусственного интеллекта, которая использует алгоритмы для анализа данных и создания моделей, способных делать прогнозы или принимать решения. Python является популярным языком для машинного обучения благодаря  библиотекам Python - Scikit-learn, TensorFlow, Keras. Эти инструменты Python упрощают процесс создания и обучения моделей машинного обучения."
    },
    {
        "id": 8,
        "title": "Что такое API?",
        "content": "API (Application Programming Interface) – это набор инструментов и протоколов, который позволяет различным программным приложениям взаимодействовать друг с другом. API предоставляет разработчикам возможность использовать функции или данные другого приложения без необходимости знать детали его внутренней работы. Api упрощает интеграцию различных систем и расширяет функциональные возможности приложений."
    },
    {
        "id": 9,
        "title": "Основы веб-разработки",
        "content": "Веб разработка включает в себя создание, поддержание веб сайтов, веб приложений. Она охватывает фронтенд-разработку (создание пользовательских интерфейсов), бэкенд-разработку (создание серверной логики и взаимодействие с базами данных). Современные веб технологии включают HTML, CSS, JavaScript для фронтенда и различные серверные языки и фреймворки для бэкенда."
    },
    {
        "id": 10,
        "title": "Программирование на Java",
        "content": "Java – это язык программирования, который известен своей переносимостью и широким применением в корпоративных системах. Java поддерживает объектно-ориентированное программирование и предоставляет богатый набор библиотек, фреймворков, таких как Spring, Hibernate. Java используется для создания веб-приложений, мобильных приложений (Android), серверных решений."
    }
]


def find_most_common_word(text: str):
    words = text.split()
    new_dict = {}
    for word in words:
        lower_word = word.lower()
        new_dict[lower_word] = new_dict.get(lower_word, 0) + 1
    max_pair = max(new_dict.items(), key=lambda x: x[1])
    return max_pair[0]



async def download_and_process(article: dict):
    await asyncio.sleep(random.uniform(0.1, 0.5))
    tag_result = await asyncio.to_thread(find_most_common_word, article['content'])
    article['tag'] = tag_result


async def main():
    download = [asyncio.create_task(download_and_process(article)) for article in articles]
    await asyncio.gather(*download)
    for article in articles:
        print(f"{article['title']}: {article['tag']}")

asyncio.run(main())



import asyncio
import contextvars

# Определяем контекстную переменную
user_context = contextvars.ContextVar('user_context')

async def authenticate_user(user_id):
    # Устанавливаем значение контекстной переменной
    token = user_context.set(user_id)
    try:
        await asyncio.sleep(1)
        print(f"User {user_context.get()} authenticated")
    finally:
        # Удаляем значение после завершения
        user_context.reset(token)

async def main():
    # Запускаем аутентификацию для разных пользователей
    await asyncio.gather(
        authenticate_user("Alice"),
        authenticate_user("Bob"),
        authenticate_user("Charlie")
    )

asyncio.run(main())



import asyncio
import contextvars

user_context = contextvars.ContextVar('user_context')

# Синхронная функция для логирования
def log_authentication():
    print(f"User {user_context.get()} authenticated")

# Корутина для логирования
async def log_authentication_coro():
    print(f"User {user_context.get()} authenticated")

async def authenticate_user(user_id):
    token = user_context.set(user_id)
    try:
        # ВАРИАНТ 1: синхронная функция
        log_authentication()
        # ВАРИАНТ 2: корутина
        # await log_authentication_coro()
        # ВАРИАНТ 3: задача
        # await asyncio.create_task(log_authentication_coro())
    finally:
        user_context.reset(token)


async def main():
    await asyncio.gather(
        authenticate_user("Alice"),
        authenticate_user("Bob"),
        authenticate_user("Charlie")
    )

asyncio.run(main())



import asyncio
import contextvars

user_context = contextvars.ContextVar('user_context')

def log_authentication():
    print(f"User {user_context.get()} authenticated")
    # пытаемся изменить контекстную переменную
    user_context.set('Unknown user')

async def log_authentication_coro():
    print(f"User {user_context.get()} authenticated")
    # пытаемся изменить контекстную переменную
    user_context.set('Unknown user')

async def authenticate_user(user_id):
    token = user_context.set(user_id)
    try:
        # ВАРИАНТ 1
        # log_authentication()
        # ВАРИАНТ 2
        # await log_authentication_coro()
        # ВАРИАНТ 3
        await asyncio.create_task(log_authentication_coro())
    finally:
        # Проверка, была ли изменена конекстная переменная
        print(f"User {user_context.get()} logout")
        user_context.reset(token)

async def main():
    await asyncio.gather(
        authenticate_user("Alice"),
        authenticate_user("Bob"),
        authenticate_user("Charlie")
    )

asyncio.run(main())



import asyncio
import contextvars
import random

# Определяем контекстные переменные
user_context = contextvars.ContextVar('user_context')
request_id_context = contextvars.ContextVar('request_id_context')


def log_message(message):
    user = user_context.get("Unknown User")
    request_id = request_id_context.get("Unknown Request ID")
    print(f"User: {user}, Request ID: {request_id}: {message}")


async def login():
    log_message("User logged in")
    await asyncio.sleep(random.random())


async def perform_work():
    log_message("Performing work")
    await asyncio.sleep(random.random())


async def logout():
    log_message("User logged out")
    await asyncio.sleep(random.random())


async def handle_user_request(user_id, request_id):
    user_token = user_context.set(user_id)
    request_id_token = request_id_context.set(request_id)
    try:
        await login()
        await perform_work()
        await logout()
    finally:
        user_context.reset(user_token)
        request_id_context.reset(request_id_token)


async def main():
    users_requests = [("Alice", 1), ("Bob", 2), ("Charlie", 3)]
    tasks = []
    for user, req_id in users_requests:
        task = asyncio.create_task(handle_user_request(user, req_id))
        tasks.append(task)
    await asyncio.gather(*tasks)
    log_message('Unknown')


asyncio.run(main())



import asyncio
import contextvars

order_state = contextvars.ContextVar('user_context')

def set_order_state(state):
    return order_state.set(state)


async def process_order(order_id):
    states = ["Принят", "Обрабатывается", "Отправлен"]
    for order_state in states:
        await asyncio.sleep(1)
        set_order_state(order_state)
        print(f"Заказ {order_id} сейчас в состоянии: {order_state}")


async def main():
    orders = ["Заказ1", "Заказ123", "Заказ12345"]
    tasks = [process_order(order) for order in orders]
    await asyncio.gather(*tasks)


asyncio.run(main())



import asyncio
import contextvars

# Контекстная переменная для хранения текущего языка
current_language = contextvars.ContextVar('current_language')

def set_language(language_code):
    current_language.set(language_code)

async def get_greeting():
    greetings = {
        'en': "Hello!",
        'ru': "Привет!",
        'es': "Hola!"
    }
    return greetings.get(current_language.get())

async def get_error_message():
    error_messages = {
        'en': "An error occurred.",
        'ru': "Произошла ошибка.",
        'es': "Ocurrió un error."
    }
    return error_messages.get(current_language.get())


async def test_user_actions(language_code):
    set_language(language_code)
    print(await get_greeting())
    print(await get_error_message())


async def main():
    await asyncio.gather(*[test_user_actions(language) for language in ('en', 'ru', 'es')])

asyncio.run(main())



import asyncio
import contextvars
import random

# Определяем контекстные переменные
user_context = contextvars.ContextVar('user_context')
request_id_context = contextvars.ContextVar('request_id_context')


def log_message(message):
    user = user_context.get("Unknown User")
    request_id = request_id_context.get("Unknown Request ID")
    print(f"User: {user}, Request ID: {request_id}: {message}")


async def login():
    log_message("User logged in")
    await asyncio.sleep(random.random())


async def perform_work():
    log_message("Performing work")
    await asyncio.sleep(random.random())


async def logout():
    log_message("User logged out")
    await asyncio.sleep(random.random())


async def handle_user_request(user_id, request_id):
    user_token = user_context.set(user_id)
    request_id_token = request_id_context.set(request_id)
    try:
        await login()
        await perform_work()
        await logout()
    finally:
        user_context.reset(user_token)
        request_id_context.reset(request_id_token)


async def main():
    users_requests = [("Alice", 1), ("Bob", 2), ("Charlie", 3)]
    tasks = []
    for user, req_id in users_requests:
        task = asyncio.create_task(handle_user_request(user, req_id))
        tasks.append(task)
    await asyncio.gather(*tasks)
    log_message('Unknown')


asyncio.run(main())
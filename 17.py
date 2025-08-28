import asyncio


async def task_coroutine(num):
    await asyncio.sleep(1)
    print(f"Задача {num} выполнена")


async def main():
    # Создание списка асинхронных задач с использованием генератора списков
    tasks = [asyncio.create_task(task_coroutine(x)) for x in range(5)]

    # Получение списка всех незавершенных задач для текущего событийного цикла

    all_tasks = asyncio.all_tasks()
    # Вывод количества задач
    print(f"Количество задач: {len(all_tasks)}")

    await asyncio.gather(*tasks)
    for task in all_tasks:
        print(task)


asyncio.run(main())



import asyncio

async def my_coroutine():
    print(f"Имя задачи: {asyncio.current_task().get_name()}")

async def main():
    task = asyncio.create_task(my_coroutine(), name="my_task")
    await task

asyncio.run(main())



import asyncio

async def my_coroutine():
    print(f"Имя задачи до изменения: {asyncio.current_task().get_name()}")
    asyncio.current_task().set_name("new_name")
    print(f"Имя задачи после изменения: {asyncio.current_task().get_name()}")

async def main():
    task = asyncio.create_task(my_coroutine(), name="my_task")
    await task

asyncio.run(main())



import asyncio
import aiohttp


async def download_file(url):
    async with aiohttp.ClientSession() as session:  # Создание асинхронного HTTP-соединения
        async with session.get(
                url) as response:  # Отправка асинхронного GET-запроса
            filename = response.headers.get(
                "content-disposition")  # Извлечение имени файла из заголовков
            if filename:
                filename = filename.split("filename=")[1]
            task = asyncio.current_task()
            task.set_name(
                f"Downloading {filename}")  # Установка имени текущей задачи
            with open(filename,
                      "wb") as f:  # Открытие файла для записи бинарных данных
                while True:
                    chunk = await response.content.read(
                        1024)  # Чтение и запись в файл содержимого ответа по частям
                    if not chunk:
                        break
                    f.write(chunk)
            task.set_name(
                f"Downloaded {filename}")  # Обновление имени текущей задачи после завершения скачивания


async def main():
    urls = [
        "<https://www.example.com/file1.txt>",
        "<https://www.example.com/file2.txt>",
        "<https://www.example.com/file3.txt>"
    ]

    tasks = [asyncio.create_task(download_file(url)) for url in urls]
    await asyncio.gather(*tasks)


asyncio.run(main())



import asyncio

# Товары на складе:
warehouse_store = {
    "Диван": 15,
    "Обеденный_стол": 10,
    "Офисное_кресло": 25,
    "Кофейный_столик": 12,
    "Кровать": 8,
    "Книжный_шкаф": 20,
    "ТВ-тумба": 7,
    "Шкаф": 9,
    "Письменный_стол": 18,
    "Тумбочка": 14,
    "Комод": 11,
    "Барный_стул": 22,
    "Угловой_диван": 4,
    "Двухъярусная_кровать": 3,
    "Шезлонг": 2,
    "Консольный_столик": 16,
    "Кресло": 17,
    "Туалетный_столик": 19,
    "Книжный_стеллаж": 24,
    "Банкетка": 10,
    "Обеденный_стул": 28,
    "Кресло-качалка": 15,
    "Шкаф-купе": 18,
    "Табуретка": 40,
    "Стеллаж": 13,
    "Кресло-мешок": 5,
    "Кухонный_гарнитур": 6,
    "Журнальный_столик": 8,
    "Витрина": 7,
    "Полка": 30
}

# Заказ:
order = {'Диван': 5, 'Обеденный_стол': 3, 'Табуретка': 50, 'Гардероб': 1}


async def check_store(item, quantity):
    task = asyncio.current_task()
    if item in warehouse_store and warehouse_store[item] >= quantity:
        task.set_name(f"В наличии: {item}")
    elif item in warehouse_store and warehouse_store[item] < quantity:
        task.set_name(f"Частично в наличии: {item}")
    else:
        task.set_name(f"Отсутствует: {item}")


async def main():
    tasks = [asyncio.create_task(check_store(key, value)) for key, value in order.items()]
    await asyncio.gather(*tasks)
    for task in sorted(tasks, key=lambda task: task.get_name()):
        print(task.get_name())

asyncio.run(main())



import asyncio


async def raise_exception():
    # Генерируем ошибку RuntimeError
    raise RuntimeError("--Установленное исключение--")


async def main():
    task = asyncio.create_task(raise_exception())
    await asyncio.sleep(0.1)
    try:
        await task
    except Exception as e:
        print(f"Пойманное исключение: {e}")
    # Получаем исключение, которое возникло во время выполнения задания (если оно возникло)
    exception = task.exception()
    if exception:
        print(f"Тут можно обработать возникшее исключение: {exception}")


asyncio.run(main())



import asyncio


async def failing_coroutine():
    await asyncio.sleep(1)
    raise ValueError("Возникла ошибка в корутине failing_coroutine()")


async def successful_coroutine():
    await asyncio.sleep(1)
    print("Успешное выполнение")


async def main():
    tasks = [asyncio.create_task(failing_coroutine()),
             asyncio.create_task(successful_coroutine())]
    try:
        await asyncio.gather(*tasks)
    except ValueError as ex:
        print(ex)

    for i, task in enumerate(tasks, start=1):
        # Получаем исключение из задачи, если оно возникло, и выводим информацию о нем
        exc = task.exception()
        if exc:
            print(f"Задача {i}: Исключение - {exc}")
        else:
            print(f"Задача {i}: Успешно выполнена")


asyncio.run(main())



import asyncio
import random

async def process_item(item):
    """Корутина, обрабатывающая один элемент списка"""
    await asyncio.sleep(random.randint(0, 5))
    if item == 13 or item == 'i':
        raise ValueError(f"Элемент {item} не может быть обработан")
    print(f"Элемент соответстует условию: {item}")


async def main():
    """Асинхронная функция для обработки списка элементов"""
    items = [13, 2, 13, 4, 13, 'a', 'b', 'c', 'i', 13, 6, 7, 8, 13, 10, 11, 13, 'i', 'e', 'f', 'i', 'h']
    tasks = [asyncio.create_task(process_item(item)) for item in items]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED, timeout=3)

    failed_tasks = [task for task in done if task.exception()]
    print(f"Количество заданий, завершившихся с ошибкой: {len(failed_tasks)} из {len(done)}")
    print(f"Количество незавершенных заданий: {len(pending)}")
    for task in pending:
        task.cancel()


asyncio.run(main())



import asyncio

files = ['image.png', 'file.csv', 'file1.txt']

# missed_files = [...] список пропущенных файлов "спрятан" внутри задачи

async def download_file(file_name):
    await asyncio.sleep(1)
    if file_name in missed_files:
        raise FileNotFoundError(f'Файл {file_name} не найден')
    else:
        await asyncio.sleep(1)
        return f'Файл {file_name} успешно скачан'


async def main():
    tasks = [asyncio.create_task(download_file(file_name)) for file_name in files]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED, timeout=3)
    for task in done:
        if task.exception():
            print(task.exception())

asyncio.run(main())



import asyncio


async def main_task():
    print("Корутина main_task запустилась")
    await asyncio.sleep(5)
    print("Корутина main_task завершилась")


async def main():
    task = asyncio.create_task(main_task())
    await asyncio.sleep(1)
    task.cancel()  # Отмена задачи (запрос на отмену выполнения корутины main_task())

    try:
        await task
    except asyncio.CancelledError:
        print("Задача отменена")


asyncio.run(main())



import asyncio


async def main_task():
    print("Корутина main_task запустилась")
    await asyncio.sleep(5)
    print("Корутина main_task завершилась")


async def main():
    task = asyncio.create_task(main_task())
    await asyncio.sleep(1)
    task.cancel()  # Отмена задачи
    await asyncio.sleep(2)
    if task.cancelled():  # Проверка, была ли задача отменена
        print(f"Задача отменена - {task.cancelled()}")


asyncio.run(main())



import asyncio

async def long_running_task():
    try:
        await asyncio.sleep(3)
    except asyncio.CancelledError:
        # Обработка отмены задачи и вывод сообщения при перехвате asyncio.CancelledError
        print("Получена команда на отмену задачи task")
        # Подъем перехваченного ранее исключения, для срабатывания логики в main().
        raise

async def main():
    task = asyncio.create_task(long_running_task())
    await asyncio.sleep(.5)
    # Отменяем задачу
    task.cancel()

    # Используем cancelling() для проверки, была ли задача помечена для отмены
    if task.cancelling() > 0:
        print("Дана команда отмены задачи task")
    else:
        print("Задача task не ожидает отмены")
    # Перехват исключения asyncio.CancelledError в main()
    try:
        await task
    except asyncio.CancelledError:
        print(f"Задача task отменена: {task.cancelled()}")


asyncio.run(main())



import asyncio
import random


async def download():
    download_progress = random.random()
    print(f'Успешно загружено {int(download_progress * 100)}%')
    while download_progress < 1:
        try:
            await asyncio.sleep(2)  # имитация загрузки файла
            print('Загрузка завершена')
            break
        except asyncio.CancelledError:
            print('Загрузка отменена')
            if download_progress > 0.5:
                print('Прогресс скачивания более 50%, возобновляем загрузку')
                # отменяем действие cancel()
                asyncio.current_task().uncancel()
            else:
                print('Прогресс скачивания менее 50%, загрузка остановлена')
                raise


async def main():
    task = asyncio.create_task(download())
    await asyncio.sleep(1)
    task.cancel()  # Отменяем задачу
    try:
        await task
    except asyncio.CancelledError:
        print('Загрузка была отменена')


asyncio.run(main())



import asyncio


data = [
    {'Name': 'Company1', 'Address': '9974 Lloyd Radial Suite 005, Andrewfort, PW 45078', 'Phone': '829-338-4124x62279',
     'Email': 'yhiggins@bishop-gentry.com', 'Website': 'https://www.griffith-diaz.org/', 'Year': 1981,
     'Employees': 2935, 'Description': 'Advanced eco-centric secured line', 'CEO': 'Amanda Hall', 'TaxID': 8627654889,
     'call_time': 8},
    {'Name': 'Company2', 'Address': '7703 Craig Spurs Suite 391, Acostafurt, MT 24156', 'Phone': '225-321-1903',
     'Email': 'amandathomas@jones.biz', 'Website': 'http://www.adkins.org/', 'Year': 2008, 'Employees': 2593,
     'Description': 'Sharable next generation hardware', 'CEO': 'Jacob Dunlap', 'TaxID': 2307021392, 'call_time': 2},
    {'Name': 'Company3', 'Address': '5850 Stewart Club Suite 286, Carolynfurt, AR 69364', 'Phone': '792.763.2559x8121',
     'Email': 'berrymichael@glass-santos.com', 'Website': 'https://www.white.biz/', 'Year': 2006, 'Employees': 21,
     'Description': 'User-friendly bi-directional software', 'CEO': 'Carl Bautista', 'TaxID': 2470607513,
     'call_time': 1},
    {'Name': 'Company4', 'Address': '4381 Roberts Parks, Payneside, AZ 03840', 'Phone': '(467)414-0033x4541',
     'Email': 'ugonzalez@shelton.com', 'Website': 'https://www.adams.com/', 'Year': 2011, 'Employees': 7084,
     'Description': 'Cloned dedicated website', 'CEO': 'David Huffman', 'TaxID': 7462166908, 'call_time': 5},
    {'Name': 'Company5', 'Address': '141 Shannon Plaza, Janetshire, FM 18139', 'Phone': '(301)716-0789x919',
     'Email': 'adamsanchez@jones-johnson.com', 'Website': 'http://www.perez.net/', 'Year': 2011, 'Employees': 8458,
     'Description': 'Extended directional initiative', 'CEO': 'Monique Anderson', 'TaxID': 1315678326, 'call_time': 9},
    {'Name': 'Company6', 'Address': '8232 Nicole Isle, New Sandra, DE 67218', 'Phone': '+1-990-955-0294x551',
     'Email': 'pmason@lynch.net', 'Website': 'http://www.ferrell.com/', 'Year': 2016, 'Employees': 5698,
     'Description': 'Automated human-resource methodology', 'CEO': 'Jessica Love', 'TaxID': 4830095509, 'call_time': 7},
    {'Name': 'Company7', 'Address': '886 Barrett Street Suite 817, Laurenstad, NH 86979',
     'Phone': '+1-208-883-7438x43251', 'Email': 'rjenkins@flores.info', 'Website': 'http://www.morse-willis.com/',
     'Year': 2022, 'Employees': 4772, 'Description': 'Persevering motivating info-mediaries', 'CEO': 'Brittany Freeman',
     'TaxID': 6278265190, 'call_time': 1},
    {'Name': 'Company8', 'Address': 'USCGC Hanna, FPO AE 22431', 'Phone': '817-374-2328', 'Email': 'tgarcia@greer.com',
     'Website': 'https://mason.com/', 'Year': 1985, 'Employees': 7270, 'Description': 'Integrated 4thgeneration frame',
     'CEO': 'Michelle Cardenas', 'TaxID': 2584423305, 'call_time': 11},
    {'Name': 'Company9', 'Address': '60164 Bailey Mountains, West Kaitlinside, AZ 10362',
     'Phone': '001-261-799-2627x62104', 'Email': 'kathryn73@burgess-berry.com', 'Website': 'https://ramirez.info/',
     'Year': 1984, 'Employees': 2211, 'Description': 'Cross-group web-enabled open system', 'CEO': 'Benjamin Sawyer',
     'TaxID': 9449376713, 'call_time': 4},
    {'Name': 'Company10', 'Address': '178 Lewis River, New Alexander, MS 54707', 'Phone': '568.275.2394x9402',
     'Email': 'walterrobert@johnson-jacobs.biz', 'Website': 'http://www.olson-weber.info/', 'Year': 1981,
     'Employees': 8674, 'Description': 'Up-sized incremental database', 'CEO': 'Alexandra Johnson', 'TaxID': 2351268827,
     'call_time': 6},
    {'Name': 'Company11', 'Address': '4709 Brooks Camp Suite 799, Port Natalie, NY 99637', 'Phone': '(818)703-8797',
     'Email': 'pamelajohnson@matthews-nelson.com', 'Website': 'https://watkins.biz/', 'Year': 1998, 'Employees': 9951,
     'Description': 'Re-contextualized logistical extranet', 'CEO': 'Kelly Savage', 'TaxID': 2234091865,
     'call_time': 1}, {'Name': 'Company12', 'Address': '0372 Jared Isle Suite 075, South Anthony, GU 21805',
                       'Phone': '451.393.2570x70097', 'Email': 'kendramurray@olson.biz',
                       'Website': 'https://clark.net/', 'Year': 2010, 'Employees': 7653,
                       'Description': 'Open-architected exuding functionalities', 'CEO': 'Anita Peterson',
                       'TaxID': 5838627215, 'call_time': 4},
    {'Name': 'Company13', 'Address': '5680 Horton Trail Suite 057, Johnsontown, WI 83282',
     'Phone': '001-735-722-1031x070', 'Email': 'amywalker@smith.org', 'Website': 'https://www.daniel-butler.info/',
     'Year': 2000, 'Employees': 2400, 'Description': 'Universal bi-directional leverage', 'CEO': 'Christina Wright MD',
     'TaxID': 7573435589, 'call_time': 8},
    {'Name': 'Company14', 'Address': '05330 Calhoun Locks, East Elizabeth, OR 21993', 'Phone': '201.750.6003',
     'Email': 'andersonbrian@hamilton.com', 'Website': 'https://www.ochoa-freeman.com/', 'Year': 2000,
     'Employees': 5806, 'Description': 'Open-source 5thgeneration open system', 'CEO': 'Garrett Griffin',
     'TaxID': 9702324758, 'call_time': 4},
    {'Name': 'Company15', 'Address': '2784 Stephanie Meadow, Kellyview, RI 41940', 'Phone': '(541)800-3165x84630',
     'Email': 'paynejacqueline@perkins.com', 'Website': 'https://galvan-ho.com/', 'Year': 2015, 'Employees': 2934,
     'Description': 'Optional disintermediate installation', 'CEO': 'Brianna Vang', 'TaxID': 9197588683,
     'call_time': 3},
    {'Name': 'Company16', 'Address': 'USS Powers, FPO AE 79645', 'Phone': '799-737-6867', 'Email': 'lhurst@ross.info',
     'Website': 'http://www.duke.org/', 'Year': 2005, 'Employees': 9444,
     'Description': 'Open-architected needs-based circuit', 'CEO': 'Denise Robinson', 'TaxID': 5242686149,
     'call_time': 9},
    {'Name': 'Company17', 'Address': '21935 Roman Common Suite 870, New Erik, GU 39550', 'Phone': '399.755.1350x632',
     'Email': 'staceygordon@jones.com', 'Website': 'https://www.williams.biz/', 'Year': 2000, 'Employees': 2496,
     'Description': 'Grass-roots tertiary matrix', 'CEO': 'Amanda Matthews', 'TaxID': 3951572194, 'call_time': 3},
    {'Name': 'Company18', 'Address': '5321 Sandra Flats Apt. 657, Port Timothy, IN 76963', 'Phone': '341-610-9720x396',
     'Email': 'christopher05@adams.com', 'Website': 'https://www.coleman.com/', 'Year': 2015, 'Employees': 7697,
     'Description': 'Multi-tiered discrete projection', 'CEO': 'Brenda Wilkerson', 'TaxID': 6565717553, 'call_time': 3},
    {'Name': 'Company19', 'Address': '35623 Julie Walk, Hopkinsside, UT 67634', 'Phone': '+1-473-361-2745x37065',
     'Email': 'uwalker@stark.com', 'Website': 'https://www.pena-walters.com/', 'Year': 1980, 'Employees': 4922,
     'Description': 'Synergized scalable encoding', 'CEO': 'Stephanie Young', 'TaxID': 9620588390, 'call_time': 20},
    {'Name': 'Company20', 'Address': '09618 Brooke Villages Apt. 178, East Spencerfurt, MA 26485',
     'Phone': '(990)441-2290', 'Email': 'xzimmerman@allen.com', 'Website': 'https://www.burton.com/', 'Year': 1997,
     'Employees': 2276, 'Description': 'Enhanced 4thgeneration website', 'CEO': 'David Valdez', 'TaxID': 9386061759,
     'call_time': 7},
    {'Name': 'Company21', 'Address': '813 Robert Way Apt. 941, South Paige, RI 03809', 'Phone': '001-292-812-7461x5232',
     'Email': 'cameronking@fleming.com', 'Website': 'http://cooper.info/', 'Year': 1999, 'Employees': 5967,
     'Description': 'Fully-configurable eco-centric capacity', 'CEO': 'Edward Allen', 'TaxID': 1198177347,
     'call_time': 1},
    {'Name': 'Company22', 'Address': '40332 Kathryn Green, South Taylor, TN 95398', 'Phone': '001-628-286-5262x2379',
     'Email': 'lperez@hall-jackson.biz', 'Website': 'http://jones-perez.info/', 'Year': 2020, 'Employees': 2944,
     'Description': 'Face-to-face fresh-thinking model', 'CEO': 'James Hansen', 'TaxID': 6392795545, 'call_time': 5},
    {'Name': 'Company23', 'Address': '094 Kathleen Stream Apt. 125, Port Ashleyside, WV 84478', 'Phone': '480.427.2828',
     'Email': 'april40@payne.com', 'Website': 'https://www.fitzpatrick-rasmussen.net/', 'Year': 1993, 'Employees': 518,
     'Description': 'Implemented analyzing knowledge user', 'CEO': 'Mary Hill', 'TaxID': 5558335589, 'call_time': 5},
    {'Name': 'Company24', 'Address': '80224 Roger Way, Michelletown, KS 84807', 'Phone': '755-817-3331x0542',
     'Email': 'nelsonfrank@bullock.com', 'Website': 'http://www.moreno.net/', 'Year': 1989, 'Employees': 1768,
     'Description': 'Fully-configurable grid-enabled moderator', 'CEO': 'Peter Spencer', 'TaxID': 8239869710,
     'call_time': 1},
    {'Name': 'Company25', 'Address': '24106 Robinson Walks, Gibsonhaven, TX 66568', 'Phone': '(947)767-2860x856',
     'Email': 'ericpratt@parker.info', 'Website': 'https://rubio-webb.com/', 'Year': 2015, 'Employees': 6385,
     'Description': 'Reduced foreground workforce', 'CEO': 'Erin Lowe', 'TaxID': 3626826838, 'call_time': 11}]


async def call_company(element):
    if element['call_time'] > 5:
        raise asyncio.CancelledError('err')
    await asyncio.sleep(element['call_time'])
    print(f'Company {element['Name']}: {element['Phone']} дозвон успешен')


async def main():
    tasks = [asyncio.create_task(call_company(element)) for element in data]
    for task in tasks:
        try:
            await task
        except asyncio.CancelledError:
            pass


asyncio.run(main())
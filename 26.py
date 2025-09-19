import aiofiles

async def read_from_file():
    async with aiofiles.open('example.txt', mode='r') as f:
        content = await f.read()
    return content



import aiofiles

async def read_from_file():
    async with aiofiles.open('example.txt', mode='r', encoding='windows-1251') as f:
        content = await f.read()
    return content



import aiofiles

async def read_from_file():
    async with aiofiles.open('example.txt', mode='r', errors='ignore') as f:
        content = await f.read()
    return content



import os
import aiofiles

# Открываем файл и получаем файловый дескриптор
fd = os.open('example.txt', os.O_RDONLY)

async def read_from_file(fd):
    async with aiofiles.open(fd, mode='r', closefd=False) as f:
        content = await f.read()
    return content



import aiofiles
import os

def custom_opener(file, flags):
    return os.open(file, flags | os.O_NONBLOCK)

async def read_from_file():
    async with aiofiles.open('example.txt', mode='r', opener=custom_opener) as f:
        content = await f.read()
    return content



import asyncio
import aiofiles

async def main():
    loop = asyncio.get_running_loop()
    async with aiofiles.open('example.txt', mode='r', loop=loop) as f:
        content = await f.read()
    print(content)

asyncio.run(main())



import asyncio
import aiofiles
from concurrent.futures import ThreadPoolExecutor

async def main():
    with ThreadPoolExecutor(max_workers=5) as executor:
        async with aiofiles.open('example.txt', mode='r', executor=executor) as f:
            content = await f.read()
        print(content)

asyncio.run(main())



import asyncio
import aiofiles


async def main():
    # Буферизация отключена, используется режим чтения бинарных данных
    async with aiofiles.open('myfile.txt', mode='rb', buffering=0) as f:
        data = await f.read()
        print(data)  # Увидим бинарные данные файла

    # Буферизация отключена, но приведет к ошибке
    try:
        async with aiofiles.open('myfile.txt', mode='r', buffering=0) as f:
            data = await f.read()
            print(data)
    except ValueError as eq:
        print(f"Обнаружена ошибка: {eq}")

    # Строковый буфер
    async with aiofiles.open('myfile.txt', mode='r', buffering=1) as f:
        print(await f.read())

    # Буферизация блока с размером буфера 4096
    async with aiofiles.open('myfile.txt', mode='r', buffering=4096) as f:
        print(await f.read())


asyncio.run(main())



import asyncio
import aiofiles


async def main():
    async with aiofiles.open('myfile.txt', mode='r') as f:
        async for line in f:
            print(line)

asyncio.run(main())



import asyncio
import aiofiles

async def main():
    async with aiofiles.open('myfile.txt', mode='w') as f:
        num_chars = await f.write('Hello, world!')
        print(f'Записано {num_chars} символов в файл.')

asyncio.run(main())



import asyncio
import aiofiles

async def main():
    lines = ['Hello, world!\n', 'How are you?\n', 'Goodbye!\n']
    async with aiofiles.open('myfile.txt', mode='w') as f:
        await f.writelines(lines)

asyncio.run(main())



import asyncio
import aiofiles

async def main():
    async with aiofiles.open('myfile.txt', mode='w') as f:
        print(f'File is writable: {await f.writable()}')

asyncio.run(main())



import asyncio
import aiofiles

async def main():
    async with aiofiles.open('myfile.txt', mode='r') as f:
        contents = await f.read(5)
        print(contents)

asyncio.run(main())



import asyncio
import aiofiles

async def main():
    async with aiofiles.open('myfile.txt', mode='r') as f:
        line = await f.readline()
        print(line)

asyncio.run(main())



import asyncio
import aiofiles

async def main():
    async with aiofiles.open('myfile.txt', mode='r') as f:
        lines = await f.readlines()
        print(lines)

asyncio.run(main())



import asyncio
import aiofiles

async def main():
    ba = bytearray(10)  # Создайте байтовый массив для хранения данных
    async with aiofiles.open('myfile.bin', mode='rb') as f:
        num_bytes = await f.readinto(ba)
        print(f'Считать {num_bytes} байт в байтовый массив.')

asyncio.run(main())



import asyncio
import aiofiles

async def main():
    f = await aiofiles.open('myfile.txt', mode='w')
    await f.write('Hello, world!')
    await f.close()

asyncio.run(main())



import asyncio
import aiofiles

async def main():
    async with aiofiles.open('myfile.txt', mode='w') as f:
        await f.write('Hello, world!')
        await f.flush()

asyncio.run(main())



import asyncio
import aiofiles

async def main():
    async with aiofiles.open('myfile.txt', mode='w') as f:
        print(f'Is file connected to a terminal: {await f.isatty()}')

asyncio.run(main())



import asyncio
import aiofiles

async def read_file(filename):
    async with aiofiles.open(filename, mode='rb') as f:
        while True:
            chunk = await f.read1(1024)
            if not chunk:
                break
            print(chunk)

asyncio.run(read_file('myfile.txt'))



import asyncio
import aiofiles

async def main():
    async with aiofiles.open('myfile.txt', mode='r') as f:
        await f.seek(10)  # Перемещаемся на 10-й байт в файле
        data = await f.read()  # Читаем остаток файла с этой позиции
        print(data)

asyncio.run(main())



import aiofiles
import asyncio


async def check_seekable(file_path):
    async with aiofiles.open(file_path, mode='r') as f:
        if await f.seekable():
            print(f"{file_path} supports random access.")
        else:
            print(f"{file_path} does not support random access.")

asyncio.run(check_seekable('your_file.txt'))



import asyncio
import aiofiles

async def main():
    async with aiofiles.open('myfile.txt', mode='r') as f:
        print(await f.read(5))  # Читаем и печатаем 5 символов из файла
        position = await f.tell()
        print(f'Текущая позиция в файле: {position} bytes')

asyncio.run(main())



import asyncio
import aiofiles

async def truncate_file():
    async with aiofiles.open('test.txt', mode='a+') as f:
        await f.write('Hello, world!')
        await f.flush()         # Асинхронно сбрасываем буфер записи файла, чтобы убедиться, что все данные записаны на диск.
        await f.seek(0)         # Асинхронно перемещаем позицию в файле в начало файла.
        print(await f.read())   # Асинхронно читаем все данные из файла и выводим их на экран. Ожидается вывод 'Hello, world!'.
        await f.seek(0)         # Асинхронно перемещаем позицию в файле в начало файла снова.
        await f.truncate(5)     # Асинхронно обрезаем файл до первых 5 байт.
        await f.seek(0)         # Асинхронно перемещаем позицию в файле в начало файла снова.
        print(await f.read())   # Асинхронно читаем все данные из файла и выводим их на экран. Теперь ожидается вывод 'Hello', так как мы обрезали файл до первых 5 байт.

asyncio.run(truncate_file())



import asyncio
import aiofiles
import os

words = [
        'дом', 'море', 'солнце', 'небо', 'лес', 'река', 'гора', 'птица',
        'цветок', 'жизнь',
        'любовь', 'работа', 'друг', 'снег', 'вода', 'ветер', 'огонь', 'поля',
        'города', 'день',
        'ночь', 'мост', 'улица', 'поезд', 'парк', 'здание', 'площадь', 'дождь',
        'собака', 'кошка',
        'свет', 'тень', 'игра', 'песок', 'книга', 'город', 'песня', 'звезда',
        'механизм', 'автомобиль',
        'поездка', 'путешествие', 'молоко', 'хлеб', 'яйцо', 'фрукт', 'овощ',
        'журнал', 'газета', 'кафе',
        'ресторан', 'рецепт', 'вино', 'чай', 'кофе', 'письмо', 'письменность',
        'рука', 'ноги', 'часы',
        'календарь', 'зеркало', 'стол', 'стул', 'диван', 'шкаф', 'завтрак',
        'обед', 'ужин', 'горы',
        'реки', 'поля', 'море', 'океан', 'пляж', 'солнечный', 'дождливый',
        'ветряный', 'холодный', 'тёплый',
        'лето', 'зима', 'весна', 'осень', 'страна', 'континент', 'планета',
        'звезда', 'галактика', 'космос',
        'мир', 'человек', 'семья', 'родители', 'дети', 'сестра', 'брат',
        'дедушка', 'бабушка', 'дядя',
        'тётя', 'кукла', 'игрушка', 'тренировка', 'спорт', 'футбол',
        'баскетбол', 'волейбол', 'тренер', 'спортзал',
        'кухня', 'спальня', 'ванная', 'коридор', 'гараж', 'сад', 'огород',
        'площадка', 'гостинная', 'столовая',
        'интернет', 'телефон', 'компьютер', 'телевизор', 'фильм', 'сериал',
        'новости', 'погода', 'прогноз', 'город',
        'посёлок', 'деревня', 'село', 'улица', 'переулок', 'площадь', 'парк',
        'горы', 'лес', 'пещера', 'водопад',
        'озеро', 'рыба', 'мясо', 'суп', 'бульон', 'пирог', 'пицца', 'паста',
        'салат', 'десерт', 'торт', 'пирожное'
    ]


async def check_word(filename):
    async with aiofiles.open(filename, 'r', encoding='utf-8') as file:
        async for word in file:
            if word.strip() not in words:
                print(filename.split('le_')[-1].strip('.txt')+':', word)
                return


async def main():
    directory = 'D:/Dev/asyncio/files_with_secret_word/'
    tasks = [asyncio.create_task(
        check_word(directory + filename)) for filename in os.listdir(directory)
    ]
    await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

asyncio.run(main())



import asyncio
import aiofiles

input_data = [
    ("Леголас", "Привет всем! Как дела?", 1.33),
    ("Гендальф", "Все готовы к рейду?", 2.61),
    ("Гимли", "Да, я готов. Встретимся у северных ворот.", 0.99),
    ("Арагорн", "Буду через 5 минут.", 4.56),
    ("Фродо", "Кто-нибудь видел Голлума?", 3.78),
    ("Боромир", "Нужно больше золота для нашей армии.", 5.12),
    ("Голлум", "Моя прелесть близко...", 2.22),
    ("Галадриэль", "Будьте осторожны, враг не дремлет.", 1.95),
    ("Элронд", "Собираемся у Великого Древа.", 7.34),
    ("Саурон", "Скоро всё будет моим!", 6.67),
    ("Леголас", "У меня стрелы кончаются, нужна помощь.", 8.35),
    ("Гендальф", "Помните, только свет может победить тьму.", 4.02),
    ("Гимли", "Защитим наших товарищей до последнего!", 0.32),
    ("Арагорн", "Пора выступать, дальше ждать нельзя.", 9.44),
    ("Фродо", "Кольцо всё ещё со мной, идём к Роковой горе.", 2.95),
    ("Боромир", "Держитесь вместе, не распадайтесь.", 3.01),
    ("Голлум", "Хозяин, мы так близко...", 1.67),
    ("Галадриэль", "Не забывайте о мудрости старших.", 6.18),
    ("Элронд", "Армия приближается, готовьтесь.", 0.46),
    ("Саурон", "Мои легионы неостановимы.", 5.75),
    ("Леголас", "Ещё одно пополнение в наши ряды!", 7.78),
    ("Гендальф", "Никогда не сдавайтесь!", 9.12),
    ("Гимли", "А где же пиво?", 8.01),
    ("Арагорн", "Время пришло, вперёд!", 4.63),
    ("Фродо", "Я устал, но должен идти дальше.", 1.48),
    ("Боромир", "Засада! Будьте на чеку.", 2.29),
    ("Голлум", "Путь всё ещё опасен.", 3.49),
    ("Галадриэль", "Вера и надежда — наши главные союзники.", 6.02),
    ("Элронд", "Эльфы идут с вами.", 9.76),
    ("Саурон", "Я чувствую ваше присутствие, герои.", 0.85),
    ("Леголас", "Заметил врага на горизонте.", 4.88),
    ("Гендальф", "Пусть удача будет на нашей стороне.", 3.55),
    ("Гимли", "Кто не выпьет за победу?", 7.11),
    ("Арагорн", "За мной! Впереди враг.", 5.89),
    ("Фродо", "Нам нужно идти, времени мало.", 1.11),
    ("Боромир", "Щиты наготове, держите строй!", 8.43),
    ("Голлум", "Пещеры безопасны.", 2.76),
    ("Галадриэль", "Сила света всегда с нами.", 6.45),
    ("Элронд", "Древние земли ждут нас.", 9.04),
    ("Саурон", "Моя армия готова к атаке.", 4.41),
    ("Леголас", "Сквозь лес идут орки.", 7.55),
    ("Гендальф", "Нам предстоит долгая ночь.", 1.72),
    ("Гимли", "Поддержите огонь в кузницах.", 3.83),
    ("Арагорн", "Мы сражаемся за свободу!", 2.09),
    ("Фродо", "Кольцо становится тяжелее.", 6.98),
    ("Боромир", "Битва только начинается.", 5.37),
    ("Голлум", "Тайные тропы приведут нас.", 0.74),
    ("Галадриэль", "Вера в победу делает нас сильнее.", 9.31),
    ("Элронд", "Подготовьте луки.", 7.67),
    ("Саурон", "Вперед, мои воины!", 8.66),
    ("Леголас", "Мы окружены.", 4.24),
    ("Гендальф", "Пусть ветер дует нам навстречу.", 1.56),
    ("Гимли", "Кто украл мою секиру?", 3.19),
    ("Арагорн", "Тень сгущается над миром.", 2.88),
    ("Фродо", "Я чувствую холод...", 7.41),
    ("Боромир", "Защитим нашего носителя кольца.", 5.49),
    ("Голлум", "Мы в опасности.", 9.97),
    ("Галадриэль", "Прислушайтесь к звукам леса.", 6.23),
    ("Элронд", "Это наш последний шанс.", 4.13),
    ("Саурон", "Я вернусь...", 0.92),
    ("Леголас", "Вижу свет впереди.", 3.67),
    ("Гендальф", "Вперед, без страха!", 2.46),
    ("Гимли", "За гномов!", 1.81),
    ("Арагорн", "Мы сражаемся вместе.", 7.89),
    ("Фродо", "Я почти у цели.", 6.12),
    ("Боромир", "Никто не пройдет через нас.", 9.21),
    ("Голлум", "Они не найдут нас.", 8.94),
    ("Галадриэль", "Держитесь за надежду.", 5.67),
    ("Элронд", "Лучи солнца приведут нас.", 4.99),
    ("Саурон", "Моя сила растет.", 2.38),
    ("Леголас", "Я вижу всё.", 1.19),
    ("Гендальф", "Мудрость - наш лучший меч.", 3.33),
    ("Гимли", "Мы пройдем через эти горы.", 8.12),
    ("Арагорн", "Вместе мы сильнее.", 5.56),
    ("Фродо", "Кажется, кольцо сгорает.", 9.55),
    ("Боромир", "Стены не удержат нас.", 7.22),
    ("Голлум", "Моя прелесть...", 6.56),
    ("Галадриэль", "Свет восходит.", 0.58),
    ("Элронд", "Мы победим.", 4.76),
    ("Саурон", "Тьма вечна.", 1.87)
]

async def write_log(filename):
    player_name, message, delay = filename
    await asyncio.sleep(delay)
    async with aiofiles.open('myfile.txt', 'a', encoding='windows-1251') as file:
        await file.write(f"{delay:.2f}: {player_name}: {message}\n")


async def main():
    tasks = [asyncio.create_task(write_log(filename)) for filename in input_data]
    await asyncio.gather(*tasks)

asyncio.run(main())
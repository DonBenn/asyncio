import asyncio

import aiofiles.os as aos

async def print_file_info(file_path):
    file_info = await aos.stat(file_path)
    print(file_info)


asyncio.run(print_file_info('myfile.txt'))



import aiofiles.os as aos
import asyncio

async def rename_file(old_name, new_name):
    await aos.rename(old_name, new_name)


asyncio.run(rename_file('old_name.txt', 'new_name.txt'))



import os
import aiofiles.os as aos
import asyncio

async def rename_file(src: str, dst: str):
    dst_dir = os.path.dirname(dst)

    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    await aos.rename(src, dst)

asyncio.run(rename_file('old_dir/old_file.txt', 'new_dir/new_file.txt'))



import aiofiles.os as aos
import asyncio

async def renames_file(old_name, new_name):
    await aos.renames(old_name, new_name)


asyncio.run(renames_file('old_dir/old_name.txt', 'new_dir/new_name.txt'))



import aiofiles.os as aos
import asyncio

async def replace_file(old_name, new_name):
    await aos.replace(old_name, new_name)

asyncio.run(replace_file('old_name.txt', 'new_name.txt'))



import aiofiles.os as aos
import asyncio

async def remove_file(path):
    await aos.remove(path)

asyncio.run(remove_file('file_to_remove.txt'))



import aiofiles.os as aos
import asyncio

async def unlink_file(path):
    await aos.unlink(path)

asyncio.run(unlink_file('file_to_unlink.txt'))



import aiofiles.os as aos
import asyncio

async def create_dir(path):
    await aos.mkdir(path)

asyncio.run(create_dir('new_directory'))



import os
import aiofiles.os as aos
import asyncio

async def create_dir(path):
    if not os.path.exists(path):
        await aos.mkdir(path)
    else:
        print(f"Директория {path} уже существует.")

asyncio.run(create_dir('new_directory'))



import aiofiles.os as aos
import asyncio

async def create_nested_dirs(path):
    await aos.makedirs(path)

asyncio.run(create_nested_dirs('dir/sub_dir/sub_sub_dir'))



import aiofiles.os as aos
import asyncio

async def create_dir(path):
    await aos.mkdir(path)

asyncio.run(create_dir('relative_directory'))
# asyncio.run(create_dir('/absolute/path/to/directory'))



import aiofiles.os as aos
import asyncio

async def create_dir(path):
    await aos.makedirs(path, exist_ok=True)

asyncio.run(create_dir('dir/subdir/subsubdir'))



import aiofiles.os as aos
import asyncio

async def remove_dir(path):
    await aos.rmdir(path)

asyncio.run(remove_dir('dir_to_remove'))



import os
import aiofiles.os as aos
import asyncio

async def safe_remove_dir(path):
    with os.scandir(path) as entries:
        if not any(entries):  # Если в директории нет элементов
            await aos.rmdir(path)
        else:
            print(f"Directory {path} is not empty.")

asyncio.run(safe_remove_dir('dir_to_remove'))



import aiofiles.os as aos
import asyncio

async def remove_empty_dirs(path):
    await aos.removedirs(path)

asyncio.run(remove_empty_dirs('dir/subdir/subsubdir'))



import aiofiles.os as aos
import asyncio

async def create_link(src, dst):
    await aos.link(src, dst)

asyncio.run(create_link('source.txt', 'link.txt'))



import aiofiles.os as aos
import asyncio

async def create_symlink(source_path, link_path):
    await aos.symlink(source_path, link_path)

asyncio.run(create_symlink('source.txt', 'link_to_source.txt'))



import aiofiles.os as aos
import asyncio

async def read_symlink(link_path):
    return await aos.readlink(link_path)

source = asyncio.run(read_symlink('link_to_source.txt'))
print(source)
# source.txt



import aiofiles.os as aos
import asyncio

async def list_directory_contents(path):
    contents = await aos.listdir(path)
    print(contents)

asyncio.run(list_directory_contents('D:/Dev/asyncio'))



import os
import asyncio
import aiofiles.os as aos

async def check_access(path):
    if await aos.access(path, os.R_OK):
        print(f'Файл {path} доступен для чтения.')
    else:
        print(f'Файл {path} не доступен для чтения.')


asyncio.run(check_access('"D:/Dev/asyncio/link.txt"'))



import asyncio
import aiofiles
import aiocsv

async def read_csv_file():
    async with aiofiles.open("doctors.csv", mode="r", encoding="utf-8", newline="") as afp:
        reader = aiocsv.AsyncReader(afp)
        async for row in reader:
            print(row)

asyncio.run(read_csv_file())



import aiocsv
import csv
import asyncio
import aiofiles

class CustomDialect(csv.Dialect):
    delimiter = ';'                 # Определяет символ-разделитель столбцов в csv файле как ";"
    quotechar = '"'                 # Определяет символ кавычек, используемый для обрамления полей в csv файле, как двойные кавычки ("")
    doublequote = True              # Если этот параметр True, две кавычки внутри поля трактуются как одна кавычка
    skipinitialspace = True         # Если параметр True, пробелы в начале каждого поля игнорируются
    lineterminator = '\n'           # Определяет символ окончания строки в csv файле как "\n"
    quoting = csv.QUOTE_MINIMAL     # Указывает, что кавычки должны окружать только те поля, которые содержат специальные символы (например, разделитель, кавычки или любой из символов новой строки)

csv.register_dialect('customDialect', CustomDialect) # Регистрирует диалект с именем 'customDialect' для последующего использования в csv.reader или csv.writer

async def read_csv_file():
    async with aiofiles.open('file.csv', mode='r') as f:
        reader = aiocsv.AsyncReader(f, dialect='customDialect')
        async for row in reader:
            print(row)

asyncio.run(read_csv_file())



import asyncio
from aiocsv import AsyncDictReader
import aiofiles

async def main():
    # 'utf-8-sig' - это кодировка UTF-8 с префиксом BOM (byte order mark), который может быть использован для определения порядка байтов в текстовых файлах.
    async with aiofiles.open('doctors.csv', mode='r', encoding='utf-8-sig') as afp:
        reader = AsyncDictReader(afp, fieldnames=[
            'Name', 'Surname', 'Age', 'Faculty', 'Average_Grade', 'Defunct_title'],
                                 delimiter=";", restval='N/A'
                                 )
        async for row in reader:
            print(row)

asyncio.run(main())



import asyncio
import aiofiles
from aiocsv import AsyncWriter

async def write_csv_file():
    async with aiofiles.open("new_file.csv", mode="w", encoding="utf-8", newline="") as afp:
        writer = AsyncWriter(afp)
        # await writer.writerows([
        #     ["John", 26],
        #     ["Sasha", 42],
        #     ["Hana", 37]
        # ])
        await writer.writerows([
            ["Name", "Age", "Hobbies"],
            ["John", 26, ["Basketball", "Football"]],
            ["Sasha", 42, ["Reading", "Swimming"]],
            ["Hana", 37, ["Cooking", "Hiking"]]
        ])

asyncio.run(write_csv_file())



import csv
import asyncio
import aiofiles
from aiocsv import AsyncWriter


class CustomDialect(csv.Dialect):
    delimiter = '+'
    quotechar = '/'
    doublequote = False
    skipinitialspace = False
    lineterminator = '\n'
    quoting = csv.QUOTE_MINIMAL

csv.register_dialect('customDialect', CustomDialect)

async def main():
    async with aiofiles.open("test_Dialect.csv", mode="w", encoding="utf-8", newline="") as afp:
        writer = AsyncWriter(afp, dialect='customDialect')
        data = [["Column1", "Column2", "Column3", "Column4", "Column5"]]
        data += [["Data1", "Data2", "Data3", "Data4", f'{str(i)}'] for i in range(1, 101)]
        for row in data:
            await writer.writerow(row)

asyncio.run(main())



import aiofiles
from aiocsv import AsyncDictWriter
import asyncio

async def write_csv_rows():
    async with aiofiles.open('output.csv', mode='w', newline='') as file:
        # Создает экземпляр AsyncDictWriter, который будет записывать данные в файл, преобразуя каждый словарь в строку CSV.
        # Ключи словаря соответствуют полям CSV файла ("Name", "Age", "City").
        writer = AsyncDictWriter(file, fieldnames=["Name", "Age", "City"],)

        # Асинхронно записывает заголовки в файл CSV. Этот метод используется для создания первой строки файла,
        # которая содержит названия полей.
        await writer.writeheader()

        # Определяет список словарей, каждый из которых будет записан в файл как отдельная строка.
        rows = [
            {"Name": "John", "Age": 30, "City": "New York"},
            {"Name": "Jane", "Age": 25, "City": "Los Angeles"},
            {"Name": "Bob", "Age": 35, "City": "Chicago"},
        ]

        # Асинхронно записывает все строки (словари) из списка rows в файл CSV.
        await writer.writerows(rows)

asyncio.run(write_csv_rows())



import asyncio
import aiofiles
from aiocsv import AsyncReader

async def main():
    async with aiofiles.open("property_data_130000.csv", mode="r", encoding="utf-8", newline="") as afp:
        async for row in AsyncReader(afp):
            print(row)

asyncio.run(main())



import asyncio
import aiofiles
from aiocsv import AsyncReader
from datetime import datetime

async def print_row(row):
    print(f"Row: {row}")

async def print_time():
    print(f"Current Time: {datetime.now()}")

async def main():
    async with aiofiles.open("property_data_130000.csv", mode="r", encoding="utf-8", newline="") as afp:
        async for row in AsyncReader(afp):
            await print_row(row)
            await print_time()

asyncio.run(main())



import asyncio
import os
import glob  # используется для получения списка файлов, которые соответствуют определенному шаблону.
import aiofiles
from datetime import datetime


async def process_csv_file(file_path):
    async with aiofiles.open(file_path, mode='r', encoding='utf-8-sig') as file:
        lines = await file.readlines()

        for line_number, line in enumerate(lines, start=1):
            await asyncio.sleep(0.1)
            current_time = await print_current_time()
            print(f"File: {file_path}\nNumber_line: {line_number}\nLine: {line.strip()}")
            print(current_time)


async def print_current_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"Current Time: {current_time}\n"


async def scan_and_process_csv_files(folder_path):
    # Получаем список всех CSV файлов в папке
    csv_files = glob.glob(os.path.join(folder_path, "*.csv"))

    tasks = [process_csv_file(file_path) for file_path in csv_files]
    await asyncio.gather(*tasks)


async def main():
    folder_path = r"D:\Dev\asyncio\car_example1\car_example1"
    await scan_and_process_csv_files(folder_path)


asyncio.run(main())
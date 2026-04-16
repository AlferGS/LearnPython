# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 18:15:45 2026

@author: Andrey
"""

import os
import zipfile

# %%
# =============================================================================

# Задача 1: Создание архива
# Напишите функцию, которая:
#
# Создает ZIP архив backup.zip
# Добавляет в него все файлы из папки test_folder/ (включая подпапки)
# Использует сжатие ZIP_DEFLATED
# Выводит список добавленных файлов
#
# =============================================================================


def task_1():
    # create zip backup
    with zipfile.ZipFile(
        "backup.zip", "w", compression=zipfile.ZIP_DEFLATED
    ) as archive:
        here = os.path.dirname(os.path.abspath(__file__))
        dir_path = os.path.join(here, "test_folder")
        filenames = []

        for root, dirs, files in os.walk(dir_path):
            for file in files:
                full_path = os.path.join(root, file)
                arcname = os.path.relpath(full_path, start=dir_path)
                filenames.append(file)
                archive.write(full_path, arcname)
            if not files and not dirs:
                folder_arc = os.path.relpath(root, start=dir_path) + "/"
                # print(folder_arc)
                archive.writestr(folder_arc, "")

        print(", ".join(filenames))
    pass


task_1()

# %%
# =============================================================================
# ⭐⭐ Задача 2: Просмотр содержимого архива
# Напишите функцию, которая:
#
# Открывает архив backup.zip
# Выводит список всех файлов с их размерами
# Показывает общий размер архива
# Выводит количество файлов в архиве
#
# =============================================================================


def task_2():
    with zipfile.ZipFile("backup.zip", "r") as archive:
        for info in archive.infolist():
            print(info.filename, " - ", f"{info.file_size} bit", sep="")
        print(f"количество файлов в архиве: {len(archive.infolist())}")
    pass


task_2()

# %%
# =============================================================================
# ⭐⭐ Задача 3: Извлечение по расширению
# Напишите функцию, которая:
#
# Открывает архив backup.zip
# Извлекает только .txt файлы в папку extracted_txt/
# Сохраняет структуру подпапок
# Выводит количество извлеченных файлов
#
# =============================================================================


def task_3():
    with zipfile.ZipFile("backup.zip", "r") as archive:
        counter = 0
        for name in archive.namelist():
            if name.endswith(".txt"):
                print(name)
                counter += 1
                archive.extract(name, path="extracted_txt")

        print(f"Количество извлеченных файлов .txt: {counter}")

    pass


task_3()
# %%
# =============================================================================
# ⭐⭐⭐ Задача 4: Добавление файлов в существующий архив
# Напишите функцию, которая:
#
# Открывает существующий архив backup.zip в режиме добавления
# Создает новый файл new_file.txt со случайным содержимым
# Добавляет его в архив
# Не удаляет и не перезаписывает существующие файлы
#
# =============================================================================


def task_4():
    with zipfile.ZipFile("backup.zip", "a") as archive:
        if "new_file.txt" not in archive.namelist():
            archive.writestr("new_file.txt", "data" * 50)
            print("new file")
        else:
            print("file are exist")
    pass


task_4()
# %%
# =============================================================================
# ⭐⭐⭐ Задача 5: Поиск файлов в архиве
# Напишите функцию, которая:
#
# Принимает название архива и поисковый запрос (строку)
# Ищет в архиве файлы, содержащие этот запрос в имени
# Для найденных файлов показывает:
# - Имя файла
# - Размер
# - Степень сжатия
# Возвращает список найденных файлов
#
# =============================================================================


def task_5(arc_name: str, search_str: str):
    search_list = search_str.strip().split()
    result_list = []

    with zipfile.ZipFile(arc_name, "r") as archive:
        for info in archive.infolist():
            name = os.path.basename(info.filename)

            if name in search_list:
                ratio = (
                    (1 - info.compress_size / info.file_size) * 100
                    if info.file_size > 0
                    else 0
                )
                print(f"""\n{name}, 
{info.file_size} байт, 
{round(ratio)}% сжатия""")
                result_list.append(name)

    print(f"\nСписок найденных файлов: {result_list}")

    pass


task_5("backup.zip", "file3.txt file2.txt")

# %%
# =============================================================================
# ⭐⭐⭐⭐ Задача 6: Распаковка с преобразованием
# Напишите функцию, которая:
#
# Открывает архив backup.zip
# Читает содержимое каждого .txt файла без извлечения на диск
# Подсчитывает в каждом файле:
# - Количество строк
# - Количество слов
# - Количество символов
# Сохраняет результаты в CSV файл analysis.csv
# Выводит статистику на экран
#
# =============================================================================


def task_6():
    data = []
    with zipfile.ZipFile("backup.zip", "r") as archive:
        for info in archive.infolist():
            if info.filename.endswith(".txt"):
                with archive.open(info.filename) as file:
                    content = file.read().decode("utf-8")

                    lines = content.count("\n") + 1 if content else 0
                    words = len(content.split())
                    chars = len(content)

            data.append(
                {
                    "filename": os.path.basename(info.filename),
                    "lines": lines,
                    "words": words,
                    "chars": chars,
                }
            )

    import csv

    with open("analysis.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, ["filename", "lines", "words", "chars"])
        writer.writeheader()
        for value in data:
            writer.writerow(value)

    print("Результаты:")
    for value in data:
        print(f"""
filename: {value["filename"]}
lines: {value["lines"]}
words: {value["words"]}
chars: {value["chars"]}
              """)

    pass


task_6()

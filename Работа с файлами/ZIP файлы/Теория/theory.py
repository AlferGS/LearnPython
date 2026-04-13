import zipfile
from datetime import datetime


def task_1():
    with zipfile.ZipFile("archive.zip", "r") as file:
        file_list = file.namelist()

        print("Содержимое архива:")
        for line in file_list:
            print(line)

        for info in file.infolist():
            print(
                f"Файл: {info.filename}, Размер: {info.file_size} байт, Сжат: {info.compress_size} байт"
            )


def task_2():
    with zipfile.ZipFile("archive.zip", "r") as zip_file:
        # Извлечь один файл
        zip_file.extract("students_txt.txt", path="extracted/")

        # Извлечь все файлы
        zip_file.extractall(path="all_extracted/")

        # Извлечь файлы по шаблону
        for file_name in zip_file.namelist():
            if file_name.endswith(".txt"):
                zip_file.extract(file_name, path="txt_files/")


def task_3():
    with zipfile.ZipFile("archive.zip", "r") as zip_file:
        # Читаем содержимое конкретного файла
        with zip_file.open("students_txt.txt") as file:
            content = file.read().decode("utf-8")
            print(content)

        # Читаем все текстовые файлы
        for file_name in zip_file.namelist():
            if file_name.endswith(".txt"):
                with zip_file.open(file_name) as file:
                    content = file.read().decode("utf-8")
                    print(f"--- {file_name} ---")
                    print(content)


def task_4():
    with zipfile.ZipFile("generated.zip", "w") as zip_file:
        # Добавляем файл из строки
        zip_file.writestr(
            "readme.txt", "Это содержимое файла, созданное программно"
        )

        # Добавляем JSON данные
        import json

        data = {"name": "Анна", "age": 25}
        zip_file.writestr("data.json", json.dumps(data, ensure_ascii=False))

        # Добавляем с информацией о времени
        info = zipfile.ZipInfo(
            "log.txt", date_time=datetime.now().timetuple()[:6]
        )
        zip_file.writestr(info, "Лог-запись")


def check_zip_integrity(zip_path):
    try:
        with zipfile.ZipFile(zip_path, "r") as zip_file:
            # Проверяем каждый файл
            bad_files = zip_file.testzip()
            if bad_files:
                print(f"Поврежденные файлы: {bad_files}")
            else:
                print("Архив цел и не поврежден")
    except zipfile.BadZipFile:
        print("Файл не является ZIP архивом или поврежден")


def file_info():
    with zipfile.ZipFile("archive.zip", "r") as zip_file:
        for info in zip_file.infolist():
            # Вычисляем степень сжатия вручную
            if info.file_size > 0:
                compress_rate = (1 - info.compress_size / info.file_size) * 100
            else:
                compress_rate = 0
            print(f"Файл: {info.filename}")
            print(f"  Оригинальный размер: {info.file_size} байт")
            print(f"  Сжатый размер: {info.compress_size} байт")
            print(f"  Степень сжатия: {compress_rate:.1f}%")
            print(f"  Дата изменения: {datetime(*info.date_time)}")
            print(f"  CRC32: {hex(info.CRC)}")
            print()


task_4()
check_zip_integrity("archive.zip")
file_info()

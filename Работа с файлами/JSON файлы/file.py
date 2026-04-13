# -*- coding: utf-8 -*-
# =============================================================================
#
# Created on Tue Apr  7 16:54:28 2026
#
# @author: Andrey
#
# =============================================================================
import json

# =============================================================================
# %% 📚 Задача 1: Загрузка и базовый анализ

# Напишите функцию, которая:
# 1) Загружает JSON файл (university.json)
# 2) Выводит основную информацию:
#   a) Название университета, год основания
#   b) Список факультетов
#   c) Общее количество студентов
#   d) Количество студентов на каждом факультете
# 3) Сохраняет эту статистику в файл university_stats.json


def task_1():
    new_data = dict()
    with open("university.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        print(
            f"{data['university']['name']} был основан в {
                data['university']['founded']
            } году."
        )
        print("Включает в себя факультеты:")
        for i, department in enumerate(
            data["university"]["departments"], start=1
        ):
            print(
                f"\t{i}) {department['name']} ({
                    department['id']
                }) - Руководитель: {department['head']}"
            )

        student_count = len(data["students"])
        new_data["university"] = {
            "name": data["university"]["name"],
            "founded": data["university"]["founded"],
            "departments": [],
            "total_student_count": student_count,
        }

        print(f"\nВ университете числится {student_count} студентов.")
        print("Количество студентов на каждом из факультетов:")
        for department in data["university"]["departments"]:
            student_per_department = len(
                [
                    x
                    for x in data["students"]
                    if x["department"] == department["id"]
                ]
            )
            new_data["university"]["departments"].append(
                {
                    "id": department["id"],
                    "name": department["name"],
                    "students_count": student_per_department,
                }
            )
            print(f"\t{department['name']} - {student_per_department} чел.")

    with open("university_stats.json", "w", encoding="utf-8") as file:
        json.dump(new_data, file, indent=4, ensure_ascii=False)


task_1()

# %% 📚 Задача 2: Поиск и фильтрация студентов

# Напишите функцию, которая принимает критерии поиска и возвращает список
# студентов, удовлетворяющих условиям:
#   Параметры:
#   min_age — минимальный возраст
#   department — факультет (опционально)
#   min_average_score — минимальный средний балл
#
# Функция должна возвращать список студентов с их средним баллом,
# отсортированных по убыванию среднего балла.
# Пример использования:
#
# result = task_2(min_age=20, department="CS", min_average_score=75)
# Должен вернуть студентов CS факультета старше 20 лет со средним баллом > 75


def task_2(min_age, min_average_score, department=None):
    student_list = list()
    with open("university.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        for student in data["students"]:
            subject_score_sum = sum(
                subject["score"] for subject in student["grades"]
            )
            subject_count = len(student["grades"])
            avg_score = round(subject_score_sum / subject_count, 1)
            if (
                student["age"] >= min_age
                and (department is None or student["department"] == department)
                and avg_score >= min_average_score
            ):
                student_list.append((student["name"], avg_score))
    student_list = sorted(student_list, key=lambda x: -x[1])
    return student_list


result = task_2(min_age=19, min_average_score=75)
for student in result:
    print(f"{student[0]}: {student[1]}")


# %% 📚 Задача 3: Анализ успеваемости по факультетам

# Создайте функцию, которая генерирует отчет по успеваемости для каждого
# факультета.
# Отчет должен содержать:
#   1) Название факультета
#   2) Количество студентов
#   3) Средний балл по факультету (по всем предметам всех студентов)
#   4) Лучший предмет на факультете (с наибольшим баллом)
#   5) Худший предмет на факультете
#   6) Список отличников (средний балл >= 85)
#
# Результат сохраните в файл department_report.json.


def task_3():
    result_data = {"departments": []}
    with open("university.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        for department in data["university"]["departments"]:
            student_list = [
                student
                for student in data["students"]
                if student["department"] == department["id"]
            ]
            total_score = 0
            min_score, max_score = 100, 0
            min_score_name = max_score_name = ""
            for student in student_list:
                grade_score = 0
                for grade in student["grades"]:
                    if grade["score"] > max_score:
                        max_score = grade["score"]
                        max_score_name = grade["subject"]
                    if grade["score"] < min_score:
                        min_score = grade["score"]
                        min_score_name = grade["subject"]
                    grade_score += grade["score"]
                total_score += grade_score / len(student["grades"])

            department_stats = dict()
            department_stats["id"] = department["id"]
            department_stats["name"] = department["name"]
            department_stats["student_count"] = len(student_list)
            department_stats["avg_score"] = round(
                total_score / len(student_list), 1
            )
            department_stats["best_grade"] = max_score_name
            department_stats["worst_grade"] = min_score_name
            department_stats["best_students"] = [
                student["name"]
                for student in student_list
                if sum(grade["score"] for grade in student["grades"])
                / len(student["grades"])
                >= 85
            ]
            result_data["departments"].append(department_stats)

    with open("department_report.json", "w", encoding="utf-8") as file:
        json.dump(result_data, file, indent=4, ensure_ascii=False)

    return result_data


task_3()

# %% 📚 Задача 4: Добавление и обновление данных

# Создайте функции для управления данными студентов:
# add_student(student_data) — добавляет нового студента (генерирует новый id)
# update_student_grades(student_id, new_grades) — обновляет оценки студента
# delete_student(student_id) — удаляет студента по id
#
# Все изменения должны сохраняться в файл.


def copy_in_file(filename, new_filename):
    """Create copy of file in new file"""
    with open(filename, "r", encoding="utf-8") as inp_file:
        with open(new_filename, "w", encoding="utf-8") as out_file:
            json.dump(
                json.load(inp_file), out_file, indent=4, ensure_ascii=False
            )
    pass


def add_student(student_data):
    """Add student_data to "university_copy.json".
    Add "id" to new student_data, and upload to file in "students" list
    Result dump in file.
    """
    data = dict()
    with open("university_copy.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    if len(data["students"]) > 0:
        student_data = {"id": data["students"][-1]["id"] + 1, **student_data}
    else:
        student_data = {"id": 1, **student_data}

    data["students"].append(student_data)

    with open("university_copy.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    pass


def update_student_grades(student_id, new_grades):
    """Search student in "students" list by "id" and change "grades" list
    for the student object. Result dump in file.
    """
    data = dict()
    flag = False
    with open("university_copy.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    for student in data["students"]:
        if student["id"] == student_id:
            student["grades"] = new_grades
            flag = True
            break

    with open("university_copy.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print(
        "Incorrect student_id. Student not found."
        if flag == False
        else "Student grades were updated."
    )

    pass


def delete_student(student_id):
    """Search student in "students" list by "id" and delete it from list.
    Result dump in file.
    """
    data = dict()
    with open("university_copy.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    student_list = list()
    for student in data["students"]:
        if student["id"] != student_id:
            student_list.append(student)

    data["students"] = student_list

    with open("university_copy.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    pass


def task_4():
    copy_in_file("university.json", "university_copy.json")
    student_data = {
        "name": "Петр Гланц",
        "age": 22,
        "department": "MATH",
        "year": 3,
        "grades": [
            {
                "subject": "Математический анализ",
                "score": 88,
                "date": "2025-01-17",
            },
            {"subject": "Линейная алгебра", "score": 81, "date": "2025-01-21"},
            {
                "subject": "Дискретная математика",
                "score": 93,
                "date": "2025-01-24",
            },
        ],
    }
    new_grades = [
        {
            "subject": "Математический анализ",
            "score": 91,
            "date": "2025-01-13",
        },
        {"subject": "Линейная алгебра", "score": 88, "date": "2025-01-23"},
        {
            "subject": "Дифференциальные уравнения",
            "score": 71,
            "date": "2025-02-01",
        },
    ]

    add_student(student_data)

    update_student_grades(3, new_grades)

    delete_student(6)

    pass


task_4()

# %% 📚 Задача 5: Экспорт в различные форматы

# Создайте функции для экспорта данных:
# export_to_csv() — экспортирует список студентов с их средними баллами в CSV
# export_to_txt() — создает текстовый отчет в читаемом формате


def export_to_csv():
    """
    Export "students" list from JSON file to CSV.

    Returns
    -------
    None
    """
    import csv

    with open("university.json", "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
        fieldnames = list()

        if data["students"]:
            fieldnames = data["students"][0].keys()
        else:
            return "'students' are empty"

        with open(
            "students_csv.csv", "w", newline="", encoding="utf-8"
        ) as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

            for student in data["students"]:
                writer.writerow(student)

    with open("students_csv.csv", "r", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(*row.values())

    pass


def export_to_txt():
    """
    Export "students" list from JSON file to summary TXT.

    Returns
    -------
    None
    """
    with open("university.json", "r", encoding="utf-8") as json_file:
        data = json.load(json_file)

        if not data["students"]:
            return "'students' are empty"

        with open(
            "students_txt.txt", "w", newline="", encoding="utf-8"
        ) as txt_file:
            txt_file.write("Students:\n")

            for student in data["students"]:
                txt_file.write(f"""\nid - {student["id"]}
name - {student["name"]}
age - {student["age"]}
department - {student["department"]}
year - {student["year"]}
grades:
""")
                for grade in student["grades"]:
                    txt_file.write(f"""\tsubject - {grade["subject"]}
\tscore - {grade["score"]}
\tdate - {grade["date"]}
""")

    with open("students_txt.txt", "r", encoding="utf-8") as txt_file:
        for line in txt_file:
            print(line)

    pass


def task_5():
    print("task_5:\nexport_to_csv")
    export_to_csv()
    print("export_to_txt")
    export_to_txt()
    pass


task_5()

# %% 📚 Задача 6: Слияние данных из нескольких источников

# Создайте функцию, которая объединяет данные из двух JSON файлов:
# Допустим, есть второй файл new_students.json с новыми студентами и
# обновленной информацией о существующих.
# Правила слияния:
#   a) Если студент с таким id существует — обновить его данные
#   b) Если нет — добавить нового
#   c) При конфликте данных приоритет у нового файла

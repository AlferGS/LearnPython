from tabulate import tabulate
import pandas as pd
import csv
from pathlib import Path

# %% Уровень 1

# Задача 1.1
""" Создайте файл students.csv и запишите в него данные из students.txt.
Прочитайте файл students.csv и выведите на экран содержимое построчно.
"""


def task_1_1():
    txt_filename = "students.txt"
    csv_filename = "students.csv"

    with open(txt_filename, "r", encoding="utf-8") as input_file:
        with open(
            csv_filename, "w", encoding="utf-8", newline=""
        ) as output_file:
            writer = csv.writer(output_file)
            for line in input_file:
                writer.writerow(line.strip().split(","))

    with open(csv_filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        print("task_1_1:")
        for line in reader:
            print(*line)


print("-" * 40)
task_1_1()

# Задача 1.2
# Используя csv.DictReader, выведите имена всех студентов.


def task_1_2():
    filename = "students.csv"
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        print("task_1_2:")
        for line in reader:
            print(line["name"])


print("-" * 40)
task_1_2()

# Задача 1.3
# Подсчитайте и выведите количество студентов в файле.


def task_1_3():
    filename = "students.csv"
    counter = 0
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for line in reader:
            counter += 1

    print(f"task_1_3 = {counter}")


print("-" * 40)
task_1_3()

# Задача 1.4
""" Создайте новый файл names_only.csv, содержащий только столбец name 
из исходного файла.
"""


def task_1_4():
    filename = "students.csv"
    with open(filename, "r", encoding="utf-8") as studets_file:
        reader = csv.DictReader(studets_file)
        with open(
            "names_only.csv", "w", encoding="utf-8", newline=""
        ) as names_file:
            writer = csv.writer(names_file)
            writer.writerow(["names"])
            for line in reader:
                writer.writerow([line["name"]])

    with open("names_only.csv", "r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)
        print("task_1_4:")
        for line in reader:
            print(line)


print("-" * 40)
task_1_4()

# Задача 1.5
""" Добавьте в исходный файл новую запись о студенте (придумайте сами) 
и сохраните изменения."""


def task_1_5():
    filename = "students.csv"
    with open(filename, "a", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file, fieldnames=["name", "age", "grade", "city", "score"]
        )
        writer.writerow(
            {
                "name": "Антось",
                "age": 22,
                "grade": 4,
                "city": "Минск",
                "score": 78,
            }
        )


print("-" * 40)
task_1_5()

# %% Уровень 2: Фильтрация и поиск
# Задача 2.1
# Выведите всех студентов из Москвы.


def task_2_1():
    with open("students.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        print("task_2_1:")
        for line in reader:
            if line["city"] == "Москва":
                print(*line.values())


print("-" * 40)
task_2_1()

# Задача 2.2
# Найдите и выведите студентов с оценкой 5 (отлично).


def task_2_2():
    with open("students.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        print("task_2_2:")
        for line in reader:
            if int(line["grade"]) == 5:
                print(*line.values())


print("-" * 40)
task_2_2()

# Задача 2.3
# Выведите студентов старше 20 лет.


def task_2_3():
    with open("students.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        print("task_2_3:")
        for line in reader:
            if int(line["age"]) > 20:
                print(*line.values())


print("-" * 40)
task_2_3()

# Задача 2.4
# Найдите студента с максимальным баллом (score).


def task_2_4():
    with open("students.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        max_score = next(reader)
        for line in reader:
            if int(line["score"]) > int(max_score["score"]):
                max_score = line
        print(f"task_2_4 = {max_score}")


print("-" * 40)
task_2_4()

# Задача 2.5
# Выведите всех студентов, чей балл выше среднего.


def task_2_5():
    avg_score = 0
    with open("students.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        sum_score = len_reader = 0
        for line in reader:
            sum_score += int(line["score"])
            len_reader += 1

        avg_score = round(sum_score / len_reader)

    with open("students.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        print("task_2_5:")
        for line in reader:
            if int(line["score"]) > avg_score:
                print(line)


print("-" * 40)
task_2_5()

# Задача 2.6
# Найдите и выведите студентов, у которых балл меньше 60 (неудовлетворительно).


def task_2_6():
    with open("students.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        print("task_2_6:")
        for line in reader:
            if int(line["score"]) < 60:
                print(*line.values())


print("-" * 40)
task_2_6()

# %% Уровень 3: Агрегация и статистика
# Задача 3.1
# Подсчитайте средний балл по всем студентам.


def task_3_1():
    with open("students.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        sum_score = len_reader = 0
        for line in reader:
            sum_score += int(line["score"])
            len_reader += 1

        print("task_3_1 =", round(sum_score / len_reader))


print("-" * 40)
task_3_1()

# Задача 3.2
""" Сгруппируйте студентов по городу и подсчитайте количество студентов 
в каждом городе."""


def task_3_2():
    students_city_dict = dict()
    with open("students.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for line in reader:
            if line["city"] not in students_city_dict:
                students_city_dict[line["city"]] = 1
            else:
                students_city_dict[line["city"]] += 1

    print("task_3_2:")
    for item in students_city_dict.items():
        print(f"{item[0]} {item[1]}")


print("-" * 40)
task_3_2()

# Задача 3.3
# Для каждого города выведите средний балл студентов.


def task_3_3():
    students_city_dict = dict()
    with open("students.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for line in reader:
            if line["city"] not in students_city_dict:
                students_city_dict[line["city"]] = (int(line["score"]), 1)
            else:
                students_city_dict[line["city"]] = (
                    int(line["score"]) + students_city_dict[line["city"]][0],
                    students_city_dict[line["city"]][1] + 1,
                )

    print("task_3_3:")
    for item in students_city_dict.items():
        print(f"{item[0]} {round(item[1][0] / item[1][1])}")


print("-" * 40)
task_3_3()

# Задача 3.4
# Найдите город с самым высоким средним баллом.


def task_3_4():
    students_city_dict = dict()
    with open("students.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for line in reader:
            if line["city"] not in students_city_dict:
                students_city_dict[line["city"]] = (int(line["score"]), 1)
            else:
                students_city_dict[line["city"]] = (
                    int(line["score"]) + students_city_dict[line["city"]][0],
                    students_city_dict[line["city"]][1] + 1,
                )

    max_value = ("", 0)
    for key in students_city_dict.keys():
        students_city_dict[key] = float(
            round(students_city_dict[key][0] / students_city_dict[key][1])
        )
        if students_city_dict[key] > max_value[1]:
            max_value = (key, students_city_dict[key])

    print("task_3_4:", max_value[0])


print("-" * 40)
task_3_4()

# Задача 3.5
# Подсчитайте количество студентов на каждой оценке (3, 4, 5).


def task_3_5():
    students_grade_dict = dict()
    with open("students.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for line in reader:
            if int(line["grade"]) not in students_grade_dict and int(
                line["grade"]
            ) in (3, 4, 5):
                students_grade_dict[int(line["grade"])] = 1
            else:
                students_grade_dict[int(line["grade"])] += 1

    print("task_3_5:")
    for item in students_grade_dict.items():
        print(f"{item[0]} - {item[1]}")


print("-" * 40)
task_3_5()

# Задача 3.6
# Найдите самую популярную оценку среди всех студентов.


def task_3_6():
    students_grade_dict = dict()
    with open("students.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for line in reader:
            if int(line["grade"]) not in students_grade_dict and int(
                line["grade"]
            ) in (3, 4, 5):
                students_grade_dict[int(line["grade"])] = 1
            else:
                students_grade_dict[int(line["grade"])] += 1

    max_grade = max(students_grade_dict, key=students_grade_dict.get)
    print("task_3_6:", max_grade)


print("-" * 40)
task_3_6()

# %% Уровень 4: Сортировка и модификация
# Задача 4.1
""" Отсортируйте студентов по баллу (от большего к меньшему) и сохраните 
в новый файл sorted_by_score.csv."""


def task_4_1():
    data = list()

    with open("students.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(
            file, fieldnames=["name", "age", "grade", "city", "score"]
        )
        next(reader)
        for line in reader:
            data.append(line)

    print("task_4_1:")
    data = sorted(data, key=lambda val: int(val["grade"]), reverse=True)

    with open("sorted_by_score.csv", "w", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file, fieldnames=["name", "age", "grade", "city", "score"]
        )
        for line in data:
            writer.writerow(line)

    with open("sorted_by_score.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(
            file, fieldnames=["name", "age", "grade", "city", "score"]
        )
        for line in reader:
            print(*line.values())


print("-" * 40)
task_4_1()

# Задача 4.2
# Отсортируйте студентов сначала по городу (алфавит), затем по баллу (убывание).


def task_4_2():
    data = list()

    with open("students.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(
            file, fieldnames=["name", "age", "grade", "city", "score"]
        )
        next(reader)
        for line in reader:
            data.append(line)

    print("task_4_2:")
    for line in sorted(
        data, key=lambda val: (val["city"], -int(val["grade"]))
    ):
        print(*line.values())


print("-" * 40)
task_4_2()

# Задача 4.3
""" Добавьте новый столбец status, который будет содержать:
"Отлично" для балла >= 90
"Хорошо" для балла 75-89
"Удовлетворительно" для балла 60-74
"Неуд" для балла < 6.0
"""


def task_4_3():
    data = list()
    with open("students.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(
            file, fieldnames=["name", "age", "grade", "city", "score"]
        )
        next(reader)
        for line in reader:
            if int(line["score"]) >= 90:
                line["status"] = "Отлично"
            elif 75 <= int(line["score"]) < 90:
                line["status"] = "Хорошо"
            elif 60 <= int(line["score"]) < 75:
                line["status"] = "Удовлетворительно"
            elif int(line["score"]) < 60:
                line["status"] = "Неуд"
            data.append(line)

    with open("students_with_status.csv", "w", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["name", "age", "grade", "city", "score", "status"],
        )
        writer.writerows(data)

    with open("students_with_status.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(
            file,
            fieldnames=["name", "age", "grade", "city", "score", "status"],
        )
        next(reader)
        print("task_4_3:")
        for line in reader:
            print(*line.values())


print("-" * 40)
task_4_3()

# Задача 4.4
# Создайте файл excellent_students.csv со студентами, у которых балл >= 90.


def task_4_4():
    fieldnames = ["name", "age", "grade", "city", "score"]

    with open("students.csv", "r", encoding="utf-8") as inp_file:
        reader = csv.DictReader(inp_file)

        with open(
            "excellent_students.csv", "w", newline="", encoding="utf-8"
        ) as out_file:
            writer = csv.DictWriter(out_file, fieldnames=fieldnames)
            writer.writeheader()

            for line in reader:
                if int(line["score"]) >= 90:
                    writer.writerow(line)

    with open("excellent_students.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        print("task_4_4:")
        for line in reader:
            print(*line.values())


print("-" * 40)
task_4_4()

# Задача 4.5
# Удалите из файла всех студентов с оценкой 3.


def task_4_5():
    with open("students.csv", "r", encoding="utf-8") as inp_file:
        reader = csv.DictReader(inp_file)
        with open(
            "high_grade_students.csv", "w", encoding="utf-8"
        ) as out_file:
            writer = csv.DictWriter(
                out_file, fieldnames=["name", "age", "grade", "city", "score"]
            )
            for line in reader:
                if int(line["grade"]) > 3:
                    writer.writerow(line)

    with open("high_grade_students.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        print("task_4_5:")
        for line in reader:
            print(*line.values())


print("-" * 40)
task_4_5()

# %% Уровень 5: Расширенные задачи
# Задача 5.1
""" Создайте отчет report.csv со следующими колонками:
city - город
student_count - количество студентов
avg_score - средний балл
max_score - максимальный балл
min_score - минимальный балл
"""


def task_5_1():
    report_fields = [
        "city",
        "student_count",
        "avg_score",
        "max_score",
        "min_score",
    ]
    data = list()
    with open("students.csv", "r", encoding="utf-8") as inp_file:
        reader = csv.DictReader(inp_file)
        for line in reader:
            data.append(line)

    with open("report.csv", "w", encoding="utf-8") as out_file:
        writer = csv.DictWriter(out_file, fieldnames=report_fields)
        writer.writeheader()
        for city in set(student["city"] for student in data):
            student_count = len([x for x in data if x["city"] == city])
            avg_score = round(
                sum([int(x["score"]) for x in data if x["city"] == city])
                / student_count
            )
            max_score = max(
                [int(x["score"]) for x in data if x["city"] == city]
            )
            min_score = min(
                [int(x["score"]) for x in data if x["city"] == city]
            )
            writer.writerow(
                {
                    report_fields[0]: city,
                    report_fields[1]: student_count,
                    report_fields[2]: avg_score,
                    report_fields[3]: max_score,
                    report_fields[4]: min_score,
                }
            )

    with open("report.csv", "r", encoding="utf-8") as inp_file:
        reader = csv.DictReader(inp_file)
        print("task_5_1:")
        for row in reader:
            print(*row.values())


print("-" * 40)
task_5_1()

# Задача 5.2
""" Найдите "золотую медаль" - студента с самым высоким баллом в каждом городе. 
Сохраните результат в top_per_city.csv."""


def task_5_2():

    data = list()
    with open("students.csv", "r", encoding="utf-8") as inp_file:
        reader = csv.DictReader(inp_file)
        for line in reader:
            data.append(line)

    with open("top_per_city.csv", "w", encoding="utf-8") as out_file:
        writer = csv.DictWriter(out_file, fieldnames=["city", "student"])
        writer.writeheader()
        for city in set(student["city"] for student in data):
            writer.writerow(
                {
                    "city": city,
                    "student": max(
                        [x for x in data if x["city"] == city],
                        key=lambda x: int(x["score"]),
                    )["name"],
                }
            )

    with open("top_per_city.csv", "r", encoding="utf-8") as inp_file:
        reader = csv.DictReader(inp_file)
        print("task_5_2:")
        for row in reader:
            print(*row.values())


print("-" * 40)
task_5_2()

# Задача 5.3
"""Создайте файл grade_distribution.csv, где для каждой оценки будет указано, 
сколько студентов её получили в каждом городе."""


def task_5_3():
    grade_distribution_fields = ["city", "grade", "count"]

    data = list()
    with open("students.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for line in reader:
            data.append(line)

    grade_distribution = list()
    for row in data:
        name, age, grade, city, score = row.values()
        grade_distribution.append((city, grade))

    with open("grade_distribution.csv", "w", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=grade_distribution_fields)
        writer.writeheader()

        for row in set(grade_distribution):
            writer.writerow(
                {
                    grade_distribution_fields[0]: row[0],
                    grade_distribution_fields[1]: row[1],
                    grade_distribution_fields[2]: len(
                        [x for x in grade_distribution if x == row]
                    ),
                }
            )

    with open("grade_distribution.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        print("task_5_3")
        for line in reader:
            print(*line.values())


print("-" * 40)
task_5_3()

# Задача 5.4
"""Напишите функцию, которая принимает название города и возвращает всех 
студентов из этого города, отсортированных по баллу."""


def task_5_4(city):
    data = list()
    with open("students.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for line in reader:
            if line["city"] == city:
                data.append(line)

    print("task_5_4:")
    for row in sorted(data, key=lambda x: int(x["grade"])):
        print(row["name"], row["grade"])


print("-" * 40)
task_5_4("Москва")

# Задача 5.5
"""Создайте функцию, которая обновляет оценку студенту по имени 
(пользователь вводит имя и новую оценку)."""


def task_5_5(name, new_grade):
    data = list()
    fieldnames = list()
    with open("students.csv", "r", encoding="utf-8") as inp_file:
        reader = csv.DictReader(inp_file)
        fieldnames = reader.fieldnames
        for line in reader:
            if line["name"] == name:
                line["grade"] = new_grade
            data.append(line)

    with open("students.csv", "w", encoding="utf-8") as out_file:
        writer = csv.DictWriter(out_file, fieldnames)
        writer.writeheader()
        for line in data:
            writer.writerow(line)

    print("task_5_5:")
    with open("students.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for line in reader:
            print(*line.values())


print("-" * 40)
task_5_5("Зинаида", 1)
print("-" * 40)

import calendar
import locale
from datetime import date, datetime, timedelta

#------------------------------------------------------------------------------
''' Задача 1. «Календарь на год»
Напишите функцию print_year_calendar(year), которая принимает год и выводит в 
консоль календарь на этот год в следующем формате:

text
2025 год
========================================
      Январь                Февраль              
Пн Вт Ср Чт Пт Сб Вс   Пн Вт Ср Чт Пт Сб Вс
       1  2  3  4  5                   1  2
 6  7  8  9 10 11 12    3  4  5  6  7  8  9
13 14 15 16 17 18 19   10 11 12 13 14 15 16
20 21 22 23 24 25 26   17 18 19 20 21 22 23
27 28 29 30 31         24 25 26 27 28
'''

def print_year_calendar(year):
    
    cal = calendar.LocaleTextCalendar(locale='ru_RU.UTF-8')
    for quart in range(0,4):
        months = []
        
        for month in range(1,4):
            months.append(cal.formatmonth(year, 3*quart + month))
        
        A = [m.ljust(max(map(len, months[0].split('\n')))) for m in months[0].split('\n')]
        B = [m.ljust(max(map(len, months[1].split('\n')))) for m in months[1].split('\n')]
        C = [m.ljust(max(map(len, months[2].split('\n'))))for m in months[2].split('\n')]
        
        for i in range(len(A)):
            print(f"{A[i]}\t{B[i]}\t{C[i]}")
        print()
        
print(f"{'='*40}\nЗадача 1:")     
print_year_calendar(2025)
print('='*40 + '\n')

#------------------------------------------------------------------------------
''' Задача 2. «Рабочие дни между датами»
Напишите функцию count_workdays(start_date, end_date, workdays), 
которая принимает:

start_date и end_date — строки в формате "YYYY-MM-DD"

workdays — список чисел, где 0=понедельник, 6=воскресенье

Функция должна вернуть количество рабочих дней между датами 
(включая start_date, исключая end_date).

Пример:

count_workdays("2025-04-01", "2025-04-10", [0,1,2,3,4])  # пн-пт
# Вернет: 7 (1,2,3,4,7,8,9 апреля)
'''
def count_workdays(start_date, end_date, workdays):
    date_format = "%Y-%m-%d"
    start = date.strptime(start_date, date_format)
    end = date.strptime(end_date, date_format)
    days = [start + timedelta(days=i) for i in range((end - start).days)]
    work_days = [d for d in days if d.weekday() in workdays]
    print(f"{len(work_days)} ({','.join([str(d.day) for d in work_days])})")

print(f"{'='*40}\nЗадача 2:")      
count_workdays("2025-04-01", "2025-04-10", [0,1,2,3,4]) 
print('='*40 + '\n')

#------------------------------------------------------------------------------
''' Задача 3. «День программиста»
День программиста отмечается в 256-й день года (если год високосный, то 12 
сентября, иначе 13 сентября).

Напишите функцию programmers_day(year), которая возвращает дату Дня 
программиста в формате "DD.MM.YYYY".

Пример:

programmers_day(2024)  # Вернет: "12.09.2024"
programmers_day(2025)  # Вернет: "13.09.2025"
'''
def programmers_day(year):
    dt = datetime(year=year, month=1, day=1).toordinal()
    return date.fromordinal(dt+255)

print(f"{'='*40}\nЗадача 3:")      
print(programmers_day(2023))
print('='*40 + '\n')

#------------------------------------------------------------------------------
''' Задача 4. «Анализ календаря»
Напишите функцию calendar_stats(year, month), которая принимает год и месяц и 
возвращает словарь со статистикой:

{
    "total_days": 30,                    # всего дней в месяце
    "workdays": 22,                      # рабочих дней (пн-пт)
    "weekends": 8,                       # выходных дней (сб, вс)
    "first_weekday": "Tuesday",          # первый день месяца
    "last_weekday": "Thursday",          # последний день месяца
}
'''
def calendar_stats(year, month):
    month_stat = dict()
    cl = calendar
    start = date(year,month,1)
    end = date(year,month+1,1)
    days = [start + timedelta(days=i) for i in range((end - start).days)]
    
    month_stat["total_days"] = cl.monthrange(year, month)[1]
    month_stat["workdays"] = len([d for d in days if d.weekday() in [0,1,2,3,4]])
    month_stat["weekends"] = len([d for d in days if d.weekday() in [5,6]])
    month_stat["first_weekday"] = days[0].weekday()
    month_stat["last_weekday"] = days[-1].weekday()
    
    return month_stat

print(f"{'='*40}\nЗадача 4:")      
print(calendar_stats(2026, 4))
print('='*40 + '\n')

#------------------------------------------------------------------------------
''' Задача 5. «Генератор календаря в Excel»
Напишите функцию generate_csv_calendar(year, filename), которая создает CSV 
файл с календарем на год.

Формат CSV:

text
Month,Day,Weekday,IsWeekend
January,1,Thursday,False
January,2,Friday,False
...
December,31,Wednesday,False
'''
def generate_csv_calendar(year, filename):
    days = [date(year,1,1) + timedelta(days=i) for i in range((date(year+1,1,1) - date(year,1,1)).days)]
    
    with open(filename, 'w') as file:
        for d in days:
            print(f'{d.strftime("%B")}, {d.day}, {d.strftime("%A")}, {d.weekday() in [5,6]}')
            file.write(f'{d.strftime("%B")}, {d.day}, {d.strftime("%A")}, {d.weekday() in [5,6]}\n')
    pass
    
print(f"{'='*40}\nЗадача 5:")      
generate_csv_calendar(2026, "calendar.csv")
print('='*40 + '\n')

#------------------------------------------------------------------------------
''' Задача 6. «Сколько раз день недели встречается в году»
Напишите функцию weekday_count(year), которая возвращает словарь, 
где ключи — дни недели (пн, вт, ср, чт, пт, сб, вс), а значения — сколько раз 
этот день недели встречается в указанном году.

Пример:

weekday_count(2024)  # 2024 - високосный
# Вернет: {"Monday": 53, "Tuesday": 53, ..., "Sunday": 52}
'''
def weekday_count(year):
    month_dict = dict()
    days = [(date(year,1,1) + timedelta(days=i)).weekday() for i in range((date(year+1,1,1) - date(year,1,1)).days)]
    for i, name in enumerate(calendar.day_name):
        month_dict[name] = days.count(i)
    
    return month_dict

print(f"{'='*40}\nЗадача 5:")      
print(weekday_count(2026))
print('='*40 + '\n')

#------------------------------------------------------------------------------
''' Задача 7. «Соседние месяцы»
Напишите функцию show_neighbors(year, month), которая выводит последние 3 дня 
предыдущего месяца и первые 3 дня следующего месяца в виде списка 
строк "DD.MM (Weekday)".

Пример:

show_neighbors(2025, 4)
# Вывод:
# Предыдущий месяц (Март):
# 29.03 (Saturday), 30.03 (Sunday), 31.03 (Monday)
# 
# Следующий месяц (Май):
# 01.05 (Thursday), 02.05 (Friday), 03.05 (Saturday)
'''
def show_neighbors(year, month):
    locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
    
    prev_month = [date(year,month-1,max(calendar.monthrange(year, month-1))-2) + timedelta(days=i) for i in range(3)]
    next_month = [date(year,month+1,1) + timedelta(days=i) for i in range(3)]
    
    print("Вывод:")
    print(f"Предыдущий месяц ({prev_month[0].strftime('%B')}):\n{', '.join([d.strftime('%d.%m (%a)') for d in prev_month])}\n")
    print(f"Следующий месяц ({next_month[0].strftime('%B')}):\n{', '.join([d.strftime('%d.%m (%a)') for d in next_month])}")
     
print(f"{'='*40}\nЗадача 6:")      
show_neighbors(2025, 4)
print('='*40 + '\n')

#------------------------------------------------------------------------------
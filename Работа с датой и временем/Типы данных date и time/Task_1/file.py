from datetime import date, time, datetime, timedelta
import zoneinfo
#------------------------------------------------------------------------------
''' Задача 1. «Ближайший уикенд»

Напишите функцию weekend_of_birth(year, month, day), которая принимает дату рождения 
и возвращает строку: какой это был день недели и сколько дней оставалось до ближайшей 
субботы или воскресенья после этой даты (если день рождения уже был в выходной — вернуть 0).
'''
def weekend_of_birth(year, month, day):
    days = {1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday', 7:'Sunday'}
    birth_date = date(year, month, day)
    return f"{days[birth_date.isoweekday()]}, {6 - birth_date.isoweekday() if 6 - birth_date.isoweekday() >= 0 else 0} days to weekend"


#------------------------------------------------------------------------------
''' Задача 2. «Тайм-менеджер: дедлайны»

Вам приходит список задач в формате:
tasks = [
    {"name": "Сдать отчет", "deadline": "2025-04-10 18:00:00"},
    {"name": "Встреча с заказчиком", "deadline": "2025-04-05 14:30:00"},
    {"name": "Завершить модуль", "deadline": "2025-04-15 23:59:59"}
]

Напишите функцию check_deadlines(tasks, now_str), которая принимает этот список и 
текущее время в виде строки now_str (формат "%Y-%m-%d %H:%M:%S"). Функция должна:

1) Определить, какие задачи просрочены (дедлайн раньше now).
2) Какие задачи нужно сдать сегодня (дедлайн сегодня, но еще не наступил).
3) Отсортировать задачи по времени до дедлайна (от самых срочных к менее срочным) и вывести топ-1.

Формат вывода (вернуть словарь):
{
    "overdue": ["Сдать отчет"],
    "due_today": ["Встреча с заказчиком"],
    "most_urgent": "Завершить модуль"  # если нет ни одной задачи, вернуть None
}
'''
tasks = [
    # === ПРОСРОЧЕННЫЕ ЗАДАЧИ ===
    {"name": "Подготовить отчет для инвестора", "deadline": "2025-01-15 10:00:00"},
    {"name": "Согласовать бюджет с финансовым отделом", "deadline": "2025-02-28 15:30:00"},
    {"name": "Обновить документацию API", "deadline": "2025-03-24 09:00:00"},
    {"name": "Провести код-ревью пулреквеста", "deadline": "2025-03-30 08:00:00"},
    {"name": "Отправить коммерческое предложение клиенту", "deadline": "2025-03-30 23:59:59"},
    {"name": "Задеплоить исправление на прод", "deadline": "2025-03-31 05:00:00"},
    {"name": "Ответить на письмо технической поддержки", "deadline": "2025-03-31 09:59:59"},
    
    # === ЗАДАЧИ НА СЕГОДНЯ (10:00) ===
    {"name": "Написать пост для корпоративного блога", "deadline": "2025-03-31 00:00:00"},
    {"name": "Провести утренний стендап", "deadline": "2025-03-31 08:00:00"},
    {"name": "Созвониться с тимлидом фронтенда", "deadline": "2025-03-31 10:00:00"},
    {"name": "Заполнить таймшит", "deadline": "2025-03-31 10:01:00"},
    {"name": "Настроить CI/CD пайплайн", "deadline": "2025-03-31 12:00:00"},
    {"name": "Подготовить презентацию для демо", "deadline": "2025-03-31 15:30:00"},
    {"name": "Встреча с заказчиком", "deadline": "2025-03-31 18:00:00"},
    {"name": "Сделать бэкап базы данных", "deadline": "2025-03-31 23:59:59"},
    
    # === ЗАДАЧИ НА БУДУЩИЕ ДНИ ===
    {"name": "Обновить зависимости в проекте", "deadline": "2025-04-01 00:00:00"},
    {"name": "Написать юнит-тесты для нового модуля", "deadline": "2025-04-01 09:00:00"},
    {"name": "Согласовать архитектуру с сеньорами", "deadline": "2025-04-01 23:59:59"},
    {"name": "Оптимизировать SQL-запросы", "deadline": "2025-04-02 12:00:00"},
    {"name": "Провести интервью с кандидатом", "deadline": "2025-04-03 18:00:00"},
    {"name": "Выкатить новую фичу на стейджинг", "deadline": "2025-04-07 10:00:00"},
    {"name": "Написать техническую документацию", "deadline": "2025-04-14 15:00:00"},
    {"name": "Провести ретроспективу спринта", "deadline": "2025-04-30 12:00:00"},
    {"name": "Организовать тимбилдинг", "deadline": "2025-05-31 09:00:00"},
    
    # === ОСОБЫЕ СЛУЧАИ ===
    {"name": "Исправить баг в легаси коде", "deadline": "2024-02-29 12:00:00"},
    {"name": "Подготовить годовой отчет", "deadline": "2025-12-31 23:59:59"},
    {"name": "Запланировать задачи на следующий год", "deadline": "2026-01-01 00:00:00"},
]

now_str = "2025-03-31 10:00:00"

def check_deadlines(tasks, now_str):
    deadlines_dict = dict({"overdue":[], "due_today":[], "most_urgent":None})
    datetime_format = "%Y-%m-%d %H:%M:%S"
    now_datetime = datetime.strptime(now_str, datetime_format)
    
    for task in sorted(tasks, key=lambda task: task['deadline']):
        task_datetime = datetime.strptime(task['deadline'], datetime_format)
        if task_datetime < now_datetime:
            deadlines_dict["overdue"].append(task["name"])
        elif task_datetime.date() == now_datetime.date() and task_datetime >= now_datetime:
            deadlines_dict["due_today"].append(task["name"])
    
    if deadlines_dict["due_today"]:
        deadlines_dict["most_urgent"] = deadlines_dict["due_today"][0]
    else:
        all_future_tasks = sorted([task for task in tasks if datetime.strptime(task["deadline"], datetime_format) >= now_datetime],  key=lambda task: task["deadline"])
        deadlines_dict["most_urgent"] = all_future_tasks[0] if all_future_tasks else None
    
    return deadlines_dict


#------------------------------------------------------------------------------
''' Задача 3. «Рабочие часы и задержки»

Создайте класс BusinessHours, который инициализируется с рабочим временем 
(например, с 9:00 до 18:00, понедельник—пятница). У класса должен быть метод:
add_business_hours(start_datetime, hours), который прибавляет к начальной дате 
(объект datetime) строго рабочие часы, пропуская выходные и нерабочее время.

Условия:
Если hours = 2, а до конца рабочего дня остался 1 час — оставшийся час 
переносится на следующий рабочий день с 9:00.

Если start_datetime выпадает на нерабочее время (вечер пятницы или выходной), 
то начало отсчета — ближайшее начало рабочего дня.

Пример использования:

bh = BusinessHours(start_hour=9, end_hour=18, workdays=[0,1,2,3,4])  # 0 = понедельник
start = datetime(2025, 4, 4, 17, 0)  # Пятница 17:00
result = bh.add_business_hours(start, 2)
# Ожидаем: понедельник 9:00 (так как пятница 17:00 +1ч = 18:00, остается 1ч -> понедельник 9:00)
'''
class BusinessHours:
    
    def __init__(self, start_hour, end_hour, workdays):
        self.start_hour = start_hour
        self.end_hour = end_hour
        self.workdays = workdays
    
    def add_business_hours(self, start_datetime, hours):
        
        def move_to_workday(forecast_datetime):
            forecast_datetime += timedelta(days=1)
            if forecast_datetime.weekday() not in self.workdays:
                while forecast_datetime.weekday() not in self.workdays:
                    forecast_datetime += timedelta(days=1)
            forecast_datetime = forecast_datetime.replace(hour=self.start_hour)
            return forecast_datetime
        
        
        forecast_datetime = start_datetime
        
        # Check that start from work time
        if forecast_datetime.weekday() not in self.workdays or forecast_datetime.hour > self.end_hour:
            forecast_datetime = move_to_workday(forecast_datetime)
            
        if forecast_datetime.hour < self.start_hour:
            forecast_datetime = forecast_datetime.replace(hour=self.start_hour)
        
        while (forecast_datetime.hour + hours) > self.end_hour:
            hours -= self.end_hour - forecast_datetime.hour
            forecast_datetime = move_to_workday(forecast_datetime)
            
        forecast_datetime += timedelta(hours=hours)
        
        return forecast_datetime
        
        
bh = BusinessHours(start_hour=9, end_hour=18, workdays=[0,2,4,6])
start = datetime(2025, 4, 4, 17, 0)  # Пятница 17:00
         

#------------------------------------------------------------------------------
''' Задача 4. «Часовые пояса и время логов»

Вы пишете парсер логов сервера. Логи хранятся с UTC временем, но вам нужно 
отображать их для пользователя в его локальном времени. 

Даны:
1) Строка лога: "2025-04-03T14:30:45Z" (Z — это UTC).
2) Часовой пояс пользователя в формате "Europe/Minsk" (или "America/New_York").
3) Напишите функцию convert_log_to_local(log_str, user_tz_str), которая:
    a) Парсит строку в datetime (aware, с UTC).
    b) Конвертирует в заданный часовой пояс.
    c) Возвращает строку в формате "%d.%m.%Y %H:%M:%S %Z".

Дополнительное усложнение: Если у пользователя действует летнее время (DST), 
это должно учитываться автоматически.

Пример:

convert_log_to_local("2025-04-03T14:30:45Z", "Europe/Minsk")
# Вернет: "03.04.2025 17:30:45 +03" (в зависимости от смещения)
'''
def convert_log_to_local(log_str, user_tz_str):    
    output_datetime_format = "%d.%m.%Y %H:%M:%S %:z"
    log_datetime = datetime.fromisoformat(log_str.replace('Z', '+00:00'))
    log_datetime = log_datetime.astimezone(zoneinfo.ZoneInfo(user_tz_str))
    if ((log_datetime.utcoffset().total_seconds()) % 3600) // 60 != 0:         # Проверка на наличие минут в tzone
        return log_datetime.strftime(output_datetime_format)
    else: 
        return log_datetime.strftime(output_datetime_format)[:-3]

# Тестовые значения для функции convert_log_to_local
test_cases_tz = [
    {
        "name": "Базовый - Europe/Minsk (UTC+3, без DST)",
        "log_str": "2025-04-03T14:30:45Z",
        "user_tz_str": "Europe/Minsk",
        "expected": "03.04.2025 17:30:45 +03"
    },
    {
        "name": "America/New_York (UTC-4, летнее время)",
        "log_str": "2025-04-03T14:30:45Z",
        "user_tz_str": "America/New_York",
        "expected": "03.04.2025 10:30:45 -04"  # UTC-4 в апреле (DST)
    },
    {
        "name": "America/New_York зимой (UTC-5)",
        "log_str": "2025-01-15T10:00:00Z",
        "user_tz_str": "America/New_York",
        "expected": "15.01.2025 05:00:00 -05"  # UTC-5 в январе
    },
    {
        "name": "Asia/Tokyo (UTC+9, нет DST)",
        "log_str": "2025-04-03T14:30:45Z",
        "user_tz_str": "Asia/Tokyo",
        "expected": "03.04.2025 23:30:45 +09"
    },
    {
        "name": "Australia/Sydney (UTC+11, летнее время в апреле)",
        "log_str": "2025-04-03T14:30:45Z",
        "user_tz_str": "Australia/Sydney",
        "expected": "04.04.2025 01:30:45 +11"  # UTC+11 в апреле
    },
    {
        "name": "Australia/Sydney зимой (UTC+10)",
        "log_str": "2025-07-15T10:00:00Z",
        "user_tz_str": "Australia/Sydney",
        "expected": "15.07.2025 20:00:00 +10"  # UTC+10 в июле
    },
    {
        "name": "Europe/London зимой (UTC+0)",
        "log_str": "2025-01-15T14:30:45Z",
        "user_tz_str": "Europe/London",
        "expected": "15.01.2025 14:30:45 +00"
    },
    {
        "name": "Europe/London летом (UTC+1, BST)",
        "log_str": "2025-04-03T14:30:45Z",
        "user_tz_str": "Europe/London",
        "expected": "03.04.2025 15:30:45 +01"
    },
    {
        "name": "Полночь UTC",
        "log_str": "2025-04-03T00:00:00Z",
        "user_tz_str": "Asia/Shanghai",
        "expected": "03.04.2025 08:00:00 +08"
    },
    {
        "name": "Конец дня UTC",
        "log_str": "2025-04-03T23:59:59Z",
        "user_tz_str": "America/Los_Angeles",
        "expected": "03.04.2025 16:59:59 -07"  # UTC-7 в апреле (DST)
    },
    {
        "name": "Индия (UTC+5:30, нестандартное смещение)",
        "log_str": "2025-04-03T14:30:45Z",
        "user_tz_str": "Asia/Kolkata",
        "expected": "03.04.2025 20:00:45 +05:30"
    },
    {
        "name": "Непал (UTC+5:45, нестандартное смещение)",
        "log_str": "2025-04-03T14:30:45Z",
        "user_tz_str": "Asia/Kathmandu",
        "expected": "03.04.2025 20:15:45 +05:45"
    },
    {
        "name": "Переход через границу даты (UTC+14)",
        "log_str": "2025-04-03T23:00:00Z",
        "user_tz_str": "Pacific/Kiritimati",
        "expected": "04.04.2025 13:00:00 +14"
    },
    {
        "name": "UTC-11 (самый отстающий)",
        "log_str": "2025-04-03T00:00:00Z",
        "user_tz_str": "Pacific/Midway",
        "expected": "02.04.2025 13:00:00 -11"
    },
    {
        "name": "Граничный случай - 31 декабря",
        "log_str": "2025-12-31T23:59:59Z",
        "user_tz_str": "Pacific/Auckland",
        "expected": "01.01.2026 12:59:59 +13"  # UTC+13 в декабре (DST)
    }
]

# Функция для запуска тестов
def run_tz_tests(convert_func):
    print("=" * 70)
    print("ТЕСТИРОВАНИЕ ФУНКЦИИ convert_log_to_local")
    print("=" * 70)
    
    passed = 0
    failed = 0
    
    for i, test in enumerate(test_cases_tz, 1):
        print(f"\nТест {i}: {test['name']}")
        print("-" * 50)
        print(f"Входные данные:")
        print(f"  log_str: {test['log_str']}")
        print(f"  user_tz: {test['user_tz_str']}")
        
        try:
            result = convert_func(test['log_str'], test['user_tz_str'])
            expected = test['expected']
            
            print(f"\nРезультат: {result}")
            print(f"Ожидалось: {expected}")
            
            if result == expected:
                print("✅ ПРОЙДЕН")
                passed += 1
            else:
                print("❌ НЕ ПРОЙДЕН")
                failed += 1
        except Exception as e:
            print(f"\n❌ ОШИБКА: {e}")
            failed += 1
    
    print("\n" + "=" * 70)
    print(f"РЕЗУЛЬТАТЫ: {passed} пройдено, {failed} не пройдено")
    print("=" * 70)
    
    return passed, failed
#------------------------------------------------------------------------------

print("Results:")
print(f"Task1 - {weekend_of_birth(2023, 9, 17)}")
print('-'*30)
print(f"Task2: \n{check_deadlines(tasks, now_str)}")
print('-'*30)
print(f"Task3 - {bh.add_business_hours(start, 36)}")
print('-'*30)
run_tz_tests(convert_log_to_local)
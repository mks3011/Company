"""
В этот раз у нас есть компания, в ней отделы, в отделах люди. У людей есть имя, должность и зарплата.

Ваши задачи такие:
1. Вывести названия всех отделов
2. Вывести имена всех сотрудников компании.
3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
4. Вывести имена всех сотрудников компании, которые получают больше 100к.
5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела

Второй уровень:
7. Вывести названия отделов с указанием минимальной зарплаты в нём.
8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.
9. Вывести среднюю зарплату по всей компании.
10. Вывести названия должностей, которые получают больше 90к без повторений.
11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).
12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.

Третий уровень:
Теперь вам пригодится ещё список taxes, в котором хранится информация о налогах на сотрудников из разных департаметов.
Если department None, значит, этот налог применяется ко всем сотрудникам компании.
Иначе он применяется только к сотрудникам департмента, название которого совпадает с тем, что записано по ключу department.
К одному сотруднику может применяться несколько налогов.

13. Вывести список отделов со средним налогом на сотрудников этого отдела.
14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
15. Вывести список отделов, отсортированный по месячной налоговой нагрузки.
16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.
"""

departments = [
    {
        "title": "HR department",
        "employers": [
            {"first_name": "Daniel", "last_name": "Berger", "position": "Junior HR", "salary_rub": 50000},
            {"first_name": "Michelle", "last_name": "Frey", "position": "Middle HR", "salary_rub": 75000},
            {"first_name": "Kevin", "last_name": "Jimenez", "position": "Middle HR", "salary_rub": 70000},
            {"first_name": "Nicole", "last_name": "Riley", "position": "HRD", "salary_rub": 120000},
        ]
    },
    {
        "title": "IT department",
        "employers": [
            {"first_name": "Christina", "last_name": "Walker", "position": "Python dev", "salary_rub": 80000},
            {"first_name": "Michelle", "last_name": "Gilbert", "position": "JS dev", "salary_rub": 85000},
            {"first_name": "Caitlin", "last_name": "Bradley", "position": "Teamlead", "salary_rub": 95000},
            {"first_name": "Brian", "last_name": "Hartman", "position": "CTO", "salary_rub": 130000},
        ]
    },
]

taxes = [
    {"department": None, "name": "vat", "value_percents": 13},
    {"department": "IT Department", "name": "hiring", "value_percents": 6},
    {"department": "BizDev Department", "name": "sales", "value_percents": 20},
]


def employers_info(key, key2=None):  # функция выводит список со значениями переданного ключа в списке employers
    value_list = []
    for value in departments:
        department_title = value["title"]
        for v in value["employers"]:
            if key2 is None:
                name = v[key]
                value_list.append(name)
            if key2 == "title":
                name_department = v[key] + " (" + department_title + ")"
                value_list.append(name_department)
            if key2 == "salary_rub":
                name = v["first_name"]
                salary = v["salary_rub"]
                value_list.append({"name": name, "salary": salary})
    return value_list
print(employers_info("first_name", "salary_rub"))

# 1. Вывести названия всех отделов
print("Названия отделов:", ', '.join(department["title"] for department in departments))

# 2. Вывести имена всех сотрудников компании.
print("Имена всех сотрудников компании:", ', '.join(employers_info("first_name")))

# 3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
print("Имена всех сотрудников компании с указанием отдела:", ', '.join(employers_info("first_name", "title")))

# 4. Вывести имена всех сотрудников компании, которые получают больше 100к.
names = [item["name"] for item in (employers_info("first_name", "salary_rub")) if item["salary"] > 100000]
print(names)






# # 1. Вывести названия всех отделов
# for department in departments:
#     print("Названия отделов:", department["title"])
# # print(", ".join(department["title"] for department in departments))
#
# # 2. Вывести имена всех сотрудников компании.
# for department in departments:
#     for personnel in department["employers"]:
#         print(personnel["first_name"], personnel["last_name"])
#
# # 3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
# for department in departments:
#     for personnel in department["employers"]:
#         print(f'{personnel["first_name"]} {personnel["last_name"]} работает в {department["title"]}')
#
# # 4. Вывести имена всех сотрудников компании, которые получают больше 100к.
# for department in departments:
#     for personnel in department["employers"]:
#         if personnel["salary_rub"] > 100000:
#             print(personnel["first_name"], personnel["last_name"])
#
# # 5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
# for department in departments:
#     for position in department["employers"]:
#         if position["salary_rub"] < 100000:
#             print(position["position"])
#
# # 6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела
# for department in departments:
#     total_salary = 0
#     for salary in department["employers"]:
#         total_salary += salary["salary_rub"]
#     print(f'{department["title"]} {total_salary}')

# 7. Вывести названия отделов с указанием минимальной зарплаты в нём.

# 8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.
# 9. Вывести среднюю зарплату по всей компании.
# 10. Вывести названия должностей, которые получают больше 90к без повторений.
# 11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).
# 12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.

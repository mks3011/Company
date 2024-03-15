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

male_staff = {"Daniel", "Kevin", "Brian"}
female_staff = {"Michelle", "Nicole", "Christina", "Caitlin"}
vowels = {"a", "e", "i", "o", "u", "y"}


def employers_info(key1, key2=None):  # функция выводит все значения по ключу для отдела
    value_list = []
    try:
        for one_dep in departments:
            department_title = one_dep["title"]
            for worker in one_dep["employers"]:
                if key2 is None:
                    value = worker[key1]
                    value_list.append(value)
                elif key2 == "title":
                    name_department = worker[key1] + " (" + department_title + ")"
                    value_list.append(name_department)
    except KeyError:
        return ["Ошибка! Ключ задан неверно"]
    return value_list


def get_average_salaries_for_gender_staff(key=None):
    result = {}
    for dept in departments:
        department_name = dept["title"]
        if key is None:
            result[department_name] = [emp["salary_rub"] for emp in dept["employers"]]
        else:
            female_salaries = [emp["salary_rub"] for emp in dept["employers"] if emp["first_name"] in key]
            average_salary = sum(female_salaries) / len(female_salaries)
            result[department_name] = round(average_salary)
    return result


# 1. Вывести названия всех отделов
print("Названия отделов:", ', '.join(department["title"] for department in departments))

# 2. Вывести имена всех сотрудников компании.
print("Имена всех сотрудников компании:", ', '.join(employers_info("first_name")))

# 3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
print("Имена всех сотрудников компании с указанием отдела:", ', '.join(employers_info("first_name", "title")))

# 4. Вывести имена всех сотрудников компании, которые получают больше 100к.
up_100 = ", ".join(f"{n} ({s})" for n, s in zip(employers_info("first_name"), employers_info("salary_rub")) if s > 100000)
print(f"Зарплата больше 100к: {up_100}")

# 5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
low_80 = ", ".join(f"{n} ({s})" for n, s in zip(employers_info("position"), employers_info("salary_rub")) if s < 80000)
print(f"Зарплата меньше 80к: {low_80}")

for department, salaries in get_average_salaries_for_gender_staff().items():
    min_salary = min(salaries)
    max_salary = max(salaries)
    sum_salary = sum(salaries)
    avg_salary = sum(salaries) / len(salaries)
# 6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела
    print(f"Сумма зарплат в отделе {department}: {sum_salary} рублей")
# 7. Вывести названия отделов с указанием минимальной зарплаты в нём.
    print(f"Минимальная зарплата в отделе {department}: {min_salary} рублей")
# 8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.
    print(f"Зарплата в отделе {department}:"
          f" минимальная {min_salary}, средняя {avg_salary}, максимальная {max_salary} рублей")

# 9. Вывести среднюю зарплату по всей компании.
print("Средняя зарплата по всей компании:", sum(employers_info("salary_rub"))/len(employers_info("first_name")))

# 10. Вывести названия должностей, которые получают больше 90к без повторений.
up_90 = ", ".join({pos for pos, sal in zip(employers_info("position"), employers_info("salary_rub")) if sal > 90000})
print(f"Должности с зарплатой больше 90000: {up_90}")

# 11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).
avg_gender = get_average_salaries_for_gender_staff(female_staff)
print("Средняя зарплата среди девушек в " + ", ".join(f"{key}: {value}" for key, value in avg_gender.items()))

# 12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.
vowel_employers = []
for department in departments:
    for employer in department["employers"]:
        if employer["last_name"][-1].lower() in vowels and employer["first_name"] not in vowel_employers:
            vowel_employers.append(employer["first_name"])
print(f"Имена людей с гласной в конце фамилии: {', '.join(vowel_employers)}")

# 13. Вывести список отделов со средним налогом на сотрудников этого отдела.

# 14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
tax_for_all = [tax for tax in taxes if tax["department"] is None]
for department in departments:
    department_title = department["title"]
    employers = department["employers"]
    tax_for_dep = [tax for tax in taxes if
                   tax["department"] and tax["department"].lower() == department_title.lower()]
    for employer in employers:
        salary = employer["salary_rub"]
        total_tax_for_emp = sum(salary * (tax["value_percents"] / 100) for tax in (tax_for_all+tax_for_dep))
        employer["salary_after_taxes_rub"] = salary - total_tax_for_emp

for department in departments:
    for employer in department["employers"]:
        print(f"{employer['first_name']} {employer['last_name']} - зарплата 'на руки' {employer['salary_rub']}, с учетом налогов: {employer['salary_after_taxes_rub']}")

# 15. Вывести список отделов, отсортированный по месячной налоговой нагрузки.
# 16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
# 17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.


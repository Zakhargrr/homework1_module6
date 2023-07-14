"""
Функции для печати отдельных частей меню
и получения параметров от пользователя
"""


def print_menu():
    print("Парсер вакансий")
    print("Введите цифру для нужной команды")
    print("1. Получить вакансии")
    print("2. Удалить вакансию по ID")
    print("3. Отсортировать вакансии из файла по зарплате")
    print("4. Найти вакансии по ключевым словам")
    print("5. Вывести вакансии из файла в консоль")
    print("0. Выйти")


def print_parser_menu():
    print("\nВведите цифру для нужной команды")
    print("1. Получить вакансии с HeadHunter")
    print("2. Получить вакансии с SuperJob")
    print("3. Получить вакансии с обоих сайтов")
    print("0. Перейти в главное меню")


def print_parsed_vacancies_menu():
    print("1. Вывести вакансии в консоль")
    print("2. Сохранить вакансии в файл (старые вакансии будут стерты)")
    print("3. Добавить вакансии в файл")
    print("4. Вывести топ N вакансий по зарплате")
    print("0. Перейти в главное меню")


def get_query_params(is_double=False):
    search_query = input("Введите поисковый запрос: ")
    print("Введите требуемое количество записей")
    print("Примечание: значение должно быть больше 0 и не больше 100")
    if is_double:
        print("(При парсинге с двух сайтов вы получите число вакансий, в два раза большее введенного числа)")
    per_page = input()
    if not per_page.isnumeric():
        print("Введенное значение не является числом")
        return None, None

    per_page = int(per_page)
    if per_page <= 0 or per_page > 100:
        print("Введено число, выходящее за установленный лимит")
        return None, None
    return search_query, per_page


def print_vacancies(arr_vacancies):
    for vacancy in arr_vacancies:
        print("\n---------------------------------------------------")
        print("Название вакансии:", vacancy.title, "\n")
        print("ID вакансии:", vacancy.vacancy_id)
        print("Ссылка на вакансию:", vacancy.url)
        print("Дата публикации:", vacancy.published_at)
        if vacancy.salary_to_compare == 0:
            print("Зарплата: не указано")
        elif vacancy.salary_to == 0:
            print("Зарплата:", vacancy.salary_from, vacancy.currency)
        elif vacancy.salary_from == 0:
            print("Зарплата:", vacancy.salary_to, vacancy.currency)
        else:
            print("Зарплата:", vacancy.salary_from, "-", vacancy.salary_to, vacancy.currency)

        if vacancy.address == "":
            print("Адрес: не указан")
        else:
            print("Адрес:", vacancy.address)
        print("Описание работы:\n", vacancy.requirements)
        print("---------------------------------------------------")


def print_menu_json_files():
    print("Вывести в консоль вакансии из файла:")
    print("1. Без сортировки по критериям")  # vacancies.json
    print("2. Отсортированные по зарплате, равной введенной")  # vacancies_by_same_salary.json
    print("3. Отсортированные по зарплате, равной или большей введенной")  # vacancies_by_same_or_bigger_salary.json
    print("4. Отсортированные по ключевым словам")  # vacancies_with_keywords.json
    print("0. Перейти в главное меню")


def print_delete_menu():
    print("Удалить вакансию из файла, содержащего вакансии:")
    print("1. Без сортировки по критериям")  # vacancies.json
    print("2. Отсортированные по зарплате, равной введенной")  # vacancies_by_same_salary.json
    print("3. Отсортированные по зарплате, равной или большей введенной")  # vacancies_by_same_or_bigger_salary.json
    print("4. Отсортированные по ключевым словам")  # vacancies_with_keywords.json
    print("0. Перейти в главное меню")


def print_vacancies_from_json_file(arr_vacancies):
    for vacancy in arr_vacancies:
        print("\n---------------------------------------------------")
        print("Название вакансии:", vacancy["title"], "\n")
        print("ID вакансии:", vacancy["id"])
        print("Ссылка на вакансию:", vacancy["url"])
        print("Дата публикации:", vacancy["published_at"])
        if vacancy["salary_to"] == "0" and vacancy["salary_from"] == "0":
            print("Зарплата: не указано")
        elif vacancy["salary_to"] == "0":
            print("Зарплата:", vacancy["salary_from"], vacancy["currency"])
        elif vacancy["salary_from"] == "0":
            print("Зарплата:", vacancy["salary_to"], vacancy["currency"])
        else:
            print("Зарплата:", vacancy["salary_from"], "-", vacancy["salary_to"], vacancy["currency"])

        if vacancy["address"] == "":
            print("Адрес: не указан")
        else:
            print("Адрес:", vacancy["address"])
        print("Описание работы:\n", vacancy["requirements"])
        print("---------------------------------------------------")


def print_sort_vacancies_menu():
    print("1. Сохранить вакансии с зарплатой, равной введенной")
    print("2. Сохранить вакансии с зарплатой, большей или равной введенной")
    print("0. Перейти в главное меню")


def get_user_value():
    user_value = input("Введите желеаемый размер зарплаты (число больше 0): ")
    if not user_value.isnumeric():
        print("Введенное значение не является числом\n")
        return None
    user_value = int(user_value)
    if user_value <= 0:
        print("Число меньше или равно 0\n")
        return None
    return user_value


def get_keywords_arr():
    keywords_arr = []
    while True:
        print("Введите ключевое слово для поиска среди вакансий")
        print("Примечание: чтобы прекратить добавлять ключевые слова, введите 'стоп'")
        keyword = input()
        if keyword.lower() == "стоп":
            break
        keywords_arr.append(keyword)
    if not keywords_arr:
        print("Список ключевых слов пуст\n")
        return None
    return keywords_arr


def print_choose_file_to_sort_menu():
    print("1. Поиск по ключевым словам в вакансиях файла vacancies.json")
    print("2. Поиск по ключевым словам в вакансиях файла vacancies_by_same_salary.json")
    print("3. Поиск по ключевым словам в вакансиях файла vacancies_by_same_or_bigger_salary.json")
    print("0. Перейти в главное меню")

import json

from models.api_classes import HeadHunterAPI
from models.saver_classes import JSONSaver
from models.vacancy_classes import Vacancy


def print_menu():
    print("Парсер вакансий")
    print("Введите цифру для нужной команды")
    print("1. Получить вакансии")
    print("0. Выйти")


def print_parser_menu():
    print("\nВведите цифру для нужной команды")
    print("1. Получить вакансии с HeadHunter")
    print("2. Получить вакансии с SuperJob")
    print("3. Получить вакансии с обоих сайтов")
    print("0. Вернуться в основное меню")


def print_parsed_vacancies_menu():
    print("1. Вывести вакансии в консоль")
    print("2. Сохранить вакансии в файл")


def print_save_vacancies():
    print("Вы хотите сохранить вакансии в файл?")
    print("1. Да")
    print("2. Нет")


def save_vacancies_json(vacancies):
    dict_vacancies = {"items": []}
    for vacancy in vacancies:
        single_vacancy_dict = {
            "id": vacancy.vacancy_id,
            "title": vacancy.title,
            "url": vacancy.url,
            "published_at": vacancy.published_at,
            "salary_from": vacancy.salary_from,
            "salary_to": vacancy.salary_to,
            "currency": vacancy.currency,
            "address": vacancy.address,
            "requirements": vacancy.requirements,
        }
        dict_vacancies["items"].append(single_vacancy_dict)
    json_saver = JSONSaver()
    json_saver.write_vacancies(dict_vacancies)


def initialize_hh_vacancies(vacancies):
    arr_vacancies = []
    for vacancy in vacancies:
        vacancy_id = vacancy["id"]
        title = vacancy["name"]
        url = vacancy["apply_alternate_url"]
        data = vacancy["published_at"]
        published_at = data[8:10] + "." + data[5:7] + "." + data[0:4]
        if vacancy["salary"] is None:
            salary_from = "0"
            salary_to = "0"
            currency = ""
        else:
            if vacancy["salary"]["from"] is None:
                salary_from = "0"
                salary_to = str(vacancy["salary"]["to"])
                if vacancy["salary"]["currency"] == "RUR":
                    currency = "RUB"
                else:
                    currency = vacancy["salary"]["currency"]
            elif vacancy["salary"]["to"] is None:
                salary_from = str(vacancy["salary"]["from"])
                salary_to = "0"
                if vacancy["salary"]["currency"] == "RUR":
                    currency = "RUB"
                else:
                    currency = vacancy["salary"]["currency"]
            else:
                salary_from = str(vacancy["salary"]["from"])
                salary_to = str(vacancy["salary"]["to"])
                if vacancy["salary"]["currency"] == "RUR":
                    currency = "RUB"
                else:
                    currency = vacancy["salary"]["currency"]
        if vacancy["address"] is None:
            address = ""
        else:
            address = vacancy["address"]["raw"]

        if vacancy["snippet"]["requirement"] is None:
            requirement = ""
        else:
            requirement = "Требования: " + vacancy["snippet"]["requirement"] + "\n"

        if vacancy["snippet"]["responsibility"] is None:
            responsibility = ""
        else:
            responsibility = "Обязанности: " + vacancy["snippet"]["responsibility"]
        requirements = requirement + responsibility
        hh_vacancy = Vacancy(vacancy_id, title, url, published_at, salary_from, salary_to, currency, address,
                             requirements)
        arr_vacancies.append(hh_vacancy)
    return arr_vacancies


def print_vacancies(arr_vacancies):
    for vacancy in arr_vacancies:
        print("\n---------------------------------")
        print("Название вакансии:", vacancy.title, "\n")
        print("ID вакансии:", vacancy.vacancy_id)
        print("Ссылка на вакансию:", vacancy.url)
        print("Дата публикации:", vacancy.published_at)
        if vacancy.salary_to_compare == "0":
            print("Зарплата: не указано")
        elif vacancy.salary_to == "0":
            print("Зарплата:", vacancy.salary_from, vacancy.currency)
        elif vacancy.salary_from == "0":
            print("Зарплата:", vacancy.salary_to, vacancy.currency)
        else:
            print("Зарплата:", vacancy.salary_from, "-", vacancy.salary_to, vacancy.currency)

        if vacancy.address == "":
            print("Адрес: не указан")
        else:
            print("Адрес:", vacancy.address)
        print("Описание работы:\n", vacancy.requirements)
        print("---------------------------------")


def main():
    while True:
        print_menu()
        switch = input()
        if switch == "1":
            arr_vacancies = []
            print_parser_menu()
            switch = input()
            if switch == "1":
                hh = HeadHunterAPI()
                search_query = input("Введите поисковый запрос: ")
                hh_vacancies = hh.get_vacancies(search_query)
                parsed_vacs_arr = initialize_hh_vacancies(hh_vacancies["items"])
                print_parsed_vacancies_menu()
                switch = input()
                if switch == "1":
                    print_vacancies(parsed_vacs_arr)
                    while True:
                        print_save_vacancies()
                        switch = input()
                        if switch == "1":
                            save_vacancies_json(parsed_vacs_arr)
                            break
                        elif switch == "2":
                            break
                        else:
                            print("Такой команды нет\n")


if __name__ == "__main__":
    main()

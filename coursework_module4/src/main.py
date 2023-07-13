from models.api_classes import HeadHunterAPI, SuperJobAPI
from models.saver_classes import JSONSaver
from models.vacancy_classes import Vacancy


def print_menu():
    print("Парсер вакансий")
    print("Введите цифру для нужной команды")
    print("1. Получить вакансии")
    print("2. Получить вакансии из файла по критериям")
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
    print("3. Добавить вакансии в файл")


def print_save_vacancies():
    print("Вы хотите сохранить или добавить вакансии в файл?")
    print("1. Да")
    print("2. Нет")


def print_save_or_add_menu():
    print("1. Сохранить вакансии  в файл (старые вакансии будут стерты)")
    print("2. Добавить вакансиии в файл")


def print_vacancies(arr_vacancies):
    for vacancy in arr_vacancies:
        print("\n---------------------------------")
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
        print("---------------------------------")


def main():
    while True:
        print_menu()
        switch = input()
        if switch == "1":
            while True:
                print_parser_menu()
                switch = input()
                if switch == "1":
                    hh = HeadHunterAPI()
                    search_query = input("Введите поисковый запрос: ")
                    hh_vacancies = hh.get_vacancies(search_query)
                    parsed_vacs_arr = Vacancy.initialize_hh_vacancies(hh_vacancies["items"])

                elif switch == "2":
                    superjob = SuperJobAPI()
                    search_query = input("Введите поисковый запрос: ")
                    superjob_vacancies = superjob.get_vacancies(search_query)
                    parsed_vacs_arr = Vacancy.initialize_superjob_vacancies(superjob_vacancies["objects"])

                elif switch == "3":
                    hh = HeadHunterAPI()
                    superjob = SuperJobAPI()
                    search_query = input("Введите поисковый запрос: ")
                    hh_vacancies = hh.get_vacancies(search_query)
                    superjob_vacancies = superjob.get_vacancies(search_query)
                    parsed_hh_vacs_arr = Vacancy.initialize_hh_vacancies(hh_vacancies["items"])
                    parsed_superjob_vacs_arr = Vacancy.initialize_superjob_vacancies(superjob_vacancies["objects"])
                    parsed_vacs_arr = parsed_hh_vacs_arr + parsed_superjob_vacs_arr
                elif switch == "0":
                    print("Переход в главное меню\n")
                    break

                else:
                    print("Такой команды нет")
                    continue
                while True:
                    print_parsed_vacancies_menu()
                    switch = input()
                    if switch == "1":
                        print_vacancies(parsed_vacs_arr)
                        while True:
                            print_save_vacancies()
                            switch = input()
                            if switch == "1":
                                while True:
                                    print_save_or_add_menu()
                                    switch = input()
                                    if switch == "1":
                                        JSONSaver.write_vacancies_json(parsed_vacs_arr)
                                        break
                                    elif switch == "2":
                                        JSONSaver.add_vacancies_json(parsed_vacs_arr)
                                        break
                                    else:
                                        print("Такой команды нет\n")
                                break
                            elif switch == "2":
                                break
                            else:
                                print("Такой команды нет\n")
                        break
                    elif switch == "2":
                        JSONSaver.write_vacancies_json(parsed_vacs_arr)
                        break
                    elif switch == "3":
                        JSONSaver.add_vacancies_json(parsed_vacs_arr)
                        break
                    else:
                        print("Такой команды нет\n")
                break


if __name__ == "__main__":
    main()

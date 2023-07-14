from models.api_classes import HeadHunterAPI, SuperJobAPI
from models.saver_classes import JSONSaver
from models.vacancy_classes import Vacancy
from src.utils import print_menu, print_parser_menu, get_query_params, print_parsed_vacancies_menu, print_vacancies, \
    print_delete_menu, print_sort_vacancies_menu, get_user_value, get_keywords_arr, print_choose_file_to_sort_menu, \
    print_menu_json_files, print_vacancies_from_json_file


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
                    search_query, per_page = get_query_params()
                    if search_query is None:
                        continue
                    hh_vacancies = hh.get_vacancies(search_query, per_page)
                    parsed_vacs_arr = Vacancy.initialize_hh_vacancies(hh_vacancies["items"])

                elif switch == "2":
                    superjob = SuperJobAPI()
                    search_query, per_page = get_query_params()
                    if search_query is None:
                        continue
                    superjob_vacancies = superjob.get_vacancies(search_query, per_page)
                    parsed_vacs_arr = Vacancy.initialize_superjob_vacancies(superjob_vacancies["objects"])

                elif switch == "3":
                    hh = HeadHunterAPI()
                    superjob = SuperJobAPI()
                    search_query, per_page = get_query_params(True)
                    if search_query is None:
                        continue
                    hh_vacancies = hh.get_vacancies(search_query, per_page)
                    superjob_vacancies = superjob.get_vacancies(search_query, per_page)
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

                    elif switch == "2":
                        JSONSaver.write_vacancies(parsed_vacs_arr)
                        print("Вакансии сохранены в файле vacancies.json\n")
                        break

                    elif switch == "3":
                        JSONSaver.add_vacancies(parsed_vacs_arr)
                        print("Вакансии добавлены в файл vacancies.json\n")
                        break

                    elif switch == "4":
                        parsed_vacs_arr = Vacancy.get_top_vacancies(parsed_vacs_arr)

                    elif switch == "0":
                        print("Переход в главное меню\n")
                        break

                    else:
                        print("Такой команды нет\n")
                break
        elif switch == "2":
            while True:
                print_delete_menu()
                switch = input()
                if switch in ["1", "2", "3", "4"]:
                    vacancy_id = input("Введите ID вакансии для удаления: ")
                    deleted_vacancy = JSONSaver.delete_vacancy(vacancy_id, switch)
                    if deleted_vacancy is None:
                        break
                    else:
                        print(f"Вакансия с ID {vacancy_id} удалена\n")
                        break
                elif switch == "0":
                    print("Переход в главное меню\n")
                    break
                else:
                    print("Такой команды нет\n")
                    continue

        elif switch == "3":
            while True:
                print_sort_vacancies_menu()
                switch = input()
                if switch == "1":
                    user_value = get_user_value()
                    if user_value is None:
                        continue
                    JSONSaver.get_vacancies_be_same_salary(user_value)
                    print("Вакансии с желаемым уровнем зарплаты сохранены в файле vacancies_by_same_salary.json\n")
                    break
                elif switch == "2":
                    user_value = get_user_value()
                    if user_value is None:
                        continue
                    JSONSaver.get_vacancies_by_same_or_bigger_salary(user_value)
                    print(
                        "Вакансии с желаемым уровнем зарплаты сохранены в файле vacancies_by_same_or_bigger_salary.json\n")
                    break

                elif switch == "0":
                    print("Переход в главное меню\n")
                    break

                else:
                    print("Такой команды нет\n")
        elif switch == "4":
            keywords_arr = get_keywords_arr()
            if keywords_arr is None:
                continue
            while True:
                print_choose_file_to_sort_menu()
                switch = input()
                if switch in ["1", "2", "3"]:
                    JSONSaver.sort_vacancies_by_keywords(keywords_arr, switch)
                    break

                elif switch == "0":
                    print("Переход в главное меню\n")
                    break

                else:
                    print("Такой команды нет\n")

        elif switch == "5":
            while True:
                print_menu_json_files()
                switch = input()
                if switch in ["1", "2", "3", "4"]:
                    arr_vacancies = JSONSaver.return_arr_from_file(switch)
                elif switch == "0":
                    print("Переход в главное меню\n")
                    break
                else:
                    print("Такой команды нет\n")
                    continue

                if arr_vacancies is None:
                    break
                print_vacancies_from_json_file(arr_vacancies)

        elif switch == "0":
            print("Завершение программы")
            break
        else:
            print("Такой команды нет\n")


if __name__ == "__main__":
    main()

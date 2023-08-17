import psycopg2

from models.db_class import DBManager


def main():
    print("Введите имя базы данных, к которой нужно подключиться")
    db_name = input()
    print("Введите пароль от базы данных")  # имя и пароль должны совпадать с данными бд, введенными в db_script.py
    db_pwd = input()
    db_manager = DBManager(db_name, db_pwd)
    try:
        db_manager.get_connection()
    except psycopg2.OperationalError:
        print("Не удалось подключиться к базе данных")
        return
    while True:
        print("Парсер вакансий по компаниям")
        print("Выберите команду и нажмите соответствующую цифру")
        print("1. Получить список всех компаний с количеством вакансий")
        print("2. Получить все вакансии")
        print("3. Получить среднюю зарплату по всем вакансиям")
        print("4. Получить те вакансии, у которых зарплата выше средней")
        print("5. Получить вакансии, в названии которых есть ключевое слово")
        print("0. Выход")

        check = input()
        if check == "1":
            vacancies = db_manager.get_companies_and_vacancies_count()
            for vacancy in vacancies:
                row = ""
                row += vacancy[0] + ": " + str(vacancy[1])
                print(row)
            print("")
        elif check == "2":
            vacancies = db_manager.get_all_vacancies()
            db_manager.print_array(vacancies)
        elif check == "3":
            avg_salary = db_manager.get_avg_salary()
            print("Средняя зарплата равна", avg_salary, "рублям\n")
        elif check == "4":
            vacancies = db_manager.get_vacancies_with_higher_salary()
            db_manager.print_array(vacancies)
        elif check == "5":
            print("Введите ключевое слово")
            keyword = input()
            vacancies = db_manager.get_vacancies_with_keyword(keyword)
            db_manager.print_array(vacancies)
        elif check == "0":
            print("Заверешение программы")
            break
        else:
            print("Такой команды нет\n")


if __name__ == "__main__":
    main()

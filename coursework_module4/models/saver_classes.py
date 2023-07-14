import json
import os
from abc import ABC, abstractmethod


class Saver(ABC):

    @classmethod
    @abstractmethod
    def write_vacancies(cls, vacancies):
        pass

    @classmethod
    @abstractmethod
    def add_vacancies(cls, vacancies):
        pass

    @classmethod
    @abstractmethod
    def delete_vacancy(cls, vacancy_id, switch):
        pass

    @classmethod
    @abstractmethod
    def get_vacancies_be_same_salary(cls, user_value):
        pass

    @classmethod
    @abstractmethod
    def get_vacancies_by_same_or_bigger_salary(cls, user_value):
        pass

    @classmethod
    @abstractmethod
    def sort_vacancies_by_keywords(cls, keywords_arr, switch):
        pass


class JSONSaver(Saver):
    @staticmethod
    def create_json_format(vacancies):
        """
        Создает массив вакансий для записи в JSON-файл
        """
        json_vacancies_arr = []
        for vacancy in vacancies:
            single_vacancy_dict = {
                "id": vacancy.vacancy_id,
                "title": vacancy.title,
                "url": vacancy.url,
                "published_at": vacancy.published_at,
                "salary_from": str(vacancy.salary_from),
                "salary_to": str(vacancy.salary_to),
                "currency": vacancy.currency,
                "address": vacancy.address,
                "requirements": vacancy.requirements,
            }
            json_vacancies_arr.append(single_vacancy_dict)
        return json_vacancies_arr

    """
    Фукнции для записи и излечения данных из четырех JSON-файлов
    """
    @staticmethod
    def vacancies_json_dump(dict_vacancies):
        with open(os.path.join("..", "files", "vacancies.json"), "w", encoding='utf-8') as f:
            json.dump(dict_vacancies, f, ensure_ascii=False)

    @staticmethod
    def vacancies_json_load():
        with open(os.path.join("..", "files", "vacancies.json"), "r", encoding='utf-8') as f:
            dict_vacancies = json.load(f)
        return dict_vacancies

    @staticmethod
    def vacancies_by_same_salary_json_dump(dict_vacancies):
        with open(os.path.join("..", "files", "vacancies_by_same_salary.json"), "w", encoding='utf-8') as f:
            json.dump(dict_vacancies, f, ensure_ascii=False)

    @staticmethod
    def vacancies_by_same_salary_json_load():
        with open(os.path.join("..", "files", "vacancies_by_same_salary.json"), "r", encoding='utf-8') as f:
            dict_vacancies = json.load(f)
        return dict_vacancies

    @staticmethod
    def vacancies_by_same_or_bigger_salary_json_dump(dict_vacancies):
        with open(os.path.join("..", "files", "vacancies_by_same_or_bigger_salary.json"), "w", encoding='utf-8') as f:
            json.dump(dict_vacancies, f, ensure_ascii=False)

    @staticmethod
    def vacancies_by_same_or_bigger_salary_json_load():
        with open(os.path.join("..", "files", "vacancies_by_same_or_bigger_salary.json"), "r", encoding='utf-8') as f:
            dict_vacancies = json.load(f)
        return dict_vacancies

    @staticmethod
    def vacancies_with_keywords_json_dump(dict_vacancies):
        with open(os.path.join("..", "files", "vacancies_with_keywords.json"), "w", encoding='utf-8') as f:
            json.dump(dict_vacancies, f, ensure_ascii=False)

    @staticmethod
    def vacancies_with_keywords_json_load():
        with open(os.path.join("..", "files", "vacancies_with_keywords.json"), "r", encoding='utf-8') as f:
            dict_vacancies = json.load(f)
        return dict_vacancies

    @classmethod
    def write_vacancies(cls, vacancies):
        """
        Функция для записи массива экземпляров класса Vacancy в файл vacancies.json
        в формате JSON
        """
        json_vacancies_arr = cls.create_json_format(vacancies)
        dict_vacancies = {"items": json_vacancies_arr}
        cls.vacancies_json_dump(dict_vacancies)

    @classmethod
    def add_vacancies(cls, vacancies_to_add):
        """
        Функция для записи массива экземпляров класса Vacancy в файл vacancies.json
        в формате JSON (старые записи из файла не стираются)
        """
        dict_vacancies = cls.vacancies_json_load()
        old_vacancies = dict_vacancies["items"]
        new_vacancies = cls.create_json_format(vacancies_to_add)
        vacancies_total = old_vacancies + new_vacancies
        dict_vacancies["items"] = vacancies_total
        cls.vacancies_json_dump(dict_vacancies)

    @classmethod
    def delete_vacancy(cls, vacancy_id, switch):
        """
        Функция для удаления записей из четырех .json файлов
        """
        arr_vacancies = cls.return_arr_from_file(switch)
        if arr_vacancies is None:
            return None
        vacancy_counter = 0
        deleted_vacancy = None
        for vacancy in arr_vacancies:
            if vacancy["id"] == vacancy_id:
                deleted_vacancy = arr_vacancies.pop(vacancy_counter)
            vacancy_counter += 1
        if deleted_vacancy is None:
            print("Вакансии с таким ID нет в файле\n")
            return None
        dict_vacancies = {"items": arr_vacancies}
        if switch == "1":
            cls.vacancies_json_dump(dict_vacancies)
            return deleted_vacancy
        elif switch == "2":
            cls.vacancies_by_same_salary_json_dump(dict_vacancies)
            return deleted_vacancy
        elif switch == "3":
            cls.vacancies_by_same_or_bigger_salary_json_dump(dict_vacancies)
            return deleted_vacancy
        elif switch == "4":
            cls.vacancies_with_keywords_json_dump(dict_vacancies)
            return deleted_vacancy
        else:
            print("Переменная switch выходит за допустимые лимиты")
            return None

    @classmethod
    def get_vacancies_be_same_salary(cls, user_value: int):
        """
        Сортирует вакансии из файла vacancies.json и сохраняет в
        файл vacancies_by_same_salary.json только те вакансии, в
        которых значение зарплаты строго равно числу, введенному пользователем
        """
        dict_vacancies = cls.vacancies_json_load()
        arr_vacancies = dict_vacancies["items"]
        chosen_vacancies = []
        for vacancy in arr_vacancies:
            if int(vacancy["salary_from"]) == user_value or int(vacancy["salary_to"]) == user_value:
                chosen_vacancies.append(vacancy)

        dict_vacancies["items"] = chosen_vacancies
        cls.vacancies_by_same_salary_json_dump(dict_vacancies)

    @classmethod
    def get_vacancies_by_same_or_bigger_salary(cls, user_value: int):
        """
        Сортирует вакансии из файла vacancies.json и сохраняет в
        файл vacancies_by_same_or_bigger_salary.json только те вакансии, в
        которых значение зарплаты больше либо равно числу, введенному пользователем
        """
        dict_vacancies = cls.vacancies_json_load()
        arr_vacancies = dict_vacancies["items"]
        chosen_vacancies = []
        for vacancy in arr_vacancies:
            if int(vacancy["salary_to"]) >= user_value:
                chosen_vacancies.append(vacancy)

        dict_vacancies["items"] = chosen_vacancies
        cls.vacancies_by_same_or_bigger_salary_json_dump(dict_vacancies)

    @classmethod
    def sort_vacancies_by_keywords(cls, keywords_arr, switch):
        """
        Сортирует вакансии из файлов vacancies.json, vacancies_by_same_salary.json,
        vacancies_by_same_or_bigger_salary.json и сохраняет в
        файл vacancies_with_keywords.json только те вакансии, в
        описании которых встретились все введенные пользователем ключевые слова
        """
        if switch == "1":
            dict_vacancies = cls.vacancies_json_load()
        elif switch == "2":
            dict_vacancies = cls.vacancies_by_same_salary_json_load()
        elif switch == "3":
            dict_vacancies = cls.vacancies_by_same_or_bigger_salary_json_load()
        else:
            raise ValueError("Переменная switch выходит за допустимые лимиты")

        arr_vacancies = dict_vacancies["items"]
        vacancies_with_keywords = []

        for keyword in keywords_arr:
            for vacancy in arr_vacancies:
                if keyword in vacancy["requirements"]:
                    vacancies_with_keywords.append(vacancy)

            arr_vacancies = vacancies_with_keywords
            vacancies_with_keywords = []
        if not arr_vacancies:
            print("Нет вакансий, подходящих по заданным ключевым словам\n")
        else:
            dict_vacancies["items"] = arr_vacancies
            cls.vacancies_with_keywords_json_dump(dict_vacancies)
            print("Подходящие вакансии записаны в файл vacancies_with_keywords.json\n")

    @classmethod
    def return_arr_from_file(cls, switch):
        """
        Возвращает массив вакансий в JSON формате из четырех файлов
        """
        if switch == "1":
            try:
                dict_vacancies = cls.vacancies_json_load()
            except FileNotFoundError:
                print("Файл не найден\n")
                return None
        elif switch == "2":
            try:
                dict_vacancies = cls.vacancies_by_same_salary_json_load()
            except FileNotFoundError:
                print("Файл не найден\n")
                return None
        elif switch == "3":
            try:
                dict_vacancies = cls.vacancies_by_same_or_bigger_salary_json_load()
            except FileNotFoundError:
                print("Файл не найден\n")
                return None
        elif switch == "4":
            try:
                dict_vacancies = cls.vacancies_with_keywords_json_load()
            except FileNotFoundError:
                print("Файл не найден\n")
                return None
        else:
            print("Переменная switch выходит за допустимые лимиты")
            return None
        arr_vacancies = dict_vacancies["items"]
        return arr_vacancies

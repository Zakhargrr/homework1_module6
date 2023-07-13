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
    def delete_vacancy(cls, vacancy_id):
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

    @staticmethod
    def json_dump(dict_vacancies):
        with open(os.path.join("..", "files", "vacancies.json"), "w", encoding='utf-8') as f:
            json.dump(dict_vacancies, f, ensure_ascii=False)

    @staticmethod
    def json_load():
        with open(os.path.join("..", "files", "vacancies.json"), "r", encoding='utf-8') as f:
            dict_vacancies = json.load(f)
        return dict_vacancies

    @classmethod
    def write_vacancies(cls, vacancies):
        json_vacancies_arr = cls.create_json_format(vacancies)
        dict_vacancies = {"items": json_vacancies_arr}
        cls.json_dump(dict_vacancies)

    @classmethod
    def add_vacancies(cls, vacancies_to_add):
        dict_vacancies = cls.json_load()
        old_vacancies = dict_vacancies["items"]
        new_vacancies = cls.create_json_format(vacancies_to_add)
        vacancies_total = old_vacancies + new_vacancies
        dict_vacancies["items"] = vacancies_total
        cls.json_dump(dict_vacancies)

    @classmethod
    def delete_vacancy(cls, vacancy_id):
        dict_vacancies = cls.json_load()
        arr_vacancies = dict_vacancies["items"]
        vacancy_counter = 0
        deleted_vacancy = None
        for vacancy in arr_vacancies:
            if vacancy["id"] == vacancy_id:
                deleted_vacancy = arr_vacancies.pop(vacancy_counter)
            vacancy_counter += 1
        dict_vacancies["items"] = arr_vacancies
        cls.json_dump(dict_vacancies)
        return deleted_vacancy

    @classmethod
    def get_vacancies_be_same_salary(cls, user_value: int):
        dict_vacancies = cls.json_load()
        arr_vacancies = dict_vacancies["items"]
        chosen_vacancies = []
        for vacancy in arr_vacancies:
            if int(vacancy["salary_from"]) == user_value or int(vacancy["salary_to"]) == user_value:
                chosen_vacancies.append(vacancy)

        dict_vacancies["items"] = chosen_vacancies
        with open(os.path.join("..", "files", "vacancies_by_same_salary.json"), "w", encoding='utf-8') as f:
            json.dump(dict_vacancies, f, ensure_ascii=False)

    @classmethod
    def get_vacancies_by_same_or_bigger_salary(cls, user_value: int):
        dict_vacancies = cls.json_load()
        arr_vacancies = dict_vacancies["items"]
        chosen_vacancies = []
        for vacancy in arr_vacancies:
            if int(vacancy["salary_to"]) >= user_value:
                chosen_vacancies.append(vacancy)

        dict_vacancies["items"] = chosen_vacancies
        with open(os.path.join("..", "files", "vacancies_by_same_or_bigger_salary.json"), "w", encoding='utf-8') as f:
            json.dump(dict_vacancies, f, ensure_ascii=False)

    @classmethod
    def sort_vacancies_by_keywords(cls, keywords_arr, switch):
        if switch == "1":
            dict_vacancies = cls.json_load()
        elif switch == "2":
            with open(os.path.join("..", "files", "vacancies_by_same_salary.json"), "r", encoding='utf-8') as f:
                dict_vacancies = json.load(f)
        elif switch == "3":
            with open(os.path.join("..", "files", "vacancies_by_same_or_bigger_salary.json"), "r", encoding='utf-8') as f:
                dict_vacancies = json.load(f)
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
            with open(os.path.join("..", "files", "vacancies_with_keywords.json"), "w", encoding='utf-8') as f:
                json.dump(dict_vacancies, f, ensure_ascii=False)
            print("Подходящие вакансии записаны в файл vacancies_with_keywords.json\n")




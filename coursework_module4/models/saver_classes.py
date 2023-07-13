import json
import os
from abc import ABC, abstractmethod


class Saver(ABC):

    @classmethod
    @abstractmethod
    def write_vacancies_json(cls, vacancies):
        pass

    @classmethod
    @abstractmethod
    def add_vacancies_json(cls, vacancies):
        pass

    @classmethod
    @abstractmethod
    def delete_vacancy(cls, vacancy_id):
        pass

    # @abstractmethod
    # def get_vacancies_be_equal_salary(self):
    #     pass
    #
    # @abstractmethod
    # def get_vacancies_by_bigger_salary(self):
    #     pass
    #
    # @abstractmethod
    # def delete_vacancy_by_id(self):
    #     pass


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
    def write_vacancies_json(cls, vacancies):
        json_vacancies_arr = cls.create_json_format(vacancies)
        dict_vacancies = {"items": json_vacancies_arr}
        cls.json_dump(dict_vacancies)

    @classmethod
    def add_vacancies_json(cls, vacancies_to_add):
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


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

    @classmethod
    def write_vacancies_json(cls, vacancies):
        json_vacancies_arr = cls.create_json_format(vacancies)
        dict_vacancies = {"items": json_vacancies_arr}

        with open(os.path.join("..", "files", "vacancies.json"), "w", encoding='utf-8') as f:
            json.dump(dict_vacancies, f, ensure_ascii=False)

    @classmethod
    def add_vacancies_json(cls, vacancies_to_add):
        with open(os.path.join("..", "files", "vacancies.json"), "r", encoding='utf-8') as f:
            dict_vacancies = json.load(f)
        old_vacancies = dict_vacancies["items"]
        new_vacancies = cls.create_json_format(vacancies_to_add)
        vacancies_total = old_vacancies + new_vacancies
        dict_vacancies["items"] = vacancies_total
        with open(os.path.join("..", "files", "vacancies.json"), "w", encoding='utf-8') as f:
            json.dump(dict_vacancies, f, ensure_ascii=False)

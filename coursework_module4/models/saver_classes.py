import json
import os
from abc import ABC, abstractmethod


class Saver(ABC):
    @abstractmethod
    def write_vacancies(self, vacancies):
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
    def write_vacancies(self, vacancies):
        with open(os.path.join("..", "files", "vacancies.json"), "w", encoding='utf-8') as f:
            json.dump(vacancies, f, ensure_ascii=False)


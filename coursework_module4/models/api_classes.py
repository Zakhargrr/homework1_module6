import os
from abc import ABC, abstractmethod

import requests as requests

superjob_api_key = os.getenv('SUPERJOB_API_KEY')


class VacancySiteAPI(ABC):
    @abstractmethod
    def get_vacancies(self, search_query, per_page):
        pass


class HeadHunterAPI(VacancySiteAPI):

    def __init__(self):
        self.__vacancies = None

    def get_vacancies(self, search_query, per_page):
        vacancies = requests.get(f'https://api.hh.ru/vacancies?area=113&text={search_query}&per_page={per_page}')
        self.__vacancies = vacancies.json()
        return self.__vacancies


class SuperJobAPI(VacancySiteAPI):
    def __init__(self):
        self.__vacancies = None

    def get_vacancies(self, search_query, per_page):
        headers = {'X-Api-App-Id': f'{superjob_api_key}'}
        vacancies = requests.get(f'https://api.superjob.ru/2.0/vacancies/?c=1&keyword={search_query}&count={per_page}',
                                 headers=headers)
        self.__vacancies = vacancies.json()
        return self.__vacancies

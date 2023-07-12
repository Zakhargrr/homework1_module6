import json
import os
from abc import ABC, abstractmethod

import requests as requests

superjob_api_key = os.getenv('SUPERJOB_API_KEY')


class VacancySiteAPI(ABC):
    @abstractmethod
    def get_vacancies(self, prog_lang):
        pass


class HeadHunterAPI(VacancySiteAPI):

    def __init__(self):
        self.vacancies = None

    def get_vacancies(self, prog_lang):
        vacancies = requests.get(f'https://api.hh.ru/vacancies?text={prog_lang}&per_page=100')
        self.vacancies = vacancies.json()
        return self.vacancies


class SuperJobAPI(VacancySiteAPI):
    def __init__(self):
        self.vacancies = None

    def get_vacancies(self, prog_lang):
        headers = {'X-Api-App-Id': f'{superjob_api_key}'}
        vacancies = requests.get(f'https://api.superjob.ru/2.0/vacancies/?keyword={prog_lang}&count=20',
                                 headers=headers)
        self.vacancies = vacancies.json()
        return self.vacancies

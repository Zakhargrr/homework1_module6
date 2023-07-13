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

# hh_r = HeadHunterAPI()
# hh_vacancies = hh_r.get_vacancies("Python")
#
# superjob_r = SuperJobAPI()
# superjob_vacancies = superjob_r.get_vacancies("Python")

#print(json.dumps(hh_vacancies))

# print(superjob_vacancies["objects"])

# for vacancy in superjob_vacancies["objects"]:
#     #print(vacancy)
#     print("Название вакансии:", vacancy["profession"])
#     print("Зарплата:", vacancy["payment_from"])
#     print("Требования:", vacancy["candidat"])
#     print("\n\n")
#
# with open("hh.json", "w", encoding='utf-8') as f:
#     json.dump(hh_vacancies, f, ensure_ascii=False)
#
# with open("hh.json", encoding='utf-8') as f:
#     print(json.dumps(hh_vacancies, indent=1, ensure_ascii=False))
#
# with open("superjob.json", "w", encoding='utf-8') as f:
#     json.dump(superjob_vacancies, f, ensure_ascii=False)
#
# with open("superjob.json", encoding='utf-8') as f:
#     print(json.dumps(superjob_vacancies, indent=1, ensure_ascii=False))

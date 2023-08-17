import requests


class HeadHunterAPI:

    def __init__(self):
        self.__vacancies = None
        self.__status_code = None

    def get_vacancies(self, employer_id, page):
        vacancies = requests.get(f'https://api.hh.ru/vacancies?employer_id={employer_id}&per_page=100&page={page}')
        self.__vacancies = vacancies.json()
        self.__status_code = vacancies.status_code
        return self.__vacancies, self.__status_code

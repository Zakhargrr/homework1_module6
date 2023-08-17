import psycopg2

from models.api_class import HeadHunterAPI
from models.vacancy_class import Vacancy


class DBManager:
    employers = ["yandex", "sberbank", "alfa_bank", "tinkoff", "vk", "kaspersky", "avito", "mts", "vtb", "ozon"]

    def __init__(self, db_name: str, password: str):
        self.__db_name = db_name
        self.__password = password

    @property
    def db_name(self):
        return self.__db_name

    @property
    def password(self):
        return self.__password

    def create_empty_table(self, employer_name: str):
        conn = self.get_connection()
        with conn.cursor() as cur:
            cur.execute(f"DROP TABLE IF EXISTS {employer_name}")
            cur.execute(f"""CREATE TABLE {employer_name} (
                                    vacancy_id int PRIMARY KEY,
                                    title varchar,
                                    url varchar,
                                    published_at date,
                                    salary_from int,
                                    salary_to int, 
                                    currency varchar,
                                    company_name varchar,
                                    requirements text
                                )""")
        conn.commit()

    def create_table(self, employer_name: str, employer_id: str):
        conn = self.get_connection()
        self.create_empty_table(employer_name)
        hh = HeadHunterAPI()
        page = 0
        with conn.cursor() as cur:
            while True:
                hh_dict, status_code = hh.get_vacancies(employer_id, page)
                if status_code == 400:
                    break
                hh_vacancies = hh_dict["items"]
                for hh_vacancy in hh_vacancies:
                    parsed_vacancy = Vacancy.initialize_hh_vacancy(hh_vacancy)
                    cur.execute(f"INSERT INTO {employer_name} VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                                (parsed_vacancy.vacancy_id, parsed_vacancy.title, parsed_vacancy.url,
                                 parsed_vacancy.published_at, parsed_vacancy.salary_from, parsed_vacancy.salary_to,
                                 parsed_vacancy.currency, parsed_vacancy.company_name, parsed_vacancy.requirements))

                if page == 4:
                    break
                page += 1
        conn.commit()
        conn.close()

    def get_connection(self):
        conn = psycopg2.connect(
            host="localhost",
            database=self.db_name,
            user="postgres",
            password=self.password  # 12345678
        )
        return conn

    def get_companies_and_vacancies_count(self):
        conn = self.get_connection()
        vacancies = []
        with conn.cursor() as cur:
            for employer in self.employers:
                cur.execute(f"SELECT company_name, COUNT(*) FROM {employer} GROUP BY company_name")
                response = cur.fetchall()
                vacancies += response
                # result += str(response[0][0]) + ": " + str(response[0][1]) + "\n"
        return vacancies

    def get_all_vacancies(self):
        conn = self.get_connection()
        vacancies = []
        with conn.cursor() as cur:
            for employer in self.employers:
                cur.execute(f"SELECT company_name, title, salary_from, salary_to, currency, url FROM {employer}")
                response = cur.fetchall()
                vacancies += response
        return vacancies

    def get_avg_salary(self):
        conn = self.get_connection()
        total_salary = 0
        counter = 0
        with conn.cursor() as cur:
            for employer in self.employers:
                cur.execute(f"SELECT (AVG(salary_from) + AVG(salary_to))/2 FROM {employer} WHERE currency = 'RUB'")
                current_avg_salary = cur.fetchall()
                if current_avg_salary[0][0] is not None:
                    total_salary += current_avg_salary[0][0]
                    counter += 1
        avg_salary = total_salary / counter
        return round(avg_salary, 4)

    def get_vacancies_with_higher_salary(self):
        conn = self.get_connection()
        avg_salary = self.get_avg_salary()
        vacancies = []
        with conn.cursor() as cur:
            for employer in self.employers:
                cur.execute(f"""SELECT company_name, title, salary_from, salary_to, currency, url FROM {employer}
                                                WHERE (salary_from > {avg_salary} OR salary_to > {avg_salary}) 
                                                AND currency = 'RUB'""")
                response = cur.fetchall()
                vacancies += response
        return vacancies

    def get_vacancies_with_keyword(self, keyword):
        conn = self.get_connection()
        vacancies = []
        with conn.cursor() as cur:
            for employer in self.employers:
                cur.execute(f"""SELECT company_name, title, salary_from, salary_to, currency, url FROM {employer} 
                                        WHERE title LIKE '%{keyword}%'""")
                response = cur.fetchall()
                vacancies += response
        return vacancies



from models.api_class import HeadHunterAPI
from models.vacancy_class import Vacancy


def create_empty_table(employer_name: str, conn):
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
                                requirements text
                            )""")


def create_table(employer_name: str, employer_id: str, conn):
    create_empty_table(employer_name, conn)
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
                cur.execute(f"INSERT INTO {employer_name} VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                            (parsed_vacancy.vacancy_id, parsed_vacancy.title, parsed_vacancy.url,
                             parsed_vacancy.published_at, parsed_vacancy.salary_from, parsed_vacancy.salary_to,
                             parsed_vacancy.currency, parsed_vacancy.requirements))

            if page == 4:
                break
            page += 1

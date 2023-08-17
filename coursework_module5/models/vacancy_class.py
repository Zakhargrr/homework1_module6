class Vacancy:

    def __init__(self, vacancy_id, title, url, published_at, salary_from, salary_to, currency, company_name,
                 requirements):
        """
        vacancy_id: ID вакансии
        title: Название вакансии
        url: Ссылка на вакансию
        published_at: Дата публикации вакансии
        salary_from: Нижняя планка зарплаты
        salary_to: Верхняя планка зарплаты
        currency: Валюта, в которой выплачивается зарплата
        company_name: Название компании
        requirements: Условия работы
        """
        self.__vacancy_id = vacancy_id
        self.__title: str = title
        self.__url: str = url
        self.__published_at = published_at
        self.__salary_from: str = salary_from
        self.__salary_to: str = salary_to
        self.__currency: str = currency
        self.__company_name: str = company_name
        self.__requirements: str = requirements

    @property
    def vacancy_id(self):
        return self.__vacancy_id

    @property
    def title(self):
        return self.__title

    @property
    def url(self):
        return self.__url

    @property
    def published_at(self):
        return self.__published_at

    @property
    def salary_from(self):
        return self.__salary_from

    @property
    def salary_to(self):
        return self.__salary_to

    @property
    def currency(self):
        return self.__currency

    @property
    def company_name(self):
        return self.__company_name

    @property
    def requirements(self):
        return self.__requirements

    @classmethod
    def initialize_hh_vacancy(cls, vacancy):
        """
        Получает массив вакансий с сайта HH.ru
        Создает массив, наполненный экземплярами класса Vacancy с полями,
        которые инициализированны данными, полуенными от API
        """
        vacancy_id = vacancy["id"]
        title = vacancy["name"]
        url = vacancy["apply_alternate_url"]
        published_at = vacancy["published_at"][:10]
        if vacancy["salary"] is None:
            salary_from = None
            salary_to = None
            currency = None
        else:
            if vacancy["salary"]["currency"] == "RUR":
                currency = "RUB"
            else:
                currency = vacancy["salary"]["currency"]

            if vacancy["salary"]["from"] is None:
                salary_from = None
                salary_to = int(vacancy["salary"]["to"])
            elif vacancy["salary"]["to"] is None:
                salary_from = int(vacancy["salary"]["from"])
                salary_to = None
            else:
                salary_from = int(vacancy["salary"]["from"])
                salary_to = int(vacancy["salary"]["to"])
        company_name = vacancy["employer"]["name"]

        if vacancy["snippet"]["requirement"] is None:
            requirement = ""
        else:
            requirement = vacancy["snippet"]["requirement"] + " "

        if vacancy["snippet"]["responsibility"] is None:
            responsibility = ""
        else:
            responsibility = vacancy["snippet"]["responsibility"]
        requirements = requirement + responsibility
        hh_vacancy = cls(vacancy_id, title, url, published_at, salary_from, salary_to, currency, company_name,
                         requirements)

        return hh_vacancy

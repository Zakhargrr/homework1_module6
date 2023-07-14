import datetime


class Vacancy:

    def __init__(self, vacancy_id, title, url, published_at, salary_from, salary_to, currency, address, requirements):
        """
        vacancy_id: ID вакансии
        title: Название вакансии
        url: Ссылка на вакансию
        published_at: Дата публикации вакансии
        salary_from: Нижняя планка зарплаты
        salary_to: Верхняя планка зарплаты
        currency: Валюта, в которой выплачивается зарплата
        address: Адрес работы
        requirements: Условия работы
        """
        self.__vacancy_id = vacancy_id
        self.__title: str = title
        self.__url: str = url
        self.__published_at = published_at
        self.__salary_from: int = salary_from
        self.__salary_to: int = salary_to

        if self.__salary_to == 0:
            if self.__salary_from == 0:
                self.__salary_to_compare = 0
            else:
                self.__salary_to_compare = self.__salary_from
        else:
            self.__salary_to_compare = self.__salary_to
        self.__currency: str = currency
        self.__address: str = address
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
    def salary_to_compare(self):
        return self.__salary_to_compare

    @property
    def currency(self):
        return self.__currency

    @property
    def address(self):
        return self.__address

    @property
    def requirements(self):
        return self.__requirements

    """
    Магические методы, отвечаюющие за сравнение вакансий по зарплате
    """
    def __lt__(self, other):
        if issubclass(other.__class__, self.__class__):
            if self.__salary_to_compare < other.__salary_to_compare:
                return True
            else:
                return False
        else:
            raise TypeError("Вторая вакансия не является экземпляром подходящего класса.")

    def __le__(self, other):
        if issubclass(other.__class__, self.__class__):
            if self.__salary_to_compare <= other.__salary_to_compare:
                return True
            else:
                return False
        else:
            raise TypeError("Вторая вакансия не является экземпляром подходящего класса.")

    def __eq__(self, other):
        if issubclass(other.__class__, self.__class__):
            if self.__salary_to_compare == other.__salary_to_compare:
                return True
            else:
                return False
        else:
            raise TypeError("Вторая вакансия не является экземпляром подходящего класса.")

    def __gt__(self, other):
        if issubclass(other.__class__, self.__class__):
            if self.__salary_to_compare > other.__salary_to_compare:
                return True
            else:
                return False
        else:
            raise TypeError("Вторая вакансия не является экземпляром подходящего класса.")

    def __ge__(self, other):
        if issubclass(other.__class__, self.__class__):
            if self.__salary_to_compare >= other.__salary_to_compare:
                return True
            else:
                return False
        else:
            raise TypeError("Вторая вакансия не является экземпляром подходящего класса.")

    @classmethod
    def initialize_hh_vacancies(cls, vacancies):
        """
        Получает массив вакансий с сайта HH.ru
        Создает массив, наполненный экземплярами класса Vacancy с полями,
        которые инициализированны данными, полуенными от API
        """
        arr_vacancies = []
        for vacancy in vacancies:
            vacancy_id = vacancy["id"]
            title = vacancy["name"]
            url = vacancy["apply_alternate_url"]
            data = vacancy["published_at"]
            published_at = data[8:10] + "." + data[5:7] + "." + data[0:4]
            if vacancy["salary"] is None:
                salary_from = 0
                salary_to = 0
                currency = ""
            else:
                if vacancy["salary"]["currency"] == "RUR":
                    currency = "RUB"
                else:
                    currency = vacancy["salary"]["currency"]

                if vacancy["salary"]["from"] is None:
                    salary_from = 0
                    salary_to = int(vacancy["salary"]["to"])
                elif vacancy["salary"]["to"] is None:
                    salary_from = int(vacancy["salary"]["from"])
                    salary_to = 0
                else:
                    salary_from = int(vacancy["salary"]["from"])
                    salary_to = int(vacancy["salary"]["to"])

            if vacancy["address"] is None:
                address = ""
            else:
                address = vacancy["address"]["raw"]

            if vacancy["snippet"]["requirement"] is None:
                requirement = ""
            else:
                requirement = "Требования: " + vacancy["snippet"]["requirement"] + "\n"

            if vacancy["snippet"]["responsibility"] is None:
                responsibility = ""
            else:
                responsibility = "Обязанности: " + vacancy["snippet"]["responsibility"]
            requirements = requirement + responsibility
            hh_vacancy = cls(vacancy_id, title, url, published_at, salary_from, salary_to, currency, address,
                             requirements)
            arr_vacancies.append(hh_vacancy)
        return arr_vacancies

    @classmethod
    def initialize_superjob_vacancies(cls, vacancies):
        """
        Получает массив вакансий с сайта SuperJob.ru
        Создает массив, наполненный экземплярами класса Vacancy с полями,
        которые инициализированны данными, полуенными от API
        """
        arr_vacancies = []
        for vacancy in vacancies:
            vacancy_id = str(vacancy["id"])
            title = vacancy["profession"]
            url = vacancy["link"]
            data = vacancy["date_published"]
            value = datetime.datetime.fromtimestamp(data)
            published_at = value.strftime('%d.%m.%Y')
            if vacancy["payment_to"] is None and vacancy["payment_from"] is None:
                salary_from = 0
                salary_to = 0
                currency = ""
            else:
                currency = vacancy["currency"].upper()
                if vacancy["payment_from"] is None:
                    salary_from = 0
                    salary_to = int(vacancy["payment_to"])

                elif vacancy["payment_to"] is None:
                    salary_from = int(vacancy["payment_from"])
                    salary_to = 0
                else:
                    salary_from = int(vacancy["payment_from"])
                    salary_to = int(vacancy["payment_to"])
            if vacancy["address"] is None:
                address = ""
            else:
                address = vacancy["address"]
            requirements = vacancy["candidat"]
            hh_vacancy = cls(vacancy_id, title, url, published_at, salary_from, salary_to, currency, address,
                             requirements)
            arr_vacancies.append(hh_vacancy)
        return arr_vacancies

    @staticmethod
    def get_top_vacancies(parsed_vacs_arr):
        """
        Получает массив экземпляров Vacancy
        Возвращает массив вакансий, отсортированных по убыванию зарплаты
        """
        if len(parsed_vacs_arr) == 0:
            print("В списке нет вакансий\n")
            return parsed_vacs_arr
        top_number = int(input("Введите чисо N вакансий: "))
        counter = 1
        sorted_arr = []
        while counter <= top_number:
            max_salary_vacancy = parsed_vacs_arr[0]

            for vacancy in parsed_vacs_arr:
                if vacancy >= max_salary_vacancy:
                    max_salary_vacancy = vacancy

            parsed_vacs_arr.remove(max_salary_vacancy)
            sorted_arr.append(max_salary_vacancy)
            counter += 1
            if len(parsed_vacs_arr) == 0:
                break

        print(f"Получен отсортированный список из {counter - 1} элементов\n")
        return sorted_arr

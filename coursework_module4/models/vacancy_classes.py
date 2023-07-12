class Vacancy:
    vacancy_id = 0

    def __init__(self, title, url, salary_from, salary_to, currency, address, requirements):
        self.__vacancy_id = Vacancy.vacancy_id
        Vacancy.vacancy_id += 1
        self.__title: str = title
        self.__url: str = url
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
        self._address: str = address
        self.__requirements: str = requirements

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





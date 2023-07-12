class Vacancy:

    def __init__(self, vacancy_id, title, url, published_at, salary_from, salary_to, currency, address, requirements):
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

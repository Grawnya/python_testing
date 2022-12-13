import requests
from datetime import date, timedelta

class Student:
    """ A Student class as a basis for method testing """

    def __init__(self, first_name, last_name):
        self._first_name = first_name # _ at start means read only
        self._last_name = last_name
        self._start_date = date.today()
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False

    @property
    def full_name(self):
        return f'{self._first_name} {self._last_name}'

    def alert_santa(self):
        self.naughty_list = True

    @property
    def email(self):
        email = f'{self._first_name}.{self._last_name}@email.com'
        return email.lower()

    def apply_extension(self, days):
        self.end_date += timedelta(days=days)

    def course_schedule(self):
        response = requests.get(f'https://company.com/course_schedule/{self._last_name}/{self._first_name}')

        if response.ok:
            return response.text
        else:
            return "Something went wrong with the request!"
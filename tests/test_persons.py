import time

import allure
from pytest import mark

from data.function_parameters import login_data
from pages.login_page import Login
from pages.persons_page import Persons


class TestAddPerson:
    @allure.title(f'Добавление физического лица под ролью АИБ')
    def test_add_person_aib(self, web_app):
        login_page = Login(web_app)
        login_page.navigate()
        login_page.login('smirnov', 'smirnovP@assw0rd')
        person_page = Persons(web_app)
        person_page.navigate()
        person_page.check_goto_persons()
        person_page.opening_form_add_person()
        person_page.check_opening_form_add_person()
        person_page.add_person('123')
        time.sleep(10)



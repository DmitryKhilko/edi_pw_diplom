import time

import allure
from pages.login_page import Login
from pages.persons_add_page import Persons


# уникальное значение email + card_id + key_id

class TestAddPerson:
    @allure.title(f'Добавление физического лица под ролью АИБ')
    def test_add_person_aib(self, web_app):
        login_page = Login(web_app)
        login_page.login_fast('smirnov', 'smirnovP@assw0rd')
        person_page = Persons(web_app)
        person_page.navigate()
        person_page.check_goto_persons()
        person_page.opening_form_add_person()
        person_page.check_opening_form_add_person()
        person_page.add_person('Павел', 'Иванович', 'Малашко', '11.02.1973', 'Женский', '21067', '733@333.com', '644', '755')
        person_page.to_be_visible_add_person('733@333.com')

        time.sleep(5)


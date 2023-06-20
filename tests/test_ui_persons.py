import logging

import allure
from pytest import mark

from data.data_ui_persons import *
from pages.login_page import Login
from pages.persons_create_page import Persons


# уникальное значение при добавлении физического лица: email + card_id + key_id

@allure.label('owner', 'khilko')
@allure.label('layer', 'ui')
@allure.label('module', 'Физические лица')
@allure.feature('Создание физического лица')
@allure.link('https://ivc-adsp.ivcmf.by/DefaultCollection/ISEB/_wiki/wikis/ISEB.wiki/32/'
             '%D0%9C%D0%B0%D1%82%D1%80%D0%B8%D1%86%D0%B0-%D1%80%D0%BE%D0%BB%D0%B5%D0%B9', '', 'Матрица ролей')
class TestUICreatePerson:
    @mark.parametrize('user, parameter_description, data', test_data_ui_cancel_create_person_valid_param)
    @allure.description(
        'Проверка нажатия кнопки "ОТМЕНИТЬ" на форме создания физического лица: заполнить форму валидными '
        'значениями обязательных для заполнения параметров и нажать кнопку "ОТМЕНА". '
        'При этом физическое лицо не должно быть создано'
    )
    @allure.id("1378")
    @allure.title('Отмена создания физ.лица (у роли есть права; валидные значения параметров)')
    def test_ui_cancel_create_person_valid_param(self, page, user, parameter_description, data, sql_delete_person_ui):
        logging.debug(f'Начать тест "Отмена создания физ.лица (у роли есть права; валидные значения параметров)" '
                      f'под ролью "{user[0]}"')
        login_page = Login(page)
        login_page.login(user)
        person_page = Persons(page)
        person_page.navigate()
        person_page.check_goto_persons()
        person_page.opening_form_create_person()
        person_page.check_opening_form_create_person()
        person_page.cancel_create_person(parameter_description, data)
        person_page.check_not_created_in_table_person(data)
        logging.debug(f'Окончить тест "Отмена создания физ.лица (у роли есть права; валидные значения параметров)" '
                      f'под ролью "{user[0]}"')

    @mark.parametrize('user, parameter_description, data', test_data_ui_can_create_person_valid_param)
    @allure.description(
        'Проверка возможности создания физического лица с использованием графического интерфейса '
        'для ролей пользователей, которым разрешено создание физического лица. Для создания физического '
        'лица используются комбинации валидных значений параметров'
    )
    @allure.id("1377")
    @allure.title('Создание физ.лица (у роли есть права; валидные значения параметров)')
    def test_ui_can_create_person_valid_param(self, page, user, parameter_description, data, sql_delete_person_ui):
        logging.debug(f'Начать тест "Создание физ.лица (у роли есть права; валидные значения параметров)" '
                      f'под ролью "{user[0]}"')
        login_page = Login(page)
        login_page.login(user)
        person_page = Persons(page)
        person_page.navigate()
        person_page.check_goto_persons()
        person_page.opening_form_create_person()
        person_page.check_opening_form_create_person()
        person_page.create_person(parameter_description, data)
        person_page.check_visible_in_table_created_person(data)
        person_page.check_create_person_in_db(data[6])

        logging.debug(f'Окончить тест "Создание физ.лица (у роли есть права; валидные значения параметров)" '
                      f'под ролью "{user[0]}"')

import logging

import allure
from pytest import mark

from data.data_ui_persons import *
from pages.login_page import Login
from pages.persons_page import Persons


@allure.label('owner', 'khilko')
@allure.label('layer', 'ui')
@allure.label('module', 'Физические лица')
@allure.feature('Список физических лиц')
@allure.link('https://ivc-adsp.ivcmf.by/DefaultCollection/ISEB/_wiki/wikis/ISEB.wiki/32/'
             '%D0%9C%D0%B0%D1%82%D1%80%D0%B8%D1%86%D0%B0-%D1%80%D0%BE%D0%BB%D0%B5%D0%B9', '', 'Матрица ролей')
class TestUIReadPersons:
    @mark.parametrize('user, expected_result', test_data_ui_visible_menu_item_persons)
    @allure.description(
        'Проверка возможности работы с физическими лицами с помощью web-интерфейса '
        'для ролей пользователей, которым разрешена работа с физическими лицами'
    )
    @allure.id("1380")
    @allure.title('Наличие пункта меню "Физические лица" (у роли есть права)')
    def test_ui_can_read_persons(self, page, user, expected_result):
        logging.debug(f'Начать тест "Наличие пункта меню "Физические лица" (у роли есть права)" '
                      f'под ролью "{user[0]}"')
        login_page = Login(page)
        login_page.login(user)
        person_page = Persons(page)
        person_page.check_visible_menu_item_persons(expected_result)
        person_page.goto_persons_page()
        person_page.check_goto_persons_page()
        logging.debug(f'Окончить тест "Наличие пункта меню "Физические лица" (у роли есть права)" '
                      f'под ролью "{user[0]}"')

    @mark.parametrize('user, expected_result', test_data_ui_not_visible_menu_item_persons)
    @allure.description(
        'Проверка невозможности работы с физическими лицами с помощью web-интерфейса '
        'для ролей пользователей, которым запрещена работа с физическими лицами'
    )
    @allure.id("1379")
    @allure.title('Отсутствие пункта меню "Физические лица" (у роли нет прав)')
    def test_ui_can_not_read_persons(self, page, user, expected_result):
        logging.debug(f'Начать тест "Отсутствие пункта меню "Физические лица" (у роли нет прав)" '
                      f'под ролью "{user[0]}"')
        login_page = Login(page)
        login_page.login(user)
        person_page = Persons(page)
        person_page.check_not_visible_menu_item_persons(expected_result)
        logging.debug(f'Окончить тест "Отсутствие пункта меню "Физические лица" (у роли нет прав)" '
                      f'под ролью "{user[0]}"')


@allure.label('owner', 'khilko')
@allure.label('layer', 'ui')
@allure.label('module', 'Физические лица')
@allure.feature('Создание физического лица')
@allure.link('https://ivc-adsp.ivcmf.by/DefaultCollection/ISEB/_wiki/wikis/ISEB.wiki/32/'
             '%D0%9C%D0%B0%D1%82%D1%80%D0%B8%D1%86%D0%B0-%D1%80%D0%BE%D0%BB%D0%B5%D0%B9', '', 'Матрица ролей')
class TestUICreatePerson:
    @mark.parametrize('user, parameter_description, data', test_data_ui_cancel_create_person_valid_param)
    @allure.description(
        'Проверка нажатия кнопки "Отменить" на форме создания физического лица: заполнить форму валидными '
        'значениями обязательных для заполнения параметров и нажать кнопку "Отменить". '
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
        person_page.goto_persons_page()
        person_page.check_goto_persons_page()
        person_page.opening_form_create_person()
        person_page.check_opening_form_create_person()
        person_page.cancel_create_person(parameter_description, data)
        person_page.check_not_created_person_in_ui(data[3])
        person_page.check_not_create_person_in_db(data[3])
        logging.debug(f'Окончить тест "Отмена создания физ.лица (у роли есть права; валидные значения параметров)" '
                      f'под ролью "{user[0]}"')

    @mark.parametrize('user, parameter_description, data, expected_result', test_data_ui_can_create_person_valid_param)
    @allure.description(
        'Проверка возможности создания физического лица с использованием графического интерфейса '
        'для ролей пользователей, которым разрешено создание физического лица. Для создания физического '
        'лица используются комбинации валидных значений параметров'
    )
    @allure.id("1377")
    @allure.title('Создание физ.лица (у роли есть права; валидные значения параметров)')
    def test_ui_can_create_person_valid_param(self, page, user, parameter_description, data, expected_result,
                                              sql_delete_person_ui):
        logging.debug(f'Начать тест "Создание физ.лица (у роли есть права; валидные значения параметров)" '
                      f'под ролью "{user[0]}"')
        login_page = Login(page)
        login_page.login(user)
        person_page = Persons(page)
        person_page.goto_persons_page()
        person_page.check_goto_persons_page()
        person_page.opening_form_create_person()
        person_page.check_opening_form_create_person()
        person_page.create_person(parameter_description, data)
        person_page.check_created_person_in_ui(data[6], expected_result)
        person_page.check_create_person_in_db(data[6])
        logging.debug(f'Окончить тест "Создание физ.лица (у роли есть права; валидные значения параметров)" '
                      f'под ролью "{user[0]}"')

    @mark.parametrize('user, parameter_description, data, expected_result',
                      test_data_ui_can_not_create_person_empty_param_required)
    @allure.description(
        'Проверка отказа в создании физического лица с помощью web-интерфейса для ролей пользователей, '
        'которым разрешено создавать физическое лицо, при использовании пустых значений обязательных для '
        'заполнения параметров'
    )
    @allure.id("1381")
    @allure.title('Отказ в создании физ.лица (у роли есть права; пустые значения обязательных параметров)')
    def test_ui_can_not_create_person_empty_param_required(self, page, user, parameter_description, data,
                                                           expected_result, sql_delete_person_ui):
        logging.debug(f'Начать тест "Отказ в создании физ.лица (у роли есть права; пустые значения обязательных '
                      f'параметров))" под ролью "{user[0]}"')
        login_page = Login(page)
        login_page.login(user)
        person_page = Persons(page)
        person_page.goto_persons_page()
        person_page.check_goto_persons_page()
        person_page.opening_form_create_person()
        person_page.check_opening_form_create_person()
        person_page.create_person(parameter_description, data)
        person_page.can_not_create_person_empty_param_required(expected_result)
        person_page.check_not_create_person_in_db(data[6])
        logging.debug(f'Окончить тест "Отказ в создании физ.лица (у роли есть права; пустые значения обязательных '
                      f'параметров)" под ролью "{user[0]}"')

    @mark.parametrize('user, parameter_description, data, expected_result',
                      test_data_ui_not_can_create_person_invalid_param)
    @allure.description(
        'Проверка отказа в создании физического лица с помощью web-интерфейса для ролей пользователей, '
        'которым разрешено создавать физическое лицо, при использовании не валидных значений параметров (внутри границ)'
    )
    @allure.id("1382")
    @allure.title('Отказ в создании физ.лица (у роли есть права; не валидные значения параметров внутри границ)')
    def test_ui_can_not_create_person_invalid_param(self, page, user, parameter_description, data,
                                                    expected_result, sql_delete_person_ui):
        logging.debug(f'Начать тест "Отказ в создании физ.лица (у роли есть права; не валидные значения параметров '
                      f'внутри границ)" под ролью "{user[0]}"')
        login_page = Login(page)
        login_page.login(user)
        person_page = Persons(page)
        person_page.goto_persons_page()
        person_page.check_goto_persons_page()
        person_page.opening_form_create_person()
        person_page.check_opening_form_create_person()
        person_page.create_person(parameter_description, data)
        person_page.check_can_not_create_person_invalid_param(expected_result)
        person_page.check_not_create_person_in_db(data[6])
        logging.debug(f'Окончить тест "Отказ в создании физ.лица (у роли есть права; не валидные значения параметров '
                      f'внутри границ)" под ролью "{user[0]}"')

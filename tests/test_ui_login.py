import logging
import allure
from pytest import mark
from pages.login_page import Login
from data.data_ui_login import *


@allure.label('owner', 'khilko')
@allure.label('layer', 'ui')
@allure.label('module', 'Вход в приложение')
@allure.feature('Авторизация по логину и паролю')
@allure.link('https://ivc-adsp.ivcmf.by/DefaultCollection/ISEB/_wiki/wikis/ISEB.wiki/32/'
             '%D0%9C%D0%B0%D1%82%D1%80%D0%B8%D1%86%D0%B0-%D1%80%D0%BE%D0%BB%D0%B5%D0%B9', '', 'Матрица ролей')
class TestUILogin:
    @mark.parametrize('user, parameter_description, expected_result', test_data_ui_can_login)
    @allure.description(
        'Проверка возможности входа в приложение c использованием графического интерфейса '
        'под всеми ролями приложения с валидными значениями логина и пароля'
    )
    @allure.id("1375")
    @allure.title('Вход в приложение (валидные значения логина и пароля)')
    def test_ui_can_login_by_role(self, web_app, user, parameter_description, expected_result):
        logging.debug(f'Начать тест "Вход в приложение (валидные значения логина и пароля)" для роли "{user[0]}"')
        login_page = Login(web_app)
        login_page.navigate()
        login_page.login_by_role(user, parameter_description)
        login_page.check_login(expected_result)
        logging.debug(f'Окончить тест "Вход в приложение (валидные значения логина и пароля)" для роли "{user[0]}"')

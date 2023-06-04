import logging

import allure
from pytest import mark

from data.login_data_api import test_data_can_login, test_data_can_not_login
from services.login_service import LoginService


@allure.label('owner', 'khilko')
@allure.label('layer', 'api')
@allure.label('module', 'Вход в приложение')
@allure.feature('Авторизация по логину и паролю')
@allure.link('https://ivc-adsp.ivcmf.by/DefaultCollection/ISEB/_wiki/wikis/ISEB.wiki/32/'
             '%D0%9C%D0%B0%D1%82%D1%80%D0%B8%D1%86%D0%B0-%D1%80%D0%BE%D0%BB%D0%B5%D0%B9', '', 'Матрица ролей')
class TestAPILogin:
    @mark.parametrize('user, message', test_data_can_login)
    @allure.description(
        'Проверка возможности входа в приложение с помощью API-запроса (POST) '
        'под всеми ролями приложения'
    )
    @allure.id("1371")
    @allure.title('api_Вход в приложение под всеми ролями')
    def test_api_can_login_by_role(self, user, message):
        logging.debug(f'Начать тест "api_Вход в приложение под всеми ролями" под ролью "{user[0]}"')
        LoginService.login_by_role(user, message, user[0])
        logging.debug(f'Окончить тест "api_Вход в приложение под всеми ролями" под ролью "{user[0]}"')

    @mark.parametrize('user, message', test_data_can_not_login)
    @allure.description(
        'Проверка невозможности входа в приложение с помощью API-запроса (POST) при использовании '
        'комбинаций не валидных логина и пароля'
    )
    @allure.id("1373")
    @allure.title('api_Отказ на вход в приложение (невалидные значения логина и пароля)')
    def test_api_can_not_login(self, user, message):
        logging.debug(f'Начать теста "api_Отказ на вход в приложение (невалидные значения логина и пароля)" '
                      f'под ролью "{user[0]}"')
        LoginService.can_not_login(user, message, user[0])
        logging.debug(f'Окончить теста "api_Отказ на вход в приложение (невалидные значения логина и пароля)" '
                      f'под ролью "{user[0]}"')

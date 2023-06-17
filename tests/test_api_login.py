import logging

import allure
from pytest import mark

from data.login_data_api import *
from services.login_service import LoginService


@allure.label('owner', 'khilko')
@allure.label('layer', 'api')
@allure.label('module', 'Вход в приложение')
@allure.feature('Авторизация по логину и паролю')
@allure.link('https://ivc-adsp.ivcmf.by/DefaultCollection/ISEB/_wiki/wikis/ISEB.wiki/32/'
             '%D0%9C%D0%B0%D1%82%D1%80%D0%B8%D1%86%D0%B0-%D1%80%D0%BE%D0%BB%D0%B5%D0%B9', '', 'Матрица ролей')
class TestAPILogin:
    @mark.parametrize('user, expected_result', test_data_can_login_api)
    @allure.description(
        'Проверка возможности входа в приложение с помощью API-запроса (POST) '
        'под всеми ролями приложения с валидными значениями логина и пароля'
    )
    @allure.id("1371")
    @allure.title('Вход в приложение')
    def test_api_can_login_by_role(self, user, expected_result):
        logging.debug(f'Начать тест "Вход в приложение" для роли "{user[0]}"')
        LoginService.login_by_role(user, expected_result, user[0])
        logging.debug(f'Окончить тест "Вход в приложение" для роли "{user[0]}"')

    @mark.parametrize('user, expected_result', test_data_can_not_login_api)
    @allure.description(
        'Проверка невозможности входа в приложение с помощью API-запроса (POST) под ролью АИБ '
        'в случае использования комбинаций не валидных (пустых) значений логина и (или) пароля'
    )
    @allure.id("1373")
    @allure.title('Невозможность входа в приложение (невалидные значения логина и пароля)')
    def test_api_can_not_login(self, user, expected_result):
        logging.debug(f'Начать теста "Невозможность входа в приложение (невалидные значения логина и пароля)" '
                      f'под ролью "{user[0]}"')
        LoginService.can_not_login(user, expected_result, user[0])
        logging.debug(f'Окончить теста "Невозможность входа в приложение (невалидные значения логина и пароля)" '
                      f'под ролью "{user[0]}"')

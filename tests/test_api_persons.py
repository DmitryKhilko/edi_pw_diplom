import logging

import allure
from pytest import mark

from data.persons_data_api import *
from services.login_service import LoginService
from services.persons_service import PersonsService


@allure.label('owner', 'khilko')
@allure.label('layer', 'api')
@allure.label('module', 'Физические лица')
@allure.feature('Список физических лиц')
@allure.link('https://ivc-adsp.ivcmf.by/DefaultCollection/ISEB/_wiki/wikis/ISEB.wiki/32/'
             '%D0%9C%D0%B0%D1%82%D1%80%D0%B8%D1%86%D0%B0-%D1%80%D0%BE%D0%BB%D0%B5%D0%B9', '', 'Матрица ролей')
class TestAPIGetPersons:
    @mark.parametrize('user, expected_result', test_data_api_can_read_persons)
    @allure.description(
        'Проверка возможности получения списка физических лиц с помощью API-запроса (GET) '
        'для ролей пользователей, которым разрешено получать и просматривать данный список'
    )
    @allure.id("1362")
    @allure.title('Получение списка физ.лиц (у роли есть права)')
    def test_api_can_read_persons(self, user, expected_result):
        logging.debug(f'Начать тест "Получение списка физ.лиц (у роли есть права)" под ролью "{user[0]}"')
        csrftoken, sessionid = LoginService.login(user, user[0])
        PersonsService.can_read_persons(csrftoken, sessionid, expected_result)
        logging.debug(f'Окончить тест "Получение списка физ.лиц (у роли есть права)" под ролью "{user[0]}"')

    @mark.parametrize('user, expected_result', test_data_api_can_not_read_persons)
    @allure.description(
        'Проверка отказа в получении списка физических лиц с помощью API-запроса (GET) '
        'для ролей пользователей, которым запрещено получать и просматривать данный список'
    )
    @allure.id("1355")
    @allure.title('Отказ в получении списка физ.лиц (у роли нет прав)')
    def test_api_can_not_read_persons(self, user, expected_result):
        logging.debug(f'Начать тест "Отказ в получении списка физ.лиц (у роли нет прав)" под ролью "{user[0]}"')
        csrftoken, sessionid = LoginService.login(user, user[0])
        PersonsService.can_not_read_persons(csrftoken, sessionid, expected_result, user[0])
        logging.debug(f'Окончить тест "Отказ в получении списка физ.лиц (у роли нет прав)" под ролью "{user[0]}"')


@allure.label('owner', 'khilko')
@allure.label('layer', 'api')
@allure.label('module', 'Физические лица')
@allure.feature('Создание физического лица')
@allure.link('https://ivc-adsp.ivcmf.by/DefaultCollection/ISEB/_wiki/wikis/ISEB.wiki/32/'
             '%D0%9C%D0%B0%D1%82%D1%80%D0%B8%D1%86%D0%B0-%D1%80%D0%BE%D0%BB%D0%B5%D0%B9', '', 'Матрица ролей')
class TestAPICreatePerson:
    @mark.parametrize('user, parameter_description, data, expected_result', test_data_api_can_create_person_valid_param)
    @allure.description(
        'Проверка возможности создания физического лица с помощью API-запроса (POST) для ролей пользователей, '
        'которым разрешено создание физического лица. Для создания физического лица используются комбинации '
        'валидных значений параметров'
    )
    @allure.id("1361")
    @allure.title('Создание физ.лица (у роли есть права; валидные значения параметров)')
    def test_api_can_create_person_valid_param(self, user, parameter_description, data, expected_result,
                                               sql_delete_person):
        logging.debug(f'Начать тест "Создание физ.лица (у роли есть права; валидные значения параметров)" '
                      f'под ролью "{user[0]}"')
        csrftoken, sessionid = LoginService.login(user, user[0])
        PersonsService.can_create_person_valid_param(csrftoken, sessionid, parameter_description, data, expected_result)
        logging.debug(f'Окончить тест "Создание физ.лица (у роли есть права; валидные значения параметров)" '
                      f'под ролью "{user[0]}"')

    @mark.parametrize('user, parameter_description, data, expected_result',
                      test_data_api_can_not_create_person_valid_param)
    @allure.description(
        'Проверка отказа в создании физического лица с помощью API-запроса (POST) для ролей пользователей, '
        'которым запрещено создание физического лица, при использовании используются комбинации валидных '
        'значений параметров'
    )
    @allure.id("1356")
    @allure.title('Отказ в создании физ.лица (у роли нет прав; валидные значения параметров)')
    def test_api_can_not_create_person_valid_param(self, user, parameter_description, data, expected_result,
                                                   sql_delete_person):
        logging.debug(f'Начать тест "Отказ в создании физ.лица (у роли нет прав; валидные значения параметров)" '
                      f'под ролью "{user[0]}"')
        csrftoken, sessionid = LoginService.login(user, user[0])
        PersonsService.can_not_create_person_valid_param(csrftoken, sessionid, parameter_description, data,
                                                         expected_result)
        logging.debug(f'Окончить тест "api_Отказ в создании физ.лица (у роли нет прав; валидные значения параметров)" '
                      f'под ролью "{user[0]}"')

    @mark.parametrize('user, parameter_description, data, expected_result',
                      test_data_api_can_not_create_person_empty_param_required)
    @allure.description(
        'Проверка отказа в создании физического лица с помощью API-запроса (POST) для ролей пользователей, '
        'которым разрешено создавать физическое лицо, при использовании пустых значений обязательных для '
        'заполнения параметров'
    )
    @allure.id("1363")
    @allure.title('Отказ в создании физ.лица (у роли есть права; пустые значения обязательных параметров)')
    def test_api_can_not_create_person_empty_param_required(self, user, parameter_description, data, expected_result,
                                                            sql_delete_person):
        logging.debug(f'Начать тест "Отказ в создании физ.лица (у роли есть права; пустые значения '
                      f'обязательных параметров)"')
        csrftoken, sessionid = LoginService.login(user, user[0])
        PersonsService.can_not_create_person_empty_param_required(csrftoken, sessionid, parameter_description, data,
                                                                  expected_result)
        logging.debug(f'Окончить тест "Отказ в создании физ.лица (у роли есть права; пустые значения '
                      f'обязательных параметров"')

    @mark.parametrize('user, parameter_description, data, expected_result',
                      test_data_api_can_not_create_person_invalid_param)
    @allure.description(
        'Проверка отказа в создании физического лица с помощью API-запроса (POST) для ролей пользователей, '
        'которым разрешено создавать физическое лицо, при использовании не валидных значений параметров (внутри границ)'
    )
    @allure.id("1368")
    @allure.title('Отказ в создании физ.лица (у роли есть права; не валидные значения параметров внутри границ)')
    def test_api_can_not_create_person_invalid_param_aib(self, user, parameter_description, data, expected_result,
                                                         sql_delete_person):
        logging.debug(f'Начать тест "Отказ в создании физ.лица (у роли есть права; не валидные значения параметров '
                      f'внутри границ)"')
        csrftoken, sessionid = LoginService.login(user, user[0])
        PersonsService.can_not_create_person_invalid_param(csrftoken, sessionid, parameter_description, data,
                                                           expected_result)
        logging.debug(f'Окончить тест "Отказ в создании физ.лица (у роли есть права; не валидные значения параметров '
                      f'внутри границ)"')

    @mark.parametrize('user, parameter_description, data, expected_result',
                      test_data_api_can_not_create_person_valid_param_out_of_limits)
    @allure.description(
        'Проверка отказа в создании физического лица с помощью API-запроса (POST) для ролей пользователей, '
        'которым разрешено создавать физическое лицо, при использовании комбинаций значений параметров, состоящих '
        'из валидных символов (значений), которые вышли за нижнюю или верхнюю границу параметра'
    )
    @allure.id("1369")
    @allure.title('Отказ в создании физ.лица (у роли есть права; валидные значения параметров вне границ)')
    def test_api_can_not_create_person_valid_param_out_of_limits(self, user, parameter_description, data,
                                                                 expected_result, sql_delete_person):
        logging.debug(f'Начать тест "Отказ в создании физ.лица (у роли есть права; валидные значения '
                      f'параметров вне границ)"')
        csrftoken, sessionid = LoginService.login(user, user[0])
        PersonsService.can_not_create_person_valid_param_out_of_limits(csrftoken, sessionid, parameter_description,
                                                                       data, expected_result)
        logging.debug(f'Окончить тест "Отказ в создании физ.лица (у роли есть права; валидные значения '
                      f'параметров вне границ)"')

    @mark.parametrize('user, parameter_description, data, expected_result',
                      test_data_api_can_not_create_person_invalid_param_out_of_limits)
    @allure.description(
        'Проверка возможности создания физического лица с помощью API-запроса (POST) для ролей пользователей, '
        'которым разрешено создание физического лица, при использовании комбинаций значений параметров, состоящих '
        'из не валидных символов (значений), которые вышли за нижнюю или верхнюю границу параметра'
    )
    @allure.id("1367")
    @allure.title('Отказ в создании физ.лица (у роли есть права; не валидные значения параметров вне границ)')
    def test_api_can_create_person_valid_param_at_limits(self, user, parameter_description, data, expected_result,
                                                         sql_delete_person):
        logging.debug(f'Начать тест "Отказ в создании физ.лица (у роли есть права; не валидные значения параметров '
                      f'вне границ)" под ролью "{user[0]}"')
        csrftoken, sessionid = LoginService.login(user, user[0])
        PersonsService.can_not_create_person_invalid_param_out_of_limits(csrftoken, sessionid, parameter_description,
                                                                         data, expected_result)
        logging.debug(f'Окончить тест "Отказ в создании физ.лица (у роли есть права; не валидные значения параметров '
                      f'вне границ)" под ролью "{user[0]}"')



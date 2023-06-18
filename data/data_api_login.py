import pytest

from settings import *

"""
Тестовые данные для параметризованных api-тестов. 
Тестовые данные предназначены для проверки входа в приложение под всеми ролями с валидными значениями логина и пароля. 
Структура кортежа: 
user (учетные данные пользователя), parameter_description (описание набора параметров для allure.step), 
expected_result (ожидаемый ответ сервера).
"""
test_data_api_can_login = (
    pytest.param((ROLE_NAME_AIB, LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
                 f'Войти в приложение под ролью "{ROLE_NAME_AIB}" с валидными логином и паролем',
                 (200, 'OK'),
                 marks=pytest.mark.smoke),

    pytest.param((ROLE_NAME_AIS, LOGIN_AIS, PASSWORD_AIS, EMAIL_ACCOUNT_AIS),
                 f'Войти в приложение под ролью "{ROLE_NAME_AIS}" с валидными логином и паролем',
                 (200, 'OK'),
                 marks=pytest.mark.smoke),

    pytest.param((ROLE_NAME_ASH, LOGIN_ASH, PASSWORD_ASH, EMAIL_ACCOUNT_ASH),
                 f'Войти в приложение под ролью "{ROLE_NAME_ASH}" с валидными логином и паролем',
                 (200, 'OK'),
                 marks=pytest.mark.smoke),

    pytest.param((ROLE_NAME_PSH, LOGIN_PSH, PASSWORD_PSH, EMAIL_ACCOUNT_PSH),
                 f'Войти в приложение под ролью "{ROLE_NAME_PSH}" с валидными логином и паролем',
                 (200, 'OK'),
                 marks=pytest.mark.smoke),

    pytest.param((ROLE_NAME_AMNS, LOGIN_AMNS, PASSWORD_AMNS, EMAIL_ACCOUNT_AMNS),
                 f'Войти в приложение под ролью "{ROLE_NAME_AMNS}" с валидными логином и паролем',
                 (200, 'OK'),
                 marks=pytest.mark.smoke),

    pytest.param((ROLE_NAME_OAMNS, LOGIN_OAMNS, PASSWORD_OAMNS, EMAIL_ACCOUNT_OAMNS),
                 f'Войти в приложение под ролью "{ROLE_NAME_OAMNS}" с валидными логином и паролем',
                 (200, 'OK'),
                 marks=pytest.mark.smoke),

    pytest.param((ROLE_NAME_RAMNS, LOGIN_RAMNS, PASSWORD_RAMNS, EMAIL_ACCOUNT_RAMNS),
                 f'Войти в приложение под ролью "{ROLE_NAME_RAMNS}" с валидными логином и паролем',
                 (200, 'OK'),
                 marks=pytest.mark.smoke),

    pytest.param((ROLE_NAME_PMNS, LOGIN_PMNS, PASSWORD_PMNS, EMAIL_ACCOUNT_PMNS),
                 f'Войти в приложение под ролью "{ROLE_NAME_PMNS}" с валидными логином и паролем',
                 (200, 'OK'),
                 marks=pytest.mark.smoke),

    pytest.param((ROLE_NAME_AGTK, LOGIN_AGTK, PASSWORD_AGTK, EMAIL_ACCOUNT_AGTK),
                 f'Войти в приложение под ролью "{ROLE_NAME_AGTK}" с валидными логином и паролем',
                 (200, 'OK'),
                 marks=pytest.mark.smoke),

    pytest.param((ROLE_NAME_PGTK, LOGIN_PGTK, PASSWORD_PGTK, EMAIL_ACCOUNT_PGTK),
                 f'Войти в приложение под ролью "{ROLE_NAME_PGTK}" с валидными логином и паролем',
                 (200, 'OK'),
                 marks=pytest.mark.smoke),
)

"""
Тестовые данные для параметризованных api-тестов. 
Тестовые данные предназначены для проверки входа в приложение под ролью АИБ с не валидными, пустыми значениями 
логина и (или) пароля. 
Структура кортежа: 
user (учетные данные пользователя), parameter_description (описание набора параметров для allure.step), 
expected_result (ожидаемый ответ сервера).
"""
test_data_api_can_not_login = (
    pytest.param((ROLE_NAME_AIB, LOGIN_AIB, 'invalid_password', EMAIL_ACCOUNT_AIB),
                 f'Войти в приложение под ролью "{ROLE_NAME_AIB}" с валидным логином и не валидным паролем',
                 (403, 'Forbidden', {'detail': 'Не найдено активной учетной записи с указанными данными.'}),
                 marks=pytest.mark.critical_path),

    pytest.param((ROLE_NAME_AIB, LOGIN_AIB, '', EMAIL_ACCOUNT_AIB),
                 f'Войти в приложение под ролью "{ROLE_NAME_AIB}" с валидным логином и пустым паролем',
                 (403, 'Forbidden', {'detail': 'Укажите логин и пароль.'}),
                 marks=pytest.mark.critical_path),

    pytest.param((ROLE_NAME_AIB, 'invalid_login', 'invalid_password', EMAIL_ACCOUNT_AIB),
                 f'Войти в приложение под ролью "{ROLE_NAME_AIB}" с не валидными логином и паролем',
                 (403, 'Forbidden', {'detail': 'Не найдено активной учетной записи с указанными данными.'}),
                 marks=pytest.mark.critical_path),

    pytest.param((ROLE_NAME_AIB, 'invalid_login', '', EMAIL_ACCOUNT_AIB),
                 f'Войти в приложение под ролью "{ROLE_NAME_AIB}" с не валидным логином и пустым паролем',
                 (403, 'Forbidden', {'detail': 'Укажите логин и пароль.'}),
                 marks=pytest.mark.critical_path),

    pytest.param((ROLE_NAME_AIB, 'invalid_login', PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
                 f'Войти в приложение под ролью "{ROLE_NAME_AIB}" с не валидным логином и валидным паролем',
                 (403, 'Forbidden', {'detail': 'Не найдено активной учетной записи с указанными данными.'}),
                 marks=pytest.mark.critical_path),

    pytest.param((ROLE_NAME_AIB, '', '', EMAIL_ACCOUNT_AIB),
                 f'Войти в приложение под ролью "{ROLE_NAME_AIB}" с пустыми логином и паролем',
                 (403, 'Forbidden', {'detail': 'Укажите логин и пароль.'}),
                 marks=pytest.mark.critical_path),

    pytest.param((ROLE_NAME_AIB, '', PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
                 f'Войти в приложение под ролью "{ROLE_NAME_AIB}" с пустым логином и валидным паролем',
                 (403, 'Forbidden', {'detail': 'Укажите логин и пароль.'}),
                 marks=pytest.mark.critical_path),

    pytest.param((ROLE_NAME_AIB, '', 'invalid_password', EMAIL_ACCOUNT_AIB),
                 f'Войти в приложение под ролью "{ROLE_NAME_AIB}" с пустым логином и не валидным паролем',
                 (403, 'Forbidden', {'detail': 'Укажите логин и пароль.'}),
                 marks=pytest.mark.critical_path),
)

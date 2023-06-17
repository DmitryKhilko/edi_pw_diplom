import pytest

from settings import *

"""
Тестовые данные для параметризованных api-тестов. 
Тестовые данные предназначены для проверки входа в приложение под всеми ролями с валидными значениями логина и пароля. 
Структура кортежа: user (учетные данные пользователя), expected_result (ожидаемый ответ сервера).
"""
test_data_can_login_api = (
    pytest.param((ROLE_NAME_AIB, LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
                 (200, 'OK'),
                 marks=pytest.mark.smoke, id="Вход под АИБ с валидным логином и паролем"),

    pytest.param((ROLE_NAME_AIS, LOGIN_AIS, PASSWORD_AIS, EMAIL_ACCOUNT_AIS),
                 (200, 'OK'),
                 marks=pytest.mark.smoke, id="Вход под АИС с валидным логином и паролем"),

    pytest.param((ROLE_NAME_ASH, LOGIN_ASH, PASSWORD_ASH, EMAIL_ACCOUNT_ASH),
                 (200, 'OK'),
                 marks=pytest.mark.smoke, id="Вход под АСХ с валидным логином и паролем"),

    pytest.param((ROLE_NAME_PSH, LOGIN_PSH, PASSWORD_PSH, EMAIL_ACCOUNT_PSH),
                 (200, 'OK'),
                 marks=pytest.mark.smoke, id="Вход под ПСХ с валидным логином и паролем"),

    pytest.param((ROLE_NAME_AMNS, LOGIN_AMNS, PASSWORD_AMNS, EMAIL_ACCOUNT_AMNS),
                 (200, 'OK'),
                 marks=pytest.mark.smoke, id="Вход под АМНС с валидным логином и паролем"),

    pytest.param((ROLE_NAME_OAMNS, LOGIN_OAMNS, PASSWORD_OAMNS, EMAIL_ACCOUNT_OAMNS),
                 (200, 'OK'),
                 marks=pytest.mark.smoke, id="Вход под ОАМНС с валидным логином и паролем"),

    pytest.param((ROLE_NAME_RAMNS, LOGIN_RAMNS, PASSWORD_RAMNS, EMAIL_ACCOUNT_RAMNS),
                 (200, 'OK'),
                 marks=pytest.mark.smoke, id="Вход под РАМНС с валидным логином и паролем"),

    pytest.param((ROLE_NAME_PMNS, LOGIN_PMNS, PASSWORD_PMNS, EMAIL_ACCOUNT_PMNS),
                 (200, 'OK'),
                 marks=pytest.mark.smoke, id="Вход под ПМНС с валидным логином и паролем"),

    pytest.param((ROLE_NAME_AGTK, LOGIN_AGTK, PASSWORD_AGTK, EMAIL_ACCOUNT_AGTK),
                 (200, 'OK'),
                 marks=pytest.mark.smoke, id="Вход под АГТК с валидным логином и паролем"),

    pytest.param((ROLE_NAME_PGTK, LOGIN_PGTK, PASSWORD_PGTK, EMAIL_ACCOUNT_PGTK),
                 (200, 'OK'),
                 marks=pytest.mark.smoke, id="Вход под ПГТК с валидным логином и паролем"),
)

"""
Тестовые данные для параметризованных api-тестов. 
Тестовые данные предназначены для проверки входа в приложение под ролью АИБ с не валидными, пустыми значениями 
логина и (или) пароля. 
Структура кортежа: user (учетные данные пользователя), expected_result (ожидаемый ответ сервера).
"""
test_data_can_not_login_api = (
    pytest.param((ROLE_NAME_AIB, LOGIN_AIB, 'invalid_password', EMAIL_ACCOUNT_AIB),
                 (403, 'Forbidden', {'detail': 'Не найдено активной учетной записи с указанными данными.'}),
                 marks=pytest.mark.critical_path, id="Вход под АИБ с не валидным паролем"),

    pytest.param((ROLE_NAME_AIB, LOGIN_AIB, '', EMAIL_ACCOUNT_AIB),
                 (403, 'Forbidden', {'detail': 'Укажите логин и пароль.'}),
                 marks=pytest.mark.critical_path, id="Вход под АИБ с пустым паролем"),

    pytest.param((ROLE_NAME_AIB, 'invalid_login', 'invalid_password', EMAIL_ACCOUNT_AIB),
                 (403, 'Forbidden', {'detail': 'Не найдено активной учетной записи с указанными данными.'}),
                 marks=pytest.mark.critical_path, id="Вход под АИБ с не валидным логином и паролем"),

    pytest.param((ROLE_NAME_AIB, 'invalid_login', '', EMAIL_ACCOUNT_AIB),
                 (403, 'Forbidden', {'detail': 'Укажите логин и пароль.'}),
                 marks=pytest.mark.critical_path, id="Вход под АИБ с не валидным логином и пустым паролем"),

    pytest.param((ROLE_NAME_AIB, 'invalid_login', PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
                 (403, 'Forbidden', {'detail': 'Не найдено активной учетной записи с указанными данными.'}),
                 marks=pytest.mark.critical_path, id="Вход под АИБ с не валидным логином"),

    pytest.param((ROLE_NAME_AIB, '', '', EMAIL_ACCOUNT_AIB),
                 (403, 'Forbidden', {'detail': 'Укажите логин и пароль.'}),
                 marks=pytest.mark.critical_path, id="Вход под АИБ с пустыми логином и паролем"),

    pytest.param((ROLE_NAME_AIB, '', PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
                 (403, 'Forbidden', {'detail': 'Укажите логин и пароль.'}),
                 marks=pytest.mark.critical_path, id="Вход под АИБ с пустым логином"),

    pytest.param((ROLE_NAME_AIB, '', 'invalid_password', EMAIL_ACCOUNT_AIB),
                 (403, 'Forbidden', {'detail': 'Укажите логин и пароль.'}),
                 marks=pytest.mark.critical_path, id="Вход под АИБ с пустым логином и не валидным паролем"),
)

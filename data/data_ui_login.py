import pytest

from settings import *

"""   
Константы, связанные с UI страницы логина.
Константа состоит из: названия метки поля ввода или названия кнопки; локатора поля ввода или кнопки
"""
FIELD_LOGIN = ('Логин', '//input[@name = "login"]')
FIELD_PASSWORD = ('Пароль', '//input[@name = "password"]')
BUTTON_LOGIN = ('Войти', '//button[text() = "Войти"]')

"""
Тестовые данные для параметризованных ui-тестов. 
Тестовые данные предназначены для проверки входа в приложение под всеми ролями с валидными значениями логина и пароля. 
Структура кортежа: user (учетные данные пользователя), parameter_description (описание набора параметров для 
allure.step), expected_result (ожидаемый результат).
"""
test_data_ui_can_login = (
    pytest.param((ROLE_NAME_AIB, LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
                 f'Войти в приложение под ролью "{ROLE_NAME_AIB}" с валидными логином и паролем',
                 (FIO_AIB, ROLE_NAME_AIB, ORGANIZATION_AIB),
                 marks=pytest.mark.smoke),

    pytest.param((ROLE_NAME_AIS, LOGIN_AIS, PASSWORD_AIS, EMAIL_ACCOUNT_AIS),
                 f'Войти в приложение под ролью "{ROLE_NAME_AIS}" с валидными логином и паролем',
                 (FIO_AIS, ROLE_NAME_AIS, ORGANIZATION_AIS),
                 marks=pytest.mark.smoke),

    pytest.param((ROLE_NAME_ASH, LOGIN_ASH, PASSWORD_ASH, EMAIL_ACCOUNT_ASH),
                 f'Войти в приложение под ролью "{ROLE_NAME_ASH}" с валидными логином и паролем',
                 (FIO_ASH, ROLE_NAME_ASH, ORGANIZATION_ASH),
                 marks=pytest.mark.smoke),

    pytest.param((ROLE_NAME_PSH, LOGIN_PSH, PASSWORD_PSH, EMAIL_ACCOUNT_PSH),
                 f'Войти в приложение под ролью "{ROLE_NAME_PSH}" с валидными логином и паролем',
                 (FIO_PSH, ROLE_NAME_PSH, ORGANIZATION_PSH),
                 marks=pytest.mark.smoke),

    pytest.param((ROLE_NAME_AMNS, LOGIN_AMNS, PASSWORD_AMNS, EMAIL_ACCOUNT_AMNS),
                 f'Войти в приложение под ролью "{ROLE_NAME_AMNS}" с валидными логином и паролем',
                 (FIO_AMNS, ROLE_NAME_AMNS, ORGANIZATION_AMNS),
                 marks=pytest.mark.smoke),

    pytest.param((ROLE_NAME_OAMNS, LOGIN_OAMNS, PASSWORD_OAMNS, EMAIL_ACCOUNT_OAMNS),
                 f'Войти в приложение под ролью "{ROLE_NAME_OAMNS}" с валидными логином и паролем',
                 (FIO_OAMNS, ROLE_NAME_OAMNS, ORGANIZATION_OAMNS),
                 marks=pytest.mark.smoke),

    pytest.param((ROLE_NAME_RAMNS, LOGIN_RAMNS, PASSWORD_RAMNS, EMAIL_ACCOUNT_RAMNS),
                 f'Войти в приложение под ролью "{ROLE_NAME_RAMNS}" с валидными логином и паролем',
                 (FIO_RAMNS, ROLE_NAME_RAMNS, ORGANIZATION_RAMNS),
                 marks=pytest.mark.smoke),

    pytest.param((ROLE_NAME_PMNS, LOGIN_PMNS, PASSWORD_PMNS, EMAIL_ACCOUNT_PMNS),
                 f'Войти в приложение под ролью "{ROLE_NAME_PMNS}" с валидными логином и паролем',
                 (FIO_PMNS, ROLE_NAME_PMNS, ORGANIZATION_PMNS),
                 marks=pytest.mark.smoke),

    pytest.param((ROLE_NAME_AGTK, LOGIN_AGTK, PASSWORD_AGTK, EMAIL_ACCOUNT_AGTK),
                 f'Войти в приложение под ролью "{ROLE_NAME_AGTK}" с валидными логином и паролем',
                 (FIO_AGTK, ROLE_NAME_AGTK, ORGANIZATION_AGTK),
                 marks=pytest.mark.smoke),

    pytest.param((ROLE_NAME_PGTK, LOGIN_PGTK, PASSWORD_PGTK, EMAIL_ACCOUNT_PGTK),
                 f'Войти в приложение под ролью "{ROLE_NAME_PGTK}" с валидными логином и паролем',
                 (FIO_PGTK, ROLE_NAME_PGTK, ORGANIZATION_PGTK),
                 marks=pytest.mark.smoke),

)

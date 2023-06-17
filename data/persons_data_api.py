import pytest

from utils.faker import Fake
from settings import *

f = Fake()

"""
Тестовые данные для параметризованных api-тестов. 
Данные предназначены для проверки получения списка физических лиц под ролями, которым разрешено получение списка. 
Структура кортежа: user (учетные данные пользователя), expected_result (ожидаемый ответ сервера).
"""
test_data_api_can_read_persons = (
    pytest.param((ROLE_NAME_AIB, LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
                 (200, 'OK'),
                 marks=pytest.mark.smoke, id="Получение списка физ.лиц под АИБ"),

    pytest.param((ROLE_NAME_AIS, LOGIN_AIS, PASSWORD_AIS, EMAIL_ACCOUNT_AIS),
                 (200, 'OK'),
                 marks=pytest.mark.smoke, id="Получение списка физ.лиц под АИС"),
)

"""
Тестовые данные для параметризованных api-тестов. 
Данные предназначены для проверки получения списка физических лиц под ролями, которым запрещено получение списка. 
Структура кортежа: user (учетные данные пользователя), expected_result (ожидаемый ответ сервера).
"""
test_data_api_can_not_read_persons = (
    pytest.param((ROLE_NAME_ASH, LOGIN_ASH, PASSWORD_ASH, EMAIL_ACCOUNT_ASH),
                 (403, 'Forbidden', {'detail': 'У вас недостаточно прав для выполнения данного действия.'}),
                 marks=pytest.mark.critical_path, id="Отказ в получении списка физ.лиц под АСХ"),

    pytest.param((ROLE_NAME_PSH, LOGIN_PSH, PASSWORD_PSH, EMAIL_ACCOUNT_PSH),
                 (403, 'Forbidden', {'detail': 'У вас недостаточно прав для выполнения данного действия.'}),
                 marks=pytest.mark.critical_path, id="Отказ в получении списка физ.лиц под ПСХ"),

    pytest.param((ROLE_NAME_AMNS, LOGIN_AMNS, PASSWORD_AMNS, EMAIL_ACCOUNT_AMNS),
                 (403, 'Forbidden', {'detail': 'У вас недостаточно прав для выполнения данного действия.'}),
                 marks=pytest.mark.critical_path, id="Отказ в получении списка физ.лиц под АМНС"),

    pytest.param((ROLE_NAME_OAMNS, LOGIN_OAMNS, PASSWORD_OAMNS, EMAIL_ACCOUNT_OAMNS),
                 (403, 'Forbidden', {'detail': 'У вас недостаточно прав для выполнения данного действия.'}),
                 marks=pytest.mark.critical_path, id="Отказ в получении списка физ.лиц под ОАМНС"),

    pytest.param((ROLE_NAME_RAMNS, LOGIN_RAMNS, PASSWORD_RAMNS, EMAIL_ACCOUNT_RAMNS),
                 (403, 'Forbidden', {'detail': 'У вас недостаточно прав для выполнения данного действия.'}),
                 marks=pytest.mark.critical_path, id="Отказ в получении списка физ.лиц под РАМНС"),

    pytest.param((ROLE_NAME_PMNS, LOGIN_PMNS, PASSWORD_PMNS, EMAIL_ACCOUNT_PMNS),
                 (403, 'Forbidden', {'detail': 'У вас недостаточно прав для выполнения данного действия.'}),
                 marks=pytest.mark.critical_path, id="Отказ в получении списка физ.лиц под ПМНС"),

    pytest.param((ROLE_NAME_AGTK, LOGIN_AGTK, PASSWORD_AGTK, EMAIL_ACCOUNT_AGTK),
                 (403, 'Forbidden', {'detail': 'У вас недостаточно прав для выполнения данного действия.'}),
                 marks=pytest.mark.critical_path, id="Отказ в получении списка физ.лиц под АГТК"),

    pytest.param((ROLE_NAME_PGTK, LOGIN_PGTK, PASSWORD_PGTK, EMAIL_ACCOUNT_PGTK),
                 (403, 'Forbidden', {'detail': 'У вас недостаточно прав для выполнения данного действия.'}),
                 marks=pytest.mark.critical_path, id="Отказ в получении списка физ.лиц под ПГТК"),
)

"""
Тестовые данные для параметризованных api-тестов. 
Данные предназначены для проверки создания физического лица под ролями, которым разрешено создание физического лица.
Для создания физического лица используются комбинации валидных значений параметров. 
Структура кортежа: 
user (учетные данные пользователя), parameter_description (значение allure.step), data (значения параметров физ.лица), 
expected_result (ожидаемый ответ сервера).
"""
test_data_api_can_create_person_valid_param = (
    pytest.param((ROLE_NAME_AIB, LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
                 'Создать физическое лицо с валидными значениями параметров (левая граница)',
                 (f.text('*person_first_name', 'min', 'valid'),
                  f.text('*person_last_name', 'min', 'valid'),
                  f.text('person_patronymic', 'min', 'valid'),
                  f.drop_down_list('person_sex', 'n', 'valid'),
                  f.date('person_birthday', 'min', 'valid'),
                  f.text('person_phone', 'min', 'valid'),
                  f.text('*person_email', 'min', 'valid'),
                  f.text('person_key_id', 'min', 'valid'),
                  f.text('person_card_id', 'min', 'valid')),
                 (201, 'Created'),
                 marks=pytest.mark.critical_path),

    pytest.param((ROLE_NAME_AIB, LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
                 'Создать физическое лицо с валидными значениями параметров (справа от левой границы)',
                 (f.text('*person_first_name', '>min', 'valid'),
                  f.text('*person_last_name', '>min', 'valid'),
                  f.text('person_patronymic', '>min', 'valid'),
                  f.drop_down_list('person_sex', 'n', 'valid'),
                  f.date('person_birthday', '>min', 'valid'),
                  f.text('person_phone', '>min', 'valid'),
                  f.text('*person_email', '>min', 'valid'),
                  f.text('person_key_id', '>min', 'valid'),
                  f.text('person_card_id', '>min', 'valid')),
                 (201, 'Created'),
                 marks=pytest.mark.critical_path),

    pytest.param((ROLE_NAME_AIB, LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
                 'Создать физическое лицо с валидными значениями параметров (внутри границ)',
                 (f.text('*person_first_name', 'n', 'valid'),
                  f.text('*person_last_name', 'n', 'valid'),
                  f.text('person_patronymic', 'n', 'valid'),
                  f.drop_down_list('person_sex', 'n', 'valid'),
                  f.date('person_birthday', 'n', 'valid'),
                  f.text('person_phone', 'n', 'valid'),
                  f.text('*person_email', 'n', 'valid'),
                  f.text('person_key_id', 'n', 'valid'),
                  f.text('person_card_id', 'n', 'valid')),
                 (201, 'Created'),
                 marks=pytest.mark.smoke),

    pytest.param((ROLE_NAME_AIB, LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
                 'Создать физическое лицо с валидными значениями параметров (слева от правой границы)',
                 (f.text('*person_first_name', '<max', 'valid'),
                  f.text('*person_last_name', '<max', 'valid'),
                  f.text('person_patronymic', '<max', 'valid'),
                  f.drop_down_list('person_sex', 'n', 'valid'),
                  f.date('person_birthday', '<max', 'valid'),
                  f.text('person_phone', '<max', 'valid'),
                  f.text('*person_email', '<max', 'valid'),
                  f.text('person_key_id', '<max', 'valid'),
                  f.text('person_card_id', '<max', 'valid')),
                 (201, 'Created'),
                 marks=pytest.mark.critical_path),

    pytest.param((ROLE_NAME_AIB, LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
                 'Создать физическое лицо с валидными значениями параметров (правая граница)',
                 (f.text('*person_first_name', 'max', 'valid'),
                  f.text('*person_last_name', 'max', 'valid'),
                  f.text('person_patronymic', 'max', 'valid'),
                  f.drop_down_list('person_sex', 'n', 'valid'),
                  f.date('person_birthday', 'max', 'valid'),
                  f.text('person_phone', 'max', 'valid'),
                  f.text('*person_email', 'max', 'valid'),
                  f.text('person_key_id', 'max', 'valid'),
                  f.text('person_card_id', 'max', 'valid')),
                 (201, 'Created'),
                 marks=pytest.mark.critical_path),

    pytest.param((ROLE_NAME_AIS, LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
                 'Создать физическое лицо с валидными значениями параметров (левая граница)',
                 (f.text('*person_first_name', 'min', 'valid'),
                  f.text('*person_last_name', 'min', 'valid'),
                  f.text('person_patronymic', 'min', 'valid'),
                  f.drop_down_list('person_sex', 'n', 'valid'),
                  f.date('person_birthday', 'min', 'valid'),
                  f.text('person_phone', 'min', 'valid'),
                  f.text('*person_email', 'min', 'valid'),
                  f.text('person_key_id', 'min', 'valid'),
                  f.text('person_card_id', 'min', 'valid')),
                 (201, 'Created'),
                 marks=pytest.mark.critical_path),

    pytest.param((ROLE_NAME_AIS, LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
                 'Создать физическое лицо с валидными значениями параметров (справа от левой границы)',
                 (f.text('*person_first_name', '>min', 'valid'),
                  f.text('*person_last_name', '>min', 'valid'),
                  f.text('person_patronymic', '>min', 'valid'),
                  f.drop_down_list('person_sex', 'n', 'valid'),
                  f.date('person_birthday', '>min', 'valid'),
                  f.text('person_phone', '>min', 'valid'),
                  f.text('*person_email', '>min', 'valid'),
                  f.text('person_key_id', '>min', 'valid'),
                  f.text('person_card_id', '>min', 'valid')),
                 (201, 'Created'),
                 marks=pytest.mark.critical_path),

    pytest.param((ROLE_NAME_AIS, LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
                 'Создать физическое лицо с валидными значениями параметров (внутри границ)',
                 (f.text('*person_first_name', 'n', 'valid'),
                  f.text('*person_last_name', 'n', 'valid'),
                  f.text('person_patronymic', 'n', 'valid'),
                  f.drop_down_list('person_sex', 'n', 'valid'),
                  f.date('person_birthday', 'n', 'valid'),
                  f.text('person_phone', 'n', 'valid'),
                  f.text('*person_email', 'n', 'valid'),
                  f.text('person_key_id', 'n', 'valid'),
                  f.text('person_card_id', 'n', 'valid')),
                 (201, 'Created'),
                 marks=pytest.mark.smoke),

    pytest.param((ROLE_NAME_AIS, LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
                 'Создать физическое лицо с валидными значениями параметров (слева от правой границы)',
                 (f.text('*person_first_name', '<max', 'valid'),
                  f.text('*person_last_name', '<max', 'valid'),
                  f.text('person_patronymic', '<max', 'valid'),
                  f.drop_down_list('person_sex', 'n', 'valid'),
                  f.date('person_birthday', '<max', 'valid'),
                  f.text('person_phone', '<max', 'valid'),
                  f.text('*person_email', '<max', 'valid'),
                  f.text('person_key_id', '<max', 'valid'),
                  f.text('person_card_id', '<max', 'valid')),
                 (201, 'Created'),
                 marks=pytest.mark.critical_path),

    pytest.param((ROLE_NAME_AIS, LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
                 'Создать физическое лицо с валидными значениями параметров (правая граница)',
                 (f.text('*person_first_name', 'max', 'valid'),
                  f.text('*person_last_name', 'max', 'valid'),
                  f.text('person_patronymic', 'max', 'valid'),
                  f.drop_down_list('person_sex', 'n', 'valid'),
                  f.date('person_birthday', 'max', 'valid'),
                  f.text('person_phone', 'max', 'valid'),
                  f.text('*person_email', 'max', 'valid'),
                  f.text('person_key_id', 'max', 'valid'),
                  f.text('person_card_id', 'max', 'valid')),
                 (201, 'Created'),
                 marks=pytest.mark.critical_path),
)

# Данные предназначены для параметризованных api-тестов по созданию физического лица для ролей
# пользователей, которым разрешено создание физического лица с помощью API-запроса. Для создания
# физического лица используются комбинации валидных значений параметров, находящихся на нижней и
# верхней границах значений параметров. Структура кортежа:
# users (учетные данные пользователя), data (параметры физического лица), message (ответ сервера)
test_data_can_add_person_valid_param_at_limits = (
    # # Проверка нижней границы значений параметров под АИБ (с email определиться)
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(2, True, ''), f.last_name(2, True, ''), f.patronymic(0, True, ''), f.sex(True, ''),
    #   f.date(True, None), f.phone(0, True, ''), f.email(20, True, ''), f.key_id(0, True, ''), f.card_id(0, True, '')),
    #  (201, 'Created')),
    # # Проверка нижней границы + 1 значений параметров под АИБ (с email определиться)
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(3, True, ''), f.last_name(3, True, ''), f.patronymic(1, True, ''), f.sex(True, ''), f.date(True, ''),
    #   f.phone(1, True, ''), f.email(20, True, ''), f.key_id(1, True, ''), f.card_id(1, True, '')),
    #  (201, 'Created')),
    # # Проверка верхней границы - 1 значений параметров под АИБ
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(49, True, ''), f.last_name(49, True, ''), f.patronymic(49, True, ''), f.sex(True, ''),
    #   f.date(True, ''), f.phone(12, True, ''), f.email(253, True, ''), f.key_id(39, True, ''), f.card_id(39, True, '')),
    #  (201, 'Created')),
    # # Проверка верхней границы значений параметров под АИБ
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(50, True, ''), f.last_name(50, True, ''), f.patronymic(50, True, ''), f.sex(True, ''),
    #   f.date(True, ''), f.phone(13, True, ''), f.email(254, True, ''), f.key_id(40, True, ''), f.card_id(40, True, '')),
    #  (201, 'Created')),
)

# Данные предназначены для параметризованных api-тестов по созданию физического лица под ролями,
# которым запрещено создание физического лица. Структура кортежа:
# users (учетные данные пользователя), data (параметры физического лица), message (ответ сервера)
test_data_can_not_add_person_valid_param_inside_limits = (
    # (('Администратор СХ', LOGIN_ASH, PASSWORD_ASH, EMAIL_ACCOUNT_ASH),
    #  (f.first_name(10, True, ''), f.last_name(10, True, ''), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, ''), f.phone(13, True, ''), f.email(20, True, ''), f.key_id(40, True, ''), f.card_id(40, True, '')),
    #  (403, 'Forbidden', {'detail': 'У вас недостаточно прав для выполнения данного действия.'})),
    # (('Пользователь СХ', LOGIN_PSH, PASSWORD_PSH, EMAIL_ACCOUNT_PSH),
    #  (f.first_name(10, True, ''), f.last_name(10, True, ''), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, ''), f.phone(13, True, ''), f.email(20, True, ''), f.key_id(40, True, ''), f.card_id(40, True, '')),
    #  (403, 'Forbidden', {'detail': 'У вас недостаточно прав для выполнения данного действия.'})),
    # (('Администратор МНС', LOGIN_AMNS, PASSWORD_AMNS, EMAIL_ACCOUNT_AMNS),
    #  (f.first_name(10, True, ''), f.last_name(10, True, ''), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, ''), f.phone(13, True, ''), f.email(20, True, ''), f.key_id(40, True, ''), f.card_id(40, True, '')),
    #  (403, 'Forbidden', {'detail': 'У вас недостаточно прав для выполнения данного действия.'})),
    # (('Областной администратор МНС', LOGIN_OAMNS, PASSWORD_OAMNS, EMAIL_ACCOUNT_OAMNS),
    #  (f.first_name(10, True, ''), f.last_name(10, True, ''), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, ''), f.phone(13, True, ''), f.email(20, True, ''), f.key_id(40, True, ''), f.card_id(40, True, '')),
    #  (403, 'Forbidden', {'detail': 'У вас недостаточно прав для выполнения данного действия.'})),
    # (('Районный администратор МНС', LOGIN_RAMNS, PASSWORD_RAMNS, EMAIL_ACCOUNT_RAMNS),
    #  (f.first_name(10, True, ''), f.last_name(10, True, ''), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, ''), f.phone(13, True, ''), f.email(20, True, ''), f.key_id(40, True, ''), f.card_id(40, True, '')),
    #  (403, 'Forbidden', {'detail': 'У вас недостаточно прав для выполнения данного действия.'})),
    # (('Пользователь МНС', LOGIN_PMNS, PASSWORD_PMNS, EMAIL_ACCOUNT_PMNS),
    #  (f.first_name(10, True, ''), f.last_name(10, True, ''), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, ''), f.phone(13, True, ''), f.email(20, True, ''), f.key_id(40, True, ''), f.card_id(40, True, '')),
    #  (403, 'Forbidden', {'detail': 'У вас недостаточно прав для выполнения данного действия.'})),
    # (('Администратор ГТК', LOGIN_AGTK, PASSWORD_AGTK, EMAIL_ACCOUNT_AGTK),
    #  (f.first_name(10, True, ''), f.last_name(10, True, ''), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, ''), f.phone(13, True, ''), f.email(20, True, ''), f.key_id(40, True, ''), f.card_id(40, True, '')),
    #  (403, 'Forbidden', {'detail': 'У вас недостаточно прав для выполнения данного действия.'})),
    # (('Пользователь ГТК', LOGIN_PGTK, PASSWORD_PGTK, EMAIL_ACCOUNT_PGTK),
    #  (f.first_name(10, True, ''), f.last_name(10, True, ''), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, ''), f.phone(13, True, ''), f.email(20, True, ''), f.key_id(40, True, ''), f.card_id(40, True, '')),
    #  (403, 'Forbidden', {'detail': 'У вас недостаточно прав для выполнения данного действия.'})),
)

# Данные предназначены для параметризованных api-тестов по проверке невозможности создания
# физического лица под АИБ с пустыми значениями обязательных для заполнения параметров: фамилия,
# имя, email. Структура кортежа:
# users (учетные данные пользователя), data (параметры физического лица), message (ответ сервера)
test_data_can_not_add_person_empty_param_required_aib = (
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(0, False, ''), f.last_name(10, True, ''), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, ''), f.phone(13, True, ''), f.email(20, True, ''), f.key_id(40, True, ''), f.card_id(40, True, '')),
    #  (400, 'Bad Request', {'first_name': ['Это поле не может быть пустым.']})),
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(10, True, ''), f.last_name(0, False, ''), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, ''), f.phone(13, True, ''), f.email(20, True, ''), f.key_id(40, True, ''), f.card_id(40, True, '')),
    #  (400, 'Bad Request', {'last_name': ['Это поле не может быть пустым.']})),
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(10, True, ''), f.last_name(10, True, ''), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, ''), f.phone(13, True, ''), f.email(0, False, ''), f.key_id(40, True, ''), f.card_id(40, True, '')),
    #  (400, 'Bad Request', {'email': ['Вы не можете создать физическое лицо с пустым email.']})),
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(0, False, ''), f.last_name(0, False, ''), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, ''), f.phone(13, True, ''), f.email(0, False, ''), f.key_id(40, True, ''), f.card_id(40, True, '')),
    #  (400, 'Bad Request', {'first_name': ['Это поле не может быть пустым.'],
    #                        'last_name': ['Это поле не может быть пустым.'],
    #                        'email': ['Вы не можете создать физическое лицо с пустым email.']})),
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(0, False, ''), f.last_name(0, False, ''), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, ''), f.phone(13, True, ''), f.email(20, True, ''), f.key_id(40, True, ''), f.card_id(40, True, '')),
    #  (400, 'Bad Request', {'first_name': ['Это поле не может быть пустым.'],
    #                        'last_name': ['Это поле не может быть пустым.']})),
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(10, True, ''), f.last_name(0, False, ''), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, ''), f.phone(13, True, ''), f.email(0, False, ''), f.key_id(40, True, ''), f.card_id(40, True, '')),
    #  (400, 'Bad Request', {'last_name': ['Это поле не может быть пустым.'],
    #                        'email': ['Вы не можете создать физическое лицо с пустым email.']})),
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(0, False, ''), f.last_name(10, True, ''), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, ''), f.phone(13, True, ''), f.email(0, False, ''), f.key_id(40, True, ''), f.card_id(40, True, '')),
    #  (400, 'Bad Request', {'first_name': ['Это поле не может быть пустым.'],
    #                        'email': ['Вы не можете создать физическое лицо с пустым email.']})),
)

# Данные предназначены для параметризованных api-тестов по проверке невозможности создания
# физического лица под АИБ с не валидными значениями параметров или при выходе значения
# параметра за нижнюю или верхнюю границу параметра. Структура кортежа:
# users (учетные данные пользователя), data (параметры физического лица), message (ответ сервера)
test_data_can_not_add_person_invalid_param_aib = (
    # # Имя без пробела и с не валидными символами
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(10, False, ''), f.last_name(10, True, ''), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, ''), f.phone(13, True, ''), f.email(20, True, ''), f.key_id(40, True, ''), f.card_id(40, True, '')),
    #  (400, 'Bad Request', {'first_name': ['Имя должно содержать только буквы кириллицы, пробел и знак дефиса.']})),
    #
    # # Фамилия с пробелом и с не валидными символами
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(10, True, ''), f.last_name(10, False, 'Khil1 %ko'), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, ''), f.phone(13, True, ''), f.email(20, True, ''), f.key_id(40, True, ''), f.card_id(40, True, '')),
    #  (400, 'Bad Request', {'last_name': ['Фамилия не должна содержать пробелов.']})),
    #
    # # Фамилия без пробела и с невалидными символами
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(10, True, ''), f.last_name(10,False, 'K!hil&ko'), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, ''), f.phone(13, True, ''), f.email(20, True, ''), f.key_id(40, True, ''), f.card_id(40, True, '')),
    #  (400, 'Bad Request', {'first_name': ['Фамилия должна содержать только буквы кириллицы и знак дефиса.']})),
    #
    # # Отчество без пробела и с невалидными символами
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(10, True, ''), f.last_name(10, True, ''), f.patronymic(10,False, 'Ni^kola{evich'), f.sex(True, ''),
    #   f.date(True, ''), f.phone(13, True, ''), f.email(20, True, ''), f.key_id(40, True, ''), f.card_id(40, True, '')),
    #  (400, 'Bad Request', {'patronymic': ['Отчество должно содержать только буквы кириллицы, пробел и знак дефиса.']})),
    #
    # # Некорректное значение пола
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(10, True, ''), f.last_name(10, True, ''), f.patronymic(10, True, ''), f.sex(True, 'мужской'),
    #   f.date(True, ''), f.phone(13, True, ''), f.email(20, True, ''), f.key_id(40, True, ''), f.card_id(40, True, '')),
    #  (400, 'Bad Request', {'sex': ['Значения мужской нет среди допустимых вариантов.']})),
    #
    # # Некорректное значение пола
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(10, True, ''), f.last_name(10, True, ''), f.patronymic(10, True, ''), f.sex(True, -1),
    #   f.date(True, ''), f.phone(13, True, ''), f.email(20, True, ''), f.key_id(40, True, ''), f.card_id(40, True, '')),
    #  (400, 'Bad Request', {'sex': ['Значения -1 нет среди допустимых вариантов.']})),
    #
    # # Некорректное значение пола
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(10, True, ''), f.last_name(10, True, ''), f.patronymic(10, True, ''), f.sex(True, 2),
    #   f.date(True, ''), f.phone(13, True, ''), f.email(20, True, ''), f.key_id(40, True, ''), f.card_id(40, True, '')),
    #  (400, 'Bad Request', {'sex': ['Значения 2 нет среди допустимых вариантов.']})),
    #
    # # Пустое значение пола
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(10, True, ''), f.last_name(10, True, ''), f.patronymic(10, True, ''), f.sex(True, None),
    #   f.date(True, ''), f.phone(13, True, ''), f.email(20, True, ''), f.key_id(40, True, ''), f.card_id(40, True, '')),
    #  (400, 'Bad Request', {'sex': ['Это поле не может быть пустым.']})),
    #
    # # Некорректное значение даты рождения
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(10, True, ''), f.last_name(10, True, ''), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, 'дата'), f.phone(13, True, ''), f.email(20, True, ''), f.key_id(40, True, ''),
    #   f.card_id(40, True, '')),
    #  (400, 'Bad Request',
    #   {'birth_date': ['Неправильный формат date. Используйте один из этих форматов: YYYY-MM-DD, DD.MM.YYYY.']})),
    #
    # # Некорректное значение даты рождения
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(10, True, ''), f.last_name(10, True, ''), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, ' '), f.phone(13, True, ''), f.email(20, True, ''), f.key_id(40, True, ''),
    #   f.card_id(40, True, '')),
    #  (400, 'Bad Request',
    #   {'birth_date': ['Неправильный формат date. Используйте один из этих форматов: YYYY-MM-DD, DD.MM.YYYY.']})),
    #
    # # Некорректное значение даты рождения
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(10, True, ''), f.last_name(10, True, ''), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, 0), f.phone(13, True, ''), f.email(20, True, ''), f.key_id(40, True, ''),
    #   f.card_id(40, True, '')),
    #  (400, 'Bad Request',
    #   {'birth_date': ['Неправильный формат date. Используйте один из этих форматов: YYYY-MM-DD, DD.MM.YYYY.']})),
    #
    # # Некорректное значение даты рождения
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(10, True, ''), f.last_name(10, True, ''), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, 1234567890), f.phone(13, True, ''), f.email(20, True, ''), f.key_id(40, True, ''),
    #   f.card_id(40, True, '')),
    #  (400, 'Bad Request',
    #   {'birth_date': ['Неправильный формат date. Используйте один из этих форматов: YYYY-MM-DD, DD.MM.YYYY.']})),
    #
    # # Некорректное значение даты рождения
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(10, True, ''), f.last_name(10, True, ''), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, '00.00.0000'), f.phone(13, True, ''), f.email(20, True, ''), f.key_id(40, True, ''),
    #   f.card_id(40, True, '')),
    #  (400, 'Bad Request',
    #   {'birth_date': ['Неправильный формат date. Используйте один из этих форматов: YYYY-MM-DD, DD.MM.YYYY.']})),
    #
    # # Некорректное значение даты рождения
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(10, True, ''), f.last_name(10, True, ''), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, '00.03.1973'), f.phone(13, True, ''), f.email(20, True, ''), f.key_id(40, True, ''),
    #   f.card_id(40, True, '')),
    #  (400, 'Bad Request',
    #   {'birth_date': ['Неправильный формат date. Используйте один из этих форматов: YYYY-MM-DD, DD.MM.YYYY.']})),
    #
    # # Некорректное значение даты рождения
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(10, True, ''), f.last_name(10, True, ''), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, '12.00.1973'), f.phone(13, True, ''), f.email(20, True, ''), f.key_id(40, True, ''),
    #   f.card_id(40, True, '')),
    #  (400, 'Bad Request',
    #   {'birth_date': ['Неправильный формат date. Используйте один из этих форматов: YYYY-MM-DD, DD.MM.YYYY.']})),
    #
    # # Некорректное значение даты рождения
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(10, True, ''), f.last_name(10, True, ''), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, '12.03.0000'), f.phone(13, True, ''), f.email(20, True, ''), f.key_id(40, True, ''),
    #   f.card_id(40, True, '')),
    #  (400, 'Bad Request',
    #   {'birth_date': ['Неправильный формат date. Используйте один из этих форматов: YYYY-MM-DD, DD.MM.YYYY.']})),
    #
    # # Некорректное значение даты рождения
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(10, True, ''), f.last_name(10, True, ''), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, '99.99.9999'), f.phone(13, True, ''), f.email(20, True, ''), f.key_id(40, True, ''),
    #   f.card_id(40, True, '')),
    #  (400, 'Bad Request',
    #   {'birth_date': ['Неправильный формат date. Используйте один из этих форматов: YYYY-MM-DD, DD.MM.YYYY.']})),
    #
    # # Некорректное значение даты рождения
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(10, True, ''), f.last_name(10, True, ''), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, 'dd.mm.yyyy'), f.phone(13, True, ''), f.email(20, True, ''), f.key_id(40, True, ''),
    #   f.card_id(40, True, '')),
    #  (400, 'Bad Request',
    #   {'birth_date': ['Неправильный формат date. Используйте один из этих форматов: YYYY-MM-DD, DD.MM.YYYY.']})),
    #
    # # Некорректное значение даты рождения
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(10, True, ''), f.last_name(10, True, ''), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, 'dd.03.1973'), f.phone(13, True, ''), f.email(20, True, ''), f.key_id(40, True, ''),
    #   f.card_id(40, True, '')),
    #  (400, 'Bad Request',
    #   {'birth_date': ['Неправильный формат date. Используйте один из этих форматов: YYYY-MM-DD, DD.MM.YYYY.']})),
    #
    # # Некорректное значение даты рождения
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(10, True, ''), f.last_name(10, True, ''), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, '12.mm.1973'), f.phone(13, True, ''), f.email(20, True, ''), f.key_id(40, True, ''),
    #   f.card_id(40, True, '')),
    #  (400, 'Bad Request',
    #   {'birth_date': ['Неправильный формат date. Используйте один из этих форматов: YYYY-MM-DD, DD.MM.YYYY.']})),
    #
    # # Некорректное значение даты рождения
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(10, True, ''), f.last_name(10, True, ''), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, '12.03.yyyy'), f.phone(13, True, ''), f.email(20, True, ''), f.key_id(40, True, ''),
    #   f.card_id(40, True, '')),
    #  (400, 'Bad Request',
    #   {'birth_date': ['Неправильный формат date. Используйте один из этих форматов: YYYY-MM-DD, DD.MM.YYYY.']})),
    #
    # # Некорректное значение даты рождения
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(10, True, ''), f.last_name(10, True, ''), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, '12/03/1973'), f.phone(13, True, ''), f.email(20, True, ''), f.key_id(40, True, ''),
    #   f.card_id(40, True, '')),
    #  (400, 'Bad Request',
    #   {'birth_date': ['Неправильный формат date. Используйте один из этих форматов: YYYY-MM-DD, DD.MM.YYYY.']})),
    #
    # # Некорректное значение телефона
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(10, True, ''), f.last_name(10, True, ''), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, ''), f.phone(13, False, ''), f.email(20, True, ''), f.key_id(40, True, ''), f.card_id(40, True, '')),
    #  (400, 'Bad Request',
    #   {'phone': ['Телефон может содержать до 12 цифр без пробелов; допускается символ «+» в начале строки.']})),
    #
    # # Некорректное значение email
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(10, True, ''), f.last_name(10, True, ''), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, ''), f.phone(13, True, ''), f.email(20, False, ''), f.key_id(40, True, ''), f.card_id(40, True, '')),
    #  (400, 'Bad Request', {'email': ['Введите правильный адрес электронной почты.']})),
    #
    # # Некорректное значение key_id
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(10, True, ''), f.last_name(10, True, ''), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, ''), f.phone(13, True, ''), f.email(20, True, ''), f.key_id(40, False, ''), f.card_id(40, True, '')),
    #  (400, 'Bad Request', {'key_id': ['Идентификатор ключа должен содержать только латинские буквы и цифры']})),
    #
    # # Некорректное значение card_id
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(10, True, ''), f.last_name(10, True, ''), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, ''), f.phone(13, True, ''), f.email(20, True, ''), f.key_id(40, True, ''), f.card_id(40, False, '')),
    #  (400, 'Bad Request', {'card_id ': ['Идентификатор ID карты должен содержать только латинские буквы и цифры']})),
)

# Данные предназначены для параметризованных api-тестов по проверке невозможности создания
# физического лица под АИБ со значениями параметров состоящих из валидных и не валидных символов,
# которые вышли за нижнюю или верхнюю границу параметра. Структура кортежа:
# users (учетные данные пользователя), data (параметры физического лица), message (ответ сервера)
test_data_can_add_person_param_out_of_limits_aib = (

    # # Параметр first_name: символы валидные, длина ниже нижней границы
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(1, True, ''), f.last_name(10, True, ''), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, ''), f.phone(13, True, ''), f.email(10, True, ''), f.key_id(10, True, ''), f.card_id(10, True, '')),
    #  (400, 'Bad Request', {'first_name': ['Убедитесь, что это значение содержит от 2 до 50 символов.']})),
    #
    # # Параметр first_name: символы не валидные, длина ниже нижней границы
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(1, False, ''), f.last_name(10, True, ''), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, ''), f.phone(13, True, ''), f.email(10, True, ''), f.key_id(10, True, ''), f.card_id(10, True, '')),
    #  (400, 'Bad Request', {'first_name': ['Убедитесь, что это значение содержит от 2 до 50 символов.',
    #                                       'Имя должно содержать только буквы кириллицы, пробел и знак дефиса.']})),
    #
    # # Параметр first_name: символы валидные, длина выше верхней границы
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(51, True, ''), f.last_name(10, True, ''), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, ''), f.phone(13, True, ''), f.email(10, True, ''), f.key_id(10, True, ''), f.card_id(10, True, '')),
    #  (400, 'Bad Request', {'first_name': ['Убедитесь, что это значение содержит не более 50 символов.']})),
    #
    # # Параметр first_name: символы не валидные, длина выше верхней границы
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(51, False, ''), f.last_name(10, True, ''), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, ''), f.phone(13, True, ''), f.email(10, True, ''), f.key_id(10, True, ''), f.card_id(10, True, '')),
    #  (400, 'Bad Request', {'first_name': ['Убедитесь, что это значение содержит не более 50 символов.',
    #                                       'Имя должно содержать только буквы кириллицы, пробел и знак дефиса.']})),
    #
    # # Параметр last_name: символы валидные, длина ниже нижней границы
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(10, True, ''), f.last_name(1, True, ''), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, ''), f.phone(13, True, ''), f.email(10, True, ''), f.key_id(10, True, ''), f.card_id(10, True, '')),
    #  (400, 'Bad Request', {'first_name': ['Убедитесь, что это значение содержит от 2 до 50 символов.']})),
    #
    # # Параметр last_name: символы не валидные, длина ниже нижней границы
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(10, True, ''), f.last_name(1, False, ''), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, ''), f.phone(13, True, ''), f.email(10, True, ''), f.key_id(10, True, ''), f.card_id(10, True, '')),
    #  (400, 'Bad Request', {'first_name': ['Убедитесь, что это значение содержит от 2 до 50 символов.',
    #                                       'Фамилия должно содержать только буквы кириллицы и знак дефиса.']})),
    #
    # # Параметр last_name: символы валидные, длина выше верхней границы
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(10, True, ''), f.last_name(51, True, ''), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, ''), f.phone(13, True, ''), f.email(10, True, ''), f.key_id(10, True, ''), f.card_id(10, True, '')),
    #  (400, 'Bad Request', {'last_name': ['Убедитесь, что это значение содержит не более 50 символов.']})),
    #
    # # Параметр last_name: символы не валидные + пробел, длина выше верхней границы
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(10, True, ''), f.last_name(51, False, '1o43<B🐰!$PH😃🍅JmsT9🐹UywQ,e🍏(lvD”?X\🐱@r+8LnC%`;_2k* &'),
    #   f.patronymic(10, True, ''), f.sex(True, ''), f.date(True, ''), f.phone(13, True, ''), f.email(10, True, ''),
    #   f.key_id(10, True, ''), f.card_id(10, True, '')),
    #  (400, 'Bad Request', {'last_name': ['Убедитесь, что это значение содержит не более 50 символов.',
    #                                       'Фамилия не должна содержать пробелов.',
    #                                       'Фамилия должно содержать только буквы кириллицы и знак дефиса.']})),
    #
    # # Параметр last_name: символы не валидные + без пробела, длина выше верхней границы
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(10, True, ''), f.last_name(51, False, '1o43<B🐰!$PH😃🍅JmsT9🐹UywQ,e🍏(lvD”?X\🐱@r+8LnC%`;_2k*&'),
    #   f.patronymic(10, True, ''), f.sex(True, ''), f.date(True, ''), f.phone(13, True, ''), f.email(10, True, ''),
    #   f.key_id(10, True, ''), f.card_id(10, True, '')),
    #  (400, 'Bad Request', {'last_name': ['Убедитесь, что это значение содержит не более 50 символов.',
    #                                       'Фамилия должна содержать только буквы кириллицы и знак дефиса.']})),
    #
    # # Параметр patronymic: символы валидные, длина выше верхней границы
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(10, True, ''), f.last_name(10, True, ''), f.patronymic(51, True, ''), f.sex(True, ''),
    #   f.date(True, ''), f.phone(13, True, ''), f.email(10, True, ''), f.key_id(10, True, ''), f.card_id(10, True, '')),
    #  (400, 'Bad Request', {'patronymic': ['Убедитесь, что это значение содержит не более 50 символов.']})),
    #
    # # Параметр patronymic: символы не валидные, длина выше верхней границы
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(10, True, ''), f.last_name(10, True, ''), f.patronymic(51, False, ''), f.sex(True, ''),
    #   f.date(True, ''), f.phone(13, True, ''), f.email(10, True, ''), f.key_id(10, True, ''), f.card_id(10, True, '')),
    #  (400, 'Bad Request', {'patronymic': ['Убедитесь, что это значение содержит не более 50 символов.',
    #                                       'Отчество должно содержать только буквы кириллицы, пробел и знак дефиса.']})),
    #
    # # Параметр phone: символы валидные, длина выше верхней границы
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(10, True, ''), f.last_name(10, True, ''), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, ''), f.phone(14, True, ''), f.email(10, True, ''), f.key_id(10, True, ''), f.card_id(10, True, '')),
    #  (400, 'Bad Request', {'phone': ['Убедитесь, что это значение содержит не более 13 символов.']})),
    #
    # # Параметр phone: символы не валидные, длина выше верхней границы
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(10, True, ''), f.last_name(10, True, ''), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, ''), f.phone(14, False, ''), f.email(10, True, ''), f.key_id(10, True, ''), f.card_id(10, True, '')),
    #  (400, 'Bad Request', {'phone': ['Убедитесь, что это значение содержит не более 13 символов.',
    #                                  'Телефон может содержать до 12 цифр без пробелов; '
    #                                  'допускается символ «+» в начале строки.']})),
    #
    # # Параметр email: символы валидные, длина выше верхней границы
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(10, True, ''), f.last_name(10, True, ''), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, ''), f.phone(10, True, ''), f.email(255, True, ''), f.key_id(10, True, ''), f.card_id(10, True, '')),
    #  (400, 'Bad Request', {'email': ['Убедитесь, что это значение содержит не более 254 символов.']})),
    #
    # # Параметр email: символы не валидные, длина выше верхней границы
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(10, True, ''), f.last_name(10, True, ''), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, ''), f.phone(10, True, ''), f.email(255, False, ''), f.key_id(10, True, ''), f.card_id(10, True, '')),
    #  (400, 'Bad Request', {'email': ['Убедитесь, что это значение содержит не более 254 символов.',
    #                                  'Введите правильный адрес электронной почты.']})),
    #
    # # Параметр key_id: символы валидные, длина выше верхней границы
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(10, True, ''), f.last_name(10, True, ''), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, ''), f.phone(10, True, ''), f.email(10, True, ''), f.key_id(41, True, ''), f.card_id(10, True, '')),
    #  (400, 'Bad Request', {'key_id': ['Убедитесь, что это значение содержит не более 40 символов.']})),
    #
    # # Параметр key_id: символы не валидные, длина выше верхней границы
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(10, True, ''), f.last_name(10, True, ''), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, ''), f.phone(10, True, ''), f.email(10, True, ''), f.key_id(41, False, ''), f.card_id(10, True, '')),
    #  (400, 'Bad Request', {'key_id': ['Убедитесь, что это значение содержит не более 40 символов.',
    #                                   'Идентификатор ключа должен содержать только латинские буквы и цифры']})),
    #
    # # Параметр card_id: символы валидные, длина выше верхней границы
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(10, True, ''), f.last_name(10, True, ''), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, ''), f.phone(10, True, ''), f.email(10, True, ''), f.key_id(10, True, ''), f.card_id(41, True, '')),
    #  (400, 'Bad Request', {'card_id': ['Убедитесь, что это значение содержит не более 40 символов.']})),
    #
    # # Параметр card_id: символы не валидные, длина выше верхней границы
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(10, True, ''), f.last_name(10, True, ''), f.patronymic(10, True, ''), f.sex(True, ''),
    #   f.date(True, ''), f.phone(10, True, ''), f.email(10, True, ''), f.key_id(10, True, ''), f.card_id(41, False, '')),
    #  (400, 'Bad Request', {'card_id': ['Убедитесь, что это значение содержит не более 40 символов.',
    #                                    'Идентификатор ID карты должен содержать только латинские буквы и цифры']})),
    #
    # # Все возможные параметры: символы валидные; длина ФИО меньше нижней границы, остальные - выше верхней границы
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(1, True, ''), f.last_name(1, True, ''), f.patronymic(1, True, ''), f.sex(True, ''),
    #   f.date(True, ''), f.phone(14, True, ''), f.email(255, True, ''), f.key_id(41, True, ''), f.card_id(41, True, '')),
    #  (400, 'Bad Request', {'key_id': ['Убедитесь, что это значение содержит не более 40 символов.'],
    #                        'card_id': ['Убедитесь, что это значение содержит не более 40 символов.'],
    #                        'first_name': ['Убедитесь, что это значение содержит от 2 до 50 символов.'],
    #                        'last_name': ['Убедитесь, что это значение содержит от 2 до 50 символов.'],
    #                        'patronymic': ['Убедитесь, что это значение содержит от 2 до 50 символов.'],
    #                        'phone': ['Убедитесь, что это значение содержит не более 13 символов.'],
    #                        'email': ['Убедитесь, что это значение содержит не более 254 символов.']})),
    #
    # # Все возможные параметры: ФИО значение не валидное меньше нижней границы; остальные - значение
    # # валидные выше верхней границы
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(1, False, ''), f.last_name(1, False, ''), f.patronymic(1, False, ''), f.sex(True, ''),
    #   f.date(True, ''), f.phone(14, True, ''), f.email(255, True, ''), f.key_id(41, True, ''), f.card_id(41, True, '')),
    #  (400, 'Bad Request', {'key_id': ['Убедитесь, что это значение содержит не более 40 символов.'],
    #                        'card_id': ['Убедитесь, что это значение содержит не более 40 символов.'],
    #                        'first_name': ['Имя должно содержать только буквы кириллицы, пробел и знак дефиса.',
    #                                       'Убедитесь, что это значение содержит от 2 до 50 символов.'],
    #                        'last_name': ['Убедитесь, что это значение содержит от 2 до 50 символов.'],
    #                        'patronymic': ['Убедитесь, что это значение содержит от 2 до 50 символов.'],
    #                        'phone': ['Убедитесь, что это значение содержит не более 13 символов.'],
    #                        'email': ['Убедитесь, что это значение содержит не более 254 символов.']})),
    #
    # # Все возможные параметры: символы валидные, длина выше верхней границы
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(51, True, ''), f.last_name(51, True, ''), f.patronymic(51, True, ''), f.sex(True, ''),
    #   f.date(True, ''), f.phone(14, True, ''), f.email(255, True, ''), f.key_id(41, True, ''), f.card_id(41, True, '')),
    #  (400, 'Bad Request', {'key_id': ['Убедитесь, что это значение содержит не более 40 символов.'],
    #                        'card_id': ['Убедитесь, что это значение содержит не более 40 символов.'],
    #                        'first_name': ['Убедитесь, что это значение содержит не более 50 символов.'],
    #                        'last_name': ['фамилия должна содержать только буквы кириллицы и знак дефиса.',
    #                                      'Убедитесь, что это значение содержит не более 50 символов.'],
    #                        'patronymic': ['Отчество должно содержать только буквы кириллицы, пробел и знак дефиса.'
    #                                       'Убедитесь, что это значение содержит не более 50 символов.'],
    #                        'phone': ['Убедитесь, что это значение содержит не более 13 символов.'],
    #                        'email': ['Убедитесь, что это значение содержит не более 254 символов.']})),
    #
    # # Все возможные параметры: символы не валидные + пробел в фамилии; длина выше верхней границы
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(51, False, ''), f.last_name(51, False, '1o43<B🐰!$PH😃🍅JmsT9🐹UywQ,e🍏(lvD”?X\🐱@r+8LnC%`;_2k* &'),
    #   f.patronymic(51, False, ''), f.sex(True, ''), f.date(True, ''), f.phone(14, False, ''), f.email(255, False, ''),
    #   f.key_id(41, False, ''), f.card_id(41, False, '')),
    #  (400, 'Bad Request', {'key_id': ['Убедитесь, что это значение содержит не более 40 символов.'],
    #                        'card_id': ['Убедитесь, что это значение содержит не более 40 символов.'],
    #                        'first_name': ['Имя должно содержать только буквы кириллицы, пробел и знак дефиса.',
    #                                       'Убедитесь, что это значение содержит не более 50 символов.'],
    #                        'last_name': ['Фамилия не должна содержать пробелов.',
    #                                      'фамилия должна содержать только буквы кириллицы и знак дефиса.',
    #                                      'Убедитесь, что это значение содержит не более 50 символов.'],
    #                        'patronymic': ['Отчество должно содержать только буквы кириллицы, пробел и знак дефиса.',
    #                                       'Убедитесь, что это значение содержит не более 50 символов.'],
    #                        'phone': ['Телефон может содержать до 12 цифр без пробелов; '
    #                                  'допускается символ «+» в начале строки.',
    #                                  'Убедитесь, что это значение содержит не более 13 символов.'],
    #                        'email': ['Убедитесь, что это значение содержит не более 254 символов.',
    #                                  'Введите правильный адрес электронной почты.']})),
    #
    # # Все возможные параметры: символы не валидные + нет пробела в фамилии; длина выше верхней границы
    # (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
    #  (f.first_name(51, False, ''), f.last_name(51, False, '1o43<B🐰!$PH😃🍅JmsT9🐹UywQ,e🍏(lvD”?X\🐱@r+8LnC%`;_2k* &'),
    #   f.patronymic(51, False, ''), f.sex(True, ''), f.date(True, ''), f.phone(14, False, ''), f.email(255, False, ''),
    #   f.key_id(41, False, ''), f.card_id(41, False, '')),
    #  (400, 'Bad Request', {'key_id': ['Убедитесь, что это значение содержит не более 40 символов.'],
    #                        'card_id': ['Убедитесь, что это значение содержит не более 40 символов.'],
    #                        'first_name': ['Имя должно содержать только буквы кириллицы, пробел и знак дефиса.',
    #                                       'Убедитесь, что это значение содержит не более 50 символов.'],
    #                        'last_name': ['фамилия должна содержать только буквы кириллицы и знак дефиса.',
    #                                      'Убедитесь, что это значение содержит не более 50 символов.'],
    #                        'patronymic': ['Отчество должно содержать только буквы кириллицы, пробел и знак дефиса.',
    #                                       'Убедитесь, что это значение содержит не более 50 символов.'],
    #                        'phone': ['Телефон может содержать до 12 цифр без пробелов; '
    #                                  'допускается символ «+» в начале строки.',
    #                                  'Убедитесь, что это значение содержит не более 13 символов.'],
    #                        'email': ['Убедитесь, что это значение содержит не более 254 символов.',
    #                                  'Введите правильный адрес электронной почты.']})),

)

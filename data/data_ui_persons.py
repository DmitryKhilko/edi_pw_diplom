
import pytest

from settings import *
from utils.faker import Fake

f = Fake()

"""
Константы, связанные с UI страницы добавления физического лица.
Константа состоит: названия метки поля ввода или названия кнопки; локатора поля ввода или кнопки
"""
MENU_ITEM_PERSONS = ('Физические лица', '//li[@data-path="/persons"]')
FIELD_FIRST_NAME = ('Имя', '//input[@name = "first_name"]')
FIELD_PATRONYMIC = ('Отчество', '//input[@name = "patronymic"]')
FIELD_LAST_NAME = ('Фамилия', '//input[@name = "last_name"]')
FIELD_BIRTHDAY = ('Дата рождения', '//input[@placeholder = "дд.мм.гггг"]')
DROP_DOWN_LIST_SEX = ('Пол', '//*[text() = "Мужской"]', '//*[text() = "Женский"]')
FIELD_PHONE = ('Телефон', '//input[@name = "phone"]')
FIELD_EMAIL = ('E-mail', '//input[@name = "email"]')
FIELD_CARD_ID = ('Идентификатор ID карты', '//input[@name = "card_id"]')
FIELD_KEY_ID = ('Идентификатор ключа', '//input[@name = "key_id"]')
BUTTON_SAVE = ('Сохранить', '//button[text() = "Сохранить"]')
BUTTON_CANCEL = ('Отменить', '//button[text() = "Отменить"]')

"""
Тестовые данные для параметризованных ui-тестов. 
Данные предназначены для проверки доступности работы с физическими лицами под ролью, 
которой разрешено создание физического лица - в вертикальном меню присутствует соответствующий пункт меню.
Структура кортежа: 
user (учетные данные пользователя), 
expected_result (ожидаемый результат для allure.step) 
"""
test_data_ui_visible_menu_item_persons = (
    pytest.param((ROLE_NAME_AIB, LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
                 'отображается пункт меню "Физические лица"',
                 marks=pytest.mark.smoke),

    pytest.param((ROLE_NAME_AIS, LOGIN_AIS, PASSWORD_AIS, EMAIL_ACCOUNT_AIS),
                 'отображается пункт меню "Физические лица"',
                 marks=pytest.mark.smoke),
)

"""
Тестовые данные для параметризованных ui-тестов. 
Данные предназначены для проверки доступности работы с физическими лицами под ролью, 
которой разрешено создание физического лица - в вертикальном меню присутствует соответствующий пункт меню.
Структура кортежа: 
user (учетные данные пользователя), 
expected_result (ожидаемый результат для allure.step) 
"""
test_data_ui_not_visible_menu_item_persons = (
    pytest.param((ROLE_NAME_ASH, LOGIN_ASH, PASSWORD_ASH, EMAIL_ACCOUNT_ASH),
                 'не отображается пункт меню "Физические лица"',
                 marks=pytest.mark.smoke),

    pytest.param((ROLE_NAME_PSH, LOGIN_PSH, PASSWORD_PSH, EMAIL_ACCOUNT_PSH),
                 'не отображается пункт меню "Физические лица"',
                 marks=pytest.mark.smoke),

    pytest.param((ROLE_NAME_AMNS, LOGIN_AMNS, PASSWORD_AMNS, EMAIL_ACCOUNT_AMNS),
                 'не отображается пункт меню "Физические лица"',
                 marks=pytest.mark.smoke),

    pytest.param((ROLE_NAME_OAMNS, LOGIN_OAMNS, PASSWORD_OAMNS, EMAIL_ACCOUNT_OAMNS),
                 'не отображается пункт меню "Физические лица"',
                 marks=pytest.mark.smoke),

    pytest.param((ROLE_NAME_RAMNS, LOGIN_RAMNS, PASSWORD_RAMNS, EMAIL_ACCOUNT_RAMNS),
                 'не отображается пункт меню "Физические лица"',
                 marks=pytest.mark.smoke),

    pytest.param((ROLE_NAME_PMNS, LOGIN_PMNS, PASSWORD_PMNS, EMAIL_ACCOUNT_PMNS),
                 'не отображается пункт меню "Физические лица"',
                 marks=pytest.mark.smoke),

    pytest.param((ROLE_NAME_AGTK, LOGIN_AGTK, PASSWORD_AGTK, EMAIL_ACCOUNT_AGTK),
                 'не отображается пункт меню "Физические лица"',
                 marks=pytest.mark.smoke),

    pytest.param((ROLE_NAME_PGTK, LOGIN_PGTK, PASSWORD_PGTK, EMAIL_ACCOUNT_PGTK),
                 'не отображается пункт меню "Физические лица"',
                 marks=pytest.mark.smoke),
)

"""
Тестовые данные для параметризованных ui-тестов. 
Данные предназначены для проверки отмены создания физического лица (заполнили форму и нажали кнопку "Отмена") 
под ролью, которой разрешено создание физического лица.
Для создания физического лица используются комбинация валидных значений обязательных для заполнения параметров. 
Структура кортежа: 
user (учетные данные пользователя), 
parameter_description (описание набора параметров для allure.step) 
"""
# TODO person_patronymic оставляем, так как по требованиям это не обязательное поле, а в реализации - обязательное
test_data_ui_cancel_create_person_valid_param = (
    pytest.param((ROLE_NAME_AIB, LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
                 'Создать физическое лицо с валидными значениями параметров (внутри границы)',
                 (f.text('*person_first_name', 'n', 'valid'),
                  f.text('person_patronymic', 'n', 'valid'),
                  f.text('*person_last_name', 'n', 'valid'),
                  f.text('*person_email', 'n', 'valid')),
                 marks=pytest.mark.critical_path),

    pytest.param((ROLE_NAME_AIS, LOGIN_AIS, PASSWORD_AIS, EMAIL_ACCOUNT_AIS),
                 'Создать физическое лицо с валидными значениями параметров (внутри границы)',
                 (f.text('*person_first_name', 'n', 'valid'),
                  f.text('person_patronymic', 'n', 'valid'),
                  f.text('*person_last_name', 'n', 'valid'),
                  f.text('*person_email', 'n', 'valid')),
                 marks=pytest.mark.critical_path),

)

"""
Тестовые данные для параметризованных ui-тестов. 
Данные предназначены для проверки создания физического лица под ролями, которым разрешено создание физического лица.
Для создания физического лица используются комбинации валидных значений параметров. 
Структура кортежа: 
user (учетные данные пользователя), 
parameter_description (описание набора параметров для allure.step),
expected_result (ожидаемый сообщение и отображение созданного физического лица в таблице) 
"""
# TODO person_birthday - для ui нужно вводить дату в формате 01.01.2021. Доработать фейкер
# TODO person_sex - для ui нужно только два рандомных значения: Мужской, Женский. Доработать фейкер
test_data_ui_can_create_person_valid_param = (
    pytest.param((ROLE_NAME_AIB, LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
                 'Создать физическое лицо с валидными значениями параметров (левая граница)',
                 (f.text('*person_first_name', 'min', 'valid'),
                  f.text('person_patronymic', 'min', 'valid'),
                  f.text('*person_last_name', 'min', 'valid'),
                  f.drop_down_list('person_sex', 'Женский', 'valid'),
                  f.date('person_birthday', '01.01.0001', 'valid'),
                  f.text('person_phone', 'min', 'valid'),
                  f.text('*person_email', 'min', 'valid'),
                  f.text('person_key_id', 'min', 'valid'),
                  f.text('person_card_id', 'min', 'valid')),
                 ('Успешно', 'Информация о физическом лице успешно добавлена.'),
                 marks=pytest.mark.critical_path),
)

"""
Тестовые данные для параметризованных ui-тестов. 
Данные предназначены для проверки отказа в создании физического лица под ролями, которым разрешено создание физического
лица, но для создания физического лица используется комбинации с пустыми значениями обязательных для заполнения 
параметров: фамилия, имя, email.  
Структура кортежа: 
user (учетные данные пользователя), 
parameter_description (описание набора параметров для allure.step),
expected_result (ожидаемый сообщение и отображение созданного физического лица в таблице) 
"""
test_data_ui_can_not_create_person_empty_param_required = (
    pytest.param((ROLE_NAME_AIB, LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
                 'Создать физическое лицо с пустыми значением поля first_name',
                 (f.text('*person_first_name', '', 'invalid'),
                  f.text('person_patronymic', 'n', 'valid'),
                  f.text('*person_last_name', 'n', 'valid'),
                  f.drop_down_list('person_sex', 'Женский', 'valid'),
                  f.date('person_birthday', '01.01.0001', 'valid'),
                  f.text('person_phone', 'n', 'valid'),
                  f.text('*person_email', 'n', 'valid'),
                  f.text('person_key_id', 'n', 'valid'),
                  f.text('person_card_id', 'n', 'valid')),
                 ('Имя', 'Пожалуйста, укажите имя', 'Ошибка', 'Не все обязательные поля заполнены!'),
                 marks=pytest.mark.critical_path),
)

"""
Тестовые данные для параметризованных ui-тестов. 
Данные предназначены для проверки отказа в создании физического лица под ролями, которым разрешено создание физического
лица, но для создания физического лица используется комбинации с не валидными значениями параметров (внутри границ) 
Структура кортежа: 
user (учетные данные пользователя), 
parameter_description (описание набора параметров для allure.step),
expected_result (ожидаемый сообщение и отображение созданного физического лица в таблице) 
"""
test_data_ui_not_can_create_person_invalid_param = (
    pytest.param((ROLE_NAME_AIB, LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
                 'Создать физическое лицо с не валидным значением параметра first_name, находящемся внутри границ',
                 (f.text('*person_first_name', 'n', 'invalid'),
                  f.text('person_patronymic', 'n', 'valid'),
                  f.text('*person_last_name', 'n', 'valid'),
                  f.drop_down_list('person_sex', 'Женский', 'valid'),
                  f.date('person_birthday', '01.01.0001', 'valid'),
                  f.text('person_phone', 'n', 'valid'),
                  f.text('*person_email', 'n', 'valid'),
                  f.text('person_key_id', 'n', 'valid'),
                  f.text('person_card_id', 'n', 'valid')),
                 ('Имя', 'Ошибка', 'Имя должно содержать только буквы кириллицы, пробел и знак дефиса.'),
                 marks=pytest.mark.critical_path),
)

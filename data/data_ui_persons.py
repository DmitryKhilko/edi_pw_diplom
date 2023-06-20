
import pytest

from settings import *
from utils.faker import Fake

f = Fake()

"""
Константы, связанные с UI страницы добавления физического лица.
Константа состоит: названия метки поля ввода или названия кнопки; локатора поля ввода или кнопки
"""
FIELD_FIRST_NAME = ('Имя', '//input[@name = "first_name"]')
FIELD_PATRONYMIC = ('Отчество', '//input[@name = "patronymic"]')
FIELD_LAST_NAME = ('Фамилия', '//input[@name = "last_name"]')
FIELD_BIRTHDAY = ('Дата рождения', '//input[@placeholder = "дд.мм.гггг"]')
DROP_DOWN_LIST_SEX = ('Пол', '//*[text() = "Мужской"]', '//*[text() = "Женский"]')
FIELD_PHONE = ('Телефон', '//input[@name = "phone"]')
FIELD_EMAIL = ('E-mail', '//input[@name = "email"]')
FIELD_CARD_ID = ('Идентификатор ID карты', '//input[@name = "card_id"]')
FIELD_KEY_ID = ('Идентификатор ключа', '//input[@name = "key_id"]')
BUTTON_SAVE = ('СОХРАНИТЬ', '//button[text() = "Сохранить"]')
BUTTON_CANCEL = ('ОТМЕНИТЬ', '//button[text() = "Отменить"]')

"""
Тестовые данные для параметризованных api-тестов. 
Данные предназначены для проверки отмены создания физического лица (заполнили форму и нажали кнопку "Отмена") 
под ролью, которой разрешено создание физического лица.
Для создания физического лица используются комбинация валидных значений обязательных для заполнения параметров. 
Структура кортежа: 
user (учетные данные пользователя), 
parameter_description (описание набора параметров для allure.step), 
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
Тестовые данные для параметризованных api-тестов. 
Данные предназначены для проверки создания физического лица под ролями, которым разрешено создание физического лица.
Для создания физического лица используются комбинации валидных значений параметров. 
Структура кортежа: 
user (учетные данные пользователя), 
parameter_description (описание набора параметров для allure.step), 
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
                 marks=pytest.mark.critical_path),
)


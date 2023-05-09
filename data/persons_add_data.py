"""   
В данном файле приведены константы, необходимые для функционирования автотестов,
предназначенных для тестирования функционала страницы добавления физического лица
"""

# Константы, связанные с UI страницы добавления физического лица:
# константы с названиями меток веб-элементов, названий кнопок страницы
# и локаторы веб-элементов
FIRST_NAME = ('Имя', '//input[@name = "first_name"]')
PATRONYMIC = ('Отчество', '//input[@name = "patronymic"]')
LAST_NAME = ('Фамилия', '//input[@name = "last_name"]')
BIRTHDAY = ('Дата рождения', '//input[@placeholder = "дд.мм.гггг"]')
SEX = ('Пол', '//*[text() = "Мужской"]', '//*[text() = "Женский"]')
PHONE = ('Телефон', '//input[@name = "phone"]')
EMAIL = ('E-mail', '//input[@name = "email"]')
CARD_ID = ('Идентификатор ID карты', '//input[@name = "card_id"]')
KEY_ID = ('Идентификатор ключа', '//input[@name = "key_id"]')
BUTTON_SAVE = ('Сохранить', '//button[text() = "Сохранить"]')
BUTTON_CANCEL = ('Отменить', '//button[text() = "Отменить"]')

# Параметры для теста test_persons_add_by_aib, расположенного в файле tests/test_persons_add.py
person_parameters_aib = (('smirnov', 'smirnovP@assw0rd', 'Татьяна', 'Юрьевна', 'Хилько', '13.06.1974', 'Женский', '21067', '8833@333.com', '8921', '684'),
                         ('smirnov', 'smirnovP@assw0rd', 'Сергей', 'Николаевич', 'Патрушев', '10.05.1981', 'Мужской', '569875', '7733@333.com', '653', '991'))

from settings import *

# Данные предназначены для параметризованных api-тестов для входа в приложение под всеми ролями. Структура кортежа:
# users (учетные данные пользователя), message (ответ сервера)
test_data_can_login = (
    (('Администратор ИБ', LOGIN_AIB, PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
     (200, 'OK')),
    (('Администратор ИС', LOGIN_AIS, PASSWORD_AIS, EMAIL_ACCOUNT_AIS),
     (200, 'OK')),
    (('Администратор СХ', LOGIN_ASH, PASSWORD_ASH, EMAIL_ACCOUNT_ASH),
     (200, 'OK')),
    (('Пользователь СХ', LOGIN_PSH, PASSWORD_PSH, EMAIL_ACCOUNT_PSH),
     (200, 'OK')),
    (('Администратор МНС', LOGIN_AMNS, PASSWORD_AMNS, EMAIL_ACCOUNT_AMNS),
     (200, 'OK')),
    (('Областной администратор МНС', LOGIN_OAMNS, PASSWORD_OAMNS, EMAIL_ACCOUNT_OAMNS),
     (200, 'OK')),
    (('Районный администратор МНС', LOGIN_RAMNS, PASSWORD_RAMNS, EMAIL_ACCOUNT_RAMNS),
     (200, 'OK')),
    (('Пользователь МНС', LOGIN_PMNS, PASSWORD_PMNS, EMAIL_ACCOUNT_PMNS),
     (200, 'OK')),
    (('Администратор ГТК', LOGIN_AGTK, PASSWORD_AGTK, EMAIL_ACCOUNT_AGTK),
     (200, 'OK')),
    (('Пользователь ГТК', LOGIN_PGTK, PASSWORD_PGTK, EMAIL_ACCOUNT_PGTK),
     (200, 'OK')),
)

# Данные предназначены для параметризованных api-тестов для проверки входа в приложение при вводе невалидных логина
# и (или пароля). Структура кортежа:
# users (учетные данные пользователя), message (ответ сервера)
test_data_can_not_login = (
    (('Администратор ИБ', LOGIN_AIB, 'invalid_password', EMAIL_ACCOUNT_AIB),
     (403, 'Forbidden', {'detail': 'Не найдено активной учетной записи с указанными данными.'})),
    # Не совсем корректное сообщение. Пустой только пароль.
    (('Администратор ИБ', LOGIN_AIB, '', EMAIL_ACCOUNT_AIB),
     (403, 'Forbidden', {'detail': 'Укажите логин и пароль.'})),
    (('Администратор ИБ', 'invalid_login', 'invalid_password', EMAIL_ACCOUNT_AIB),
     (403, 'Forbidden', {'detail': 'Не найдено активной учетной записи с указанными данными.'})),
    # Не совсем корректное сообщение. Пустой только пароль.
    (('Администратор ИБ', 'invalid_login', '', EMAIL_ACCOUNT_AIB),
     (403, 'Forbidden', {'detail': 'Укажите логин и пароль.'})),
    (('Администратор ИБ', 'invalid_login', PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
     (403, 'Forbidden', {'detail': 'Не найдено активной учетной записи с указанными данными.'})),
    (('Администратор ИБ', '', '', EMAIL_ACCOUNT_AIB),
     (403, 'Forbidden', {'detail': 'Укажите логин и пароль.'})),
    (('Администратор ИБ', '', PASSWORD_AIB, EMAIL_ACCOUNT_AIB),
     (403, 'Forbidden', {'detail': 'Укажите логин и пароль.'})),
    (('Администратор ИБ', '', 'invalid_password', EMAIL_ACCOUNT_AIB),
     (403, 'Forbidden', {'detail': 'Укажите логин и пароль.'})),
)

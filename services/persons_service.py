import logging

import allure

from services.base_service import BaseService
from sql_requests.sql import SQLRequests


class PersonsService(BaseService):

    @staticmethod
    def can_get_persons(csrftoken: str, sessionid: str, expected_result: tuple):

        """
        Метод получения с помощью get-запроса списка физических лиц
        для ролей, имеющих права получать и просматривать данный список

        :param csrftoken: CSRF-токен, передаваемый в запрос
        :param sessionid: сгенерированный идентификатор сессии
        :param expected_result: ожидаемый ответ сервера
       """

        with allure.step('Получить список физических лиц'):
            logging.debug(f'Приступить к получению списка физических лиц')
            status_code, reason, result = BaseService.get_persons(csrftoken, sessionid)

        with allure.step('Ожидаемый результат: получен список физических лиц'):
            print(f"Ожидаемый status_code: '{expected_result[0]}', '{expected_result[1]}'")
            print(f"Фактический status_code: '{status_code}', '{reason}'")
            print(f"Фактический response.json(): {result}'")
            assert status_code == expected_result[0], 'Не получен список физических лиц под допустимой ролью'
            assert result['count'] >= 1, 'Фактическое и ожидаемое количество записей физических лиц не совпали'
            logging.debug(f'Список физических лиц успешно получен')

    @staticmethod
    def can_not_get_persons(csrftoken: str, sessionid: str, expected_result: tuple):

        """
        Метод, подтверждающий невозможность получения списка физических
        лиц с помощью get-запроса для ролей, не имеющих права получать и
        просматривать данный список

        :param csrftoken: CSRF-токен, передаваемый в запрос
        :param sessionid: сгенерированный идентификатор сессии
        :param expected_result: ожидаемый ответ сервера
        """

        with allure.step('Получить список физических лиц'):
            logging.debug(f'Приступить к получению списка физических лиц')
            status_code, reason, result = BaseService.get_persons(csrftoken, sessionid)

        with allure.step('Ожидаемый результат: недостаточно прав для получения списка физических лиц'):
            print(f"Ожидаемый status_code: '{expected_result[0]}', '{expected_result[1]}'")
            print(f"Фактический status_code: '{status_code}', '{reason}'")
            print(f"Фактический response.json(): {result}'")
            assert status_code == expected_result[0], 'Возможно есть доступ к списку физических лиц ' \
                                                      'для недопустимой роли'
            assert result == expected_result[2], 'Сообщение не соответствует ожидаемому'
            logging.debug(f'Список физических лиц не получен')

    @staticmethod
    def can_add_person_valid_param(csrftoken: str, sessionid: str, data: tuple, message: tuple):

        """
            Метод создания с помощью post-запроса физического лица для
            ролей приложения, которым разрешено создание физического лица

            Parameters:
            ------------------------
            - csrftoken: CSRF-токен, передаваемый в запрос
            - sessionid: сгенерированный идентификатор сессии
            - data: набор значений параметров для создания физического лица
            - message: ожидаемый ответ сервера
        """

        with allure.step('Создать физическое лицо'):
            logging.debug(f'Приступить к добавлению физ. лица с валидными параметрами')
            status_code, reason, result = BaseService.add_person(csrftoken, sessionid, data)

        with allure.step('Ожидаемый результат: создано физическое лицо'):
            print(f"Ожидаемый status_code: '{message[0]}', '{message[1]}'")
            print(f"Фактический status_code: '{status_code}', '{reason}'")
            print(f"Фактический response.json(): {result}'")
            assert status_code == message[0], 'Не создано физическое лицо'
            fio = (data[1].strip() + ' ' + data[0].strip() + ' ' + data[2].strip())
            # Привожу к нижнему регистру, так как при записи в БД система только первые буквы делает большими
            assert result['full_name'].lower() == fio.lower(), 'Фактическое и ожидаемое ФИО физического лица ' \
                                                               'не совпали'
            assert result['email'].strip() == data[6].strip(), 'Фактический и ожидаемый email физического лица ' \
                                                               'не совпали'
            logging.debug(f'Физическое лицо "{fio}" успешно создано')

        with allure.step('Ожидаемый результат: физическое лицо добавлено в БД'):
            logging.debug(f'Приступить к поиску добавленного физ. лица в БД')
            db_rowcount, db_fio, db_email = SQLRequests.db_select_row(result['person_id'])
            print(f"Фактическое ФИО из БД: '{db_fio}'")
            print(f"Фактический email из БД: '{db_email}'")
            assert db_rowcount == 1, 'Физическое лицо в базу данных не добавлено'
            # Привожу к нижнему регистру, так как при записи в БД система только первые буквы делает большими
            assert db_fio.lower() == fio.lower(), 'Фактическое из БД и ожидаемое ФИО физического лица не совпали'
            assert db_email == data[6].lower(), 'Фактический из БД и ожидаемый email физического лица не совпали'
            logging.debug(f'Физическое лицо "{fio}" успешно добавлено в БД')

    @staticmethod
    def can_not_add_person_valid_param(csrftoken: str, sessionid: str, data: tuple, message: tuple):

        """
            Метод создания с помощью post-запроса физического лица для
            ролей приложения, которым запрещено создание физического лица.

            Parameters:
            ------------------------
            - csrftoken: CSRF-токен, передаваемый в запрос
            - sessionid: сгенерированный идентификатор сессии
            - data: набор значений параметров для создания физического лица
            - message: ожидаемый ответ сервера
        """

        with allure.step('Создать физическое лицо'):
            logging.debug(f'Приступить к добавлению физ. лица с валидными параметрами')
            status_code, reason, result = BaseService.add_person(csrftoken, sessionid, data)

        with allure.step('Ожидаемый результат: недостаточно прав для создания физического лица'):
            print(f"Ожидаемый status_code: '{message[0]}', '{message[1]}'")
            print(f"Фактический status_code: '{status_code}', '{reason}'")
            print(f"Ожидаемый response.json(): {message[2]}'")
            print(f"Фактический response.json(): {result}'")
            assert status_code == message[0], 'Возможно физическое лицо добавлено в базу данных под ' \
                                              'недопустимой ролью'
            assert result == message[2], 'Сообщение не соответствует ожидаемому'
            logging.debug(f'Физическое лицо не создано, так как недостаточно прав для создания физического лица')

    @staticmethod
    def can_not_add_person_empty_param_required(csrftoken: str, sessionid: str, data: tuple, message: tuple):

        """
            Метод проверки невозможности создания с помощью post-запроса
            физического лица под ролью АИБ с незаполненными обязательными
            полями.

            Parameters:
            ------------------------
            - csrftoken: CSRF-токен, передаваемый в запрос
            - sessionid: сгенерированный идентификатор сессии
            - data: набор значений параметров для создания физического лица
            - message: ожидаемый ответ сервера
        """

        with allure.step('Создать физическое лицо'):
            logging.debug(f'Приступить к добавлению физ. лица с пустыми параметрами')
            status_code, reason, result = BaseService.add_person(csrftoken, sessionid, data)

        with allure.step('Ожидаемый результат: не создано физическое лицо из-за пустых обязательных параметров'):
            print(f"Ожидаемый status_code: '{message[0]}', '{message[1]}'")
            print(f"Фактический status_code: '{status_code}', '{reason}'")
            print(f"Ожидаемый response.json(): {message[2]}'")
            print(f"Фактический response.json(): {result}'")
            assert status_code == message[0], 'Возможно физическое лицо добавлено в базу данных при пустых ' \
                                              'обязательных параметрах'
            assert result == message[2], 'Сообщение не соответствует ожидаемому'
            logging.debug(f'Физическое лицо не создано из-за пустых обязательных параметров')

    @staticmethod
    def can_not_add_person_invalid_param(csrftoken: str, sessionid: str, data: tuple, message: tuple):

        """
            Метод проверки невозможности создания с помощью post-запроса
            физического лица под ролью АИБ с невалидными значениями параметров

            Parameters:
            ------------------------
            - csrftoken: CSRF-токен, передаваемый в запрос
            - sessionid: сгенерированный идентификатор сессии
            - data: набор значений параметров для создания физического лица
            - message: ожидаемый ответ сервера
        """

        with allure.step('Создать физическое лицо'):
            logging.debug(f'Приступить к добавлению физ. лица с невалидными параметрами')
            status_code, reason, result = BaseService.add_person(csrftoken, sessionid, data)

        with allure.step('Ожидаемый результат: не создано физическое лицо из-за невалидных значений параметров'):
            print(f"Ожидаемый status_code: '{message[0]}', '{message[1]}'")
            print(f"Фактический status_code: '{status_code}', '{reason}'")
            print(f"Ожидаемый response.json(): {message[2]}'")
            print(f"Фактический response.json(): {result}'")
            assert status_code == message[0], 'Возможно физическое лицо добавлено в базу данных при ' \
                                              'наличии невалидных значений параметров'
            assert result == message[2], 'Сообщение не соответствует ожидаемому'
            logging.debug(f'Физическое лицо не создано из-за невалидных значений параметров')

    @staticmethod
    def can_not_add_person_param_out_of_limits(csrftoken: str, sessionid: str, data: tuple, message: tuple):

        """
            Метод проверки невозможности создания с помощью post-запроса
            физического лица под ролью АИБ со значениями параметров, вышедших
            по длине за допустимые пределы (вниз или вверх)

            Parameters:
            ------------------------
            - csrftoken: CSRF-токен, передаваемый в запрос
            - sessionid: сгенерированный идентификатор сессии
            - data: набор значений параметров для создания физического лица
            - message: ожидаемый ответ сервера
        """

        with allure.step('Создать физическое лицо'):
            logging.debug(f'Приступить к добавлению физ. лица с параметрами, вышедшими по длине за допустимые границы')
            status_code, reason, result = BaseService.add_person(csrftoken, sessionid, data)

        with allure.step('Ожидаемый результат: не создано физическое лицо из-за значений параметров, '
                         'вышедших по длине за допустимые границы'):
            print(f"Ожидаемый status_code: '{message[0]}', '{message[1]}'")
            print(f"Фактический status_code: '{status_code}', '{reason}'")
            print(f"Ожидаемый response.json(): {message[2]}'")
            print(f"Фактический response.json(): {result}'")
            assert status_code == message[0], 'Возможно физическое лицо добавлено в базу данных при ' \
                                              'наличии значений параметров, вышедших по длине за допустимые границы'
            assert result == message[2], 'Сообщение не соответствует ожидаемому'
            logging.debug(f'Физическое лицо не создано из-за из-за значений параметров, вышедших по длине за'
                          f' допустимые границы')

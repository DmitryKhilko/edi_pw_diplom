import logging

import allure

from services.base_service import BaseService
from sql_requests.persons_sql import SQLRequests


class PersonsService(BaseService):

    @staticmethod
    def can_read_persons(csrftoken: str, sessionid: str, parameter_description: str, expected_result: tuple):

        """
        Метод получения с помощью get-запроса списка физических лиц
        для ролей, имеющих права получать и просматривать данный список

        :param csrftoken: CSRF-токен, передаваемый в запрос
        :param sessionid: сгенерированный идентификатор сессии
        :param parameter_description: описание набора параметров из набора тестовых данных для allure.step
        :param expected_result: ожидаемый ответ сервера
       """

        with allure.step(f'{parameter_description}'):  # Получить список физических лиц под ролью
            logging.debug(f'Приступить к получению списка физических лиц')
            status_code, reason, result = BaseService.get_persons(csrftoken, sessionid)

        with allure.step('Ожидаемый результат: получен список физических лиц'):
            print(f'Ожидаемый status_code: "{expected_result[0]}", "{expected_result[1]}"')
            print(f'Фактический status_code: "{status_code}", "{reason}"')
            print(f'Фактический response.json(): {result}')
            assert status_code == expected_result[0], 'Не получен список физических лиц под допустимой ролью'
            assert result['count'] >= 1, 'Фактическое и ожидаемое количество записей физических лиц не совпали'
            logging.debug(f'Список физических лиц успешно получен')

    @staticmethod
    def can_not_read_persons(csrftoken: str, sessionid: str, parameter_description: str, expected_result: tuple,
                             user_role: str):

        """
        Метод, подтверждающий невозможность получения списка физических
        лиц с помощью get-запроса для ролей, не имеющих права получать и
        просматривать данный список

        :param csrftoken: CSRF-токен, передаваемый в запрос
        :param sessionid: сгенерированный идентификатор сессии
        :param parameter_description: описание набора параметров из набора тестовых данных для allure.step
        :param expected_result: ожидаемый ответ сервера
        :param user_role: роль пользователя, под которой была попытка получить список физ.лиц

        """

        with allure.step(f'{parameter_description}'):  # Получить список физических лиц под ролью
            logging.debug(f'Приступить к получению списка физических лиц')
            status_code, reason, result = BaseService.get_persons(csrftoken, sessionid)

        with allure.step('Ожидаемый результат: у пользователя недостаточно прав для получения списка физических лиц'):
            print(f'Ожидаемый status_code: "{expected_result[0]}", "{expected_result[1]}"')
            print(f'Фактический status_code: "{status_code}", "{reason}"')
            print(f'Фактический response.json(): {result}')
            assert status_code == expected_result[0], f'Возможно есть доступ к списку физических лиц ' \
                                                      f'для роли "{user_role}"'
            assert result == expected_result[2], 'Сообщение не соответствует ожидаемому'
            logging.debug(f'Список физических лиц не получен')

    @staticmethod
    def can_create_person_valid_param(csrftoken: str, sessionid: str, parameter_description: str, data: tuple,
                                      expected_result: tuple):
        """
        Метод создания с помощью post-запроса физического лица для
        ролей приложения, которым разрешено создание физического лица
        с валидными значениями параметров

        :param csrftoken: CSRF-токен, передаваемый в запрос
        :param sessionid: сгенерированный идентификатор сессии
        :param parameter_description: описание набора параметров из набора тестовых данных для allure.step
        :param data: набор значений параметров для создания физического лица
        :param expected_result: ожидаемый ответ сервера
        """

        with allure.step(f'{parameter_description}'):  # создать физическое лицо с валидными значениями параметров
            logging.debug(f'Приступить к созданию физ. лица с валидными параметрами')
            status_code, reason, result = BaseService.add_person(csrftoken, sessionid, data)

        with allure.step('Ожидаемый результат: физическое лицо создано'):
            print(f'Ожидаемый status_code: "{expected_result[0]}", "{expected_result[1]}"')
            print(f'Фактический status_code: "{status_code}", "{reason}"')
            print(f'Фактический response.json(): {result}')
            assert status_code == expected_result[0], 'Физическое лицо не создано'
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
            print(f'Фактическое ФИО из БД: "{db_fio}"')
            print(f'Фактический email из БД: "{db_email}"')
            assert db_rowcount == 1, 'Физическое лицо в базу данных не добавлено'
            # Привожу к нижнему регистру, так как при записи в БД система только первые буквы делает большими
            assert db_fio.lower() == fio.lower(), 'Фактическое из БД и ожидаемое ФИО физического лица не совпали'
            assert db_email == data[6].lower(), 'Фактический из БД и ожидаемый email физического лица не совпали'
            logging.debug(f'Физическое лицо "{fio}" успешно добавлено в БД')

    @staticmethod
    def can_not_create_person_valid_param(csrftoken: str, sessionid: str, parameter_description: str, data: tuple,
                                          expected_result: tuple):

        """
        Метод проверки невозможности создания с помощью post-запроса
        физического лица для ролей приложения, которым запрещено
        создание физического лица

        :param csrftoken: CSRF-токен, передаваемый в запрос
        :param sessionid: сгенерированный идентификатор сессии
        :param parameter_description: описание набора параметров из набора тестовых данных для allure.step
        :param data: набор значений параметров для создания физического лица
        :param expected_result: ожидаемый ответ сервера
        """

        with allure.step(f'{parameter_description}'):  # создать физическое лицо с валидными значениями параметров
            logging.debug(f'Приступить к созданию физ. лица с валидными значениями параметров')
            status_code, reason, result = BaseService.add_person(csrftoken, sessionid, data)

        with allure.step('Ожидаемый результат: у пользователя недостаточно прав для создания физического лица'):
            print(f'Ожидаемый status_code: "{expected_result[0]}", "{expected_result[1]}"')
            print(f'Фактический status_code: "{status_code}", "{reason}"')
            print(f'Ожидаемый response.json(): {expected_result[2]}')
            print(f'Фактический response.json(): {result}')
            assert status_code == expected_result[0], 'Возможно физическое лицо добавлено в базу данных под ' \
                                                      'недопустимой ролью'
            assert result == expected_result[2], 'Сообщение не соответствует ожидаемому'
            logging.debug(f'Физическое лицо не создано, так как недостаточно прав для создания физического лица')

    @staticmethod
    def can_not_create_person_empty_param_required(csrftoken: str, sessionid: str, parameter_description: str,
                                                   data: tuple, expected_result: tuple):

        """
        Метод проверки невозможности создания с помощью post-запроса
        физического лица под ролью, которой разрешено создавать
        физическое лицо, с незаполненными обязательными для
        заполнения параметрами

        :param csrftoken: CSRF-токен, передаваемый в запрос
        :param sessionid: сгенерированный идентификатор сессии
        :param parameter_description: описание набора параметров из набора тестовых данных для allure.step
        :param data: набор значений параметров для создания физического лица
        :param expected_result: ожидаемый ответ сервера
        """

        with allure.step(f'{parameter_description}'):  # создать физическое лицо с пустыми значениями параметров
            logging.debug(f'Приступить к созданию физ. лица с пустыми значениями '
                          f'обязательных для заполнения параметров')
            status_code, reason, result = BaseService.add_person(csrftoken, sessionid, data)

        with allure.step('Ожидаемый результат: физическое лицо не создано из-за пустых обязательных '
                         'для заполнения параметров'):
            print(f'Ожидаемый status_code: "{expected_result[0]}", "{expected_result[1]}"')
            print(f'Фактический status_code: "{status_code}", "{reason}"')
            print(f'Ожидаемый response.json(): {expected_result[2]}')
            print(f'Фактический response.json(): {result}')
            assert status_code == expected_result[0], 'Возможно физическое лицо добавлено в базу данных при пустых ' \
                                                      'обязательных параметрах'
            assert result == expected_result[2], 'Сообщение не соответствует ожидаемому'
            logging.debug(f'Физическое лицо не создано из-за пустых значений обязательных параметров')

    @staticmethod
    def can_not_create_person_invalid_param(csrftoken: str, sessionid: str, parameter_description: str, data: tuple,
                                            expected_result: tuple):

        """
        Метод проверки невозможности создания с помощью post-запроса
        физического лица под ролью, которой разрешено создавать физическое
        лицо, с не валидными значениями параметров, которые не выходят за
        допустимые пределы (вниз или вверх)

        :param csrftoken: CSRF-токен, передаваемый в запрос
        :param sessionid: сгенерированный идентификатор сессии
        :param parameter_description: описание набора параметров из набора тестовых данных для allure.step
        :param data: набор значений параметров для создания физического лица
        :param expected_result: ожидаемый ответ сервера
        """

        with allure.step(f'{parameter_description}'):  # создать физическое лицо с не валидными значениями параметров
            logging.debug(f'Приступить к созданию физ. лица с невалидными значениями параметров внутри границ')
            status_code, reason, result = BaseService.add_person(csrftoken, sessionid, data)

        with allure.step('Ожидаемый результат: физическое лицо не создано из-за невалидных значений параметров'):
            print(f'Ожидаемый status_code: "{expected_result[0]}", "{expected_result[1]}"')
            print(f'Фактический status_code: "{status_code}", "{reason}"')
            print(f'Ожидаемый response.json(): {expected_result[2]}')
            print(f'Фактический response.json(): {result}')
            assert status_code == expected_result[0], 'Возможно физическое лицо добавлено в базу данных при ' \
                                                      'наличии невалидных значений параметров'
            assert result == expected_result[2], 'Сообщение не соответствует ожидаемому'
            logging.debug(f'Физическое лицо не создано из-за невалидных значений параметров')

    @staticmethod
    def can_not_create_person_valid_param_out_of_limits(csrftoken: str, sessionid: str, parameter_description: str,
                                                        data: tuple, expected_result: tuple):

        """
        Метод проверки невозможности создания с помощью post-запроса
        физического лица под ролью, которой разрешено создавать
        физическое лицо, с валидными значениями параметров, вышедшими
        за допустимые границы (вниз или вверх)

        :param csrftoken: CSRF-токен, передаваемый в запрос
        :param sessionid: сгенерированный идентификатор сессии
        :param parameter_description: описание набора параметров из набора тестовых данных для allure.step
        :param data: набор значений параметров для создания физического лица
        :param expected_result: ожидаемый ответ сервера
        """

        with allure.step(f'{parameter_description}'):  # создать физическое лицо
            logging.debug(f'Приступить к созданию физ. лица с валидными значениями параметрами, вышедшими '
                          f'за допустимые границы')
            status_code, reason, result = BaseService.add_person(csrftoken, sessionid, data)

        with allure.step('Ожидаемый результат: физическое лицо не создано из-за валидных значений параметров, '
                         'вышедших за допустимые границы'):
            print(f'Ожидаемый status_code: "{expected_result[0]}", "{expected_result[1]}"')
            print(f'Фактический status_code: "{status_code}", "{reason}"')
            print(f'Ожидаемый response.json(): {expected_result[2]}')
            print(f'Фактический response.json(): {result}')
            assert status_code == expected_result[0], 'Возможно физическое лицо добавлено в базу данных при наличии ' \
                                                      'валидных значений параметров, вышедших по длине за допустимые ' \
                                                      'границы'
            assert result == expected_result[2], 'Сообщение не соответствует ожидаемому'
            logging.debug(f'Физическое лицо не создано из-за валидных значений параметров, вышедших за '
                          f'допустимые границы')

    @staticmethod
    def can_not_create_person_invalid_param_out_of_limits(csrftoken: str, sessionid: str, parameter_description: str,
                                                          data: tuple, expected_result: tuple):
        """
        Метод проверки невозможности создания с помощью post-запроса
        физического лица под ролью, которой разрешено создавать
        физическое лицо, с не валидными значениями параметров, вышедшими
        за допустимые границы (вниз или вверх)

        :param csrftoken: CSRF-токен, передаваемый в запрос
        :param sessionid: сгенерированный идентификатор сессии
        :param parameter_description: описание набора параметров из набора тестовых данных для allure.step
        :param data: набор значений параметров для создания физического лица
        :param expected_result: ожидаемый ответ сервера
        """

        with allure.step(f'{parameter_description}'):  # создать физическое лицо
            logging.debug(f'Приступить к созданию физ. лица с не валидными значениями параметрами, вышедшими '
                          f'за допустимые границы')
            status_code, reason, result = BaseService.add_person(csrftoken, sessionid, data)

        with allure.step('Ожидаемый результат: физическое лицо не создано из-за не валидных значений параметров, '
                         'вышедших за допустимые границы'):
            print(f'Ожидаемый status_code: "{expected_result[0]}", "{expected_result[1]}"')
            print(f'Фактический status_code: "{status_code}", "{reason}"')
            print(f'Ожидаемый response.json(): {expected_result[2]}')
            print(f'Фактический response.json(): {result}')
            assert status_code == expected_result[0], 'Возможно физическое лицо добавлено в базу данных при наличии ' \
                                                      'не валидных значений параметров, вышедших по длине за ' \
                                                      'допустимые границы'
            assert result == expected_result[2], 'Сообщение не соответствует ожидаемому'
            logging.debug(f'Физическое лицо не создано из-за не валидных значений параметров, вышедших за '
                          f'допустимые границы')

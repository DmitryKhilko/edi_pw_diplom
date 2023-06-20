import logging
import os

from utils.files import FilesWork
from sql_requests.base_sql import BaseSQL


class SQLRequests(BaseSQL):

    @staticmethod
    def db_select_row(param: str):

        """
        Метод проверки наличия записи в БД для физического лица,
        созданного (измененного) API-запросом.
        С помощью cursor.rowcount возвращаем количество отобранных
        запросом записей = 1; с помощью cursor.fetchall() возвращаем
        содержимое записи для последующего анализа.

        :param param: параметр, передаваемый в SQL-запрос для отбора записи
        :return db_rowcount: количество отобранных записей
        :return db_fio: ФИО физического лица из базы данных для сверки с ожидаемым результатом
        :return db_email: email из базы данных для сверки с ожидаемым результатом
        """

        connection = BaseSQL.db_connection()

        cursor = connection.cursor()
        cursor.execute('SELECT person_id, first_name, last_name, patronymic, email '
                       'FROM person WHERE person_id = %s', (param,))

        if cursor.rowcount == 1:
            db_rowcount = cursor.rowcount
            """
            Обязательно нужно cursor.fetchone() записывать в переменную,
            если обращаться к cursor.fetchone() в нескольких строках, БД
            блокирует такие частые обращения.
            """
            fetchone = cursor.fetchone()
            db_fio = (fetchone[2].strip() + ' ' + fetchone[1].strip() + ' ' + fetchone[3].strip())
            db_email = fetchone[4]
        else:
            db_rowcount = 0
            db_fio = ''
            db_email = ''

        BaseSQL.db_disconnection(connection)

        return db_rowcount, db_fio, db_email

    @staticmethod
    def db_select_row_ui(param: str):

        """
        Метод проверки наличия записи в БД для физического лица,
        созданного (измененного) через web-интерфейс.
        С помощью cursor.rowcount возвращаем количество отобранных
        запросом записей = 1; с помощью cursor.fetchall() возвращаем
        содержимое записи для последующего анализа.

        :param param: параметр, передаваемый в SQL-запрос для отбора записи
        :return db_person_id: id созданного физического лица
        :return db_rowcount: количество отобранных записей
        :return db_fio: ФИО физического лица из базы данных для сверки с ожидаемым результатом
        :return db_email: email из базы данных для сверки с ожидаемым результатом
        """

        connection = BaseSQL.db_connection()

        cursor = connection.cursor()
        cursor.execute('SELECT person_id, first_name, last_name, patronymic, email '
                       'FROM person WHERE email = %s', (param.lower(),))

        if cursor.rowcount == 1:
            db_rowcount = cursor.rowcount
            """
            Обязательно нужно cursor.fetchone() записывать в переменную,
            если обращаться к cursor.fetchone() в нескольких строках, БД
            блокирует такие частые обращения.
            """
            fetchone = cursor.fetchone()
            db_person_id = fetchone[0].strip()
            db_fio = (fetchone[2].strip() + ' ' + fetchone[1].strip() + ' ' + fetchone[3].strip())
            db_email = fetchone[4]
        else:
            db_rowcount = 0
            db_person_id = ''
            db_fio = ''
            db_email = ''

        BaseSQL.db_disconnection(connection)

        return db_rowcount, db_person_id, db_fio, db_email

    @staticmethod
    def db_delete_row(file_name: str):

        """
        Метод удаления физического лица из базы данных с помощью
        SQL-delete с целью очисти базы данных от созданных тестовых
        данных. Удаление производится по person_id физического лица.
        Данный параметр в пределах базы данных уникальный.
        После удаления записей из базы данных, удаляется файл 'file_name'

        :param file_name: имя файла, в котором хранятся person_id
        """

        if os.path.isfile(f'./{file_name}'):  # операции проводить только если файл существует
            logging.debug(f'Приступить к удалению физ.лица из БД')

            person_id = FilesWork.read_file(file_name)

            connection = BaseSQL.db_connection()
            cursor = connection.cursor()
            cursor.execute('DELETE FROM person WHERE person_id = %s', (person_id.strip(),))
            connection.commit()
            logging.debug(f'Физ. лицо удалено из БД')
            BaseSQL.db_disconnection(connection)

            logging.debug(f'Приступить к удалению файла "{file_name}"')
            FilesWork.delete_file(file_name)
            logging.debug(f'Файл "{file_name}" удален')

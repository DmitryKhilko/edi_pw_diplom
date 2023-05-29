import os

from helper.files import FilesWork
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

            Parameters:
            ------------------------
            - param: параметр, передаваемый в SQL-запрос для отбора записи
        """

        connection = BaseSQL.db_connection()

        cursor = connection.cursor()
        cursor.execute('SELECT person_id, first_name, last_name, patronymic, email '
                       'FROM person WHERE person_id = %s', (param,))

        if cursor.rowcount == 1:
            db_rowcount = cursor.rowcount
            # Обязательно нужно cursor.fetchone() записывать в переменную,
            #  если обращаться к cursor.fetchone() в нескольких строках, БД
            #  блокирует такие частые обращения.
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
    def db_delete_row(file_name: str):

        """
            Метод удаления физического лица из базы данных с помощью
            SQL-delete с целью очисти базы данных от созданных тестовых
            данных. Удаление производится по person_id физического лица.
            Данный параметр в пределах базы данных уникальный.
            После удаления записей из базы данных, удаляется файл 'file_name'

            Parameters:
            ------------------------
            - file_name: имя файла, в котором хранятся person_id
        """

        if os.path.isfile(f'./{file_name}'):  # операции проводить только если файл существует

            person_id = FilesWork.read_file(file_name)

            connection = BaseSQL.db_connection()
            cursor = connection.cursor()
            cursor.execute('DELETE FROM person WHERE person_id = %s', (person_id.strip(),))
            connection.commit()
            BaseSQL.db_disconnection(connection)

            FilesWork.delete_file(file_name)

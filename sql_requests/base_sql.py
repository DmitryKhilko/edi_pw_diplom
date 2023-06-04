import psycopg2

from settings import DATABASE, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT


class BaseSQL:

    @staticmethod
    def db_connection():
        """
            Метод, осуществляющий подключение к БД приложения
            с целью проверки записи в БД и удаления из БД
            тестовых данных

            Returns:
            ------------------------
            - connection: соединие с БД
        """
        connection = psycopg2.connect(
            database=DATABASE,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT)
        return connection

    @staticmethod
    def db_disconnection(connection):
        """
            Метод, разрывающий подключение
            к БД приложения
        """
        connection.close()

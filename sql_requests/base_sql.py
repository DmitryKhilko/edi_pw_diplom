import psycopg2


class BaseSQL:

    @staticmethod
    def db_connection():
        connection = psycopg2.connect(
            database='eform_lok291',
            user='eform_user_lok291',
            password='pAs_SworD_lok291',
            host='172.20.208.125',
            port='5432')
        return connection

    @staticmethod
    def db_disconnection(connection):
        connection.close()




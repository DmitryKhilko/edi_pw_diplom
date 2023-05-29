import random
from datetime import datetime, date
from datetime import timedelta


class Fake:

    @staticmethod
    def last_name(length: int, valid: bool, value: any):

        """
            Метод формирования тестовой фамилии пользователя.
            Требования к фамилии: длина от 2 до 50 символов; допустимые
            значения: буквы кириллицы верхнего и нижнего регистра; символ
            «дефис». Обязательно для заполнения.
            Метод может сформировать как валидное значение (valid=True),
            так и невалидное (valid=False). Для этого он будет использовать
            валидные и невалидные наборы символов.
            Метод может генерировать тестовое значение, если value=''.
            Так же возможен ввод значения вручную, если value <> ''

            :parameter
            _____________________
            - length: заданная длина от 0 до ...
            - valid: какую строку сформирует метод - валидную (True) или нет (False)
            - value: значение, введенное вручную

            :return
            _____________________
            - result_str: сформированная строка заданной длины
        """

        if value == '':

            valid_set_1 = 'йцукенгшщзхъфывапролджэячсмитьбю'
            valid_set_2 = 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
            valid_set_3 = '-'
            invalid_set_1 = 'qwertyuiopasdfghjklzxcvbnm'
            invalid_set_2 = 'QWERTYUIOPASDFGHJKLZXCVBNM'
            invalid_set_3 = '`~!@#$%^&*()_+{}|”:?><=[]\’;/.,'
            invalid_set_4 = '🍏😀😃😄😜🐶🐱🐭🐹🐰🐻🍅🍻'
            invalid_set_5 = '1234567890'
            invalid_set_6 = ' '

            result = ''

            if length == 0:  # невалидное значение при любом значении параметра метода valid
                if valid:  # формируем валидное значение (выбрано valid=True)
                    result = ''
                else:  # формируем не валидное значение (выбрано valid=False)
                    result = ''

            elif length == 1:  # невалидное значение при любом значении параметра метода valid
                if valid:  # формируем валидное значение (выбрано valid=True)
                    result = ''.join(random.sample((valid_set_1 + valid_set_2), length))
                else:  # формируем не валидное значение (выбрано valid=False)
                    result = ''.join(random.sample((invalid_set_1 + invalid_set_2 + invalid_set_3 +
                                                    invalid_set_4 + invalid_set_5), length))

            elif length == 2:
                if valid:  # формируем валидное значение (выбрано valid=True)
                    # Формирование результирующей строки без повтора разрешенных символов, без дефиса
                    result = ''.join(random.sample((valid_set_1 + valid_set_2), length - 1))
                    # Формирование результирующей строки без повтора разрешенных символов с дефисом
                    result = ''.join(random.sample((result + valid_set_3), length))
                else:  # формируем не валидное значение (выбрано valid=False)
                    # Формирование результирующей строки без повтора недопустимых символов
                    result = ''.join(random.sample((invalid_set_1 + invalid_set_2 + invalid_set_3 +
                                                    invalid_set_4 + invalid_set_5), length))

            elif 3 <= length <= 51:
                if valid:  # формируем валидное значение (выбрано valid=True)
                    # Формирование результирующей строки без повтора разрешенных символов, без дефиса
                    result = ''.join(random.sample((valid_set_1 + valid_set_2), length - 1))
                    # Формирование результирующей строки без повтора разрешенных символов с дефисом
                    result = ''.join(random.sample((result + valid_set_3), length))
                else:  # формируем не валидное значение (выбрано valid=False)
                    # Формирование результирующей строки без повторов недопустимых символов, без пробела
                    result = ''.join(random.sample((invalid_set_1 + invalid_set_2 + invalid_set_3 +
                                                    invalid_set_4 + invalid_set_5), length - 1))
                    # Добавление внутрь результирующей строки пробела, так как начальный и конечный пробелы
                    # приложение обрезает
                    result = result[:(len(result) - 1)] + invalid_set_6 + result[(len(result) - 1):]

            elif length > 51:
                if valid:  # формируем валидное значение (выбрано valid=True)
                    # Формирование результирующей строки с повтором разрешенных символов без дефиса, так
                    # как не хватает количества символов в наборах символов для формирования длинных строк
                    # без повторов символов
                    result = ''.join(random.choice((valid_set_1 + valid_set_2)) for i in range(length - 1))
                    # Формирование результирующей строки без повтора символов с добавлением дефиса
                    result = ''.join(random.sample((result + valid_set_3), length))
                else:  # формируем не валидное значение (выбрано valid=False)
                    # Формирование результирующей строки с повтором недопустимых символов без пробела, так
                    # как не хватает количества символов в наборах символов для формирования длинных строк
                    # без повторов символов
                    result = ''.join(random.choice((invalid_set_1 + invalid_set_2 + invalid_set_3 +
                                                    invalid_set_4 + invalid_set_5)) for i in range(length - 1))
                    # Добавление внутрь результирующей строки пробел, так как начальный и конечный пробелы
                    # приложение обрезает
                    result = result[:(len(result) - 1)] + invalid_set_6 + result[(len(result) - 1):]

            return result

        else:
            return value

    @staticmethod
    def first_name(length: int, valid: bool, value: any):

        """
            Метод формирования тестового имени пользователя.
            Требования к имени: длина от 2 до 50 символов; допустимые
            значения: буквы кириллицы верхнего и нижнего регистра;
            символ «дефис»; пробелы внутри строки. Обязательно для
            заполнения.
            Метод может сформировать как валидное значение (valid=True),
            так и невалидное (valid=False). Для этого он будет использовать
            валидные и невалидные наборы символов.
            Метод может генерировать тестовое значение, если value=''.
            Так же возможен ввод значения вручную, если value <> ''

            :parameter
            _____________________
            - length: заданная длина от 0 до ...
            - valid: какую строку сформирует метод - валидную (True) или нет (False)
            - value: значение, введенное вручную

            :return
            _____________________
            - result_str: сформированная строка заданной длины
        """

        if value == '':
            if valid:  # формируем валидное значение (выбрано valid=True)
                char_set_1 = 'йцукенгшщзхъфывапролджэячсмитьбю' \
                             'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
            else:  # формируем не валидное значение (выбрано valid=False)
                char_set_1 = 'qwertyuiopasdfghjklzxcvbnm' \
                             'QWERTYUIOPASDFGHJKLZXCVBNM' \
                             '1234567890' \
                             '`~!@#$%^&*()_+{}|”:?><=[]\’;/.,' \
                             '🍏😀😃😄😜🐶🐱🐭🐹🐰🐻🍅🍻'

            char_set_2 = '-'
            char_set_3 = ''
            result_str = ''

            if length == 0:
                result_str = ''

            elif length == 1:
                result_str = ''.join(random.sample(char_set_1, length))

            elif length == 2:
                if valid:  # формируем валидное значение
                    result_str = ''.join(random.sample(char_set_1, length - 1))
                    result_str = ''.join(random.sample((result_str + char_set_2), length))
                else:  # формируем не валидное значение
                    result_str = ''.join(random.sample(char_set_1, length))

            elif 3 <= length <= 51:
                if valid:  # формируем валидное значение
                    result_str = ''.join(random.sample(char_set_1, length - 2))
                    result_str = ''.join(random.sample((result_str + char_set_2), length - 1))
                    result_str = result_str[:(len(result_str) - 1)] + char_set_3 + result_str[(len(result_str) - 1):]
                else:  # формируем не валидное значение
                    result_str = ''.join(random.sample(char_set_1, length))

            elif length > 51:
                if valid:  # формируем валидное значение
                    result_str = ''.join(random.choice(char_set_1) for i in range(length - 2))
                    result_str = ''.join(random.sample((result_str + char_set_2), length - 1))
                    result_str = result_str[:(len(result_str) - 1)] + char_set_3 + result_str[(len(result_str) - 1):]
                else:
                    result_str = ''.join(random.sample(char_set_1, length))

            return result_str

        else:
            return value

    @staticmethod
    def patronymic(length: int, valid: bool, value: any):

        """
            Метод формирования тестового отчества пользователя.
            Требования к отчеству: длина до 50 символов; допустимые
            значения: буквы кириллицы верхнего и нижнего регистра;
            символ «дефис»; пробелы внутри строки. Необязательно для
            заполнения.
            Метод может сформировать как валидное значение (valid=True),
            так и невалидное (valid=False). Для этого он будет использовать
            валидные и невалидные наборы символов.
            Метод может генерировать тестовое значение, если value=''.
            Так же возможен ввод значения вручную, если value <> ''

            :parameter
            _____________________
            - length: заданная длина от 0 до ...
            - valid: какую строку сформирует метод - валидную (True) или нет (False)
            - value: значение, введенное вручную

            :return
            _____________________
            - result_str: сформированная строка заданной длины
        """

        if value == '':

            if valid:  # формируем валидное значение (выбрано valid=True)
                char_set_1 = 'йцукенгшщзхъфывапролджэячсмитьбю' \
                             'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
            else:  # формируем не валидное значение (выбрано valid=False)
                char_set_1 = 'qwertyuiopasdfghjklzxcvbnm' \
                             'QWERTYUIOPASDFGHJKLZXCVBNM' \
                             '1234567890' \
                             '`~!@#$%^&*()_+{}|”:?><=[]\’;/.,' \
                             '🍏😀😃😄😜🐶🐱🐭🐹🐰🐻🍅🍻'

            char_set_2 = '-'
            char_set_3 = ''
            result_str = ''

            if length == 0:
                result_str = ''

            elif length == 1:
                result_str = ''.join(random.sample(char_set_1, length))

            elif length == 2:
                if valid:  # формируем валидное значение
                    result_str = ''.join(random.sample(char_set_1, length - 1))
                    result_str = ''.join(random.sample((result_str + char_set_2), length))
                else:  # формируем не валидное значение
                    result_str = ''.join(random.sample(char_set_1, length))

            elif 3 <= length <= 51:
                if valid:  # формируем валидное значение
                    result_str = ''.join(random.sample(char_set_1, length - 2))
                    result_str = ''.join(random.sample((result_str + char_set_2), length - 1))
                    result_str = result_str[:(len(result_str) - 1)] + char_set_3 + result_str[(len(result_str) - 1):]
                else:  # формируем не валидное значение
                    result_str = ''.join(random.sample(char_set_1, length))

            elif length > 51:
                if valid:  # формируем валидное значение
                    result_str = ''.join(random.choice(char_set_1) for i in range(length - 2))
                    result_str = ''.join(random.sample((result_str + char_set_2), length - 1))
                    result_str = result_str[:(len(result_str) - 1)] + char_set_3 + result_str[(len(result_str) - 1):]
                else:
                    result_str = ''.join(random.sample(char_set_1, length))

            return result_str

        else:
            return value

    @staticmethod
    def date(valid: bool, value: any):

        """
            Метод формирования тестовой даты в формате DD-MM-YYYY
            в диапазоне от 01.01.1900 до сегодняшнего дня.
            Метод может сформировать как валидное значение (valid=True),
            так и невалидное (valid=False).
            Метод может генерировать значение, если value=''.
            Так же возможен ввод значения вручную, если value <> ''

            :parameter
            _____________________
            - valid: какую строку сформирует метод - валидную (True) или нет (False)
            - value: значение, введенное вручную

            :return
            _____________________
            - result_str: сформированная дата
        """

        if value == '':

            result_str = ''

            if valid:  # формируем валидное значение (выбрано valid=True)
                start_date = datetime.strptime('1900-01-01', '%Y-%m-%d')
                end_date = datetime.strptime(str(date.today()), '%Y-%m-%d')
                delta = end_date - start_date
                result_str = str(datetime.date(start_date + timedelta(random.randint(0, delta.days))))
            else:
                tomorrow = str(datetime.date(datetime.strptime(str(date.today() + timedelta(days=1)), '%Y-%m-%d')))
                set_date = (
                    '', ' ', 'датадатада', '0', '1234567890', '00.00.0000', '00.03.1973', '12.00.1973', '12.03.0000',
                    '31.12.1899', '99.99.9999', '12.03.9999', '12.99.1973', '99.03.1973', 'dd.03.1973',
                    '12.mm.1973', '12.03.yyyy', 'dd.mm.yyyy', tomorrow, '12/03/1973')
                result_str = random.choice(set_date)

            return result_str

        else:
            return value

    @staticmethod
    def sex(valid: bool, value: any):

        """
            Метод формирования тестового значения пола.
            Метод может сформировать как валидное значение (valid=True),
            так и невалидное (valid=False).
            Метод может генерировать тестовое значение, если value=''.
            Так же возможен ввод значения вручную, если value <> ''

            :parameter
            _____________________
            - valid: какую строку сформирует метод - валидную (True) или нет (False)
            - value: значение, введенное вручную

            :return
            _____________________
            - result_str: сформированная дата
        """

        if value == '':

            result_str = ''

            if valid:  # формируем валидное значение (выбрано valid=True)
                char_set = (0, 1)
            else:  # формируем не валидное значение (выбрано valid=False)
                char_set = ('-1', '2', '99', None, '', ' ', 'ZsЯщ@5')

            result_str = random.choice(char_set)

            return result_str

        else:
            return value

    @staticmethod
    def phone(length: int, valid: bool, value: any):

        """
            Метод формирования тестового телефона пользователя.
            Требования к телефону: длина до 13 символов; допустимые
            значения: цифры (не больше 12), символ «+» (первым
            символом строки)
            Метод может сформировать как валидное значение (valid=True),
            так и невалидное (valid=False).
            Метод может генерировать тестовое значение, если value=''.
            Так же возможен ввод значения вручную, если value <> ''


            :parameter
            _____________________
            - length: заданная длина от 0 до ...
            - valid: какую строку сформирует метод - валидную (True) или нет (False)
            - value: значение, введенное вручную

            :return
            _____________________
            - result_str: сформированная строка
        """

        if value == '':

            if valid:  # формируем валидное значение (выбрано valid=True)
                char_set_1 = '1234567890'
            else:
                char_set_1 = 'ёйцукенгшщзхъфывапролджэячсмитьбю' \
                             'ЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ' \
                             'qwertyuiopasdfghjklzxcvbnm' \
                             'QWERTYUIOPASDFGHJKLZXCVBNM' \
                             '1234567890' \
                             '`~!@#$%^&*()_{}|”:?><=[]\’;/.,' \
                             '🍏😀😃😄😜🐶🐱🐭🐹🐰🐻🍅🍻'

            char_set_2 = '+'
            result_str = ''

            if length == 0:
                result_str = ''

            elif length == 1:
                result_str = ''.join(random.choice(char_set_1) for i in range(length))

            elif length >= 2:
                if valid:  # формируем валидное значение
                    result_str = ''.join(random.choice(char_set_1) for i in range(length - 1))
                    result_str = char_set_2 + result_str
                else:  # формируем не валидное значение
                    result_str = ''.join(random.choice(char_set_1) for i in range(length - 1))
                    result_str = ''.join(random.sample((result_str + char_set_2), length))

            return result_str

        else:
            return value

    @staticmethod
    def email(length: int, valid: bool, value: any):

        """
            Метод формирования тестового email пользователя.
            Требования к email: длина до 254 символов; должен
            быть валидным адресом электронной почты.
            Метод может сформировать как валидное значение (valid=True),
            так и невалидное (valid=False).
            Метод может генерировать тестовое значение, если value=''.
            Так же возможен ввод значения вручную, если value <> ''

            :parameter
            _____________________
            - length: заданная длина от 0 до ...
            - valid: какую строку сформирует метод - валидную (True) или нет (False)
            - value: значение, введенное вручную

            :return
            _____________________
            - result_str: сформированная строка
        """

        if value == '':

            result = ''

            valid_set_login_1 = 'qwertyuiopasdfghjklzxcvbnm'
            valid_set_login_2 = 'QWERTYUIOPASDFGHJKLZXCVBNM'
            valid_set_login_3 = '1234567890'
            valid_set_login_4 = '^[]-!#$%&*+/=?^_`{}|~'
            valid_set_login_5 = '.'

            valid_set_domain_1 = 'qwertyuiopasdfghjklzxcvbnm'
            valid_set_domain_2 = 'QWERTYUIOPASDFGHJKLZXCVBNM'
            valid_set_domain_3 = '1234567890'
            valid_set_domain_4 = '-'
            valid_set_domain_5 = '.'
            valid_set_domain_6 = ['biz', 'com ', 'edu', 'gov', 'net']

            invalid_set_1 = 'йцукенгшщзхъфывапролджэячсмитьбю'
            invalid_set_2 = 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
            invalid_set_3 = '🍏😀😃😄😜🐶🐱🐭🐹🐰🐻🍅🍻'
            invalid_set_4 = ' '

            if length == 0:
                result = ''

            if length >= 7:
                if valid:  # формируем валидное значение
                    # Формируем domain (правую часть email). Она не должна быть больше 63 символов.
                    if (length - 5)//2 <= 63:
                        domain = ''.join(random.choice(valid_set_domain_1 + valid_set_domain_2 + valid_set_domain_3)
                                         for i in range((length - 5)//2))
                        login = ''.join(random.choice(valid_set_login_1 + valid_set_login_2 + valid_set_login_3) for i in range(length - 5 - ((length - 5)//2)))
                    else:
                        domain = ''.join(random.choice(valid_set_domain_1 + valid_set_domain_2 + valid_set_domain_3)
                                         for i in range(63))
                        login = ''.join(random.choice(valid_set_login_1 + valid_set_login_2 + valid_set_login_3) for i in range(length - 63 - 5))

                    result = login + '@' + domain + '.' + random.choice(valid_set_domain_6)
                    # ? пропускает ли большие буквы?
                    result = result.lower()

                else:  # формируем не валидное значение
                    result = ''.join(random.choice(invalid_set_1 + invalid_set_2 + invalid_set_3) for i in range(length))

            return result

        else:
            return value

    @staticmethod
    def key_id(length: int, valid: bool, value: any):

        """
            Метод формирования тестового идентификатора ключа ЭЦП.
            Требования к строке: длина до 40 символов; допустимые
            значения: латинские буквы верхнего регистра; цифры.
            Метод может сформировать как валидное значение (valid=True),
            так и невалидное (valid=False).
            Метод может генерировать тестовое значение, если value=''.
            Так же возможен ввод значения вручную, если value <> ''

            :parameter
            _____________________
            - length: заданная длина от 0 до ...
            - valid: какую строку сформирует метод - валидную (True) или нет (False)
            - value: значение, введенное вручную

            :return
            _____________________
            - result_str: сформированная строка

        """

        if value == '':

            if valid:  # формируем валидное значение
                char_set_1 = 'QWERTYUIOPASDFGHJKLZX1234567890'
            else:  # формируем не валидное значение
                char_set_1 = 'ёйцукенгшщзхъфывапролджэячсмитьбю' \
                             'ЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ' \
                             'qwertyuiopasdfghjklzxcvbnm' \
                             'QWERTYUIOPASDFGHJKLZXCVBNM' \
                             '1234567890' \
                             '`~!@#$%^&*()_{}|”:?><=[]\’;/.,' \
                             '🍏😀😃😄😜🐶🐱🐭🐹🐰🐻🍅🍻'
            result_str = ''

            if length == 0:
                result_str = ''
            elif length >= 1:
                result_str = ''.join(random.choice(char_set_1) for i in range(length))

            return result_str

        else:
            return value

    @staticmethod
    def card_id(length: int, valid: bool, value: any):

        """
            Метод формирования тестового идентификатора ID-карты.
            Требования к строке: длина до 40 символов; допустимые
            значения: латинские буквы верхнего регистра; цифры.
            Метод может сформировать как валидное значение (valid=True),
            так и невалидное (valid=False).
            Метод может генерировать тестовое значение, если value=''.
            Так же возможен ввод значения вручную, если value <> ''

            :parameter
            _____________________
            - length: заданная длина от 0 до ...
            - valid: какую строку сформирует метод - валидную (True) или нет (False)
            - value: значение, введенное вручную

            :return
            _____________________
            - result_str: сформированная строка

        """

        if value == '':

            if valid:  # формируем валидное значение
                char_set_1 = 'QWERTYUIOPASDFGHJKLZX1234567890'
            else:  # формируем не валидное значение
                char_set_1 = 'ёйцукенгшщзхъфывапролджэячсмитьбю' \
                             'ЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ' \
                             'qwertyuiopasdfghjklzxcvbnm' \
                             'QWERTYUIOPASDFGHJKLZXCVBNM' \
                             '1234567890' \
                             '`~!@#$%^&*()_{}|”:?><=[]\’;/.,' \
                             '🍏😀😃😄😜🐶🐱🐭🐹🐰🐻🍅🍻'
            result_str = ''

            if length == 0:
                result_str = ''
            elif length >= 1:
                result_str = ''.join(random.choice(char_set_1) for i in range(length))

            return result_str

        else:
            return value

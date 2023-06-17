import random
from datetime import datetime, date, timedelta


class Fake:
    @staticmethod
    def text(param_name: str, param_value: any, validation: str):
        """
        Метод формирования тестовой строки для подстановки в текстовые поля.
        Метод не требует введения конкретных значений. Сделано это с целью минимизации
        модернизации тестового фреймворка при изменении разработчиками min и max длины
        параметров. В этом случае замену min и max значений нужно будет сделать только в
        конкретном методе фейкера, не придется модернизировать тестовые данные.
        Возможные значения параметра param_value:
        '' - пустая строка;
        '   ' - три пробела;
        '<min' - длина строки меньше min (нижней границы);
        ' <min' - начальный пробел + длина строки меньше min (+ проверка удаления начальных и конечных пробелов);
        '<min ' - длина строки меньше нижней границы + конечный пробел;
        ' <min ' - начальный пробел + длина строки меньше нижней границы + конечный пробел;
        'min' - длина строки равна нижней границы;
        ' min' - начальный пробел + длина строки равна нижней границы;
        'min ' - длина строки равна нижней границы + конечный пробел;
        ' min ' - начальный длина строки равна нижней границы + конечный пробел;
        '>min' - длина строки больше нижней границы;
        'n' - случайно сгенерированная длина строки между нижней и верхней границей (для избежания эффекта пестицида);
        '<max' - длина строки меньше max (верхней границы);
        'max' - длина строки равна верхней границе;
        ' max' - начальный пробел + длина строки равна max (+ проверка удаления начальных и конечных пробелов);
        'max ' - длина строки равна верхней границе + конечный пробел;
        ' max ' - начальный пробел + длина строки равна верхней границе + конечный пробел;
        '>max' - длина строки больше верхней границы.

        Метод может формировать как валидное значение (validation='valid') - метод использует валидные наборы символов,
        так и невалидное значение (validation='invalid') - метод использует не валидные наборы символов.

        Пользователь может ввести в param_value вручную конкретное (не генерируемое) значение параметра для проверки.

        :param param_name: имя текстового поля на форме; '*' в имени - указание на обязательность заполнения поля
        :param param_value: подстановочные значения, выбираемые для генерации текстовой строки
        :param validation: признак валидности значения параметра: 'valid' или 'invalid'
        :return: возвращаемая сгенерированная строка
        """

        result = ''

        """
        Если пользователь ввел конкретное значение для параметра метода param_value,
        например, f.text('*person_last_name', '123', 'invalid') 
        """
        if param_value not in ('', '   ', '<min', ' <min', '<min ', ' <min ', 'min', ' min', 'min ', ' min ',
                               '>min', 'n', '<max', 'max', ' max', 'max ', ' max ', '>max'):
            return param_value

        else:

            """
            Если пользователь ввел подстановочное значение для параметра метода param_value,
            например, f.text('*person_last_name', 'n', 'valid') 
            """

            if param_name == '*person_last_name':
                """
                Метод формирования тестовой фамилии пользователя.
                Требования к фамилии: 
                - длина от 2 до 50 символов; 
                - допустимые значения: буквы кириллицы верхнего и нижнего регистра; символ «дефис»
                - обязательно для заполнения;
                - начальные и конечные пробелы удаляются.
                """
                min_length = 2
                max_length = 50

                valid_set_1 = 'йцукенгшщзхъфывапролджэячсмитьбю'
                valid_set_2 = 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
                valid_set_3 = '-'
                invalid_set_1 = 'qwertyuiopasdfghjklzxcvbnm'
                invalid_set_2 = 'QWERTYUIOPASDFGHJKLZXCVBNM'
                invalid_set_3 = '`~!@#$%^&*()_+{}|”:?><=[]\’;/.,'
                invalid_set_4 = '🍏😀😃😄😜🐶🐱🐭🐹🐰🐻🍅🍻'
                invalid_set_5 = '1234567890'
                invalid_set_6 = ' '

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == '' and (validation == 'valid' or validation == 'invalid'):
                    result = ''

                if param_value == '   ' and (validation == 'valid' or validation == 'invalid'):
                    result = '   '

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == '<min' and validation == 'valid':
                    # Формирование результирующей строки без повтора валидных символов
                    result = ''.join(random.sample((valid_set_1 + valid_set_2 + valid_set_3), min_length - 1))

                if param_value == '<min' and validation == 'invalid':
                    # Формирование результирующей строки без повтора не валидных символов, без пробела
                    result = ''.join(random.sample((invalid_set_1 + invalid_set_2 + invalid_set_3 +
                                                    invalid_set_4 + invalid_set_5), min_length - 1))

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == ' <min' and validation == 'valid':
                    # Формирование результирующей строки без повтора валидных символов; с начальным пробелом
                    # для проверки автоматического удаления начальных и конечных пробелов
                    result = ' ' + ''.join(random.sample((valid_set_1 + valid_set_2 + valid_set_3), min_length - 1))

                if param_value == ' <min' and validation == 'invalid':
                    # Формирование результирующей строки без повтора не валидных символов; с начальным пробелом
                    # для проверки автоматического удаления начальных и конечных пробелов
                    result = ' ' + ''.join(random.sample((invalid_set_1 + invalid_set_2 + invalid_set_3 +
                                                          invalid_set_4 + invalid_set_5), min_length - 1))

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == '<min ' and validation == 'valid':
                    # Формирование результирующей строки без повтора валидных символов; с конечным пробелом
                    # для проверки автоматического удаления начальных и конечных пробелов
                    result = ''.join(random.sample((valid_set_1 + valid_set_2 + valid_set_3), min_length - 1)) + ' '

                if param_value == '<min ' and validation == 'invalid':
                    # Формирование результирующей строки без повтора не валидных символов; с конечным пробелом
                    # для проверки автоматического удаления начальных и конечных пробелов
                    result = ''.join(random.sample((invalid_set_1 + invalid_set_2 + invalid_set_3 +
                                                    invalid_set_4 + invalid_set_5), min_length - 1)) + ' '

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == ' <min ' and validation == 'valid':
                    # Формирование результирующей строки без повтора валидных символов; с начальным и конечным пробелом
                    # для проверки автоматического удаления начальных и конечных пробелов
                    result = ' ' + ''.join(random.sample((valid_set_1 + valid_set_2 + valid_set_3),
                                                         min_length - 1)) + ' '

                if param_value == ' <min ' and validation == 'invalid':
                    # Формирование результирующей строки без повтора валидных не символов; с начальным и конечным
                    # пробелом для проверки автоматического удаления начальных и конечных пробелов
                    result = ' ' + ''.join(random.sample((invalid_set_1 + invalid_set_2 + invalid_set_3 +
                                                          invalid_set_4 + invalid_set_5), min_length - 1)) + ' '

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == 'min' and validation == 'valid':
                    # Формирование результирующей строки без повтора валидных символов; без дефиса
                    result = ''.join(random.sample((valid_set_1 + valid_set_2), min_length - 1))
                    # Добавление дефиса
                    result = ''.join(random.sample((result + valid_set_3), min_length))

                if param_value == 'min' and validation == 'invalid':
                    # Формирование результирующей строки без повтора не валидных символов
                    result = ''.join(random.sample((invalid_set_1 + invalid_set_2 + invalid_set_3 +
                                                    invalid_set_4 + invalid_set_5), min_length))

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == '>min' and validation == 'valid':
                    # Формирование результирующей строки без повтора валидных символов; без дефиса
                    result = ''.join(random.sample((valid_set_1 + valid_set_2), min_length))
                    # Добавление дефиса
                    result = ''.join(random.sample((result + valid_set_3), min_length + 1))

                if param_value == '>min' and validation == 'invalid':
                    # Формирование результирующей строки без повтора не валидных символов
                    result = ''.join(random.sample((invalid_set_1 + invalid_set_2 + invalid_set_3 +
                                                    invalid_set_4 + invalid_set_5), min_length))
                    # Добавление внутрь результирующей строки пробела
                    result = result[:(len(result) - 1)] + invalid_set_6 + result[(len(result) - 1):]

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == 'n' and validation == 'valid':
                    # Генерация значения случайной длины внутри min и max для генерации строки
                    # min_length + 2 - так как есть отдельная проверка '>min'
                    # max_length - 2 - так как есть отдельная проверка '<max'
                    random_length = random.randint(min_length + 2, max_length - 2)
                    # Формирование результирующей строки без повтора валидных символов со случайной длиной; без дефиса
                    result = ''.join(random.sample((valid_set_1 + valid_set_2), random_length - 1))
                    # Добавление дефиса
                    result = ''.join(random.sample((result + valid_set_3), random_length))

                if param_value == 'n' and validation == 'invalid':
                    # Генерация значения случайной длины внутри min и max для генерации строки
                    random_length = random.randint(min_length + 2, max_length - 2)
                    # Формирование результирующей строки без повтора не валидных символов со случайной длиной
                    result = ''.join(random.sample((invalid_set_1 + invalid_set_2 + invalid_set_3 +
                                                    invalid_set_4 + invalid_set_5), random_length - 1))
                    # Генерация случайного индекса - позиции, куда будут вставлен пробел
                    index = random.randint(1, len(result))
                    # Добавление внутрь результирующей строки пробела
                    result = result[:(len(result) - index)] + invalid_set_6 + result[(len(result) - index):]

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == '<max' and validation == 'valid':
                    # Формирование результирующей строки без повтора валидных символов; без дефиса
                    result = ''.join(random.sample((valid_set_1 + valid_set_2), max_length - 2))
                    # Добавление дефиса
                    result = ''.join(random.sample((result + valid_set_3), max_length - 1))

                if param_value == '<max' and validation == 'invalid':
                    # Формирование результирующей строки без повтора не валидных символов
                    result = ''.join(random.sample((invalid_set_1 + invalid_set_2 + invalid_set_3 +
                                                    invalid_set_4 + invalid_set_5), max_length - 2))
                    # Генерация случайного индекса - позиции, куда будут вставлен пробел
                    index = random.randint(1, len(result))
                    # Добавление внутрь результирующей строки пробела
                    result = result[:(len(result) - index)] + invalid_set_6 + result[(len(result) - index):]

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == 'max' and validation == 'valid':
                    # Формирование результирующей строки без повтора валидных символов; без дефиса
                    result = ''.join(random.sample((valid_set_1 + valid_set_2), max_length - 1))
                    # Добавление дефиса
                    result = ''.join(random.sample((result + valid_set_3), max_length))

                if param_value == 'max' and validation == 'invalid':
                    # Формирование результирующей строки без повтора не валидных символов
                    result = ''.join(random.sample((invalid_set_1 + invalid_set_2 + invalid_set_3 +
                                                    invalid_set_4 + invalid_set_5), max_length - 1))
                    # Генерация случайного индекса - позиции, куда будут вставлен пробел
                    index = random.randint(1, len(result))
                    # Добавление внутрь результирующей строки пробела
                    result = result[:(len(result) - index)] + invalid_set_6 + result[(len(result) - index):]

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == ' max' and validation == 'valid':
                    # Формирование результирующей строки без повтора валидных символов; без дефиса
                    result = ''.join(random.sample((valid_set_1 + valid_set_2), max_length - 1))
                    # Добавление дефиса и начального пробела для проверки автоматического удаления
                    # начальных и конечных пробелов
                    result = ' ' + ''.join(random.sample((result + valid_set_3), max_length))

                if param_value == ' max' and validation == 'invalid':
                    # Формирование результирующей строки без повтора не валидных символов
                    result = ''.join(random.sample((invalid_set_1 + invalid_set_2 + invalid_set_3 +
                                                    invalid_set_4 + invalid_set_5), max_length - 1))
                    # Генерация случайного индекса - позиции, куда будут вставлен пробел
                    index = random.randint(1, len(result))
                    # Добавление внутрь результирующей строки пробела и начального пробела для проверки
                    # автоматического удаления начальных и конечных пробелов
                    result = ' ' + result[:(len(result) - index)] + invalid_set_6 + result[(len(result) - index):]

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == 'max ' and validation == 'valid':
                    # Формирование результирующей строки без повтора валидных символов; без дефиса
                    result = ''.join(random.sample((valid_set_1 + valid_set_2), max_length - 1))
                    # Добавление дефиса и конечного пробела для проверки автоматического удаления
                    # начальных и конечных пробелов
                    result = ''.join(random.sample((result + valid_set_3), max_length)) + ' '

                if param_value == 'max ' and validation == 'invalid':
                    # Формирование результирующей строки без повтора не валидных символов
                    result = ''.join(random.sample((invalid_set_1 + invalid_set_2 + invalid_set_3 +
                                                    invalid_set_4 + invalid_set_5), max_length - 1))
                    # Генерация случайного индекса - позиции, куда будут вставлен пробел
                    index = random.randint(1, len(result))
                    # Добавление внутрь результирующей строки пробела и конечного пробела для проверки
                    # автоматического удаления начальных и конечных пробелов
                    result = result[:(len(result) - index)] + invalid_set_6 + result[(len(result) - index):] + ' '

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == ' max ' and validation == 'valid':
                    # Формирование результирующей строки без повтора валидных символов; без дефиса
                    result = ''.join(random.sample((valid_set_1 + valid_set_2), max_length - 1))
                    # Добавление дефиса, начального и конечного пробела для проверки автоматического удаления
                    # начальных и конечных пробелов
                    result = ' ' + ''.join(random.sample((result + valid_set_3), max_length)) + ' '

                if param_value == ' max ' and validation == 'invalid':
                    # Формирование результирующей строки без повтора не валидных символов
                    result = ''.join(random.sample((invalid_set_1 + invalid_set_2 + invalid_set_3 +
                                                    invalid_set_4 + invalid_set_5), max_length - 1))
                    # Генерация случайного индекса - позиции, куда будут вставлен пробел
                    index = random.randint(1, len(result))
                    # Добавление внутрь результирующей строки пробела, начального и конечного пробела для проверки
                    # автоматического удаления начальных и конечных пробелов
                    result = ' ' + result[:(len(result) - index)] + invalid_set_6 + result[(len(result) - index):] + ' '

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == '>max' and validation == 'valid':
                    # Формирование результирующей строки без повтора валидных символов; без дефиса
                    result = ''.join(random.sample((valid_set_1 + valid_set_2), max_length))
                    # Добавление дефиса
                    result = ''.join(random.sample((result + valid_set_3), max_length + 1))

                if param_value == '>max' and validation == 'invalid':
                    # Формирование результирующей строки без повтора не валидных символов
                    result = ''.join(random.sample((invalid_set_1 + invalid_set_2 + invalid_set_3 +
                                                    invalid_set_4 + invalid_set_5), max_length))
                    # Генерация случайного индекса - позиции, куда будут вставлен пробел
                    index = random.randint(1, len(result))
                    # Добавление внутрь результирующей строки пробела
                    result = result[:(len(result) - index)] + invalid_set_6 + result[(len(result) - index):]

                """ ------------------------------------------------------------------------------------------------"""
                """ ------------------------------------------------------------------------------------------------"""
                """ ------------------------------------------------------------------------------------------------"""

            if param_name in ('*person_first_name', 'person_patronymic'):
                """
                Метод формирования тестового имени физического лица, отчества физического лица.
                Требования к имени, к отчеству: 
                - длина от 2 до 50 символов; 
                - допустимые значения: буквы кириллицы верхнего и нижнего регистра; «дефис»; пробелы внутри строки. 
                - имя обязательно для заполнения;
                - отчество не обязательно для заполнения;
                - начальные и конечные пробелы удаляются.
                """
                min_length = 2
                max_length = 50

                valid_set_1 = 'йцукенгшщзхъфывапролджэячсмитьбю'
                valid_set_2 = 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
                valid_set_3 = '-'
                # TODO Пробел в имени, отчестве вызывает ошибку. Это отклонение от требований
                valid_set_4 = ' '
                # valid_set_4 = ''
                invalid_set_1 = 'qwertyuiopasdfghjklzxcvbnm'
                invalid_set_2 = 'QWERTYUIOPASDFGHJKLZXCVBNM'
                invalid_set_3 = '`~!@#$%^&*()_+{}|”:?><=[]\’;/.,'
                invalid_set_4 = '🍏😀😃😄😜🐶🐱🐭🐹🐰🐻🍅🍻'
                invalid_set_5 = '1234567890'

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == '' and (validation == 'valid' or validation == 'invalid'):
                    result = ''

                if param_value == '   ' and (validation == 'valid' or validation == 'invalid'):
                    result = '   '

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == '<min' and validation == 'valid':
                    # Формирование результирующей строки без повтора валидных символов, без дефиса, без пробела внутри
                    result = ''.join(random.sample((valid_set_1 + valid_set_2 + valid_set_3), min_length - 1))

                if param_value == '<min' and validation == 'invalid':
                    # Формирование результирующей строки без повтора не валидных символов
                    result = ''.join(random.sample((invalid_set_1 + invalid_set_2 + invalid_set_3 +
                                                    invalid_set_4 + invalid_set_5), min_length - 1))

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == ' <min' and validation == 'valid':
                    # Формирование результирующей строки без повтора валидных символов, без дефиса, без пробела внутри;
                    # с начальным пробелом для проверки автоматического удаления начальных и конечных пробелов
                    result = ' ' + ''.join(random.sample((valid_set_1 + valid_set_2 + valid_set_3), min_length - 1))

                if param_value == ' <min' and validation == 'invalid':
                    # Формирование результирующей строки без повтора не валидных символов; с начальным пробелом
                    # для проверки автоматического удаления начальных и конечных пробелов
                    result = ' ' + ''.join(random.sample((invalid_set_1 + invalid_set_2 + invalid_set_3 +
                                                          invalid_set_4 + invalid_set_5), min_length - 1))

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == '<min ' and validation == 'valid':
                    # Формирование результирующей строки без повтора валидных символов, без дефиса, без пробела внутри;
                    # с конечным пробелом для проверки автоматического удаления начальных и конечных пробелов
                    result = ''.join(random.sample((valid_set_1 + valid_set_2 + valid_set_3), min_length - 1)) + ' '

                if param_value == '<min ' and validation == 'invalid':
                    # Формирование результирующей строки без повтора не валидных символов; с конечным пробелом
                    # для проверки автоматического удаления начальных и конечных пробелов
                    result = ''.join(random.sample((invalid_set_1 + invalid_set_2 + invalid_set_3 +
                                                    invalid_set_4 + invalid_set_5), min_length - 1)) + ' '

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == ' <min ' and validation == 'valid':
                    # Формирование результирующей строки без повтора валидных символов, без дефиса,
                    # без пробела внутри; с начальным и конечным пробелом для проверки автоматического удаления
                    # начальных и конечных пробелов
                    result = ' ' + ''.join(random.sample((valid_set_1 + valid_set_2 + valid_set_3),
                                                         min_length - 1)) + ' '

                if param_value == ' <min ' and validation == 'invalid':
                    # Формирование результирующей строки без повтора валидных не символов; с начальным и конечным
                    # пробелом для проверки автоматического удаления начальных и конечных пробелов
                    result = ' ' + ''.join(random.sample((invalid_set_1 + invalid_set_2 + invalid_set_3 +
                                                          invalid_set_4 + invalid_set_5), min_length - 1)) + ' '

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == 'min' and validation == 'valid':
                    # Формирование результирующей строки без повтора валидных символов; без дефиса, без пробела внутри
                    result = ''.join(random.sample((valid_set_1 + valid_set_2), min_length - 1))
                    # Добавление дефиса
                    result = ''.join(random.sample((result + valid_set_3), min_length))

                if param_value == 'min' and validation == 'invalid':
                    # Формирование результирующей строки без повтора не валидных символов
                    result = ''.join(random.sample((invalid_set_1 + invalid_set_2 + invalid_set_3 +
                                                    invalid_set_4 + invalid_set_5), min_length))

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == '>min' and validation == 'valid':
                    # Формирование результирующей строки без повтора валидных символов; без дефиса, без пробела внутри
                    result = ''.join(random.sample((valid_set_1 + valid_set_2), min_length - 1))
                    # Добавление дефиса
                    result = ''.join(random.sample((result + valid_set_3), min_length))
                    # Добавление внутрь результирующей строки пробела
                    result = result[:(len(result) - 1)] + valid_set_4 + result[(len(result) - 1):]

                if param_value == '>min' and validation == 'invalid':
                    # Формирование результирующей строки без повтора не валидных символов
                    result = ''.join(random.sample((invalid_set_1 + invalid_set_2 + invalid_set_3 +
                                                    invalid_set_4 + invalid_set_5), min_length + 1))

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == 'n' and validation == 'valid':
                    # Генерация значения случайной длины внутри min и max для генерации строки
                    # min_length + 2 - так как есть отдельная проверка '>min'
                    # max_length - 2 - так как есть отдельная проверка '<max'
                    random_length = random.randint(min_length + 2, max_length - 2)
                    # Формирование результирующей строки без повтора валидных символов со случайной длиной;
                    # без дефиса, без пробела внутри
                    result = ''.join(random.sample((valid_set_1 + valid_set_2), random_length - 2))
                    # Добавление дефиса
                    result = ''.join(random.sample((result + valid_set_3), random_length - 1))
                    # Генерация случайного индекса - позиции, куда будут вставлен пробел
                    index = random.randint(1, len(result))
                    # Добавление внутрь результирующей строки пробела
                    result = result[:(len(result) - index)] + valid_set_4 + result[(len(result) - index):]

                if param_value == 'n' and validation == 'invalid':
                    # Генерация значения случайной длины внутри min и max для генерации строки
                    random_length = random.randint(min_length + 2, max_length - 2)
                    # Формирование результирующей строки без повтора не валидных символов со случайной длиной
                    result = ''.join(random.sample((invalid_set_1 + invalid_set_2 + invalid_set_3 +
                                                    invalid_set_4 + invalid_set_5), random_length))

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == '<max' and validation == 'valid':
                    # Формирование результирующей строки без повтора валидных символов; без дефиса, без пробела внутри
                    result = ''.join(random.sample((valid_set_1 + valid_set_2), max_length - 3))
                    # Добавление дефиса
                    result = ''.join(random.sample((result + valid_set_3), max_length - 2))
                    # Генерация случайного индекса - позиции, куда будут вставлен пробел
                    index = random.randint(1, len(result))
                    # Добавление внутрь результирующей строки пробела
                    result = result[:(len(result) - index)] + valid_set_4 + result[(len(result) - index):]

                if param_value == '<max' and validation == 'invalid':
                    # Формирование результирующей строки без повтора не валидных символов
                    result = ''.join(random.sample((invalid_set_1 + invalid_set_2 + invalid_set_3 +
                                                    invalid_set_4 + invalid_set_5), max_length - 1))

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == 'max' and validation == 'valid':
                    # Формирование результирующей строки без повтора валидных символов; без дефиса, без пробела внутри
                    result = ''.join(random.sample((valid_set_1 + valid_set_2), max_length - 2))
                    # Добавление дефиса
                    result = ''.join(random.sample((result + valid_set_3), max_length - 1))
                    # Генерация случайного индекса - позиции, куда будут вставлен пробел
                    index = random.randint(1, len(result))
                    # Добавление внутрь результирующей строки пробела
                    result = result[:(len(result) - index)] + valid_set_4 + result[(len(result) - index):]

                if param_value == 'max' and validation == 'invalid':
                    # Формирование результирующей строки без повтора не валидных символов
                    result = ''.join(random.sample((invalid_set_1 + invalid_set_2 + invalid_set_3 +
                                                    invalid_set_4 + invalid_set_5), max_length))

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == ' max' and validation == 'valid':
                    # Формирование результирующей строки без повтора валидных символов; без дефиса, без пробела внутри
                    result = ''.join(random.sample((valid_set_1 + valid_set_2), max_length - 2))
                    # Добавление дефиса
                    result = ''.join(random.sample((result + valid_set_3), max_length - 1))
                    # Генерация случайного индекса - позиции, куда будут вставлен пробел
                    index = random.randint(1, len(result))
                    # Добавление внутрь результирующей строки пробела и начального пробела для проверки автоматического
                    # удаления начальных и конечных пробелов
                    result = ' ' + result[:(len(result) - index)] + valid_set_4 + result[(len(result) - index):]

                if param_value == ' max' and validation == 'invalid':
                    # Формирование результирующей строки без повтора не валидных символов; добавление начального
                    # пробела для проверки автоматического удаления начальных и конечных пробелов
                    result = ' ' + ''.join(random.sample((invalid_set_1 + invalid_set_2 + invalid_set_3 +
                                                          invalid_set_4 + invalid_set_5), max_length))

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == 'max ' and validation == 'valid':
                    # Формирование результирующей строки без повтора валидных символов; без дефиса, без пробела внутри
                    result = ''.join(random.sample((valid_set_1 + valid_set_2), max_length - 2))
                    # Добавление дефиса
                    result = ''.join(random.sample((result + valid_set_3), max_length - 1))
                    # Генерация случайного индекса - позиции, куда будут вставлен пробел
                    index = random.randint(1, len(result))
                    # Добавление внутрь результирующей строки пробела и конечного пробела для проверки автоматического
                    # удаления начальных и конечных пробелов
                    result = result[:(len(result) - index)] + valid_set_4 + result[(len(result) - index):] + ' '

                if param_value == 'max ' and validation == 'invalid':
                    # Формирование результирующей строки без повтора не валидных символов; добавление конечного
                    # пробела для проверки автоматического удаления начальных и конечных пробелов
                    result = ''.join(random.sample((invalid_set_1 + invalid_set_2 + invalid_set_3 +
                                                    invalid_set_4 + invalid_set_5), max_length)) + ' '

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == ' max ' and validation == 'valid':
                    # Формирование результирующей строки без повтора валидных символов; без дефиса, без пробела внутри
                    result = ''.join(random.sample((valid_set_1 + valid_set_2), max_length - 2))
                    # Добавление дефиса
                    result = ''.join(random.sample((result + valid_set_3), max_length - 1))
                    # Генерация случайного индекса - позиции, куда будут вставлен пробел
                    index = random.randint(1, len(result))
                    # Добавление внутрь результирующей строки пробела, начального и конечного пробелов для проверки
                    # автоматического удаления начальных и конечных пробелов
                    result = ' ' + result[:(len(result) - index)] + valid_set_4 + result[(len(result) - index):] + ' '

                if param_value == ' max ' and validation == 'invalid':
                    # Формирование результирующей строки без повтора не валидных символов; добавление начального и
                    # конечного пробелов для проверки автоматического удаления начальных и конечных пробелов
                    result = ' ' + ''.join(random.sample((invalid_set_1 + invalid_set_2 + invalid_set_3 +
                                                          invalid_set_4 + invalid_set_5), max_length)) + ' '

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == '>max' and validation == 'valid':
                    # Формирование результирующей строки без повтора валидных символов; без дефиса, без пробела внутри
                    result = ''.join(random.sample((valid_set_1 + valid_set_2), max_length - 1))
                    # Добавление дефиса
                    result = ''.join(random.sample((result + valid_set_3), max_length))
                    # Генерация случайного индекса - позиции, куда будут вставлен пробел
                    index = random.randint(1, len(result))
                    # Добавление внутрь результирующей строки пробела
                    result = result[:(len(result) - index)] + valid_set_4 + result[(len(result) - index):]

                if param_value == '>max' and validation == 'invalid':
                    # Формирование результирующей строки без повтора не валидных символов
                    result = ''.join(random.sample((invalid_set_1 + invalid_set_2 + invalid_set_3 +
                                                    invalid_set_4 + invalid_set_5), max_length + 1))

                """ ------------------------------------------------------------------------------------------------"""
                """ ------------------------------------------------------------------------------------------------"""
                """ ------------------------------------------------------------------------------------------------"""

            if param_name == 'person_phone':
                """
                Метод формирования тестового телефона физического лица.
                Требования к телефону: 
                - длина до 13 символов; 
                - допустимые значения: цифры (не больше 12), символ «+» (первым символом строки)
                - не обязательно для заполнения;
                - начальные и конечные пробелы удаляются.                
                """

                min_length = 0
                max_length = 13

                valid_set_1 = '1234567890'
                valid_set_2 = '+'
                invalid_set_1 = 'йцукенгшщзхъфывапролджэячсмитьбю'
                invalid_set_2 = 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
                invalid_set_3 = 'qwertyuiopasdfghjklzxcvbnm'
                invalid_set_4 = 'QWERTYUIOPASDFGHJKLZXCVBNM'
                invalid_set_5 = '`~!@#$%^&*()_{-}|”:?><=[]\’;/.,'
                invalid_set_6 = '🍏😀😃😄😜🐶🐱🐭🐹🐰🐻🍅🍻'
                invalid_set_7 = ' '

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == '' and validation == 'valid':
                    result = ''

                if param_value == '   ' and validation == 'valid':
                    result = '   '

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == 'min' and validation == 'valid':
                    result = ''

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == '>min' and validation == 'valid':
                    # Формирование результирующей строки без повтора валидных символов; без плюса
                    result = ''.join(random.sample(valid_set_1, min_length + 1))

                if param_value == '>min' and validation == 'invalid':
                    # Формирование результирующей строки без повтора не валидных символов
                    result = ''.join(random.sample((invalid_set_1 + invalid_set_2 + invalid_set_3 +
                                                    invalid_set_4 + invalid_set_5 + invalid_set_6), min_length + 1))

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == 'n' and validation == 'valid':
                    # Генерация значения случайной длины внутри min и max для генерации строки
                    # min_length + 2 - так как есть отдельная проверка '>min'
                    # max_length - 2 - так как есть отдельная проверка '<max'
                    random_length = random.randint(min_length + 2, max_length - 2)
                    # Формирование результирующей строки без повтора валидных символов со случайной длиной; без плюса
                    result = ''.join(random.sample(valid_set_1, random_length - 1))
                    # Добавление плюса
                    result = valid_set_2 + result

                if param_value == 'n' and validation == 'invalid':
                    # Генерация значения случайной длины внутри min и max для генерации строки
                    random_length = random.randint(min_length + 2, max_length - 2)
                    # Формирование результирующей строки без повтора не валидных символов со случайной длиной
                    result = ''.join(random.sample((invalid_set_1 + invalid_set_2 + invalid_set_3 +
                                                    invalid_set_4 + invalid_set_5 + invalid_set_6), random_length - 2))
                    # Генерация случайного индекса - позиции, куда будут вставлен пробел
                    index = random.randint(1, len(result))
                    # Добавление внутрь результирующей строки пробела
                    result = result[:(len(result) - index)] + invalid_set_7 + result[(len(result) - index):]
                    # Добавление плюса
                    result = valid_set_2 + result

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == '<max' and validation == 'valid':
                    # Формирование результирующей строки с повтором валидных символов; без плюса
                    result = ''.join(random.choice(valid_set_1) for i in range(max_length - 2))
                    # Добавление плюса
                    result = valid_set_2 + result

                if param_value == '<max' and validation == 'invalid':
                    # Формирование результирующей строки без повтора не валидных символов
                    result = ''.join(random.sample((invalid_set_1 + invalid_set_2 + invalid_set_3 +
                                                    invalid_set_4 + invalid_set_5 + invalid_set_6), max_length - 3))
                    # Генерация случайного индекса - позиции, куда будут вставлен пробел
                    index = random.randint(1, len(result))
                    # Добавление внутрь результирующей строки пробела
                    result = result[:(len(result) - index)] + invalid_set_7 + result[(len(result) - index):]
                    # Добавление плюса
                    result = valid_set_2 + result

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == 'max' and validation == 'valid':
                    # Формирование результирующей строки с повтором валидных символов; без плюса
                    result = ''.join(random.choice(valid_set_1) for i in range(max_length - 1))
                    # Добавление плюса
                    result = valid_set_2 + result

                if param_value == 'max' and validation == 'invalid':
                    # Формирование результирующей строки без повтора не валидных символов
                    result = ''.join(random.sample((invalid_set_1 + invalid_set_2 + invalid_set_3 +
                                                    invalid_set_4 + invalid_set_5 + invalid_set_6), max_length - 2))
                    # Генерация случайного индекса - позиции, куда будут вставлен пробел
                    index = random.randint(1, len(result))
                    # Добавление внутрь результирующей строки пробела
                    result = result[:(len(result) - index)] + invalid_set_7 + result[(len(result) - index):]
                    # Добавление плюса
                    result = valid_set_2 + result

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == ' max' and validation == 'valid':
                    # Формирование результирующей строки с повтором валидных символов; без плюса
                    result = ''.join(random.choice(valid_set_1) for i in range(max_length - 1))
                    # Добавление плюса и начального пробела для проверки автоматического удаления
                    # начальных и конечных пробелов
                    result = ' ' + valid_set_2 + result

                if param_value == ' max' and validation == 'invalid':
                    # Формирование результирующей строки без повтора не валидных символов
                    result = ''.join(random.sample((invalid_set_1 + invalid_set_2 + invalid_set_3 +
                                                    invalid_set_4 + invalid_set_5 + invalid_set_6), max_length - 2))
                    # Генерация случайного индекса - позиции, куда будут вставлен пробел
                    index = random.randint(1, len(result))
                    # Добавление внутрь результирующей строки пробела
                    result = result[:(len(result) - index)] + invalid_set_7 + result[(len(result) - index):]
                    # Добавление плюса
                    # Добавление плюса и начального пробела для проверки автоматического удаления
                    # начальных и конечных пробелов
                    result = ' ' + valid_set_2 + result

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == 'max ' and validation == 'valid':
                    # Формирование результирующей строки с повтором валидных символов; без плюса
                    result = ''.join(random.choice(valid_set_1) for i in range(max_length - 1))
                    # Добавление плюса и конечного пробела для проверки автоматического удаления
                    # начальных и конечных пробелов
                    result = valid_set_2 + result + ' '

                if param_value == 'max ' and validation == 'invalid':
                    # Формирование результирующей строки без повтора не валидных символов
                    result = ''.join(random.sample((invalid_set_1 + invalid_set_2 + invalid_set_3 +
                                                    invalid_set_4 + invalid_set_5 + invalid_set_6), max_length - 2))
                    # Генерация случайного индекса - позиции, куда будут вставлен пробел
                    index = random.randint(1, len(result))
                    # Добавление внутрь результирующей строки пробела
                    result = result[:(len(result) - index)] + invalid_set_7 + result[(len(result) - index):]
                    # Добавление плюса
                    # Добавление плюса и конечного пробела для проверки автоматического удаления
                    # начальных и конечных пробелов
                    result = valid_set_2 + result + ' '

                """ ------------------------------------------------------------------------------------------------"""
                if param_value == ' max ' and validation == 'valid':
                    # Формирование результирующей строки с повтором валидных символов; без плюса
                    result = ''.join(random.choice(valid_set_1) for i in range(max_length - 1))
                    # Добавление плюса, начального и конечного пробела для проверки автоматического удаления
                    # начальных и конечных пробелов
                    result = ' ' + valid_set_2 + result + ' '

                if param_value == ' max ' and validation == 'invalid':
                    # Формирование результирующей строки без повтора не валидных символов
                    result = ''.join(random.sample((invalid_set_1 + invalid_set_2 + invalid_set_3 +
                                                    invalid_set_4 + invalid_set_5 + invalid_set_6), max_length - 2))
                    # Генерация случайного индекса - позиции, куда будут вставлен пробел
                    index = random.randint(1, len(result))
                    # Добавление внутрь результирующей строки пробела
                    result = result[:(len(result) - index)] + invalid_set_7 + result[(len(result) - index):]
                    # Добавление плюса
                    # Добавление плюса, начального и конечного пробела для проверки автоматического удаления
                    # начальных и конечных пробелов
                    result = ' ' + valid_set_2 + result + ' '

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == '>max' and validation == 'valid':
                    # Формирование результирующей строки с повтором валидных символов; без плюса
                    result = ''.join(random.choice(valid_set_1) for i in range(max_length))
                    # Добавление плюса
                    result = valid_set_2 + result

                if param_value == '>max' and validation == 'invalid':
                    # Формирование результирующей строки без повтора не валидных символов
                    result = ''.join(random.sample((invalid_set_1 + invalid_set_2 + invalid_set_3 +
                                                    invalid_set_4 + invalid_set_5 + invalid_set_6), max_length - 1))
                    # Генерация случайного индекса - позиции, куда будут вставлен пробел
                    index = random.randint(1, len(result))
                    # Добавление внутрь результирующей строки пробела
                    result = result[:(len(result) - index)] + invalid_set_7 + result[(len(result) - index):]
                    # Добавление плюса
                    result = valid_set_2 + result

                """ ------------------------------------------------------------------------------------------------"""
                """ ------------------------------------------------------------------------------------------------"""
                """ ------------------------------------------------------------------------------------------------"""

            if param_name == '*person_email':
                """
                Метод формирования тестового email физического лица.
                Требования к email: 
                - длина до 254 символов; 
                - допустимые значения: должен быть валидным email
                - обязательно для заполнения;
                - начальные и конечные пробелы удаляются.                
                """

                min_length = 7
                max_length = 254

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
                valid_set_domain_6 = ['biz', 'com', 'edu', 'gov', 'net']

                invalid_set_1 = 'йцукенгшщзхъфывапролджэячсмитьбю'
                invalid_set_2 = 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
                invalid_set_3 = '🍏😀😃😄😜🐶🐱🐭🐹🐰🐻🍅🍻'
                invalid_set_4 = ' '

                def email(length: int):
                    """
                    Вложенная функция, генерирующая email заданной длины

                    :param length: длина генерируемого email
                    :return: сгенерированный email
                    """

                    result_email = ''
                    login_part = ''
                    domain_part = ''

                    if validation == 'valid':
                        if (length - 5) // 2 <= 63:
                            # Формируем domain (правую часть email). Она не должна быть больше 63 символов.
                            domain_part = ''.join(random.choice(valid_set_domain_1 + valid_set_domain_2 +
                                                                valid_set_domain_3) for i in range((length - 5) // 2))
                            # Формируем login (левую часть email) как разность общей длины, длины domain-части, длины
                            # обязательных составных частей email - '@', '.', 'com'
                            login_part = ''.join(random.choice(valid_set_login_1 + valid_set_login_2 +
                                                               valid_set_login_3) for i in range(length - 5 -
                                                                                                 ((length - 5) // 2)))
                        else:
                            domain_part = ''.join(random.choice(valid_set_domain_1 + valid_set_domain_2 +
                                                                valid_set_domain_3) for i in range(63))
                            login_part = ''.join(random.choice(valid_set_login_1 + valid_set_login_2 +
                                                               valid_set_login_3) for i in range(length - 63 - 5))

                    if validation == 'invalid':
                        if (length - 5) // 2 <= 63:
                            # Формируем domain (правую часть email). Она не должна быть больше 63 символов.
                            domain_part = ''.join(random.choice(invalid_set_1 + invalid_set_2 + invalid_set_3)
                                                  for i in range((length - 5) // 2))
                            # Формируем login (левую часть email) как разность общей длины, длины domain-части, длины
                            # обязательных составных частей email - '@', '.', 'com'
                            login_part = ''.join(random.choice(invalid_set_1 + invalid_set_2 + invalid_set_3)
                                                 for i in range(length - 5 - ((length - 5) // 2)))
                        else:
                            domain_part = ''.join(random.choice(invalid_set_1 + invalid_set_2 + invalid_set_3)
                                                  for i in range(63))
                            login_part = ''.join(random.choice(invalid_set_1 + invalid_set_2 + invalid_set_3)
                                                 for i in range(length - 63 - 5))

                    # Соединяем полученные части для формирования email
                    result_email = login_part + '@' + domain_part + '.' + random.choice(valid_set_domain_6)

                    return result_email

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == '' and validation == 'invalid':
                    result = ''

                if param_value == '   ' and validation == 'invalid':
                    result = '   '

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == 'min' and validation == 'valid':
                    result = email(min_length)

                if param_value == 'min' and validation == 'invalid':
                    result = email(min_length)

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == ' min' and validation == 'valid':
                    # Добавляем начальный пробел для проверки автоматического удаления начального и конечного пробелов
                    result = ' ' + email(min_length)

                if param_value == ' min' and validation == 'invalid':
                    # Добавляем начальный пробел для проверки автоматического удаления начального и конечного пробелов
                    result = ' ' + email(min_length)

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == 'min ' and validation == 'valid':
                    # Добавляем конечный пробел для проверки автоматического удаления начального и конечного пробелов
                    result = email(min_length) + ' '

                if param_value == 'min ' and validation == 'invalid':
                    # Добавляем конечный пробел для проверки автоматического удаления начального и конечного пробелов
                    result = email(min_length) + ' '

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == ' min ' and validation == 'valid':
                    # Добавляем начальный и конечный пробелы для проверки автоматического удаления начального
                    # и конечного пробелов
                    result = ' ' + email(min_length) + ' '

                if param_value == ' min ' and validation == 'invalid':
                    # Добавляем начальный и конечный пробелы для проверки автоматического удаления начального
                    # и конечного пробелов
                    result = ' ' + email(min_length) + ' '

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == '>min' and validation == 'valid':
                    result = email(min_length + 1)

                if param_value == '>min' and validation == 'invalid':
                    result = email(min_length + 1)

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == 'n' and validation == 'valid':
                    # Генерация значения случайной длины внутри min и max для генерации email
                    # min_length + 2 - так как есть отдельная проверка '>min'
                    # max_length - 2 - так как есть отдельная проверка '<max'
                    random_length = random.randint(min_length + 2, max_length - 2)
                    result = email(random_length)

                if param_value == 'n' and validation == 'invalid':
                    # Генерация значения случайной длины внутри min и max для генерации email
                    random_length = random.randint(min_length + 2, max_length - 2)
                    result = email(random_length)

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == '<max' and validation == 'valid':
                    result = email(max_length - 1)

                if param_value == '<max' and validation == 'invalid':
                    result = email(max_length - 1)

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == 'max' and validation == 'valid':
                    result = email(max_length)

                if param_value == 'max' and validation == 'invalid':
                    result = email(max_length)

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == ' max' and validation == 'valid':
                    result = ' ' + email(max_length)

                if param_value == ' max' and validation == 'invalid':
                    result = ' ' + email(max_length)

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == 'max ' and validation == 'valid':
                    result = email(max_length) + ' '

                if param_value == 'max ' and validation == 'invalid':
                    result = email(max_length) + ' '

                """ ------------------------------------------------------------------------------------------------"""
                if param_value == ' max ' and validation == 'valid':
                    result = ' ' + email(max_length) + ' '

                if param_value == ' max ' and validation == 'invalid':
                    result = ' ' + email(max_length) + ' '

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == '>max' and validation == 'valid':
                    result = email(max_length + 1)

                if param_value == '>max' and validation == 'invalid':
                    result = email(max_length + 1)

                """ ------------------------------------------------------------------------------------------------"""
                """ ------------------------------------------------------------------------------------------------"""
                """ ------------------------------------------------------------------------------------------------"""

            if param_name == 'person_card_id':
                """
                Метод формирования тестового идентификатора ID-карты физического лица.
                Требования к card_id: 
                - длина до 40 символов; 
                - допустимые значения: латинские буквы верхнего регистра (преобразование к верхнему регистру); цифры;
                - не обязательно для заполнения;
                - начальные и конечные пробелы удаляются.                
                """

                min_length = 0
                max_length = 40

                valid_set_1 = '1234567890'
                valid_set_2 = 'qwertyuiopasdfghjklzxcvbnm'
                valid_set_3 = 'QWERTYUIOPASDFGHJKLZXCVBNM'
                invalid_set_1 = 'йцукенгшщзхъфывапролджэячсмитьбю'
                invalid_set_2 = 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
                invalid_set_3 = '`~!@#$%^&*()_{+-}|”:?><=[]\’;/.,'
                invalid_set_4 = '🍏😀😃😄😜🐶🐱🐭🐹🐰🐻🍅🍻'
                invalid_set_5 = ' '

                def card_id(length: int):
                    """
                    Вложенная функция, генерирующая card_id заданной длины

                    :param length: длина генерируемого card_id
                    :return: сгенерированный card_id
                    """

                    result_card_id = ''

                    if validation == 'valid':
                        result_card_id = ''.join(random.choice(valid_set_1 + valid_set_2 + valid_set_3)
                                                 for i in range(length))

                    if validation == 'invalid':
                        if length <= 2:
                            result_card_id = ''.join(random.choice(invalid_set_1 + invalid_set_2 + invalid_set_3 +
                                                                   invalid_set_4) for i in range(length))
                        if length >= 3:
                            result_card_id = ''.join(random.choice(invalid_set_1 + invalid_set_2 + invalid_set_3 +
                                                                   invalid_set_4) for i in range(length - 1))
                            # Генерация случайного индекса - позиции, куда будут вставлен пробел
                            index = random.randint(1, len(result_card_id))
                            # Добавление внутрь результирующей строки пробела
                            result_card_id = result_card_id[:(len(result_card_id) - index)] + invalid_set_5 + \
                                             result_card_id[(len(result_card_id) - index):]

                    return result_card_id

                """ ------------------------------------------------------------------------------------------------"""

                if param_value in ('', 'min') and validation == 'valid':
                    result = ''

                if param_value == '   ' and validation == 'valid':
                    result = '   '

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == '>min' and validation == 'valid':
                    result = card_id(min_length + 1)

                if param_value == '>min' and validation == 'invalid':
                    result = card_id(min_length + 1)

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == 'n' and validation == 'valid':
                    # Генерация значения случайной длины внутри min и max для генерации email
                    # min_length + 2 - так как есть отдельная проверка '>min'
                    # max_length - 2 - так как есть отдельная проверка '<max'
                    random_length = random.randint(min_length + 2, max_length - 2)
                    result = card_id(random_length)

                if param_value == 'n' and validation == 'invalid':
                    # Генерация значения случайной длины внутри min и max для генерации email
                    random_length = random.randint(min_length + 2, max_length - 2)
                    result = card_id(random_length)

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == '<max' and validation == 'valid':
                    result = card_id(max_length - 1)

                if param_value == '<max' and validation == 'invalid':
                    # max_length, так как на UI пробелы автоматически стираются, проверить на уровне API
                    result = card_id(max_length)

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == 'max' and validation == 'valid':
                    result = card_id(max_length)

                if param_value == 'max' and validation == 'invalid':
                    # max_length + 1, так как на UI пробелы автоматически стираются, проверить на уровне API
                    result = card_id(max_length + 1)

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == ' max' and validation == 'valid':
                    result = ' ' + card_id(max_length)

                if param_value == ' max' and validation == 'invalid':
                    # max_length + 1, так как на UI пробелы автоматически стираются, проверить на уровне API
                    result = ' ' + card_id(max_length + 1)

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == 'max ' and validation == 'valid':
                    result = card_id(max_length) + ' '

                if param_value == 'max ' and validation == 'invalid':
                    # max_length + 1, так как на UI пробелы автоматически стираются, проверить на уровне API
                    result = card_id(max_length + 1) + ' '

                """ ------------------------------------------------------------------------------------------------"""
                if param_value == ' max ' and validation == 'valid':
                    result = ' ' + card_id(max_length) + ' '

                if param_value == ' max ' and validation == 'invalid':
                    # max_length + 1, так как на UI пробелы автоматически стираются, проверить на уровне API
                    result = ' ' + card_id(max_length + 1) + ' '

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == '>max' and validation == 'valid':
                    result = card_id(max_length + 1)

                if param_value == '>max' and validation == 'invalid':
                    # max_length + 2, так как на UI пробелы автоматически стираются, проверить на уровне API
                    result = card_id(max_length + 2)

                """ ------------------------------------------------------------------------------------------------"""
                """ ------------------------------------------------------------------------------------------------"""
                """ ------------------------------------------------------------------------------------------------"""

            if param_name == 'person_key_id':
                """
                Метод формирования тестового идентификатора ключа ЭЦП физического лица.
                Требования к card_id: 
                - длина до 40 символов; 
                - допустимые значения: латинские буквы верхнего регистра (преобразование к верхнему регистру); цифры;
                - не обязательно для заполнения;
                - начальные и конечные пробелы удаляются.                
                """

                min_length = 0
                max_length = 40

                valid_set_1 = '1234567890'
                valid_set_2 = 'qwertyuiopasdfghjklzxcvbnm'
                valid_set_3 = 'QWERTYUIOPASDFGHJKLZXCVBNM'
                invalid_set_1 = 'йцукенгшщзхъфывапролджэячсмитьбю'
                invalid_set_2 = 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
                invalid_set_3 = '`~!@#$%^&*()_{+-}|”:?><=[]\’;/.,'
                invalid_set_4 = '🍏😀😃😄😜🐶🐱🐭🐹🐰🐻🍅🍻'
                invalid_set_5 = ' '

                def key_id(length: int):
                    """
                    Вложенная функция, генерирующая key_id заданной длины

                    :param length: длина генерируемого key_id
                    :return: сгенерированный key_id
                    """

                    result_key_id = ''

                    if validation == 'valid':
                        result_key_id = ''.join(random.choice(valid_set_1 + valid_set_2 + valid_set_3)
                                                for i in range(length))

                    if validation == 'invalid':
                        if length <= 2:
                            result_key_id = ''.join(random.choice(invalid_set_1 + invalid_set_2 + invalid_set_3 +
                                                                  invalid_set_4) for i in range(length))

                        if length >= 3:
                            result_key_id = ''.join(random.choice(invalid_set_1 + invalid_set_2 + invalid_set_3 +
                                                                  invalid_set_4) for i in range(length - 1))
                            # Генерация случайного индекса - позиции, куда будут вставлен пробел
                            index = random.randint(1, len(result_key_id))
                            # Добавление внутрь результирующей строки пробела
                            result_key_id = result_key_id[:(len(result_key_id) - index)] + invalid_set_5 + \
                                            result_key_id[(len(result_key_id) - index):]

                    return result_key_id

                """ ------------------------------------------------------------------------------------------------"""

                if param_value in ('', 'min') and validation == 'valid':
                    result = ''

                if param_value == '   ' and validation == 'valid':
                    result = '   '

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == '>min' and validation == 'valid':
                    result = key_id(min_length + 1)

                if param_value == '>min' and validation == 'invalid':
                    result = key_id(min_length + 1)

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == 'n' and validation == 'valid':
                    # Генерация значения случайной длины внутри min и max для генерации email
                    # min_length + 2 - так как есть отдельная проверка '>min'
                    # max_length - 2 - так как есть отдельная проверка '<max'
                    random_length = random.randint(min_length + 2, max_length - 2)
                    result = key_id(random_length)

                if param_value == 'n' and validation == 'invalid':
                    # Генерация значения случайной длины внутри min и max для генерации email
                    random_length = random.randint(min_length + 2, max_length - 2)
                    result = key_id(random_length)

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == '<max' and validation == 'valid':
                    result = key_id(max_length - 1)

                if param_value == '<max' and validation == 'invalid':
                    # max_length, так как на UI пробелы автоматически стираются, проверить на уровне API
                    result = key_id(max_length)

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == 'max' and validation == 'valid':
                    result = key_id(max_length)

                if param_value == 'max' and validation == 'invalid':
                    # max_length + 1, так как на UI пробелы автоматически стираются, проверить на уровне API
                    result = key_id(max_length + 1)

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == ' max' and validation == 'valid':
                    result = ' ' + key_id(max_length)

                if param_value == ' max' and validation == 'invalid':
                    # max_length + 1, так как на UI пробелы автоматически стираются, проверить на уровне API
                    result = ' ' + key_id(max_length + 1)

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == 'max ' and validation == 'valid':
                    result = key_id(max_length) + ' '

                if param_value == 'max ' and validation == 'invalid':
                    # max_length + 1, так как на UI пробелы автоматически стираются, проверить на уровне API
                    result = key_id(max_length + 1) + ' '

                """ ------------------------------------------------------------------------------------------------"""
                if param_value == ' max ' and validation == 'valid':
                    result = ' ' + key_id(max_length) + ' '

                if param_value == ' max ' and validation == 'invalid':
                    # max_length + 1, так как на UI пробелы автоматически стираются, проверить на уровне API
                    result = ' ' + key_id(max_length + 1) + ' '

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == '>max' and validation == 'valid':
                    result = key_id(max_length + 1)

                if param_value == '>max' and validation == 'invalid':
                    # max_length + 2, так как на UI пробелы автоматически стираются, проверить на уровне API
                    result = key_id(max_length + 2)

                """ ------------------------------------------------------------------------------------------------"""
                """ ------------------------------------------------------------------------------------------------"""
                """ ------------------------------------------------------------------------------------------------"""

        return result

    @staticmethod
    def date(param_name: str, param_value: any, validation: str):
        """
        Метод формирования тестовой даты в формате DD-MM-YYYY для подстановки в соответствующие поля.
        Метод не требует введения конкретных значений. Сделано это с целью минимизации
        модернизации тестового фреймворка при изменении разработчиками min и max даты.
        В этом случае замену min и max значений нужно будет сделать только в
        конкретном методе фейкера, не придется модернизировать тестовые данные.
        Возможные значения параметра param_value:
        '' - пустая строка;
        '   ' - три пробела;
        '<min' - дата меньше min (нижней границы);
        'min' - дата равна нижней границы;
        '>min' - дата больше нижней границы;
        'n' - случайно сгенерированная дата между нижней и верхней границей (для избежания эффекта пестицида);
        ' n' - начальный пробел + случайно сгенерированная дата между нижней и верхней границей;
        'n ' - случайно сгенерированная дата между нижней и верхней границей + конечный пробел;
        ' n ' - начальный и конечный пробелы + случайно сгенерированная дата между нижней и верхней границей;
        '<max' - дата меньше max (верхней границы);
        'max' - дата равна верхней границе;
        '>max' - дата больше верхней границы.

        Метод может формировать как валидное значение (validation='valid') - метод генерирует валидные даты,
        так и невалидное значение (validation='invalid') - метод использует набор не валидных дат.

        Пользователь может ввести в param_value вручную конкретное (не генерируемое) значение параметра для проверки.

        :param param_name: наименование поля на форме; '*' в имени - указание на обязательность заполнения поля
        :param param_value: подстановочные значения, выбираемые для генерации даты
        :param validation: признак валидности значения параметра: 'valid' или 'invalid'
        :return: возвращаемая сгенерированная дата
        """

        result = ''

        invalid_set = (
            'датадатада', '0', '1234567890', '00.00.0000', '0000-00-00', '00.03.1973', '1973-03-00',
            '12.00.1973', '1973-00-12', '12.03.0000', '0000-03-12', '99.99.9999', '9999-99-99', '12.99.1973',
            '1973-99-12', '99.03.1973', '1973-03-99', 'dd.03.1973', '1973-03-dd', '12.mm.1973', '1973-mm-12',
            '12.03.yyyy', 'yyyy-03-12' 'dd.mm.yyyy', 'yyyy-mm-dd', '12/03/1973', '1973/03/12',
            '🍏😀.🐱🐹.🐰🐻🍅🍻', '🍏😀🐱🐹-🐰🐻-🍅🍻'
        )

        """
        Если пользователь ввел конкретное значение для параметра метода param_value,
        например, f.data('person_birthday', '99.03.1973', 'invalid') 
        """
        if param_value not in ('', '   ', '<min', 'min', '>min', 'n', ' n', 'n ', ' n ', '<max', 'max', '>max'):
            return param_value

        else:

            """
            Если пользователь ввел подстановочное значение для параметра метода param_value,
            например, f.text('person_birthday', 'n', 'valid') 
            """

            if param_name == 'person_birthday':
                """
                Метод формирования даты рождения физического лица.
                Требования к дате: 
                - формат YYYY-MM-DD или DD.MM.YYYY
                - не обязательно для заполнения.
                """

                min_date = datetime.strptime('0001-01-01', '%Y-%m-%d')
                max_date = datetime.strptime(str(date.today()), '%Y-%m-%d')  # не больше сегодняшней даты

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == '' and validation == 'invalid':
                    result = ''

                if param_value == '   ' and validation == 'invalid':
                    result = '   '

                """ ------------------------------------------------------------------------------------------------"""

                # if param_value == '<min': - меньше минимальной даты не введешь, она самая минимальная 01.01.0001
                #     result = str(min_date - timedelta(days=1))

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == 'min' and validation == 'valid':
                    result = str(min_date.date())

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == '>min' and validation == 'valid':
                    result = str(min_date.date() + timedelta(days=1))

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == 'n' and validation == 'valid':
                    delta = max_date - min_date
                    result = str(datetime.date(min_date + timedelta(random.randint(0, delta.days))))

                if param_value == 'n' and validation == 'invalid':
                    result = random.choice(invalid_set)

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == ' n' and validation == 'valid':
                    delta = max_date - min_date
                    result = ' ' + str(datetime.date(min_date + timedelta(random.randint(0, delta.days))))

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == 'n ' and validation == 'valid':
                    delta = max_date - min_date
                    result = str(datetime.date(min_date + timedelta(random.randint(0, delta.days)))) + ' '

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == ' n ' and validation == 'valid':
                    delta = max_date - min_date
                    result = ' ' + str(datetime.date(min_date + timedelta(random.randint(0, delta.days)))) + ' '

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == '<max' and validation == 'valid':
                    result = str(max_date.date() - timedelta(days=1))

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == 'max' and validation == 'valid':
                    result = str(max_date.date())

                """ ------------------------------------------------------------------------------------------------"""

                if param_value == '>max' and validation == 'invalid':
                    result = str(max_date.date() + timedelta(days=1))

        return result

    @staticmethod
    def drop_down_list(param_name: str, param_value: any, validation: str):

        """
        Метод выбора кода значения раскрывающегося списка.
        Метод не требует введения конкретных значений. Сделано это с целью минимизации
        модернизации тестового фреймворка при изменении (добавлении новых) разработчиками кодов элементов
        раскрывающегося списка. В этом случае изменения нужно будет внести только в
        конкретном методе фейкера (изменить соответствующий set), не придется модернизировать тестовые данные.
        Возможные значения параметра param_value:
        'n' - случайно выбранное значение из valid_set или invalid_set (для избежания эффекта пестицида).

        Метод может формировать как валидное значение (validation='valid') - выбираются валидные значения кодов,
        так и невалидное значение (validation='invalid') - выбираются не валидные значения кодов.

        Пользователь может ввести в param_value вручную конкретное (не генерируемое) значение параметра для проверки.

        :param param_name: наименование раскрывающегося списка на форме
        :param param_value: выбранный код элемента раскрывающегося списка
        :param validation: признак валидности значения параметра: 'valid' или 'invalid'
        :return: возвращаемый код элемента раскрывающегося списка
        """

        result = ''

        if param_name == 'person_sex':
            """
            Метод выбора пола физического лица.
            Требования к дате: 
            - 0 - женский пол;
            - 1 - мужской пол;
            - не обязательно для заполнения.
            """

            valid_set = (0, 1)
            invalid_set = (-1, 2, 11, '0', '1', None, '', '  ', 'ZsЯщ@5')

            """
            Если пользователь ввел конкретное значение для параметра метода param_value,
            например, f.drop_down_list('person_sex', 'ZsЯщ@5', 'invalid') 
            """
            if param_value not in ('', '   ', 'n', ' n', 'n ', ' n '):
                return param_value

            else:

                """
                Если пользователь ввел подстановочное значение для параметра метода param_value,
                например, f.drop_down_list('person_sex', 'n', 'valid') 
                """

                if param_value == 'n' and validation == 'valid':
                    result = random.choice(valid_set)

                if param_value == ' n' and validation == 'valid':
                    result = ' ' + random.choice(valid_set)

                if param_value == 'n ' and validation == 'valid':
                    result = random.choice(valid_set) + ' '

                if param_value == ' n ' and validation == 'valid':
                    result = ' ' + random.choice(valid_set) + ' '

                if param_value == 'n' and validation == 'invalid':
                    result = random.choice(invalid_set)

        return result

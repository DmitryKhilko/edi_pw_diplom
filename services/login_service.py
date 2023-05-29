import allure

from services.base_service import BaseService


class LoginService(BaseService):
    @staticmethod
    @allure.step('Войти в приложении под ролью {user_role}')
    def login(user: tuple, user_role: str, expected_set_csrf_code=200, expected_login_code=200):
        """
            Метод авторизации: с помощью get-запроса создается CSRF-токен,
            далее с помощью post-запроса происходит вход в приложение по
            логину и паролю с использованием ранее созданного CSRF-токена.
            Результатом работы метода являются возвращаемые значения cookie
            для их передачи в иные запросы: csrftoken, sessionid.
            Метод необходим для выполнения последующих операций в приложении

            Parameters:
            ------------------------
            - user: кортеж, содержащий логин, пароль, email_account пользователя
            - user_role: роль пользователя для отображения в allure.steps
            - expected_set_csrf_code: ожидаемый код ответа при успешном создании CSRF-токена
            - expected_login_code: ожидаемый код ответа при успешном входе в приложение
        """

        with allure.step(f'Создать CSRF-токен'):
            csrftoken, status_code = BaseService.get_csrftoken()
            assert status_code == expected_set_csrf_code, 'CSRF куки не установлен'

        with allure.step(f'Авторизоваться с помощью логина и пароля'):
            csrftoken, sessionid, status_code, reason, result = BaseService.authorization(csrftoken, user)
            assert status_code == expected_login_code, 'Авторизация с помощью логина и пароля неуспешна'
            assert result['user']['email'] == user[3], 'Фактический и ожидаемый email учетной записи не совпали'
            return csrftoken, sessionid

    @staticmethod
    @allure.step('Войти в приложении под ролью {user_role}')
    def login_by_role(user: tuple, message: tuple, user_role: str, expected_set_csrf_code=200):
        """
            Метод проверки успешности входа в приложение под разными ролями приложения:
            с помощью get-запроса создается CSRF-токен, далее с помощью post-запроса
            происходит вход в приложение по логину и паролю для конкретной роли приложения
            с использованием ранее созданного CSRF-токена. Результатом работы метода
            являются вход в приложение

            Parameters:
            ------------------------
            - user: кортеж, содержащий логин, пароль, email_account пользователя
            - user_role: роль пользователя для отображения в allure.steps
            - expected_set_csrf_code: ожидаемый код ответа при успешном создании CSRF-токена
            - message: ожидаемый ответ сервера
        """

        with allure.step(f'Создать CSRF-токен'):
            csrftoken, status_code = BaseService.get_csrftoken()
            assert status_code == expected_set_csrf_code, 'CSRF куки не установлен'

        with allure.step(f'Авторизоваться с помощью логина и пароля'):
            csrftoken, sessionid, status_code, reason, result = BaseService.authorization(csrftoken, user)
            with allure.step('Ожидаемый результат: пользователь успешно вошёл в приложение'):
                print(f"Ожидаемый status_code: '{message[0]}', '{message[1]}'")
                print(f"Фактический status_code: '{status_code}', '{reason}'")
                print(f"Ожидаемая роль: '{user[0]}'")
                print(f"Фактическая роль: '{result['user']['role']['name']}'")
                print(f"Ожидаемый email: '{user[3]}'")
                print(f"Фактический email: '{result['user']['email']}'")
                assert status_code == message[0], 'Авторизация с помощью логина и пароля неуспешна'
                assert result['user']['role']['name'] == user[0], 'Фактическая и ожидаемая роль учетной записи не совпали'
                assert result['user']['email'] == user[3], 'Фактический и ожидаемый email учетной записи не совпали'

    @staticmethod
    @allure.step('Войти в приложении под ролью {user_role}')
    def can_not_login(user: tuple, message: tuple, user_role: str, expected_set_csrf_code=200):
        """
            Метод проверки невозможности входа в приложение при невалидных
            логине и (или) пароле: с помощью get-запроса создается CSRF-токен,
            далее с помощью post-запроса происходит попытка входа в приложение по
            логину и паролю с использованием ранее созданного CSRF-токена.
            Результатом работы метода являются сообщения о невозможности входа
            в приложение

            Parameters:
            ------------------------
            - user: кортеж, содержащий логин, пароль, email_account пользователя
            - user_role: роль пользователя для отображения в allure.steps
            - expected_set_csrf_code: ожидаемый код ответа при успешном создании CSRF-токена
            - message: ожидаемый ответ сервера
        """

        with allure.step(f'Создать CSRF-токен'):
            csrftoken, status_code = BaseService.get_csrftoken()
            assert status_code == expected_set_csrf_code, 'CSRF куки не установлен'

        with allure.step(f'Авторизоваться с помощью логина и пароля'):
            csrftoken, sessionid, status_code, reason, result = BaseService.authorization(csrftoken, user)
            with allure.step('Ожидаемый результат: пользователь не смог войти в приложение'):
                print(f"Ожидаемый status_code: '{message[0]}', '{message[1]}'")
                print(f"Фактический status_code: '{status_code}', '{reason}'")
                print(f"Ожидаемый response.json(): {message[2]}'")
                print(f"Фактический response.json(): {result}'")
                assert status_code == message[0], 'Возможно авторизация прошла успешно при использовании ' \
                                                  'невалидных логина и пароля'
                assert result == message[2], 'Сообщение не соответствует ожидаемому'

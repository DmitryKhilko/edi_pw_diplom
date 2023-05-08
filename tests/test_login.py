import allure
from pytest import mark

from data.function_parameters import login_data
from pages.loginpage import Login


class TestLoginPassword:
    @mark.parametrize('login, password, fio, user_organization, user_role', login_data)
    @allure.title(f'Вход пользователя в EDI-Flow по валидным логину и паролю')
    def test_login_by_role(self, web_app, login, password, fio, user_organization, user_role):
        login_page = Login(web_app)
        login_page.navigate()
        login_page.login(login, password)
        login_page.check_login(fio, user_organization, user_role)

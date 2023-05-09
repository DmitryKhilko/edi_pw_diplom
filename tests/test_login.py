import allure
from pytest import mark
from pages.login_page import Login
from data.login_data import login_parameters


class TestLoginPassword:

    @mark.parametrize('p01_login, p02_password, result01_fio, result02_user_role, result03_user_organization', login_parameters)
    @allure.title(f'Вход пользователя в EDI-Flow по валидным логину и паролю')
    def test_login_by_role(self, web_app, p01_login, p02_password, result01_fio, result02_user_role, result03_user_organization):
        # login_page = Login(web_app)
        # login_page.navigate()
        # login_page.login(p01_login, p02_password)
        # login_page.check_login(result01_fio, result02_user_role, result03_user_organization)

        Login(web_app).\
            navigate().\
            login(p01_login, p02_password).\
            check_login(result01_fio, result02_user_role, result03_user_organization)

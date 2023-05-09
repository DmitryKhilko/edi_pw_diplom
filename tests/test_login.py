import allure
from pytest import mark
from pages.login_page import Login
from data.login_data import login_parameters


class TestLoginPassword:

    @mark.parametrize('p1_login, p2_password, result1_fio, result2_user_role, result3_user_organization', login_parameters)
    @allure.title(f'Вход пользователя в EDI-Flow по валидным логину и паролю')
    def test_login_by_role(self, web_app, p1_login, p2_password, result1_fio, result2_user_role, result3_user_organization):
        # login_page = Login(web_app)
        # login_page.navigate()
        # login_page.login(p1_login, p2_password)
        # login_page.check_login(result1_fio, result2_user_role, result3_user_organization)

        Login(web_app).\
            navigate().\
            login(p1_login, p2_password).\
            check_login(result1_fio, result2_user_role, result3_user_organization)

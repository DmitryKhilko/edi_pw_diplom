import allure
from playwright.sync_api import expect
from pages.basepage import BasePage, BASE_URL

LOGIN_PAGE_URL = '/login'


class Login(BasePage):

    def navigate(self):
        with allure.step(f'Перейти на страницу: {BASE_URL + LOGIN_PAGE_URL}'):
            self.page.goto(BASE_URL + LOGIN_PAGE_URL)

    def login(self, login: str, password: str):
        with allure.step(f'Ввести в поле "Логин" значение: {login}'):
            self.page.get_by_label('Логин').fill(login)
        with allure.step(f'Ввести в поле "Пароль" значение: {password}'):
            self.page.get_by_label('Пароль').fill(password)
        with allure.step(f'Нажать кнопку "Войти"'):
            self.page.get_by_role('button', name='Войти', exact=True).click()

    @allure.step('Ожидаемый результат: вход в приложение')
    def check_login(self, fio: str, user_organization: str, user_role: str):
        expect(self.page.get_by_text(fio, exact=True)).to_be_visible()
        expect(self.page.get_by_role('button', name=user_role)).to_be_visible()
        expect(self.page.get_by_role('paragraph').filter(has_text=user_organization)).to_be_visible()

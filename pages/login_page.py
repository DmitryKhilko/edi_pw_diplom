import allure
from playwright.sync_api import expect

from pages.base_page import BasePage
from data.url_data import BASE_URL, LOGIN_PAGE_URL
from data.login_data import *


class Login(BasePage):

    def navigate(self):
        self.goto_with_allure_step(BASE_URL + LOGIN_PAGE_URL)

    def login(self, login: str, password: str):
        self.text_field_fill_with_allure_step(LOGIN_LOGIN_LABEL_NAME, login)
        self.text_field_fill_with_allure_step(LOGIN_PASSWORD_LABEL_NAME, password)
        self.button_click_with_allure_step(LOGIN_BUTTON_LOGIN_NAME)

    """
    Метод для входа в приложение, содержащий только один allure.step,
    для использования в проверках функциях, отличных от логина 
    """
    @allure.step('Войти в приложение')
    def login_fast(self, login: str, password: str):
        self.navigate()
        self.text_field_fill(LOGIN_LOGIN_LABEL_NAME, login)
        self.text_field_fill(LOGIN_PASSWORD_LABEL_NAME, password)
        self.button_click(LOGIN_BUTTON_LOGIN_NAME)

    # TODO Сделать: в base_page сделать универсальную функцию expect_to_be_visible, локаторы заменить на xpath
    @allure.step('Ожидаемый результат: вход в приложение')
    def check_login(self, result1_fio: str, result2_user_role: str, result3_user_organization: str):
        expect(self.page.get_by_text(result1_fio, exact=True)).to_be_visible()  # //*[text() = "Смирнов" and text() = "Алексей" and text() = "Павлович"]   fio.split(' ')[0] - это из ФИО выделяется фамилия
        expect(self.page.get_by_role('button', name=result2_user_role)).to_be_visible()  # //*[contains(@class, "logo")]//*[text() = "Администратор ИБ"]
        expect(self.page.get_by_role('paragraph').filter(has_text=result3_user_organization)).to_be_visible()  # //*[contains(@class, "logo")]//*[text() = 'УП "ИВЦ "Минфина"']

import allure
from playwright.sync_api import expect

from data.constants import BASE_URL, LOGIN_PAGE_URL
from pages.base_page import BasePage


class Login(BasePage):

    def navigate(self):
        self.goto(BASE_URL + LOGIN_PAGE_URL)

    def login(self, login: str, password: str):
        self.text_field_fill('Логин', login)
        self.text_field_fill('Пароль', password)
        self.button_click('Войти')

    # TODO Сделать: сделать еще один метод login для входа в приложение с целью проведения иных проверок. В этом методе не расписывать шаги - будет один шаг - войти в приложение.
    def login_fast(self):
        pass

    # TODO Сделать: в base_page сделать универсальную функцию expect_to_be_visible, локаторы заменить на xpath
    @allure.step('Ожидаемый результат: вход в приложение')
    def check_login(self, result1_fio: str, result2_user_role: str, result3_user_organization: str):
        expect(self.page.get_by_text(result1_fio, exact=True)).to_be_visible()  # //*[text() = "Смирнов" and text() = "Алексей" and text() = "Павлович"]   fio.split(' ')[0] - это из ФИО выделяется фамилия
        expect(self.page.get_by_role('button', name=result2_user_role)).to_be_visible()  # //*[contains(@class, "logo")]//*[text() = "Администратор ИБ"]
        expect(self.page.get_by_role('paragraph').filter(has_text=result3_user_organization)).to_be_visible()  # //*[contains(@class, "logo")]//*[text() = 'УП "ИВЦ "Минфина"']

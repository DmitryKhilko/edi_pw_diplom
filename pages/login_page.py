import allure
from playwright.sync_api import expect

from pages.base_page import BasePage
from data.url_data import BASE_URL, LOGIN_PAGE_URL
from data.login_data import *


class Login(BasePage):

    locator_first_name = '//input[@name="first_name"]'

    def navigate(self):
        """
        Метод перехода на указанную страницу приложения,
        содержащий allure.step для формирования детальных шагов
        в тест-кейсах Allure TestOps

        Parameters:
        -----------------
        url: адрес страницы
        """
        self.goto_with_allure_step(BASE_URL + LOGIN_PAGE_URL)
        return self

    def login(self, p01_login: str, p02_password: str):
        """
        Метод входа в приложение, содержащий allure.step
        для формирования детальных шагов в тест-кейсах Allure TestOps

        Parameters:
        ------------------------
        - login: значение логина, вводимое в поле ввода
        - password: значение пароля, вводимое в поле ввода
        - LOGIN[0]: название метки соответствующего поля ввода
        - LOGIN[1]: xpath-локатор соответствующего поля ввода
        """
        self.text_field_fill_with_allure_step(LOGIN[0], LOGIN[1], p01_login)
        self.text_field_fill_with_allure_step(PASSWORD[0], PASSWORD[1], p02_password)
        self.button_click_with_allure_step(BUTTON_LOGIN[0], BUTTON_LOGIN[1])
        return self  # данная конструкция позволяет реализовать в тесте цепочку вызовов, когда один метод заканчивается, ставится точка и вызывается следующий

    @allure.step('Войти в приложение')
    def login_fast(self, login: str, password: str):
        """
        Метод входа в приложение, содержащий только один allure.step,
        для использования в проверках функций, отличных от логина

        Parameters:
        ------------------------
        - login: значение логина, вводимое в поле ввода
        - password: значение пароля, вводимое в поле ввода
        """
        self.navigate()
        self.text_field_fill(LOGIN[1], login)
        self.text_field_fill(PASSWORD[1], password)
        self.button_click(BUTTON_LOGIN[1])
        return self  # данная конструкция позволяет реализовать в тесте цепочку вызовов, когда один метод заканчивается, ставится точка и вызывается следующий

    # TODO Сделать: в base_page сделать универсальную функцию expect_to_be_visible, локаторы заменить на xpath
    def check_login(self, result01_fio: str, result02_user_role: str, result03_user_organization: str):
        """
        Метод проверка ожидаемого результата после входа в приложение,
        содержащий только один allure.step. После входа на странице
        должны отображаться ФИО, роль и организация пользователя

        Parameters:
        ------------------------
        - result01_fio: ожидаемое значение ФИО пользователя
        - result02_user_role: ожидаемое значение роли пользователя
        - result03_user_organization: ожидаемое значение организации пользователя
        """
        with allure.step(f'Ожидаемое результат: вход в приложение и отображение на странице реквизитов пользователя "{result01_fio}"'):
            expect(self.page.get_by_text(result01_fio, exact=True)).to_be_visible()  # //*[text() = "Смирнов" and text() = "Алексей" and text() = "Павлович"]   fio.split(' ')[0] - это из ФИО выделяется фамилия
            expect(self.page.get_by_role('button', name=result02_user_role)).to_be_visible()  # //*[contains(@class, "logo")]//*[text() = "Администратор ИБ"]
            expect(self.page.get_by_role('paragraph').filter(has_text=result03_user_organization)).to_be_visible()  # //*[contains(@class, "logo")]//*[text() = 'УП "ИВЦ "Минфина"']
            return self

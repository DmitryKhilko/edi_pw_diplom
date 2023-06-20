import allure
from allure_commons.types import AttachmentType
from playwright.sync_api import expect

from pages.base_page import BasePage
from data.url_data import LOGIN_PAGE_URL
from settings import BASE_URL
from data.data_ui_login import *


class Login(BasePage):

    def navigate(self):
        """
        Метод перехода на указанную страницу приложения,
        содержащий allure.step для формирования детальных шагов
        в тест-кейсах Allure TestOps
        """
        self.goto_with_allure_step(BASE_URL + LOGIN_PAGE_URL)

    def login(self, user: tuple):
        """
        Метод входа в приложение, содержащий только один allure.step,
        для использования в проверках функций, отличных от логина

        :param user: кортеж, содержащий логин, пароль, email_account пользователя
        """
        with allure.step(f'Войти в приложении под ролью "{user[0]}" с валидными логином и паролем'):
            self.navigate()
            self.text_field_fill(FIELD_LOGIN[1], user[1])
            self.text_field_fill(FIELD_PASSWORD[1], user[2])
            self.button_click(BUTTON_LOGIN[1])

    def login_by_role(self, user: tuple, parameter_description: str):
        """
        Метод входа в приложение, содержащий allure.step
        для формирования детальных шагов в тест-кейсах Allure TestOps

        LOGIN[0]: название метки соответствующего поля ввода
        LOGIN[1]: xpath-локатор соответствующего поля ввода

        :param user: кортеж, содержащий логин, пароль, email_account пользователя
        :param parameter_description: описание набора параметров из набора тестовых данных для allure.step
        """
        with allure.step(f'{parameter_description}'):  # войти в приложение под ролью
            self.text_field_fill_with_allure_step(FIELD_LOGIN[0], FIELD_LOGIN[1], user[1])
            self.text_field_fill_with_allure_step(FIELD_PASSWORD[0], FIELD_PASSWORD[1], user[2])
            self.button_click_with_allure_step(BUTTON_LOGIN[0], BUTTON_LOGIN[1])

    # TODO Сделать: в base_page сделать универсальную функцию expect_to_be_visible, локаторы заменить на xpath
    def check_login(self, expected_result: tuple):
        """
        Метод проверки ожидаемого результата после входа в приложение.
        После входа на странице должны отображаться ФИО, роль и организация
        пользователя

        :param expected_result: ожидаемый результат
        """
        with allure.step(f'Ожидаемый результат: вход в приложение и отображение на странице реквизитов '
                         f'пользователя {expected_result[0]}'):
            expect(self.page.get_by_text(expected_result[0], exact=True)).to_be_visible()
            expect(self.page.get_by_role('button', name=expected_result[1])).to_be_visible()
            expect(self.page.get_by_role('paragraph').filter(has_text=expected_result[2])).to_be_visible()
            allure.attach(self.page.screenshot(type='png'), name='screenshot', attachment_type=AttachmentType.PNG)

    def check_message(self, expected_result: tuple):
        """
        Метод проверки отображения ожидаемых сообщений на странице:
        об ошибке или информационных.

        :param expected_result: ожидаемый результат
        """
        with allure.step(f'Ожидаемый результат: отобразилось сообщение "{expected_result[1]}"'):
            expect(self.page.get_by_text(expected_result[1])).to_be_visible()
            allure.attach(self.page.screenshot(type='png'), name='screenshot', attachment_type=AttachmentType.PNG)

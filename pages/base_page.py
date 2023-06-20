import logging

import allure
from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    # @staticmethod
    # def locator_label_by_xpath(label: str):
    #     """
    #     Базовый метод создания xpath-локатора, производящего
    #     поиск веб-элемента (как правило, текстового поля ввода)
    #     по частичному совпадению названия метки текстового поля.
    #     Этот метод работает на странице login
    #       Parameters:
    #      ------------------------
    #      label: искомый в xpath текст
    #     """
    #     return f'//label[contains(text(), "{label}")]'
    #
    # @staticmethod
    # def locator_input_by_xpath(name_value: str):
    #     """
    #     Базовый метод создания xpath-локатора, производящего
    #     поиск веб-элемента (как правило, текстового поля ввода)
    #     по имени текстового поля
    #       Parameters:
    #      ------------------------
    #      name_value: значение атрибута name в xpath
    #     """
    #     return f'//input[@name = \"{name_value}\")]'
    #
    # @staticmethod
    # def locator_button_by_xpath(label: str):
    #     """
    #     Базовый метод создания xpath-локатора, производящего
    #     поиск веб-элемента (кнопки) по названию на кнопке
    #        Parameters:
    #       ------------------------
    #       label: искомый в xpath текст
    #     """
    #     return f'//button[text() = "{label}"]'

    def goto(self, url: str):
        """
        Базовый метод перехода на указанную страницу приложения,
        не содержащий allure.step

        :param url: адрес страницы
        """
        self.page.goto(url)

    def goto_with_allure_step(self, url: str):
        """
        Базовый метод перехода на указанную страницу приложения,
        содержащий allure.step для формирования детальных шагов
        в тест-кейсах Allure TestOps

        :param url: адрес страницы
        """
        with allure.step(f'Перейти на страницу {url}'):
            logging.debug(f'Перейти на страницу {url}')
            self.page.goto(url)

    def text_field_fill(self, locator: str, value: str):
        """
        Базовый метод заполнения текстового поля ввода,
        не содержащий allure.step

        :param locator: xpath-локатор текстового поля ввода
        :param value: значение, вводимое в поле ввода
        """
        logging.debug(f'Очистить текстовое поле с локатором "{locator}"')
        self.page.locator(locator).clear()
        logging.debug(f'Ввести в текстовое поле с значение "{value}"')
        self.page.locator(locator).fill(value)

    def text_field_fill_with_allure_step(self, label: str, locator: str, value: str):
        """
        Базовый метод заполнения текстового поля ввода, содержащий allure.step
        для формирования детальных шагов в тест-кейсах Allure TestOps

        :param label: название метки текстового поля ввода для allure.step
        :param locator: xpath-локатор текстового поля ввода
        :param value: значение, вводимое в поле ввода
        """

        with allure.step(f'Ввести в поле "{label}" значение: {value}'):
            logging.debug(f'Очистить текстовое поле с локатором "{locator}"')
            self.page.locator(locator).clear()
            logging.debug(f'Ввести в текстовое поле с значение "{value}"')
            self.page.locator(locator).fill(value)

    def button_click(self, locator: str):
        """
        Базовый метод нажатия на кнопку,
        не содержащий allure.step

        :param locator: xpath-локатор кнопки
        """
        logging.debug(f'Нажать кнопку с локатором "{locator}"')
        self.page.locator(locator).click()

    def button_click_with_allure_step(self, text: str, locator: str):
        """
        Базовый метод нажатия на кнопку, содержащий allure.step
        для формирования детальных шагов в тест-кейсах Allure TestOps

        :param text: название кнопки
        :param locator: xpath-локатор кнопки
        """
        with allure.step(f'Нажать кнопку "{text}"'):
            logging.debug(f'Нажать кнопку с локатором "{locator}"')
            self.page.locator(locator).click()

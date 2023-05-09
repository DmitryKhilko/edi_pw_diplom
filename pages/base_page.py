import allure
from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    # TODO Продумать, как вынести сделать универсальным данный метод, чтобы любой локатор обрабатывал, чтобы в allure.step выводились названия меток, названий кнопок
    @staticmethod
    def locator_label_by_xpath(label: str):
        return f'//label[contains(text(), "{label}")]'

    @staticmethod
    def locator_button_by_xpath(label: str):
        return f'//button[text() = "{label}"]'

    def goto(self, url: str):
        with allure.step(f'Перейти на страницу: {url}'):
            self.page.goto(url)

    def text_field_fill(self, label: str, value: str):  # Функция внесения в поле ввода значения
        with allure.step(f'Ввести в поле "{label}" значение: {value}'):
            self.page.locator(self.locator_label_by_xpath(label)).clear()
            self.page.locator(self.locator_label_by_xpath(label)).fill(value)

    def button_click(self, label: str):  # Функция нажатия кнопки
        with allure.step(f'Нажать кнопку "{label}"'):
            self.page.locator(self.locator_button_by_xpath(label)).click()

    def expect_to_be_visible(self):
        pass

import allure
from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    # TODO Продумать, как вынести сделать универсальным данный метод, чтобы любой локатор обрабатывал, чтобы в allure.step выводились названия меток, названий кнопок

    """ 
    Базовый метод создания xpath-локатора, производящего
    поиск веб-элемента (как правило, текстового поля ввода) 
    по частичному совпадению интерфейсного названия веб-элемента
    """
    @staticmethod
    def locator_label_by_xpath(label: str):
        return f'//label[contains(text(), "{label}")]'

    """ 
    Базовый метод создания xpath-локатора, производящего
    поиск веб-элемента (кнопки) по интерфейсному названия 
    веб-элемента
    """
    @staticmethod
    def locator_button_by_xpath(label: str):
        return f'//button[text() = "{label}"]'

    """ 
    Базовый метод перехода на указанную страницу приложения,
    не содержащий allure.step
    """
    def goto(self, url: str):
        self.page.goto(url)

    """ 
    Базовый метод перехода на указанную страницу приложения,
    содержащий allure.step для формирования детальных шагов 
    в тест-кейсах Allure TestOps
    """
    def goto_with_allure_step(self, url: str):
        with allure.step(f'Перейти на страницу: {url}'):
            self.page.goto(url)

    """ 
    Базовый метод заполнения текстового поля, 
    не содержащий allure.step 
    """
    def text_field_fill(self, label: str, value: str):
        self.page.locator(self.locator_label_by_xpath(label)).clear()
        self.page.locator(self.locator_label_by_xpath(label)).fill(value)

    """ 
    Базовый метод заполнения текстового поля, содержащий allure.step 
    для формирования детальных шагов в тест-кейсах Allure TestOps
    """
    def text_field_fill_with_allure_step(self, label: str, value: str):
        with allure.step(f'Ввести в поле "{label}" значение: {value}'):
            self.page.locator(self.locator_label_by_xpath(label)).clear()
            self.page.locator(self.locator_label_by_xpath(label)).fill(value)

    """ 
    Базовый метод нажатия на кнопку, 
    не содержащий allure.step 
    """
    def button_click(self, label: str):
        self.page.locator(self.locator_button_by_xpath(label)).click()

    """ 
    Базовый метод нажатия на кнопку, содержащий allure.step 
    для формирования детальных шагов в тест-кейсах Allure TestOps
    """
    def button_click_with_allure_step(self, label: str):
        with allure.step(f'Нажать кнопку "{label}"'):
            self.page.locator(self.locator_button_by_xpath(label)).click()

    def expect_to_be_visible(self):
        pass

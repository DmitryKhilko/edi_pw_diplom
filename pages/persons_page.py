import allure
from playwright.sync_api import expect

from data.constants import BASE_URL, PERSONS_PAGE_URL
from pages.base_page import BasePage


class Persons(BasePage):

    def navigate(self):
        with allure.step(f'Перейти на страницу "Физические лица": {BASE_URL + PERSONS_PAGE_URL}'):
            self.page.get_by_role("link", name="Физические лица").click()

    @allure.step('Ожидаемый результат: перешли на страницу "Физические лица"')
    def check_goto_persons(self):
        expect(self.page.get_by_role("link", name="Физические лица").nth(1)).to_be_visible()

    @allure.step('Нажать кнопку "Добавить"')
    def opening_form_add_person(self):
        self.page.get_by_role("button", name="Добавить").click()

    @allure.step('Ожидаемый результат: форма добавления физического лица открыта')
    def check_opening_form_add_person(self):
        expect(self.page.get_by_role("link", name="Физические лица").nth(1)).to_be_visible()
        expect(self.page.get_by_role("link", name="Добавить")).to_be_visible()

    @allure.step('Добавить физическое лицо"')
    def add_person(self, first_name):
        with allure.step(f'Ввести в поле "Имя" значение: {first_name}'):
            self.page.locator('//input[@name="first_name"]').fill(first_name)
            # self.page.get_by_label('Телефон').fill(first_name)



 # page.locator("input[name=\"first_name\"]").click()
 #    page.locator("input[name=\"first_name\"]").fill("123")
 #    page.locator("input[name=\"first_name\"]").press("Tab")
 #    page.locator("input[name=\"patronymic\"]").fill("123")
 #    page.locator("input[name=\"patronymic\"]").press("Tab")
 #    page.locator("input[name=\"last_name\"]").fill("123")
 #    page.locator("input[name=\"last_name\"]").press("Tab")
 #    page.get_by_placeholder("дд.мм.гггг").fill("11.02.1973")
 #    page.get_by_placeholder("дд.мм.гггг").press("Enter")
 #    page.get_by_placeholder("дд.мм.гггг").press("Tab")
 #    page.get_by_role("button", name="Choose date, selected date is 11 февр. 1973 г.").press("Tab")
 #    page.get_by_role("button", name="Мужской").press("Enter")
 #    page.get_by_role("option", name="Мужской").press("ArrowDown")
 #    page.get_by_role("option", name="Женский").press("Enter")
 #    page.get_by_role("button", name="Женский").press("Tab")
 #    page.locator("input[name=\"phone\"]").fill("123")
 #    page.locator("input[name=\"phone\"]").press("Tab")
 #    page.locator("input[name=\"email\"]").fill("123@123.ru")
 #    page.locator("input[name=\"email\"]").press("Tab")
 #    page.locator("input[name=\"card_id\"]").fill("123")
 #    page.locator("input[name=\"card_id\"]").press("Tab")
 #    page.locator("input[name=\"key_id\"]").fill("123")
 #    page.get_by_role("button", name="Отменить").click()
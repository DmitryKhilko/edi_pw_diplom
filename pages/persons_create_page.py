import logging

import allure
from allure_commons.types import AttachmentType
from playwright.sync_api import expect

from data.data_file_name import FILENAME_UI_PERSON_ID
from data.data_ui_persons import *
from data.url_data import PERSONS_PAGE_URL
from settings import BASE_URL
from pages.base_page import BasePage
from sql_requests.persons_sql import SQLRequests
from utils.files import FilesWork


class Persons(BasePage):

    def navigate(self):
        with allure.step(f'Перейти на страницу {BASE_URL + PERSONS_PAGE_URL}'):
            self.page.get_by_role("link", name="Физические лица").click()

    @allure.step('Ожидаемый результат: перешли на страницу "Физические лица"')
    def check_goto_persons(self):
        expect(self.page.get_by_role("link", name="Физические лица").nth(1)).to_be_visible()
        allure.attach(self.page.screenshot(type='png'), name='screenshot', attachment_type=AttachmentType.PNG)

    @allure.step('Нажать кнопку "Добавить"')
    def opening_form_create_person(self):
        self.page.get_by_role("button", name="Добавить").click()

    @allure.step('Ожидаемый результат: форма добавления физического лица открыта')
    def check_opening_form_create_person(self):
        expect(self.page.get_by_role("link", name="Физические лица").nth(1)).to_be_visible()
        expect(self.page.get_by_role("link", name="Добавить")).to_be_visible()
        allure.attach(self.page.screenshot(type='png'), name='screenshot', attachment_type=AttachmentType.PNG)

    def cancel_create_person(self, parameter_description: str, data: tuple):
        """
        Метод, проверяющий нажатие кнопки "ОТМЕНИТЬ" на форме создания физического лица:
        заполнить форму валидными значениями обязательных для заполнения параметров и
        нажать кнопку "ОТМЕНА". При этом физическое лицо не должно быть создано.

        :param parameter_description: описание набора параметров из набора тестовых данных для allure.step
        :param data: набор значений параметров для создания физического лица
        """
        with allure.step(f'{parameter_description}'):  # создать физическое лицо с валидными значениями параметров
            self.text_field_fill_with_allure_step(FIELD_FIRST_NAME[0], FIELD_FIRST_NAME[1], data[0])
            self.text_field_fill_with_allure_step(FIELD_PATRONYMIC[0], FIELD_PATRONYMIC[1], data[1])
            self.text_field_fill_with_allure_step(FIELD_LAST_NAME[0], FIELD_LAST_NAME[1], data[2])
            self.text_field_fill_with_allure_step(FIELD_EMAIL[0], FIELD_EMAIL[1], data[3])
            self.button_click_with_allure_step(BUTTON_CANCEL[0], BUTTON_CANCEL[1])

    def check_not_created_in_table_person(self, data: tuple):
        with allure.step(f'Ожидаемое результат: отменено создание физического лица'):
            expect(self.page.locator(f'//*[@data-rowindex = 0]//*[contains(text(), '
                                     f'"{data[3].lower()}")]')).not_to_be_visible()
            allure.attach(self.page.screenshot(type='png'), name='screenshot', attachment_type=AttachmentType.PNG)

    def create_person(self, parameter_description: str, data: tuple):
        """
        Метод создания с помощью графического интерфейса физического лица для
        ролей приложения, которым разрешено создание физического лица
        с валидными значениями параметров.

        :param parameter_description: описание набора параметров из набора тестовых данных для allure.step
        :param data: набор значений параметров для создания физического лица
        """
        with allure.step(f'{parameter_description}'):  # создать физическое лицо с валидными значениями параметров
            self.text_field_fill_with_allure_step(FIELD_FIRST_NAME[0], FIELD_FIRST_NAME[1], data[0])
            self.text_field_fill_with_allure_step(FIELD_PATRONYMIC[0], FIELD_PATRONYMIC[1], data[1])
            self.text_field_fill_with_allure_step(FIELD_LAST_NAME[0], FIELD_LAST_NAME[1], data[2])
            # по умолчанию выбрано значение "Мужской", поэтому если нужен пол "Мужской", то ничего не делаем
            if data[3] == 'Женский':
                # TODO Сделать отдельный метод в base_page или в persons_page, так же добавить allure.step
                with allure.step(f'Выбрать в раскрывающемся списке "{DROP_DOWN_LIST_SEX[0]}" значение: {data[3]}'):
                    self.page.locator(DROP_DOWN_LIST_SEX[1]).click()
                    self.page.locator(DROP_DOWN_LIST_SEX[2]).click()
            self.text_field_fill_with_allure_step(FIELD_BIRTHDAY[0], FIELD_BIRTHDAY[1], data[4])
            self.text_field_fill_with_allure_step(FIELD_PHONE[0], FIELD_PHONE[1], data[5])
            self.text_field_fill_with_allure_step(FIELD_EMAIL[0], FIELD_EMAIL[1], data[6])
            self.text_field_fill_with_allure_step(FIELD_CARD_ID[0], FIELD_CARD_ID[1], data[7])
            self.text_field_fill_with_allure_step(FIELD_KEY_ID[0], FIELD_KEY_ID[1], data[8])
            self.button_click_with_allure_step(BUTTON_SAVE[0], BUTTON_SAVE[1])

    # TODO Сделать базовый метод без allure.step, так как allure.step будет оригинальный для каждой таблицы
    def check_visible_in_table_created_person(self, data: tuple):
        with allure.step(f'Ожидаемое результат: в первой строке таблицы отображается email "{data[6].lower()}" '
                         f'вновь добавленного физического лица'):
            expect(self.page.locator(f'//*[@data-rowindex = 0]//*[contains(text(), '
                                     f'"{data[6].lower()}")]')).to_be_visible()
            allure.attach(self.page.screenshot(type='png'), name='screenshot', attachment_type=AttachmentType.PNG)

    @staticmethod
    def check_create_person_in_db(email: str):
        with allure.step('Ожидаемый результат: физическое лицо добавлено в БД'):
            logging.debug(f'Приступить к поиску добавленного физ. лица в БД')
            db_rowcount, db_person_id, db_fio, db_email = SQLRequests.db_select_row_ui(email)
            print(f'Фактическое ФИО из БД: "{db_fio}"')
            print(f'Фактический email из БД: "{db_email}"')
            assert db_rowcount == 1, 'Физическое лицо в базу данных не добавлено'
            # Привожу к нижнему регистру, так как при записи в БД система только первые буквы делает большими
            assert db_email == email.lower(), 'Фактический из БД и ожидаемый email физического лица не совпали'
            logging.debug(f'Физическое лицо c id="{db_person_id}" успешно добавлено в БД')
            # Если создалась запись физического лица в базе данных, записываем personal_id в файл
            # для последующего удаления физического лица из БД
            if db_rowcount == 1:
                logging.debug(f'В базе данных создано физическое лицо с id="{db_person_id}"')
                logging.debug(f'Приступить к записи id физ.лица в файл')
                FilesWork.write_file(FILENAME_UI_PERSON_ID, db_person_id)
                logging.debug(f'id физ.лица успешно записан в файл')

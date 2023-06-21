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
    def check_visible_menu_item_persons(self, message: str):
        """
        Метод проверки доступности для ролей, которым разрешена работа
        с физическими лицами, пункта вертикального меню "Физические лица"
        """
        with allure.step(f'Ожидаемый результат: {message}'):
            expect(self.page.locator(MENU_ITEM_PERSONS[1])).to_be_visible()
            allure.attach(self.page.screenshot(type='png'), name='screenshot', attachment_type=AttachmentType.PNG)

    def check_not_visible_menu_item_persons(self, message: str):
        """
        Метод проверки недоступности для ролей, которым не разрешена работа
        с физическими лицами, пункта вертикального меню "Физические лица"
        """
        with allure.step(f'Ожидаемый результат: {message}'):
            expect(self.page.locator(MENU_ITEM_PERSONS[1])).not_to_be_visible()
            allure.attach(self.page.screenshot(type='png'), name='screenshot', attachment_type=AttachmentType.PNG)

    def goto_persons_page(self):
        """
        Метод перехода на страницу физических лиц
        """
        with allure.step(f'Перейти на страницу {BASE_URL + PERSONS_PAGE_URL}'):
            self.page.get_by_role("link", name="Физические лица").click()

    def check_goto_persons_page(self):
        """
        Метод проверки успешности перехода
        на страницу физических лиц
        """
        with allure.step(f'Ожидаемый результат: перешли на страницу "Физические лица"'):
            expect(self.page.get_by_role("link", name="Физические лица").nth(1)).to_be_visible()
            allure.attach(self.page.screenshot(type='png'), name='screenshot', attachment_type=AttachmentType.PNG)

    def opening_form_create_person(self):
        """
        Метод открытия формы добавления физического лица
        при нажатии кнопки "Добавить"
        """
        with allure.step(f'Нажать кнопку "Добавить"'):
            self.page.get_by_role("button", name="Добавить").click()

    def check_opening_form_create_person(self):
        """
        Метод проверки открытия формы добавления физического лица
        при нажатии кнопки "Добавить"
        """
        with allure.step(f'Ожидаемый результат: форма добавления физического лица открыта'):
            expect(self.page.get_by_role("link", name="Физические лица").nth(1)).to_be_visible()
            expect(self.page.get_by_role("link", name="Добавить")).to_be_visible()
            allure.attach(self.page.screenshot(type='png'), name='screenshot', attachment_type=AttachmentType.PNG)

    def cancel_create_person(self, parameter_description: str, data: tuple):
        """
        Метод, проверяющий нажатие кнопки "Отменить" на форме создания физического лица.
        Для проверки: заполнить форму валидными значениями обязательных для заполнения параметров;
        нажать кнопку "Отменить". При этом физическое лицо не должно быть создано.

        :param parameter_description: описание набора параметров из набора тестовых данных для allure.step
        :param data: набор значений параметров для создания физического лица
        """
        with allure.step(f'{parameter_description}'):  # создать физическое лицо с валидными значениями параметров
            self.text_field_fill_with_allure_step(FIELD_FIRST_NAME[0], FIELD_FIRST_NAME[1], data[0])
            self.text_field_fill_with_allure_step(FIELD_PATRONYMIC[0], FIELD_PATRONYMIC[1], data[1])
            self.text_field_fill_with_allure_step(FIELD_LAST_NAME[0], FIELD_LAST_NAME[1], data[2])
            self.text_field_fill_with_allure_step(FIELD_EMAIL[0], FIELD_EMAIL[1], data[3])
            self.button_click_with_allure_step(BUTTON_CANCEL[0], BUTTON_CANCEL[1])

    def check_not_created_person_in_ui(self, email: str):
        """
        Проверка на уровне web-интерфейса того, что после нажатия кнопки "Отменить"
        физическое лицо не создано

        :param email: email для поиска в первой строке таблицы физических лиц
        """
        with allure.step(f'Ожидаемое результат: отменено создание физического лица'):
            expect(self.page.locator(f'//*[@data-rowindex = 0]//*[contains(text(), '
                                     f'"{email.lower()}")]')).not_to_be_visible()
            allure.attach(self.page.screenshot(type='png'), name='screenshot', attachment_type=AttachmentType.PNG)

    @staticmethod
    def check_not_create_person_in_db(email: str):
        """
        Проверка на уровне базы данных того, что после нажатия кнопки "Отменить"
        физическое лицо не создано

        :param email: email для поиска в базе данных
        """
        with allure.step('Ожидаемый результат: физическое лицо не добавлено в базу данных'):
            logging.debug(f'Приступить к поиску физ. лица в БД')
            db_rowcount, db_person_id, db_fio, db_email = SQLRequests.db_select_row_ui(email)
            assert db_rowcount != 1, 'Физическое лицо добавлено в базу данных'
            logging.debug(f'Физическое лицо не добавлено в базу данных')

    def create_person(self, parameter_description: str, data: tuple):
        """
        Метод создания физического лица с помощью web-интерфейса для
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
    def check_created_person_in_ui(self, email: str, expected_result: tuple):
        """
        Проверка создания физического лица на уровне web-интерфейса

        :param email: email для поиска в первой строке таблицы физических лиц
        :param expected_result: сообщения, выдаваемые системой после успешного добавления физического лица
        """
        with allure.step(f'Ожидаемый результат: в первой строке таблицы отображается email "{email.lower()}" '
                         f'вновь добавленного физического лица'):
            expect(self.page.locator(f'//*[@data-rowindex = 0]//*[contains(text(), '
                                     f'"{email.lower()}")]')).to_be_visible()
        with allure.step(f'Ожидаемый результат: сообщение "{expected_result[1]}" в правом нижнем углу'):
            expect(self.page.get_by_text(expected_result[1])).to_be_visible()
            allure.attach(self.page.screenshot(type='png'), name='screenshot', attachment_type=AttachmentType.PNG)

    @staticmethod
    def check_create_person_in_db(email: str):
        """
        Проверка создания физического лица на уровне базы данных

        :param email: email для поиска в первой строке таблицы физических лиц
        """
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

    def can_not_create_person_empty_param_required(self, expected_result: tuple):
        """
        Проверка отказа в создании физического лица на уровне web-интерфейса
        при незаполненных обязательных для заполнения параметрах

        :param expected_result: сообщения, выдаваемые системой
        """
        with allure.step(f'Ожидаемый результат: сообщение "{expected_result[1]}" '
                         f'под полем ввода "{expected_result[0]}"'):
            expect(self.page.get_by_text(expected_result[1])).to_be_visible()
        with allure.step(f'Ожидаемый результат: сообщение "{expected_result[3]}" в правом нижнем углу'):
            expect(self.page.get_by_text(expected_result[3])).to_be_visible()
        allure.attach(self.page.screenshot(type='png'), name='screenshot', attachment_type=AttachmentType.PNG)

    def check_can_not_create_person_invalid_param(self, expected_result: tuple):
        """
        Проверка отказа в создании физического лица на уровне web-интерфейса
        при невалидных значениях параметров

        :param expected_result: сообщения, выдаваемые системой
        """
        # with allure.step(f'Ожидаемый результат: сообщение "{expected_result[1]}" '
        #                  f'под полем ввода "{expected_result[0]}"'):
        #     expect(self.page.get_by_text(expected_result[1])).to_be_visible()
        with allure.step(f'Ожидаемый результат: сообщение "{expected_result[2]}" в правом нижнем углу'):
            expect(self.page.get_by_text(expected_result[2])).to_be_visible()
        allure.attach(self.page.screenshot(type='png'), name='screenshot', attachment_type=AttachmentType.PNG)

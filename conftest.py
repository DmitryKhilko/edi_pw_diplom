import logging

import allure
from playwright.sync_api import sync_playwright
from pytest import fixture

from data.data_file_name import FILENAME_API_PERSON_ID, FILENAME_UI_PERSON_ID
from sql_requests.persons_sql import SQLRequests


"""
Настройка вывода логов
"""
logging.basicConfig(
    level=logging.DEBUG,
    filename="utils/mylog.log",
    filemode="w",
    encoding="utf8",
    format="%(asctime)s - %(levelname)s [%(module)s.%(funcName)s: %(lineno)d] - %(message)s",
    datefmt='%d.%m.%Y %H:%M:%S',
)


@fixture(scope='function', autouse=False)
def sql_delete_person():
    """
    Фикстура для удаления физического лица по окончании теста,
    связанного с физическими лицами
    """
    yield
    with allure.step('Удалить физическое лицо из базы данных, в случае его создания'):
        SQLRequests.db_delete_row(FILENAME_API_PERSON_ID)


@fixture(scope='function', autouse=False)
def sql_delete_person_ui():
    """
    Фикстура для удаления физического лица, созданного через web-интерфейс,
    по окончании теста, связанного с физическими лицами
    """
    yield
    with allure.step('Удалить физическое лицо из базы данных, в случае его создания'):
        SQLRequests.db_delete_row(FILENAME_UI_PERSON_ID)


@fixture()
def page():
    """
    Фикстура для запуска и закрытия ui-автотестов
    """
    with sync_playwright() as playwright:
        with allure.step(f'Открыть браузер'):
            browser = playwright.chromium.launch(headless=True)
            context = browser.new_context(viewport={'width': 1920, 'height': 1080})
            # context = browser.new_context()
            page = context.new_page()

            yield page

        with allure.step(f'Закрыть браузер'):
            page.close()
            context.close()
            browser.close()

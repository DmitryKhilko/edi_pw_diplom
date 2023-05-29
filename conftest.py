import allure
from playwright.sync_api import sync_playwright
from pytest import fixture

from data.file_name_data import FILENAME_API_PERSON_ID
from services.login_service import LoginService
from services.persons_service import PersonsService
from sql_requests.sql import SQLRequests

# # Инициализация экземпляров классов, описанных в пакетах pages и services,
# # с которыми мы будем работать в тестах
login_service = LoginService()
persons_service = PersonsService()


@fixture(scope='function', autouse=False)
def sql_delete_person():
    yield
    with allure.step('Удалить физическое лицо из базы данных, в случае его создания'):
        SQLRequests.db_delete_row(FILENAME_API_PERSON_ID)


@fixture()
def web_app():
    with sync_playwright() as playwright:
        with allure.step(f'Открыть браузер'):
            browser = playwright.chromium.launch(headless=False)
            context = browser.new_context(viewport={'width': 1920, 'height': 1080})
            # context = browser.new_context()
            page = context.new_page()

            yield page

        with allure.step(f'Закрыть браузер'):
            page.close()
            context.close()
            browser.close()

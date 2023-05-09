import allure
import psycopg2
from pytest import fixture
from playwright.sync_api import sync_playwright


@fixture()
def web_app():
    with sync_playwright() as playwright:
        with allure.step(f'Открыть браузер'):
            browser = playwright.chromium.launch(headless=False)
            # context = browser.new_context(viewport={'width': 1920, 'height': 1080})
            context = browser.new_context()
            page = context.new_page()

            yield page

        with allure.step(f'Закрыть браузер'):
            page.close()
            context.close()
            browser.close()


@fixture
def connection_db():
    connection = psycopg2.connect(
        database="eform_lok281",
        user="eform_user_lok281",
        password="pAs_SworD_lok281",
        host="172.20.1.109",
        port="15432"
    )
    return connection

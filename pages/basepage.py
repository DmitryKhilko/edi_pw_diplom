from playwright.sync_api import Page

BASE_URL = 'https://enode02.ivcmf.by'


class BasePage:
    def __init__(self, page: Page):
        self.page = page

from playwright.sync_api import Page
from config import BASE_URL

# Class dasar untuk semua Page Object
class BasePage:
    def __init__(self, page: Page):
        self.page = page

    # Navigasi ke URL relatif
    def open(self, path: str):
        self.page.goto(f"{BASE_URL}{path}")
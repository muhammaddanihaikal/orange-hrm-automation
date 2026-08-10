from playwright.sync_api import Page
from config import BASE_URL


class LoginPage:
    def __init__(self, page: Page):

        self.page = page

        self.PATH = "/web/index.php/auth/login"

        self.username = page.get_by_role("textbox", name="Username")
        self.password = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")

        self.heading = page.get_by_role("heading", name="Login")
        self.error_message = page.get_by_role("alert")

    def open(self):
        self.page.goto(f"{BASE_URL}{self.PATH}")

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()
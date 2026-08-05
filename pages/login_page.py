from playwright.sync_api import Page
from config import BASE_URL


class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.base_url = BASE_URL

        self.username = page.get_by_role("textbox", name="Username")
        self.password = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error_message = page.get_by_role("alert")

    def open(self):
        self.page.goto(
            f"{self.base_url}/web/index.php/auth/login",
            wait_until="domcontentloaded",
        )

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()
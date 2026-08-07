from playwright.sync_api import Page
from pages.base_page import BasePage


# Page Object untuk halaman Login
class LoginPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        # Lokator elemen-elemen login
        self.PATH = "/web/index.php/auth/login"
        self.username = page.get_by_role("textbox", name="Username")
        self.password = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")

        self.heading = page.get_by_role("heading", name="Login")
        self.error_message = page.get_by_role("alert")

    # Membuka halaman login
    def open(self):
        super().open(self.PATH)

    # Mengisi form dan klik button login
    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()
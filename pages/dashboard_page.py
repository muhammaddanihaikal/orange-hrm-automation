from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class DashboardPage(BasePage) :

    def __init__(self, page: Page):
        super().__init__(page)

        self.PATH = "/web/index.php/dashboard/index"
        self.heading = page.get_by_role("heading", name="Dashboard")

    # membuka halaman dashboard
    def open(self):
        super().open(self.PATH)
from playwright.sync_api import Page

class DashboardPage():

    def __init__(self, page: Page):

        self.PATH = "/web/index.php/dashboard/index"
        self.heading = page.get_by_role("heading", name="Dashboard")
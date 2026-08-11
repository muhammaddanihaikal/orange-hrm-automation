from playwright.sync_api import Page

class AdminPage:
    def __init__(self, page: Page):
        self.page = page

        self.PATH = "/web/index.php/admin/viewSystemUsers"
        self.add_btn = page.get_by_role("button", name="Add")
        
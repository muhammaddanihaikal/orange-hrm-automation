from playwright.sync_api import Page

class AdminPage:
    def __init__(self, page: Page):
        self.page = page

        self.PATH = "/web/index.php/admin/viewSystemUsers"

        # filter
        self.field_container = page.locator(".oxd-grid-item")
        self.username =(
             self.field_container
             .filter(has_text="Username")
             .get_by_role("textbox")
        )
        self.search_btn = page.get_by_role("button", name="Search")

        # table
        self.user_table = page.get_by_role("table")


        self.add_btn = page.get_by_role("button", name="Add")


    def search(self, username):
        self.username.fill(username)
        self.search_btn.click()

    # cari data di tabel
    def user_row(self, username):
        return self.user_table.get_by_role("row").filter(has_text=username)

        
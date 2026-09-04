from playwright.sync_api import Page


class AdminPage:
    def __init__(self, page: Page):
        self.page = page
        self.PATH = "/web/index.php/admin/viewSystemUsers"
        self.field_container = page.locator(".oxd-grid-item")
        self.username = self.field_container.filter(has_text="Username").get_by_role(
            "textbox"
        )
        self.search_btn = page.get_by_role("button", name="Search")
        self.user_table = page.get_by_role("table")
        self.add_btn = page.get_by_role("button", name="Add")
        self.confirm_delete_btn = page.get_by_role("button", name="Yes, Delete")

    def search(self, username):
        self.username.fill(username)
        self.search_btn.click()

    # Cari baris user di tabel untuk keperluan assertion
    def user_row(self, username):
        return self.user_table.get_by_role("row").filter(has_text=username)

    # Action langsung Edit
    def click_edit(self, username):
        self.user_row(username).get_by_role("button").filter(
            has=self.page.locator("i.bi-pencil-fill")
        ).click()

    # Action langsung Delete tuntas dengan popup
    def delete_user(self, username):
        self.user_row(username).get_by_role("button").filter(
            has=self.page.locator("i.bi-trash")
        ).click()
        self.confirm_delete_btn.click()

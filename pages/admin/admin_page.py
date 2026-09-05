from playwright.sync_api import Page


class AdminPage:
    def __init__(self, page: Page):
        self.page = page
        self.PATH = "/web/index.php/admin/viewSystemUsers"

        # === FILTER SECTION===
        self.field_container = page.locator(".oxd-grid-item")
        # --- USERNAME ---
        self.username_filter = self.field_container.filter(
            has_text="Username"
        ).get_by_role("textbox")

        # --- USER ROLE (Drop Down) ---
        self.user_role_filter = self.field_container.filter(
            has_text="User Role"
        ).locator(".oxd-select-text")

        # --- EMPLOYEE NAME (Autocomplete) ---
        self.employee_name_filter = self.field_container.filter(
            has_text="Employee Name"
        ).get_by_role("textbox")
        self.employee_name_option = (
            self.field_container.filter(has_text="Employee Name")
            .get_by_role("listbox")
            .locator("div")
        )

        # --- STATUS (Drop Down) ---
        self.status_filter = self.field_container.filter(has_text="Status").locator(
            ".oxd-select-text"
        )
        self.search_btn = page.get_by_role("button", name="Search")
        self.reset_btn = page.get_by_role("button", name="Reset")

        # === TABEL USER ===
        self.add_btn = page.get_by_role("button", name="Add")
        self.user_table = page.get_by_role("table")
        self.confirm_delete_btn = page.get_by_role("button", name="Yes, Delete")

    def filter_by_username(self, username: str):
        self.username_filter.fill(username)
        self.search_btn.click()

    def filter_by_user_role(self, user_role: str):
        self.user_role_filter.click()
        self.page.get_by_role("option", name=user_role).click()
        self.search_btn.click()

    def filter_by_employee_name(self, employee_name: str):
        self.employee_name_filter.fill(employee_name)

        # nunggu searching.. menghilang
        self.page.get_by_text("Searching....", exact=True).wait_for(state="hidden")

        # nunggu employee name option muncul dan klik
        self.employee_name_option.first.wait_for(state="visible")
        self.employee_name_option.first.click()
        self.search_btn.click()

    def filter_by_status(self, status: str):
        self.status_filter.click()
        self.page.get_by_role("option", name=status).click()
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

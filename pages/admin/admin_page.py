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
        self.user_table = page.get_by_role("table")
        self.delete_selected_btn = page.get_by_role("button", name="Delete Selected")
        self.add_btn = page.get_by_role("button", name="Add")
        self.table_rows = self.user_table.locator(".oxd-table-card")
        self.confirm_delete_btn = page.get_by_role("button", name="Yes, Delete")

    # ==== FUNCTION FILTER SECTION ====
    def filter_by_username(self, username: str):
        """Mengisi input filter Username."""
        self.username_filter.fill(username)

    def filter_by_user_role(self, user_role: str):
        """Memilih opsi pada filter User Role."""
        self.user_role_filter.click()
        self.page.get_by_role("option", name=user_role).click()

    def filter_by_employee_name(self, employee_name: str):
        """Mengisi dan memilih opsi autocomplete pada filter Employee Name."""
        self.employee_name_filter.fill(employee_name)

        # nunggu searching.. menghilang
        self.page.get_by_text("Searching....", exact=True).wait_for(state="hidden")

        # nunggu employee name option muncul dan klik
        self.employee_name_option.first.wait_for(state="visible")
        self.employee_name_option.first.click()

    def filter_by_status(self, status: str):
        """Memilih opsi pada filter Status."""
        self.status_filter.click()
        self.page.get_by_role("option", name=status).click()

    def search(self):
        """Menekan tombol Search dan menunggu respon API pencarian selesai."""
        # tunggu response selesai baru lanjut
        with self.page.expect_response("**/api/v2/admin/users*"):
            self.search_btn.click()

    def reset(self):
        """Menekan tombol Reset dan menunggu reload data dari API selesai."""
        # tunggu response selesai baru lanjut
        with self.page.expect_response("**/api/v2/admin/users*"):
            self.reset_btn.click()

    # ===== FUNCTION TABLE SECTION ====
    def user_row(self, username: str):
        """Mencari baris user spesifik di tabel (bisa dipakai aksi maupun assert)"""
        return self.user_table.get_by_role("row").filter(has_text=username)

    def edit(self, username: str):
        """Mengeklik tombol edit pada baris user yang dipilih."""
        self.user_row(username).get_by_role("button").filter(
            has=self.page.locator("i.bi-pencil-fill")
        ).click()

    def delete(self, username: str):
        """Mengeklik tombol hapus dan mengonfirmasi penghapusan user."""
        self.user_row(username).get_by_role("button").filter(
            has=self.page.locator("i.bi-trash")
        ).click()
        self.confirm_delete_btn.click()

    def bulk_delete(self, usernames: list[str]):
        """Mencentang daftar user yang diberikan dan menghapusnya secara massal."""
        for username in usernames:
            self.user_row(username).locator("label").click()
        self.delete_selected_btn.click()
        self.confirm_delete_btn.click()

from playwright.sync_api import Page


class PimPage:
    def __init__(self, page: Page):
        self.page = page
        self.PATH = "/web/index.php/pim/viewEmployeeList"

        # Isi locator filter & tabel di sini
        self.add_btn = page.get_by_role("button", name="Add")

        self.employee_id_filter = (
            page.locator(".oxd-input-group")
            .filter(has_text="Employee Id")
            .get_by_role("textbox")
        )

        self.employee_table = page.get_by_role("table")

        self.search_btn = page.get_by_role("button", name="Search")
        self.reset_btn = page.get_by_role("button", name="Reset")

    # ==== FUNCTION FILTER SECTION ====
    def filter_by_employee_name(self, employee_name: str):
        """Mengisi dan memilih opsi autocomplete pada filter Employee Name."""
        pass

    def filter_by_employee_id(self, employee_id: str):
        """Mengisi input filter Employee Id."""
        self.employee_id_filter.fill(employee_id)

    def search(self):
        """Menekan tombol Search dan menunggu respon API pencarian selesai."""
        with self.page.expect_response("**/api/v2/pim/employees*"):
            self.search_btn.click()

    def reset(self):
        """Menekan tombol Reset dan menunggu reload data dari API selesai."""
        pass

    # ==== FUNCTION TABLE SECTION ====
    def employee_row(self, identifier: str):
        """Mencari baris employee spesifik di tabel berdasarkan nama atau ID."""
        return self.employee_table.get_by_role("row").filter(has_text=identifier)

    def edit(self, identifier: str):
        """Mengeklik tombol edit (icon pensil) pada baris employee yang dipilih."""
        with self.page.expect_response("**/api/v2/pim/employees/*/personal-details"):
            self.employee_row(identifier).get_by_role("button").filter(
                has=self.page.locator("i.bi-pencil-fill")
            ).click()

    def delete(self, identifier: str):
        """Mengeklik tombol hapus (icon tong sampah) dan konfirmasi hapus employee."""
        pass

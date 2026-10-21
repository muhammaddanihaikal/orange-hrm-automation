from playwright.sync_api import Page


class PimPage:
    def __init__(self, page: Page):
        self.page = page
        self.PATH = "/web/index.php/pim/viewEmployeeList"

        # TODO: Isi locator filter & tabel di sini
        self.add_btn = page.get_by_role("button", name="Add")

    # ==== FUNCTION FILTER SECTION ====
    def filter_by_employee_name(self, employee_name: str):
        """TODO: Mengisi dan memilih opsi autocomplete pada filter Employee Name."""
        pass

    def filter_by_employee_id(self, employee_id: str):
        """TODO: Mengisi input filter Employee Id."""
        pass

    def search(self):
        """TODO: Menekan tombol Search dan menunggu respon API pencarian selesai."""
        pass

    def reset(self):
        """TODO: Menekan tombol Reset dan menunggu reload data dari API selesai."""
        pass

    # ==== FUNCTION TABLE SECTION ====
    def employee_row(self, identifier: str):
        """TODO: Mencari baris employee spesifik di tabel berdasarkan nama atau ID."""
        pass

    def edit(self, identifier: str):
        """TODO: Mengeklik tombol edit (icon pensil) pada baris employee yang dipilih."""
        pass

    def delete(self, identifier: str):
        """TODO: Mengeklik tombol hapus (icon tong sampah) dan konfirmasi hapus employee."""
        pass

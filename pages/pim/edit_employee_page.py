from playwright.sync_api import Page


class EditEmployeePage:
    def __init__(self, page: Page):
        self.page = page

        # TODO: Isi locator form Personal Details di sini
        pass

    def edit_employee(self, data: dict):
        """TODO: Mengubah data Employee pada form Personal Details dan klik Save."""
        pass

    def clear_mandatory_fields(self):
        """TODO: Mengosongkan field mandatory (First Name & Last Name) lalu klik Save."""
        pass

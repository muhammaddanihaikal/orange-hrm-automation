from playwright.sync_api import Page


class AddEmployeePage:
    def __init__(self, page: Page):
        self.page = page
        self.PATH = "/web/index.php/pim/addEmployee"

        # TODO: Isi locator form Add Employee di sini
        # locator input nama
        self.first_name = page.get_by_role("textbox", name="First Name")
        self.middle_name = page.get_by_role("textbox", name="Middle Name")
        self.last_name = page.get_by_role("textbox", name="Last Name")

        # locator employee id
        self.employee_id = (
            page.locator(".oxd-input-group")
            .filter(has_text="Employee Id")
            .get_by_role("textbox")
        )

        # locator login details
        self.create_login_details_togle = (
            page.locator(".oxd-form-row")
            .filter(has_text="Create Login Details")
            .locator(".oxd-switch-input")
        )

        self.username = (
            page.locator(".oxd-input-group")
            .filter(has_text="Username")
            .get_by_role("textbox")
        )
        self.status_enable = page.locator(".oxd-radio-wrapper").filter(
            has_text="Enabled"
        )
        self.status_disable = page.locator(".oxd-radio-wrapper").filter(
            has_text="Disabled"
        )
        self.password = (
            page.locator(".oxd-input-group")
            .filter(has=page.get_by_text("Password", exact=True))
            .get_by_role("textbox")
        )
        self.confirm_password = (
            page.locator(".oxd-input-group")
            .filter(has_text="Confirm Password")
            .get_by_role("textbox")
        )

        # locator tombol save
        self.save_btn = page.get_by_role("button", name="Save")

    def add_employee(self, data: dict):
        """TODO: Mengisi form Add Employee dan klik tombol Save."""
        self.first_name.fill(data["first_name"])
        self.middle_name.fill(data["middle_name"])
        self.last_name.fill(data["last_name"])
        self.employee_id.fill(data["employee_id"])

        # KLIK TOGGLE dulu biar field username & password kebuka!
        self.create_login_details_togle.click()

        self.username.fill(data["username"])
        self.password.fill(data["password"])
        self.confirm_password.fill(data["confirm_password"])
        self.save_btn.click()

    def add_employee_empty(self):
        """TODO: Mengosongkan field mandatory lalu klik tombol Save."""
        pass

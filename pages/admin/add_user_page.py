from playwright.sync_api import Page

class AddUserPage():
    def __init__(self, page:Page):
        self.page = page

        self.PATH = "/web/index.php/admin/saveSystemUser"
        self.field_container = page.locator(".oxd-input-group")
        
        self.user_role = (
            self.field_container
            .filter(has_text="User Role")
            .locator(".oxd-select-text")
        )
        self.employee_name = (
            self.field_container
            .filter(has_text="Employee Name")
            .get_by_role("textbox")
        )
        self.status = (
            self.field_container
            .filter(has_text="Status")
            .locator(".oxd-select-text")
        )
        self.username = (
            self.field_container
            .filter(has_text="Username")
            .get_by_role("textbox")
        )
        self.password = (
            self.field_container
            .filter(
                has=page.get_by_text("Password", exact=True)
            )
            .get_by_role("textbox")
        )
        self.confirm_password = (
            self.field_container
            .filter(has_text="Confirm Password")
            .get_by_role("textbox")
        )
        self.save_btn = page.get_by_role("button", name="Save")
        
    def add_user(self):
        # isi user role
        self.user_role.click()
        self.page.get_by_role("option", name="Admin").click()

        # isi employee name
        self.employee_name.fill("a")
        self.page.get_by_role("option").first.click()

        # isi status
        self.status.click()
        self.page.get_by_role("option", name="Enabled").click()

        # isi username
        self.username.fill("dani")

        # isi password
        self.password.fill("dani123")

        # isi confirm password
        self.confirm_password.fill("dani123")

        # klik button save
        self.save_btn.click()
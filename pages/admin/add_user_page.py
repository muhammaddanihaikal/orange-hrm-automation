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
        self.employee_options = (
            self.field_container
            .filter(has_text="Employee Name")
            .get_by_role("listbox")
            .locator("div")
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
        
    def add_user(self, data):
        # isi user role
        self.user_role.click()
        self.page.get_by_role(
            "option",
            name=data["user_role"]
        ).click()

        # isi employee name
        self.employee_name.fill(data["employee_keyword"])
        self.page.get_by_text("Searching....", exact=True).wait_for(state="hidden")
        self.employee_options.first.wait_for(state="visible")
        self.employee_options.first.click()

        # isi status
        self.status.click()
        self.page.get_by_role(
            "option",
            name=data["status"]
        ).click()

        # isi username
        self.username.fill(data["username"])

        # isi password & conf password
        self.password.fill(data["password"])
        self.confirm_password.fill(data["password"])

        # klik button save
        self.save_btn.click()
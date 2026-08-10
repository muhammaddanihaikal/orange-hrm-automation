from playwright.sync_api import Page
from pages.sidebar import Sidebar


class AdminPage:
    def __init__(self, page: Page):

        self.PATH = "web/index.php/admin/viewSystemUsers"

        # add
        self.add_btn = page.get_by_role("button", name="Add")
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
        self.user_role.click()
        self.employee_name.click()
        self.status.click()
        self.username.click()
        self.password.click()
        self.confirm_password.click()
        self.save_btn.click()
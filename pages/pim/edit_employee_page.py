from playwright.sync_api import Page


class EditEmployeePage:
    def __init__(self, page: Page):
        self.page = page

        self.first_name = page.get_by_role("textbox", name="First Name")
        self.middle_name = page.get_by_role("textbox", name="Middle Name")
        self.last_name = page.get_by_role("textbox", name="Last Name")

        self.other_id = (
            page.locator(".oxd-input-group")
            .filter(has_text="Other Id")
            .get_by_role("textbox")
        )
        self.driver_license_number = (
            page.locator(".oxd-input-group")
            .filter(has_text="Driver's License Number")
            .get_by_role("textbox")
        )
        self.license_expiry_date = (
            page.locator(".oxd-input-group")
            .filter(has_text="License Expiry Date")
            .get_by_role("textbox")
        )

        self.nationality = (
            page.locator(".oxd-input-group")
            .filter(has_text="Nationality")
            .locator(".oxd-select-text")
        )
        self.material_status = (
            page.locator(".oxd-input-group")
            .filter(has_text="Marital Status")
            .locator(".oxd-select-text")
        )
        self.date_of_birth = (
            page.locator(".oxd-input-group")
            .filter(has_text="Date of Birth")
            .get_by_role("textbox")
        )
        self.gender_male = page.get_by_text("Male", exact=True)
        self.gender_female = page.get_by_text("Female", exact=True)

        self.save_btn = page.get_by_role("button", name="Save").first

    def edit_employee(self, data: dict):
        """TODO: Mengubah data Employee pada form Personal Details dan klik Save."""
        self.first_name.fill(data["first_name"])
        self.middle_name.fill(data["middle_name"])
        self.last_name.fill(data["last_name"])

        self.other_id.fill(data["other_id"])
        self.driver_license_number.fill(data["driver_license_number"])
        self.license_expiry_date.fill(data["license_expiry_date"])

        self.nationality.click()
        self.page.get_by_text(data["nationality"], exact=True).click()

        self.material_status.click()
        self.page.get_by_text(data["material_status"], exact=True).click()

        self.date_of_birth.fill(data["date_of_birth"])

        if data["gender"] == "Male":
            self.gender_male.click()
        elif data["gender"] == "Female":
            self.gender_female.click()

        self.save_btn.click()

    def clear_mandatory_fields(self):
        """TODO: Mengosongkan field mandatory (First Name & Last Name) lalu klik Save."""
        pass

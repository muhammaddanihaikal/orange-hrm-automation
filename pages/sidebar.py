from playwright.sync_api import Page

class Sidebar():
    def __init__(self, page: Page):

        self.admin = page.get_by_role("link", name="Admin")
        self.pim = page.get_by_role("link", name="PIM")
        self.leave = page.get_by_role("link", name="Leave")
        self.time = page.get_by_role("link", name="Time")
        self.recruitment = page.get_by_role("link", name="Recruitment")
        self.my_info = page.get_by_role("link", name="My Info")
        self.performance = page.get_by_role("link", name="Performance")
        self.dashboard = page.get_by_role("link", name="Dashboard")
        self.directory = page.get_by_role("link", name="Directory")
        self.maintenance = page.get_by_role("link", name="Maintenance")
        self.claim = page.get_by_role("link", name="Claim")
        self.buzz = page.get_by_role("link", name="Buzz")
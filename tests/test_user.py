from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.admin.admin_page import AdminPage
from pages.admin.add_user_page import AddUserPage
from pages.sidebar import Sidebar

def test_add_user(page):
    "Menambah data user"

    login_page = LoginPage(page)
    admin_page = AdminPage(page)
    add_user_page = AddUserPage(page)
    sidebar = Sidebar(page)

    login_page.open()
    login_page.login("Admin", "admin123")

    sidebar.admin.click()
    admin_page.add_btn.click()
    add_user_page.add_user()

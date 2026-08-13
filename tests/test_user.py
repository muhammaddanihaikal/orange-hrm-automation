from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.admin.admin_page import AdminPage
from pages.admin.add_user_page import AddUserPage
from pages.sidebar import Sidebar
from utils.data_factory import generate_username
from utils.read_data import read_data
from config import BASE_URL
from pages.admin.edit_user_page import EditUserPage

user_data = read_data("user_data.json")

add_user_data = user_data["add_user"]
add_user_data["username"] = generate_username(
    add_user_data["username_prefix"]
)
username = add_user_data["username"]

edit_user_data = user_data["edit_user"]


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

    add_user_page.add_user(add_user_data)
    expect(page).to_have_url(f"{BASE_URL}/web/index.php/admin/viewSystemUsers")

    admin_page.search(username)
    expect(admin_page.user_row(username)).to_be_visible()


def test_edit_user(page):
    "Mengubah data user"
    login_page = LoginPage(page)
    admin_page = AdminPage(page)
    edit_user_page = EditUserPage(page)
    sidebar = Sidebar(page)

    login_page.open()
    login_page.login("Admin", "admin123")

    sidebar.admin.click()
    admin_page.search(username)
    expect(admin_page.user_row(username)).to_be_visible()

    admin_page.edit_button(username).click()

    edit_user_page.edit_user(edit_user_data)
    expect(page).to_have_url(f"{BASE_URL}/web/index.php/admin/viewSystemUsers")
    
    admin_page.search(username)
    expect(admin_page.user_row(username)).to_be_visible()



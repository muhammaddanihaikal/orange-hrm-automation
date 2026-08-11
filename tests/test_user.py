from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.admin.admin_page import AdminPage
from pages.admin.add_user_page import AddUserPage
from pages.sidebar import Sidebar
from utils.data_factory import generate_username
from utils.read_data import read_data
from config import BASE_URL

user_data = read_data("user_data.json")
# generate username random
user_data["username"] = generate_username(
    user_data["username_prefix"]
)

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
    add_user_page.add_user(user_data)

    expect(page).to_have_url(f"{BASE_URL}/web/index.php/admin/viewSystemUsers")
    admin_page.search(user_data["username"])
    admin_page.user_row(user_data["username"])





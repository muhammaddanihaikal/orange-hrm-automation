from playwright.sync_api import expect

from config import BASE_URL
from pages.admin.add_user_page import AddUserPage
from pages.admin.admin_page import AdminPage
from pages.admin.edit_user_page import EditUserPage
from pages.login_page import LoginPage
from pages.sidebar import Sidebar
from utils.data_factory import generate_username
from utils.read_data import read_data


user_data = read_data("user_data.json")

add_user_data = user_data["add_user"]
add_user_data["username"] = generate_username(
    add_user_data["username_prefix"]
)
username = add_user_data["username"]

edit_user_data = user_data["edit_user"]


def test_add_user(page):
    "menambah data user"

    login_page = LoginPage(page)
    admin_page = AdminPage(page)
    add_user_page = AddUserPage(page)
    sidebar = Sidebar(page)

    # login
    login_page.open()
    login_page.login("Admin", "admin123")

    # buka admin page
    sidebar.admin.click()

    # buka form add user
    admin_page.add_btn.click()

    # tambah user
    add_user_page.add_user(add_user_data)

    # pastikan kembali ke admin page
    expect(page).to_have_url(
        f"{BASE_URL}/web/index.php/admin/viewSystemUsers"
    )

    # cari user yang baru dibuat
    admin_page.search(username)

    # pastikan user berhasil ditambahkan
    expect(
        admin_page.user_row(username)
    ).to_be_visible()


def test_edit_user(page):
    "Mengubah data user"

    login_page = LoginPage(page)
    admin_page = AdminPage(page)
    edit_user_page = EditUserPage(page)
    sidebar = Sidebar(page)

    # login
    login_page.open()
    login_page.login("Admin", "admin123")

    # buka admin page
    sidebar.admin.click()

    # cari user
    admin_page.search(username)
    expect(admin_page.user_row(username)).to_be_visible()

    # buka halaman edit
    admin_page.click_edit(username)

    # edit user dan simpan employee yang dipilih
    selected_employee = edit_user_page.edit_user(edit_user_data)
    name_parts = selected_employee.split()
    expected_employee = (
        f"{name_parts[0]} {name_parts[-1]}"
    )

    # pastikan kembali ke admin page
    expect(page).to_have_url(
        f"{BASE_URL}/web/index.php/admin/viewSystemUsers"
    )

    # cari user yang sudah diedit
    admin_page.search(username)

    # pastikan user masih ada
    row = admin_page.user_row(username)
    expect(row).to_be_visible()

    # validasi hasil edit
    expect(row.get_by_role("cell").nth(2)).to_have_text(edit_user_data["user_role"])
    expect(row.get_by_role("cell").nth(3)).to_have_text(expected_employee)
    expect(row.get_by_role("cell").nth(4)).to_have_text(edit_user_data["status"])



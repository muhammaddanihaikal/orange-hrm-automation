import allure
from playwright.sync_api import Page, expect

from config import BASE_URL
from pages.admin.add_user_page import AddUserPage
from pages.admin.admin_page import AdminPage
from pages.admin.edit_user_page import EditUserPage
from pages.sidebar import Sidebar
from utils.data_factory import generate_username
from utils.read_data import read_data

USER_DATA = read_data("user_data.json")


@allure.title("[TC-ADMIN-01] Menambahkan data System Users")
def test_add_user(logged_in_page: Page):
    page = logged_in_page
    admin_page = AdminPage(page)
    add_user_page = AddUserPage(page)
    sidebar = Sidebar(page)

    # 1. Arrange (persiapan)
    add_user_data = USER_DATA["add_user"].copy()
    username = generate_username(add_user_data["username_prefix"])
    add_user_data["username"] = username

    sidebar.admin.click()
    admin_page.add_btn.click()

    # 2. Act (aksi)
    add_user_page.add_user(add_user_data)

    # 3. Assert (validasi)
    expect(page.get_by_text("Successfully Saved")).to_be_visible()
    expect(page).to_have_url(f"{BASE_URL}/web/index.php/admin/viewSystemUsers")

    # cari user yang baru dibuat dan pastikan ada di tabel
    admin_page.filter_by_username(username)
    admin_page.search()
    expect(admin_page.user_row(username)).to_be_visible()


@allure.title(
    "[TC-ADMIN-02] Menambahkan data System Users tanpa mengisi field mandatory"
)
def test_add_user_empty(logged_in_page: Page):
    page = logged_in_page
    admin_page = AdminPage(page)
    add_user_page = AddUserPage(page)
    sidebar = Sidebar(page)

    # 1. Arrange (persiapan)
    sidebar.admin.click()
    admin_page.add_btn.click()

    # 2. Act (aksi)
    add_user_page.save_btn.click()

    # 3. Assert (validasi)
    expect(page.get_by_text("Required", exact=True)).to_have_count(5)
    expect(page.get_by_text("Passwords do not match")).to_be_visible()


@allure.title("[TC-ADMIN-03] Mengubah data System Users")
def test_edit_user(logged_in_page: Page, api_create_user: str):
    page = logged_in_page
    admin_page = AdminPage(page)
    edit_user_page = EditUserPage(page)
    sidebar = Sidebar(page)

    # 1. Arrange (persiapan)
    edit_user_data = USER_DATA["edit_user"]

    sidebar.admin.click()
    admin_page.filter_by_username(api_create_user)
    admin_page.search()
    expect(admin_page.user_row(api_create_user)).to_be_visible()
    admin_page.edit(api_create_user)

    # 2. Act (aksi)
    selected_employee = edit_user_page.edit_user(edit_user_data)
    name_parts = selected_employee.split()
    expected_employee = f"{name_parts[0]} {name_parts[-1]}"

    # 3. Assert (validasi)
    expect(page.get_by_text("Successfully Updated")).to_be_visible()
    expect(page).to_have_url(f"{BASE_URL}/web/index.php/admin/viewSystemUsers")

    # cari user yang sudah diedit dan pastikan data di tabel terupdate
    admin_page.filter_by_username(api_create_user)
    admin_page.search()
    row = admin_page.user_row(api_create_user)
    expect(row).to_be_visible()
    expect(row.get_by_role("cell").nth(2)).to_have_text(edit_user_data["user_role"])
    expect(row.get_by_role("cell").nth(3)).to_have_text(expected_employee)
    expect(row.get_by_role("cell").nth(4)).to_have_text(edit_user_data["status"])


@allure.title("[TC-ADMIN-04] Menghapus data System Users")
def test_delete_user(logged_in_page: Page, api_create_user: str):
    page = logged_in_page
    admin_page = AdminPage(page)
    sidebar = Sidebar(page)

    # 1. Arrange (persiapan)
    sidebar.admin.click()
    admin_page.filter_by_username(api_create_user)
    admin_page.search()
    expect(admin_page.user_row(api_create_user)).to_be_visible()

    # 2. Act (aksi)
    admin_page.delete(api_create_user)

    # 3. Assert (validasi)
    admin_page.filter_by_username(api_create_user)
    admin_page.search()
    expect(admin_page.user_row(api_create_user)).to_be_hidden()
    expect(page.get_by_text("No Records Found").first).to_be_visible()


@allure.title("[TC-ADMIN-05] Melakukan filter data System Users berdasarkan Username")
def test_filter_user_by_username(logged_in_page: Page, api_create_user: str):
    page = logged_in_page
    sidebar = Sidebar(page)
    admin_page = AdminPage(page)
    username = api_create_user

    # 1. Arrange (persiapan)
    sidebar.admin.click()

    # 2. Act (aksi)
    admin_page.filter_by_username(username)
    admin_page.search()

    # 3. Assert (validasi)
    # memeastikan user dengan username yg di filter ada di tabel
    expect(admin_page.user_row(username)).to_be_visible()


@allure.title("[TC-ADMIN-06] Melakukan filter data System Users berdasarkan User Role")
def test_filter_user_by_user_role(logged_in_page: Page):
    page = logged_in_page
    sidebar = Sidebar(page)
    admin_page = AdminPage(page)

    # 1. Arrange (persiapan)
    sidebar.admin.click()

    # 2. Act (aksi)
    admin_page.filter_by_user_role("Admin")
    admin_page.search()

    # 3. Assert (validasi)
    # ambil semua baris data yg ada di tabel
    rows = admin_page.table_rows

    # pastikan tabelnya ngga kosong (syarat loop)
    expect(rows.first).to_be_visible()

    # LOOP SEMUA BARIS: pastikan semua baris pada kolom "User Role" bernilai "Admin"
    for row in rows.all():
        expect(row.get_by_role("cell").nth(2)).to_have_text("Admin")


@allure.title(
    "[TC-ADMIN-07] Melakukan filter data System Users berdasarkan Employee Name"
)
def test_filter_user_by_employee_name(logged_in_page: Page, api_create_user: str):
    page = logged_in_page
    sidebar = Sidebar(page)
    admin_page = AdminPage(page)
    username = api_create_user

    # 1. Arrange (persiapan)
    sidebar.admin.click()

    # 2. Act (aksi)
    admin_page.filter_by_employee_name("Budi")
    admin_page.search()

    # 3. Assert (validasi)
    expect(admin_page.user_row(username)).to_be_visible()


@allure.title("[TC-ADMIN-08] Melakukan filter data System Users berdasarkan Status")
def test_filter_user_by_status(logged_in_page: Page):
    page = logged_in_page
    sidebar = Sidebar(page)
    admin_page = AdminPage(page)

    # 1. Arrange (persiapan)
    sidebar.admin.click()

    # 2. Act (aksi)
    admin_page.filter_by_status("Disabled")
    admin_page.search()

    # 3. Assert (validasi)
    # ambil semua baris data yg ada di tabel
    rows = admin_page.table_rows

    # pastikan tabelnya ngga kosong (syarat loop)
    expect(rows.first).to_be_visible()

    # LOOP SEMUA BARIS: pastikan semua baris pada kolom "Status" bernilai "Disabled"
    for row in rows.all():
        expect(row.get_by_role("cell").nth(4)).to_have_text("Disabled")


@allure.title("[TC-ADMIN-09] Mereset filter System Users")
def test_reset_filter(logged_in_page: Page):
    page = logged_in_page
    admin_page = AdminPage(page)
    sidebar = Sidebar(page)

    # 1. Arrange (persiapan)
    sidebar.admin.click()

    # ambil semua teks jumlah data awal
    initial_records = page.get_by_text("Records Found").first.inner_text()

    # 2. Act (aksi)
    admin_page.filter_by_username("dani")
    admin_page.filter_by_user_role("Admin")
    admin_page.filter_by_employee_name("Budi")
    admin_page.filter_by_status("Disabled")
    admin_page.search()
    admin_page.reset()

    # 3. Assert (validasi)
    # validasi: filter terreset
    expect(admin_page.username_filter).to_have_value("")
    expect(admin_page.user_role_filter).to_contain_text("-- Select --")
    expect(admin_page.employee_name_filter).to_have_value("")
    expect(admin_page.status_filter).to_contain_text("-- Select --")

    # validasi: data kembali seperti semula
    expect(page.get_by_text("Records Found").first).to_have_text(initial_records)


@allure.title("[TC-ADMIN-10] Melakukan filter data System Users kombinasi")
def test_filter_user_combination(logged_in_page: Page):
    page = logged_in_page
    sidebar = Sidebar(page)
    admin_page = AdminPage(page)

    # 1. Arrange (persiapan)
    sidebar.admin.click()

    # 2. Act (aksi)
    admin_page.filter_by_username("admin1")
    admin_page.filter_by_user_role("Admin")
    admin_page.filter_by_employee_name("Budi")
    admin_page.filter_by_status("Enabled")
    admin_page.search()

    # 3. Assert (validasi)
    # pastiin ada satu data
    rows = admin_page.table_rows
    expect(rows.first).to_be_visible()

    for row in rows.all():
        # cek kolom username
        expect(row.get_by_role("cell").nth(1)).to_have_text("admin1")
        # cek kolom user role
        expect(row.get_by_role("cell").nth(2)).to_have_text("Admin")
        # cek kolom employee name
        expect(row.get_by_role("cell").nth(3)).to_contain_text("Budi")
        # cek kolom status
        expect(row.get_by_role("cell").nth(4)).to_have_text("Enabled")

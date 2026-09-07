from playwright.sync_api import Page, expect

from config import BASE_URL
from pages.admin.add_user_page import AddUserPage
from pages.admin.admin_page import AdminPage
from pages.admin.edit_user_page import EditUserPage
from pages.sidebar import Sidebar
from utils.data_factory import generate_username
from utils.read_data import read_data

user_data = read_data("user_data.json")

add_user_data = user_data["add_user"]
add_user_data["username"] = generate_username(add_user_data["username_prefix"])
username = add_user_data["username"]

edit_user_data = user_data["edit_user"]


def test_add_user(logged_in_page: Page):
    """Menambah data user"""
    page = logged_in_page

    admin_page = AdminPage(page)
    add_user_page = AddUserPage(page)
    sidebar = Sidebar(page)

    # buka admin page
    sidebar.admin.click()

    # buka form add user
    admin_page.add_btn.click()

    # tambah user
    add_user_page.add_user(add_user_data)

    # validasi nunggu sampe alert sukses saves muncul
    expect(page.get_by_text("Successfully Saved")).to_be_visible()

    # pastikan kembali ke admin page
    expect(page).to_have_url(f"{BASE_URL}/web/index.php/admin/viewSystemUsers")

    # cari user yang baru dibuat
    admin_page.filter_by_username(username)
    admin_page.search()

    # pastikan user berhasil ditambahkan
    expect(admin_page.user_row(username)).to_be_visible()


def test_add_user_empty(logged_in_page: Page):
    """Negative Test: Memastikan muncul error 'Required' jika form kosong"""
    page = logged_in_page
    admin_page = AdminPage(page)
    add_user_page = AddUserPage(page)
    sidebar = Sidebar(page)

    # 1. Arrange (Persiapan)
    # buka menu admin lalu klik tombol add
    sidebar.admin.click()
    admin_page.add_btn.click()

    # 2. Act (Aksi)
    # sengaja tidak isi form dan langsung klik save
    add_user_page.save_btn.click()

    # 3. Assert (Validasi)
    # validasi 1 : tulisan 'Required' harus muncul 5 buah
    # validasi 2 : tulisan 'Passwords do not match' muncul 1 buat
    expect(page.get_by_text("Required", exact=True)).to_have_count(5)
    expect(page.get_by_text("Passwords do not match")).to_be_visible()


def test_edit_user(logged_in_page: Page, api_create_user: str):
    """Mengubah data user"""
    page = logged_in_page

    admin_page = AdminPage(page)
    edit_user_page = EditUserPage(page)
    sidebar = Sidebar(page)

    # buka admin page
    sidebar.admin.click()

    # cari user
    admin_page.filter_by_username(api_create_user)
    expect(admin_page.user_row(api_create_user)).to_be_visible()

    # buka halaman edit
    admin_page.edit(api_create_user)

    # edit user dan simpan employee yang dipilih
    selected_employee = edit_user_page.edit_user(edit_user_data)
    name_parts = selected_employee.split()
    expected_employee = f"{name_parts[0]} {name_parts[-1]}"

    # validasi nunggu sampe alert sukses update muncul
    expect(page.get_by_text("Successfully Updated")).to_be_visible()

    # pastikan kembali ke admin page
    expect(page).to_have_url(f"{BASE_URL}/web/index.php/admin/viewSystemUsers")

    # cari user yang sudah diedit
    admin_page.filter_by_username(api_create_user)
    admin_page.search()

    # pastikan user masih ada
    row = admin_page.user_row(api_create_user)
    expect(row).to_be_visible()

    # validasi hasil edit
    expect(row.get_by_role("cell").nth(2)).to_have_text(edit_user_data["user_role"])
    expect(row.get_by_role("cell").nth(3)).to_have_text(expected_employee)
    expect(row.get_by_role("cell").nth(4)).to_have_text(edit_user_data["status"])


def test_delete_user(logged_in_page: Page, api_create_user: str):
    """Menghapus data user"""
    page = logged_in_page

    admin_page = AdminPage(page)
    sidebar = Sidebar(page)

    # buka sidebar admin
    sidebar.admin.click()

    # cari user dan validasi
    admin_page.filter_by_username(api_create_user)
    expect(admin_page.user_row(api_create_user)).to_be_visible()

    # hapus user
    admin_page.delete(api_create_user)

    # cari user dan validasi
    admin_page.filter_by_username(api_create_user)
    admin_page.search()
    expect(admin_page.user_row(api_create_user)).to_be_hidden()
    expect(page.get_by_text("No Records Found").first).to_be_visible()


def test_filter_user_by_username(logged_in_page: Page, api_create_user: str):
    """Filter user berdasarkan username dan memastikan user muncul di tabel."""
    page = logged_in_page
    sidebar = Sidebar(page)
    admin_page = AdminPage(page)
    username = api_create_user

    # 1. Arrange
    sidebar.admin.click()

    # 2. Act
    admin_page.filter_by_username(username)
    admin_page.search()

    # 3. Assert
    # memeastikan user dengan username yg di filter ada di tabel
    expect(admin_page.user_row(username)).to_be_visible()


def test_filter_user_by_user_role(logged_in_page: Page):
    """Filter user berdasarkan role dan memastikan semua baris di tabel sesuai role."""
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
    rows = admin_page.user_table.locator(".oxd-table-card")

    # pastikan tabelnya ngga kosong (syarat loop)
    expect(rows.first).to_be_visible()

    # LOOP SEMUA BARIS: pastikan semua baris pada kolom "User Role" bernilai "Admin"
    for row in rows.all():
        expect(row.get_by_role("cell").nth(2)).to_have_text("Admin")


def test_filter_user_by_employee_name(logged_in_page: Page, api_create_user: str):
    """Filter user berdasarkan nama karyawan dan memastikan user muncul di tabel."""
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


def test_filter_user_by_status(logged_in_page: Page):
    """Filter user berdasarkan status dan memastikan semua baris di tabel sesuai status."""
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
    rows = admin_page.user_table.locator(".oxd-table-card")

    # pastikan tabelnya ngga kosong (syarat loop)
    expect(rows.first).to_be_visible()

    # LOOP SEMUA BARIS: pastikan semua baris pada kolom "Status" bernilai "Disabled"
    for row in rows.all():
        expect(row.get_by_role("cell").nth(4)).to_have_text("Disabled")


def test_reset_filter(logged_in_page: Page):
    """Memastikan tombol Reset mengosongkan seluruh filter dan memulihkan tabel."""
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

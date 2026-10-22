import allure
from playwright.sync_api import Page, expect

from config import BASE_URL
from pages.pim.add_employee_page import AddEmployeePage
from pages.pim.edit_employee_page import EditEmployeePage
from pages.pim.pim_page import PimPage
from pages.sidebar import Sidebar
from utils.data_factory import generate_employee_data
from utils.read_data import read_data

EMPLOYEE_DATA = read_data("employee_data.json")


@allure.title("[TC-PIM-01] Membuka halaman Employee List")
def test_open_employee_list(logged_in_page: Page):
    page = logged_in_page
    sidebar = Sidebar(page)
    pim_page = PimPage(page)

    # 1. Arrange (persiapan)
    # (Sudah otomatis login via logged_in_page)

    # 2. Act (aksi)
    sidebar.pim.click()

    # 3. Assert (validasi)
    expect(page).to_have_url(f"{BASE_URL}{pim_page.PATH}")
    expect(page.get_by_role("heading", name="PIM")).to_be_visible()


@allure.title("[TC-PIM-02] Menambahkan data Employee")
def test_add_employee(logged_in_page: Page):
    page = logged_in_page
    sidebar = Sidebar(page)
    pim_page = PimPage(page)
    add_employee_page = AddEmployeePage(page)

    # 1. Arrange (persiapan)
    employee_data = generate_employee_data()

    # 2. Act (aksi)
    sidebar.pim.click()
    pim_page.add_btn.click()
    add_employee_page.add_employee(employee_data)

    # 3. Assert (validasi)
    expect(page.get_by_text("Successfully Saved")).to_be_visible()

    # navigasi ke halaman Employee List
    sidebar.pim.click()
    pim_page.filter_by_employee_id(employee_data["employee_id"])
    pim_page.search()

    # validasi: hanya ada 1 row di tabel yang sesuai dengan employee_id
    employee_rows = pim_page.employee_row(employee_data["employee_id"])
    expect(employee_rows).to_have_count(1)


@allure.title("[TC-PIM-03] Menambahkan data Employee tanpa mengisi field mandatory")
def test_add_employee_empty(logged_in_page: Page):
    page = logged_in_page
    sidebar = Sidebar(page)
    pim_page = PimPage(page)
    add_employee_page = AddEmployeePage(page)

    # 1. Arrange (persiapan)
    sidebar.pim.click()
    pim_page.add_btn.click()

    # 2. Act (aksi)
    add_employee_page.add_employee_empty()

    # 3. Assert (validasi)
    expect(add_employee_page.first_name_error).to_be_visible()
    expect(add_employee_page.last_name_error).to_be_visible()
    expect(add_employee_page.username_error).to_be_visible()
    expect(add_employee_page.password_error).to_be_visible()
    expect(add_employee_page.confirm_password_error).to_be_visible()

    # Pastikan tetap berada di form Add Employee
    expect(page).to_have_url(f"{BASE_URL}{add_employee_page.PATH}")


@allure.title("[TC-PIM-04] Mengubah data Employee")
def test_edit_employee(logged_in_page: Page, api_create_employee: dict):
    page = logged_in_page
    sidebar = Sidebar(page)
    pim_page = PimPage(page)
    edit_employee_page = EditEmployeePage(page)
    employee_data = api_create_employee

    # 1. Arrange (persiapan)
    sidebar.pim.click()
    pim_page.filter_by_employee_id(employee_data["employee_id"])
    pim_page.search()
    pim_page.edit(employee_data["employee_id"])

    # 2. Act (aksi)
    edit_data = EMPLOYEE_DATA["edit_employee"].copy()
    edit_employee_page.edit_employee(edit_data)

    # 3. Assert (validasi)
    expect(page.get_by_text("Successfully Updated")).to_be_visible()

    sidebar.pim.click()
    pim_page.filter_by_employee_id(employee_data["employee_id"])
    pim_page.search()
    expect(pim_page.employee_row(employee_data["employee_id"])).to_contain_text(
        edit_data["first_name"]
    )


@allure.title("[TC-PIM-05] Mengubah data Employee tanpa mengisi field mandatory")
def test_edit_employee_empty(logged_in_page: Page):
    page = logged_in_page
    sidebar = Sidebar(page)
    pim_page = PimPage(page)
    edit_employee_page = EditEmployeePage(page)

    # 1. Arrange (persiapan)
    pass

    # 2. Act (aksi)
    pass

    # 3. Assert (validasi)
    pass


@allure.title("[TC-PIM-06] Menghapus data Employee")
def test_delete_employee(logged_in_page: Page):
    page = logged_in_page
    sidebar = Sidebar(page)
    pim_page = PimPage(page)

    # 1. Arrange (persiapan)
    pass

    # 2. Act (aksi)
    pass

    # 3. Assert (validasi)
    pass


@allure.title("[TC-PIM-07] Melakukan filter data Employee berdasarkan Employee Name")
def test_filter_employee_by_name(logged_in_page: Page):
    page = logged_in_page
    sidebar = Sidebar(page)
    pim_page = PimPage(page)

    # 1. Arrange (persiapan)
    pass

    # 2. Act (aksi)
    pass

    # 3. Assert (validasi)
    pass


@allure.title("[TC-PIM-08] Melakukan filter data Employee berdasarkan Employee Id")
def test_filter_employee_by_id(logged_in_page: Page):
    page = logged_in_page
    sidebar = Sidebar(page)
    pim_page = PimPage(page)

    # 1. Arrange (persiapan)
    pass

    # 2. Act (aksi)
    pass

    # 3. Assert (validasi)
    pass


@allure.title("[TC-PIM-09] Melakukan filter data Employee secara kombinasi")
def test_filter_employee_combination(logged_in_page: Page):
    page = logged_in_page
    sidebar = Sidebar(page)
    pim_page = PimPage(page)

    # 1. Arrange (persiapan)
    pass

    # 2. Act (aksi)
    pass

    # 3. Assert (validasi)
    pass


@allure.title("[TC-PIM-10] Mereset filter Employee")
def test_reset_filter_employee(logged_in_page: Page):
    page = logged_in_page
    sidebar = Sidebar(page)
    pim_page = PimPage(page)

    # 1. Arrange (persiapan)
    pass

    # 2. Act (aksi)
    pass

    # 3. Assert (validasi)
    pass

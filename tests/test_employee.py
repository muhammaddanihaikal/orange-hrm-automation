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
    pass


@allure.title("[TC-PIM-03] Menambahkan data Employee tanpa mengisi field mandatory")
def test_add_employee_empty(logged_in_page: Page):
    page = logged_in_page
    sidebar = Sidebar(page)
    pim_page = PimPage(page)
    add_employee_page = AddEmployeePage(page)

    # 1. Arrange (persiapan)
    pass

    # 2. Act (aksi)
    pass

    # 3. Assert (validasi)
    pass


@allure.title("[TC-PIM-04] Mengubah data Employee")
def test_edit_employee(logged_in_page: Page):
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

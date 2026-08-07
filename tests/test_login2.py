from playwright.sync_api import expect
from pages.base_page import BASE_URL
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.read_data import read_data

# Load data pengujian dari JSON
login_data = read_data("login_data.json")


def test_login_valid(page):
    """Melakukan login menggunakan data yang valid"""
    data = login_data["valid_login"]

    # buat object
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    # buka halaman login
    login_page.open()
    expect(login_page.heading).to_be_visible()

    # melakukan login
    login_page.login(data["username"], data["password"])
    expect(page).to_have_url(f"{BASE_URL}{dashboard_page.PATH}")
    expect(dashboard_page.heading).to_be_visible()



def test_login_invalid_username(page):
    """"Melakukan login menggunakan username yang tidak valid"""
    data = login_data["invalid_username"]

    login_page = LoginPage(page)
    login_page.open()
    login_page.login(data["username"], data["password"])



def test_login_invalid_password(page):
    """Melakukan login menggunakan password yang tidak valid"""
    data = login_data["invalid_password"]

    login_page = LoginPage(page)
    login_page.open()
    login_page.login(data["username"], data["password"])


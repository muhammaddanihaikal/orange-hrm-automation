from playwright.sync_api import expect
from pages.login_page import LoginPage
from utils.read_data import read_data

# Load data pengujian dari JSON
login_data = read_data("login_data.json")


def test_login_valid(page):
    """Pengujian login dengan data kredensial valid."""
    data = login_data["valid_login"]

    # Buka halaman dan lakukan login
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(data["username"], data["password"])


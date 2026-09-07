import allure
import pytest
from playwright.sync_api import expect

from config import BASE_URL
from pages.dashboard.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from utils.read_data import read_data

# Load data pengujian dari JSON
login_data = read_data("login_data.json")


@allure.title("[TC-AUTH-01] Melakukan login menggunakan data yang valid")
def test_login_valid(page):
    """[TC-AUTH-01] Melakukan login menggunakan data yang valid."""

    # ARRANGE - Persiapan Awal
    # ambil data
    data = login_data["valid_login"]

    # buat object
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    # buka halaman login
    login_page.open()
    expect(login_page.heading).to_be_visible()

    # ACT - melakukan login
    with page.expect_response("**/auth/validate"):
        login_page.login(data["username"], data["password"])

    # ASSERT - validasi
    expect(page).to_have_url(f"{BASE_URL}{dashboard_page.PATH}")
    expect(dashboard_page.heading).to_be_visible()


@allure.title("[TC-AUTH-02, TC-AUTH-03] Melakukan login menggunakan data tidak valid ({data_key})")
@pytest.mark.parametrize(
    "data_key", ["invalid_username", "invalid_password", "invalid_credentials"]
)
def test_login_invalid(page, data_key):
    """[TC-AUTH-02, TC-AUTH-03] Melakukan login menggunakan data yang tidak valid."""
    # ARRANGE (Persiapan data & state awal)
    # ambil data
    data = login_data[data_key]

    # buka halaman login
    login_page = LoginPage(page)
    login_page.open()

    # ACT - melakukan login
    with page.expect_response("**/auth/validate"):
        login_page.login(data["username"], data["password"])

    # ASSERT - validasi
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text("Invalid credentials")


@allure.title("[TC-AUTH-04] Melakukan login dengan form dibiarkan kosong ({data_key})")
@pytest.mark.parametrize("data_key", ["empty_username", "empty_password", "empty_both"])
def test_login_empty_field(page, data_key):
    """[TC-AUTH-04] Melakukan login dengan form dibiarkan kosong."""
    # ARRANGE (Persiapan data & state awal)
    # ambil data
    data = login_data[data_key]

    # buka halaman login
    login_page = LoginPage(page)
    login_page.open()

    # ACT - melakukan login
    login_page.login(data["username"], data["password"])

    # ASSERT - validasi tulisan Required
    expect(login_page.required_message).to_be_visible()

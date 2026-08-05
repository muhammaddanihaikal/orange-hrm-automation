from playwright.sync_api import expect
from pages.login_page import LoginPage
from data.login_data import LOGIN_DATA


def test_login(page):
    # buat object LoginPage
    login_page = LoginPage(page)

    # buka halaman login
    login_page.open()

    # verifikasi user berada di halaman login
    expect(page).to_have_title("OrangeHRM")
    expect(
        page.get_by_role("heading", name="Login")
    ).to_be_visible()

    # login sebagai Admin
    login_page.login(
        LOGIN_DATA["username"],
        LOGIN_DATA["password"]
    )

    # verifikasi login berhasil
    expect(page).to_have_url(
        f"{login_page.base_url}/web/index.php/dashboard/index"
    )

    expect(
        page.get_by_role("heading", name="Dashboard")
    ).to_be_visible()
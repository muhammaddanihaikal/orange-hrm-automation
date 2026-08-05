from playwright.sync_api import expect
from pages.login_page import LoginPage
from utils.read_data import read_data

login_data = read_data("login_data.json")


def test_login_success(page):
    """Melakukan login menggunakan data yang valid"""
    data = login_data["valid_login"]
    login_page = LoginPage(page)
    login_page.open()

    expect(page).to_have_title("OrangeHRM")
    expect(page.get_by_role("heading", name="Login")).to_be_visible()

    login_page.login(data["username"], data["password"])

    expect(page).to_have_url(
        f"{login_page.base_url}/web/index.php/dashboard/index"
    )
    expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()


def test_login_invalid_username(page):
    """Melakukan login menggunakan username yang tidak valid"""
    data = login_data["invalid_username"]
    login_page = LoginPage(page)
    login_page.open()

    login_page.login(data["username"], data["password"])

    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text("Invalid credentials")


def test_login_invalid_password(page):
    """Melakukan login menggunakan password yang tidak valid"""
    data = login_data["invalid_password"]
    login_page = LoginPage(page)
    login_page.open()

    login_page.login(data["username"], data["password"])

    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text("Invalid credentials")


def test_login_invalid_credentials(page):
    """Melakukan login menggunakan username dan password yang tidak valid"""
    data = login_data["invalid_credentials"]
    login_page = LoginPage(page)
    login_page.open()

    login_page.login(data["username"], data["password"])

    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text("Invalid credentials")
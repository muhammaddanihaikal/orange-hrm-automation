import pytest
from playwright.sync_api import sync_playwright, Browser
from config import HEADLESS, BASE_URL
from pages.login_page import LoginPage
import os


@pytest.fixture(scope="session")
def playwright():
    """Menginisiasi engine Playwright untuk seluruh sesi pengujian."""
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright):
    """Membuka browser (Chromium) sekali untuk seluruh sesi test."""
    browser = playwright.chromium.launch(
        headless=HEADLESS,
        slow_mo=0
    )

    yield browser

    browser.close()


@pytest.fixture
def context(browser):
    """Membuka context browser (sesi penjelajahan) baru yang bersih."""
    context = browser.new_context()

    yield context

    context.close()


@pytest.fixture
def page(context):
    """Membuka tab (halaman) baru untuk eksekusi test."""
    page = context.new_page()

    yield page

    page.close()


@pytest.fixture(scope="session")
def global_login(playwright):
    """Berjalan 1x di awal untuk login UI dan menyimpan cookies sesi."""
    # bikin folder auth kalo belum ada
    os.makedirs(".auth", exist_ok=True)

    # buka browser
    browser = playwright.chromium.launch(headless=HEADLESS)
    context = browser.new_context()
    page = context.new_page()

    # proses login
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("Admin", "admin123")

    # tunggu masuk ke dashboard
    page.wait_for_url(f"{BASE_URL}/web/index.php/dashboard/index")

    # simpan cookies kedalam file json
    context.storage_state(path=".auth/state.json")

    # tutup browser
    browser.close()


@pytest.fixture
def logged_in_page(browser: Browser, global_login):
    """Menyediakan halaman yang sudah login menggunakan cookies yang tersimpan."""
    # buka context baru, TAPI langsung pake cookie dari state.json
    context = browser.new_context(storage_state=".auth/state.json")
    page = context.new_page()
    
    # Langsung arahkan ke dashboard supaya test tinggal pakai
    page.goto(f"{BASE_URL}/web/index.php/dashboard/index")

    yield page

    context.close()
import os

import pytest
from playwright.sync_api import Browser, Page, sync_playwright

from config import BASE_URL, HEADLESS
from pages.login_page import LoginPage


@pytest.fixture(scope="session")
def playwright():
    """Menginisiasi engine Playwright untuk seluruh sesi pengujian."""
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright):
    """Membuka browser (Chromium) sekali untuk seluruh sesi test."""
    browser = playwright.chromium.launch(headless=HEADLESS, slow_mo=0)

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


@pytest.fixture
def api_create_user(logged_in_page: Page):
    """Menyiapkan user data (Setup) via API dan menghapusnya setelah test (Teardown)."""
    tumbal_username = "tumbal_username_123"

    # 1. buat user
    post_response = logged_in_page.request.post(
        f"{BASE_URL}/web/index.php/api/v2/admin/users",
        data={
            "userRoleId": 1,
            "empNumber": 2,
            "username": tumbal_username,
            "password": "JagungManis_9192",
            "status": True,
        },
    )
    assert post_response.ok, f"Gagal bikin user via API: {post_response.text()}"

    response_json = post_response.json()
    user_id = response_json["data"]["id"]

    # 2. pinjemin username
    yield tumbal_username

    # 3. teardown (hapus user)
    delete_response = logged_in_page.request.delete(
        f"{BASE_URL}/web/index.php/api/v2/admin/users", data={"ids": [user_id]}
    )

    # abaikan kalo statusnya 404, karena tujuanya udah tercapai yaitu "User Terhapus"
    if delete_response.status != 404:
        assert delete_response.ok, f"Gagal hapus user via API: {delete_response.text()}"


@pytest.fixture
def api_create_bulk_users(logged_in_page: Page):
    """Menyiapkan 2 user data via API untuk pengujian bulk action dan menghpusnya seletah test"""
    prefix = "bulk_user_"
    usernames = [f"{prefix}1", f"{prefix}2"]
    created_user_ids = []

    # 1. Setup: buat 2 user via API
    for username in usernames:
        post_response = logged_in_page.request.post(
            f"{BASE_URL}/web/index.php/api/v2/admin/users",
            data={
                "userRoleId": 1,
                "empNumber": 2,
                "username": username,
                "password": "JagungManis_9192",
                "status": True,
            },
        )

        assert post_response.ok, (
            f"Gagal bikin user {username} via API: {post_response.text()}"
        )
        user_id = post_response.json()["data"]["id"]
        created_user_ids.append(user_id)

    # 2. Pinjamkan prefix dan list username ke fungsi test
    yield {"prefix": prefix, "usernames": usernames}

    # 3. Teardown: Hapus kedua user via API
    delete_response = logged_in_page.request.delete(
        f"{BASE_URL}/web/index.php/api/v2/admin/users",
        data={"ids": created_user_ids},
    )

    if delete_response.status != 404:
        assert delete_response.ok, (
            f"Gagal hapus bulk user via API: {delete_response.text()}"
        )

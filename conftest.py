import pytest
from playwright.sync_api import sync_playwright
from config import HEADLESS
from pages.login_page import LoginPage

@pytest.fixture
def logged_in_page():
    pass


@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright):
    browser = playwright.chromium.launch(
        headless=HEADLESS,
        slow_mo=0
    )

    yield browser

    browser.close()


@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context()

    yield context

    context.close()


@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()

    yield page

    page.close()
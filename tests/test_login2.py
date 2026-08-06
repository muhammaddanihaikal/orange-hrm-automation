from playwright.sync_api import expect
from pages.login_page import LoginPage
from utils.read_data import read_data

login_data = read_data("login_data.json")

def test_login_valid(page):
    """"Melakukan login menggunakan data yang valid"""
    # ambil data
    username = login_data["valid_login"]["username"]
    password = login_data["valid_login"]["password"]

    # buat object login page
    login_page = LoginPage(page)
    # masuk ke halaman login
    login_page.open()
    # melakukan login
    login_page.login(username, password)
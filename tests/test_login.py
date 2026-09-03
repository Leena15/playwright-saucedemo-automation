import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.mark.login
def test_valid_login_standard_user(page, load_users):
    login = LoginPage(page)
    login.navigate()
    login.login(load_users["standard"]["username"], load_users["standard"]["password"])
    assert "/inventory" in page.url
    inventory = InventoryPage(page)
    assert inventory.get_item_count() == 6


@pytest.mark.login
def test_locked_out_user(page, load_users):
    login = LoginPage(page)
    login.navigate()
    login.login(load_users["locked"]["username"], load_users["locked"]["password"])
    assert login.is_error_displayed()
    assert "locked out" in login.get_error_message().lower()


@pytest.mark.login
def test_invalid_password(page, load_users):
    login = LoginPage(page)
    login.navigate()
    login.login(load_users["standard"]["username"], "wrong_password")
    assert login.is_error_displayed()
    assert "Username and password do not match" in login.get_error_message()


@pytest.mark.login
def test_empty_username(page, load_users):
    login = LoginPage(page)
    login.navigate()
    login.login("", load_users["standard"]["password"])
    assert login.is_error_displayed()
    assert "Username is required" in login.get_error_message()


@pytest.mark.login
def test_empty_password(page, load_users):
    login = LoginPage(page)
    login.navigate()
    login.login(load_users["standard"]["username"], "")
    assert login.is_error_displayed()
    assert "Password is required" in login.get_error_message()


@pytest.mark.login
def test_empty_both_fields(page):
    login = LoginPage(page)
    login.navigate()
    login.login("", "")
    assert login.is_error_displayed()
    assert "Username is required" in login.get_error_message()


@pytest.mark.login
@pytest.mark.parametrize("user_key", ["standard", "problem", "glitch", "error", "visual"])
def test_login_all_valid_users(page, load_users, user_key):
    login = LoginPage(page)
    login.navigate()
    login.login(load_users[user_key]["username"], load_users[user_key]["password"])
    assert "/inventory" in page.url


@pytest.mark.login
def test_logout(page, load_users):
    login = LoginPage(page)
    login.navigate()
    login.login(load_users["standard"]["username"], load_users["standard"]["password"])
    inventory = InventoryPage(page)
    inventory.logout()
    assert page.url == LoginPage.URL or page.url == LoginPage.URL + "/"

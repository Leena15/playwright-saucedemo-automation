import pytest
from pages.inventory_page import InventoryPage
from pages.product_detail_page import ProductDetailPage


@pytest.mark.inventory
def test_inventory_displays_six_products(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    assert inventory.get_item_count() == 6


@pytest.mark.inventory
def test_product_names_match_expected(logged_in_page, load_products):
    inventory = InventoryPage(logged_in_page)
    actual_names = inventory.get_all_item_names()
    expected_names = [p["name"] for p in load_products["products"]]
    assert sorted(actual_names) == sorted(expected_names)


@pytest.mark.inventory
def test_product_prices_match_expected(logged_in_page, load_products):
    inventory = InventoryPage(logged_in_page)
    actual_prices = inventory.get_all_item_prices()
    expected_prices = [p["price"] for p in load_products["products"]]
    assert sorted(actual_prices) == sorted(expected_prices)


@pytest.mark.inventory
def test_add_single_item_to_cart(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.add_item_to_cart("Sauce Labs Backpack")
    assert inventory.get_cart_badge_count() == 1


@pytest.mark.inventory
def test_add_multiple_items_to_cart(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.add_item_to_cart("Sauce Labs Backpack")
    inventory.add_item_to_cart("Sauce Labs Bike Light")
    inventory.add_item_to_cart("Sauce Labs Bolt T-Shirt")
    assert inventory.get_cart_badge_count() == 3


@pytest.mark.inventory
def test_remove_item_from_inventory_page(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.add_item_to_cart("Sauce Labs Backpack")
    assert inventory.get_cart_badge_count() == 1
    inventory.remove_item_from_cart("Sauce Labs Backpack")
    assert inventory.get_cart_badge_count() == 0


@pytest.mark.inventory
def test_click_product_navigates_to_detail(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.click_item("Sauce Labs Backpack")
    detail = ProductDetailPage(logged_in_page)
    assert detail.get_product_name() == "Sauce Labs Backpack"
    assert detail.get_product_price() == 29.99


@pytest.mark.inventory
def test_problem_user_images(page, load_users):
    from pages.login_page import LoginPage
    login = LoginPage(page)
    login.navigate()
    login.login(load_users["standard"]["username"], load_users["standard"]["password"])
    standard_imgs = page.locator(".inventory_item img").evaluate_all("els => els.map(e => e.src)")

    login.navigate()
    login.login(load_users["problem"]["username"], load_users["problem"]["password"])
    problem_imgs = page.locator(".inventory_item img").evaluate_all("els => els.map(e => e.src)")

    assert standard_imgs != problem_imgs

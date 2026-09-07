import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@pytest.mark.cart
def test_added_item_appears_in_cart(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.add_item_to_cart("Sauce Labs Backpack")
    inventory.go_to_cart()
    cart = CartPage(logged_in_page)
    assert "Sauce Labs Backpack" in cart.get_cart_item_names()


@pytest.mark.cart
def test_multiple_items_in_cart(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.add_item_to_cart("Sauce Labs Backpack")
    inventory.add_item_to_cart("Sauce Labs Bike Light")
    inventory.add_item_to_cart("Sauce Labs Bolt T-Shirt")
    inventory.go_to_cart()
    cart = CartPage(logged_in_page)
    names = cart.get_cart_item_names()
    assert "Sauce Labs Backpack" in names
    assert "Sauce Labs Bike Light" in names
    assert "Sauce Labs Bolt T-Shirt" in names


@pytest.mark.cart
def test_remove_item_from_cart(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.add_item_to_cart("Sauce Labs Backpack")
    inventory.add_item_to_cart("Sauce Labs Bike Light")
    inventory.go_to_cart()
    cart = CartPage(logged_in_page)
    cart.remove_item("Sauce Labs Bike Light")
    assert cart.get_cart_item_count() == 1
    assert "Sauce Labs Backpack" in cart.get_cart_item_names()


@pytest.mark.cart
def test_cart_prices_match_inventory_prices(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    prices = inventory.get_all_item_prices()
    names = inventory.get_all_item_names()
    backpack_price = prices[names.index("Sauce Labs Backpack")]
    inventory.add_item_to_cart("Sauce Labs Backpack")
    inventory.go_to_cart()
    cart = CartPage(logged_in_page)
    cart_prices = cart.get_cart_item_prices()
    assert cart_prices[0] == backpack_price


@pytest.mark.cart
def test_continue_shopping_returns_to_inventory(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.add_item_to_cart("Sauce Labs Backpack")
    inventory.go_to_cart()
    cart = CartPage(logged_in_page)
    cart.continue_shopping()
    assert "/inventory" in logged_in_page.url


@pytest.mark.cart
def test_empty_cart(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.go_to_cart()
    cart = CartPage(logged_in_page)
    assert cart.get_cart_item_count() == 0

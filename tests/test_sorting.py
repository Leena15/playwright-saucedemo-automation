import pytest
from pages.inventory_page import InventoryPage


@pytest.mark.sorting
def test_sort_name_a_to_z(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.sort_by("az")
    names = inventory.get_all_item_names()
    assert names == sorted(names)


@pytest.mark.sorting
def test_sort_name_z_to_a(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.sort_by("za")
    names = inventory.get_all_item_names()
    assert names == sorted(names, reverse=True)


@pytest.mark.sorting
def test_sort_price_low_to_high(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.sort_by("lohi")
    prices = inventory.get_all_item_prices()
    assert prices == sorted(prices)


@pytest.mark.sorting
def test_sort_price_high_to_low(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.sort_by("hilo")
    prices = inventory.get_all_item_prices()
    assert prices == sorted(prices, reverse=True)


@pytest.mark.sorting
def test_default_sort_is_a_to_z(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    names = inventory.get_all_item_names()
    assert names == sorted(names)

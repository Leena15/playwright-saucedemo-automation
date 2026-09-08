import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.checkout_complete_page import CheckoutCompletePage


def _add_and_go_to_checkout(page, items):
    inventory = InventoryPage(page)
    for item in items:
        inventory.add_item_to_cart(item)
    inventory.go_to_cart()
    cart = CartPage(page)
    cart.proceed_to_checkout()
    return CheckoutStepOnePage(page)


@pytest.mark.checkout
def test_complete_checkout_flow(logged_in_page, load_checkout_info):
    step_one = _add_and_go_to_checkout(logged_in_page, ["Sauce Labs Backpack"])
    info = load_checkout_info["valid"]
    step_one.fill_info(info["firstName"], info["lastName"], info["postalCode"])
    step_one.continue_checkout()

    step_two = CheckoutStepTwoPage(logged_in_page)
    assert "Sauce Labs Backpack" in step_two.get_item_names()
    step_two.finish()

    complete = CheckoutCompletePage(logged_in_page)
    assert complete.get_header_text() == "Thank you for your order!"


@pytest.mark.checkout
def test_checkout_missing_first_name(logged_in_page, load_checkout_info):
    step_one = _add_and_go_to_checkout(logged_in_page, ["Sauce Labs Backpack"])
    info = load_checkout_info["missing_first"]
    step_one.fill_info(info["firstName"], info["lastName"], info["postalCode"])
    step_one.continue_checkout()
    assert step_one.is_error_displayed()
    assert "First Name is required" in step_one.get_error_message()


@pytest.mark.checkout
def test_checkout_missing_last_name(logged_in_page, load_checkout_info):
    step_one = _add_and_go_to_checkout(logged_in_page, ["Sauce Labs Backpack"])
    info = load_checkout_info["missing_last"]
    step_one.fill_info(info["firstName"], info["lastName"], info["postalCode"])
    step_one.continue_checkout()
    assert step_one.is_error_displayed()
    assert "Last Name is required" in step_one.get_error_message()


@pytest.mark.checkout
def test_checkout_missing_postal_code(logged_in_page, load_checkout_info):
    step_one = _add_and_go_to_checkout(logged_in_page, ["Sauce Labs Backpack"])
    info = load_checkout_info["missing_zip"]
    step_one.fill_info(info["firstName"], info["lastName"], info["postalCode"])
    step_one.continue_checkout()
    assert step_one.is_error_displayed()
    assert "Postal Code is required" in step_one.get_error_message()


@pytest.mark.checkout
def test_checkout_total_calculation(logged_in_page, load_checkout_info):
    step_one = _add_and_go_to_checkout(logged_in_page, ["Sauce Labs Backpack"])
    info = load_checkout_info["valid"]
    step_one.fill_info(info["firstName"], info["lastName"], info["postalCode"])
    step_one.continue_checkout()

    step_two = CheckoutStepTwoPage(logged_in_page)
    subtotal = step_two.get_subtotal()
    tax = step_two.get_tax()
    total = step_two.get_total()

    assert subtotal == 29.99
    assert round(total, 2) == round(subtotal + tax, 2)


@pytest.mark.checkout
def test_checkout_multiple_items_total(logged_in_page, load_checkout_info):
    step_one = _add_and_go_to_checkout(
        logged_in_page, ["Sauce Labs Backpack", "Sauce Labs Bike Light"]
    )
    info = load_checkout_info["valid"]
    step_one.fill_info(info["firstName"], info["lastName"], info["postalCode"])
    step_one.continue_checkout()

    step_two = CheckoutStepTwoPage(logged_in_page)
    subtotal = step_two.get_subtotal()
    tax = step_two.get_tax()
    total = step_two.get_total()

    assert round(subtotal, 2) == 39.98
    assert round(total, 2) == round(subtotal + tax, 2)


@pytest.mark.checkout
def test_cancel_on_step_one_returns_to_cart(logged_in_page):
    step_one = _add_and_go_to_checkout(logged_in_page, ["Sauce Labs Backpack"])
    step_one.cancel()
    assert "/cart" in logged_in_page.url


@pytest.mark.checkout
def test_cancel_on_step_two_returns_to_inventory(logged_in_page, load_checkout_info):
    step_one = _add_and_go_to_checkout(logged_in_page, ["Sauce Labs Backpack"])
    info = load_checkout_info["valid"]
    step_one.fill_info(info["firstName"], info["lastName"], info["postalCode"])
    step_one.continue_checkout()
    step_two = CheckoutStepTwoPage(logged_in_page)
    step_two.cancel()
    assert "/inventory" in logged_in_page.url

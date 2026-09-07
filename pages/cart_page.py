class CartPage:
    def __init__(self, page):
        self.page = page
        self.cart_items = page.locator(".cart_item")
        self.item_names = page.locator(".inventory_item_name")
        self.item_prices = page.locator(".inventory_item_price")
        self.remove_buttons = page.locator('[data-test^="remove"]')
        self.continue_shopping_button = page.locator('[data-test="continue-shopping"]')
        self.checkout_button = page.locator('[data-test="checkout"]')

    def get_cart_item_names(self) -> list:
        return self.item_names.all_inner_texts()

    def get_cart_item_prices(self) -> list:
        raw = self.item_prices.all_inner_texts()
        return [float(p.replace("$", "")) for p in raw]

    def get_cart_item_count(self) -> int:
        return self.cart_items.count()

    def remove_item(self, item_name: str):
        slug = item_name.lower().replace(" ", "-")
        self.page.locator(f'[data-test="remove-{slug}"]').click()

    def continue_shopping(self):
        self.continue_shopping_button.click()

    def proceed_to_checkout(self):
        self.checkout_button.click()

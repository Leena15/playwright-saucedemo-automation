class InventoryPage:
    SORT_OPTIONS = {
        "az": "az",
        "za": "za",
        "lohi": "lohi",
        "hilo": "hilo",
    }

    def __init__(self, page):
        self.page = page
        self.inventory_items = page.locator(".inventory_item")
        self.item_names = page.locator(".inventory_item_name")
        self.item_prices = page.locator(".inventory_item_price")
        self.sort_dropdown = page.locator('[data-test="product-sort-container"]')
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")
        self.menu_button = page.locator("#react-burger-menu-btn")
        self.logout_link = page.locator("#logout_sidebar_link")

    def get_all_item_names(self) -> list:
        return self.item_names.all_inner_texts()

    def get_all_item_prices(self) -> list:
        raw = self.item_prices.all_inner_texts()
        return [float(p.replace("$", "")) for p in raw]

    def get_item_count(self) -> int:
        return self.inventory_items.count()

    def add_item_to_cart(self, item_name: str):
        slug = item_name.lower().replace(" ", "-")
        self.page.locator(f'[data-test="add-to-cart-{slug}"]').click()

    def remove_item_from_cart(self, item_name: str):
        slug = item_name.lower().replace(" ", "-")
        self.page.locator(f'[data-test="remove-{slug}"]').click()

    def sort_by(self, option: str):
        self.sort_dropdown.select_option(self.SORT_OPTIONS[option])

    def get_cart_badge_count(self) -> int:
        if self.cart_badge.is_visible():
            return int(self.cart_badge.inner_text())
        return 0

    def go_to_cart(self):
        self.cart_link.click()

    def click_item(self, item_name: str):
        self.page.locator(".inventory_item_name", has_text=item_name).click()

    def logout(self):
        self.menu_button.click()
        self.logout_link.click()

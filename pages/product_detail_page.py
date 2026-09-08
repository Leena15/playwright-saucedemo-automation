class ProductDetailPage:
    def __init__(self, page):
        self.page = page
        self.product_name = page.locator(".inventory_details_name")
        self.product_price = page.locator(".inventory_details_price")
        self.product_description = page.locator(".inventory_details_desc")
        self.add_to_cart_button = page.locator('[data-test^="add-to-cart"]')
        self.remove_button = page.locator('[data-test^="remove"]')
        self.back_button = page.locator('[data-test="back-to-products"]')

    def get_product_name(self) -> str:
        return self.product_name.inner_text()

    def get_product_price(self) -> float:
        return float(self.product_price.inner_text().replace("$", ""))

    def get_product_description(self) -> str:
        return self.product_description.inner_text()

    def add_to_cart(self):
        self.add_to_cart_button.click()

    def remove_from_cart(self):
        self.remove_button.click()

    def go_back(self):
        self.back_button.click()

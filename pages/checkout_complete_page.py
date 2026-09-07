class CheckoutCompletePage:
    def __init__(self, page):
        self.page = page
        self.complete_header = page.locator(".complete-header")
        self.complete_text = page.locator(".complete-text")
        self.back_button = page.locator('[data-test="back-to-products"]')

    def get_header_text(self) -> str:
        return self.complete_header.inner_text()

    def get_complete_text(self) -> str:
        return self.complete_text.inner_text()

    def go_back_to_products(self):
        self.back_button.click()

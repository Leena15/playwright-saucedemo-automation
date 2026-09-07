class CheckoutStepTwoPage:
    def __init__(self, page):
        self.page = page
        self.item_names = page.locator(".inventory_item_name")
        self.item_prices = page.locator(".inventory_item_price")
        self.subtotal = page.locator(".summary_subtotal_label")
        self.tax = page.locator(".summary_tax_label")
        self.total = page.locator(".summary_total_label")
        self.finish_button = page.locator('[data-test="finish"]')
        self.cancel_button = page.locator('[data-test="cancel"]')

    def get_item_names(self) -> list:
        return self.item_names.all_inner_texts()

    def get_subtotal(self) -> float:
        text = self.subtotal.inner_text()
        return float(text.split("$")[1])

    def get_tax(self) -> float:
        text = self.tax.inner_text()
        return float(text.split("$")[1])

    def get_total(self) -> float:
        text = self.total.inner_text()
        return float(text.split("$")[1])

    def finish(self):
        self.finish_button.click()

    def cancel(self):
        self.cancel_button.click()

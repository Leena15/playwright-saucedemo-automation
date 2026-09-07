class CheckoutStepOnePage:
    def __init__(self, page):
        self.page = page
        self.first_name_field = page.locator('[data-test="firstName"]')
        self.last_name_field = page.locator('[data-test="lastName"]')
        self.postal_code_field = page.locator('[data-test="postalCode"]')
        self.continue_button = page.locator('[data-test="continue"]')
        self.cancel_button = page.locator('[data-test="cancel"]')
        self.error_message = page.locator('[data-test="error"]')

    def fill_info(self, first_name: str, last_name: str, postal_code: str):
        self.first_name_field.fill(first_name)
        self.last_name_field.fill(last_name)
        self.postal_code_field.fill(postal_code)

    def continue_checkout(self):
        self.continue_button.click()

    def cancel(self):
        self.cancel_button.click()

    def get_error_message(self) -> str:
        return self.error_message.inner_text()

    def is_error_displayed(self) -> bool:
        return self.error_message.is_visible()

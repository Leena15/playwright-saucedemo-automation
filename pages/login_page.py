class LoginPage:
    URL = "https://www.saucedemo.com"

    def __init__(self, page):
        self.page = page
        self.username_field = page.locator('[data-test="username"]')
        self.password_field = page.locator('[data-test="password"]')
        self.login_button = page.locator('[data-test="login-button"]')
        self.error_message = page.locator('[data-test="error"]')

    def navigate(self):
        self.page.goto(self.URL)

    def login(self, username: str, password: str):
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()

    def get_error_message(self) -> str:
        return self.error_message.inner_text()

    def is_error_displayed(self) -> bool:
        return self.error_message.is_visible()

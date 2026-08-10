"""Page Object Model for SauceDemo Login Page."""

from playwright.sync_api import Locator, Page


class LoginPage:
    """Page Object Model encapsulating locators and actions for SauceDemo Login Page."""

    URL: str = "https://www.saucedemo.com/"

    def __init__(self, page: Page) -> None:
        self.page: Page = page

        # Locators using data-test attributes for test stability
        self.username_input: Locator = page.locator("[data-test='username']")
        self.password_input: Locator = page.locator("[data-test='password']")
        self.login_button: Locator = page.locator("[data-test='login-button']")
        self.error_message: Locator = page.locator("[data-test='error']")

    def navigate(self) -> None:
        """Navigate to the SauceDemo login page."""
        self.page.goto(self.URL)

    def enter_username(self, username: str) -> None:
        """Fill username input field."""
        self.username_input.fill(username)

    def enter_password(self, password: str) -> None:
        """Fill password input field."""
        self.password_input.fill(password)

    def click_login(self) -> None:
        """Click the login button."""
        self.login_button.click()

    def login(self, username: str, password: str) -> None:
        """Perform complete login workflow."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message_text(self) -> str:
        """Retrieve inner text of the login error message banner."""
        return self.error_message.inner_text()

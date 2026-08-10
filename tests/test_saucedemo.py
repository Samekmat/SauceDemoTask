"""Automated test suite for SauceDemo using Playwright and Page Object Model."""

from playwright.sync_api import Page, expect

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_successful_login(login_page: LoginPage, inventory_page: InventoryPage, page: Page) -> None:
    """Scenario 1: Verify successful login for 'standard_user'."""
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url(InventoryPage.URL)
    expect(inventory_page.title_heading).to_be_visible()
    expect(inventory_page.title_heading).to_have_text("Products")


def test_failed_login_locked_out_user(login_page: LoginPage) -> None:
    """Scenario 2: Verify failed login for 'locked_out_user' with exact error message assertion."""
    login_page.login("locked_out_user", "secret_sauce")

    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_have_text(
        "Epic sadface: Sorry, this user has been locked out."
    )


def test_e2e_add_item_to_cart(login_page: LoginPage, inventory_page: InventoryPage) -> None:
    """Scenario 3: E2E flow - successful login, add specific item to cart, verify badge count."""
    item_name = "Sauce Labs Backpack"

    # Step 1: Perform successful login
    login_page.login("standard_user", "secret_sauce")

    # Step 2: Add item to cart
    expect(inventory_page.title_heading).to_be_visible()
    inventory_page.add_item_to_cart(item_name)

    # Step 3: Verify the cart badge auto-retries and updates to '1'
    expect(inventory_page.cart_badge).to_be_visible()
    expect(inventory_page.cart_badge).to_have_text("1")

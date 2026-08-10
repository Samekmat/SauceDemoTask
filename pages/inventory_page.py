"""Page Object Model for SauceDemo Inventory Page."""

from playwright.sync_api import Locator, Page


class InventoryPage:
    """Page Object Model encapsulating locators and actions for SauceDemo Inventory Page."""

    URL: str = "https://www.saucedemo.com/inventory.html"

    def __init__(self, page: Page) -> None:
        self.page: Page = page

        # Locators
        self.title_heading: Locator = page.locator(".title")
        self.cart_badge: Locator = page.locator(".shopping_cart_badge")
        self.inventory_items: Locator = page.locator(".inventory_item")

    def get_item_by_name(self, item_name: str) -> Locator:
        """Locate an inventory item container by its visible item name using locator filtering."""
        return self.inventory_items.filter(has_text=item_name)

    def add_item_to_cart(self, item_name: str) -> None:
        """Add a specific product to the shopping cart by product name using locator chaining."""
        item_container = self.get_item_by_name(item_name)
        item_container.get_by_role("button", name="Add to cart").click()

    def get_cart_badge_text(self) -> str:
        """Retrieve the current count badge text on the cart icon."""
        return self.cart_badge.inner_text()

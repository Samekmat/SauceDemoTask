"""Pytest configuration and shared fixtures for SauceDemo test suite."""

import pytest
from playwright.sync_api import Page

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    """Fixture initializing LoginPage and performing initial navigation."""
    login_pg = LoginPage(page)
    login_pg.navigate()
    return login_pg


@pytest.fixture
def inventory_page(page: Page) -> InventoryPage:
    """Fixture initializing InventoryPage instance attached to active Playwright page."""
    return InventoryPage(page)

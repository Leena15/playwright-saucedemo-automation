import pytest
import json
import os
from pathlib import Path

FIXTURES_DIR = Path(__file__).parent.parent / "fixtures"


def pytest_runtest_makereport(item, call):
    if call.when == "call" and call.excinfo is not None:
        page = item.funcargs.get("page")
        if page:
            screenshots_dir = Path("reports/screenshots")
            screenshots_dir.mkdir(parents=True, exist_ok=True)
            screenshot_path = screenshots_dir / f"{item.name}.png"
            page.screenshot(path=str(screenshot_path))


@pytest.fixture(autouse=True)
def configure_page(page):
    page.set_default_navigation_timeout(30000)
    page.set_default_timeout(10000)
    yield page


@pytest.fixture(scope="session")
def load_users():
    with open(FIXTURES_DIR / "users.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def load_products():
    with open(FIXTURES_DIR / "products.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def load_checkout_info():
    with open(FIXTURES_DIR / "checkout_info.json") as f:
        return json.load(f)


@pytest.fixture
def logged_in_page(page, load_users):
    from pages.login_page import LoginPage
    login = LoginPage(page)
    login.navigate()
    login.login(
        load_users["standard"]["username"],
        load_users["standard"]["password"]
    )
    return page

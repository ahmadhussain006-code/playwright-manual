from playwright.sync_api import Page

from pages.home_page import HomePage


def test_launch_browser(page: Page) -> None:
    home_page = HomePage(page)
    home_page.open()
    home_page.assert_title(HomePage.PAGE_TITLE)

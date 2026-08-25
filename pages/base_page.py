from playwright.sync_api import Page, Locator, expect


class BasePage:
    """Base page object with shared Playwright interactions."""

    def __init__(self, page: Page) -> None:
        self.page = page

    def navigate_to(self, url: str) -> None:
        """Navigate to the given URL (absolute or relative to base_url)."""
        self.page.goto(url)

    def click_element(self, selector: str) -> None:
        """Click an element identified by selector."""
        self.page.locator(selector).click()

    def fill_element(self, selector: str, text: str) -> None:
        """Fill a text input identified by selector."""
        self.page.locator(selector).fill(text)

    def get_text(self, selector: str) -> str:
        """Return the inner text of an element."""
        return self.page.locator(selector).inner_text()

    def is_visible(self, selector: str) -> bool:
        """Return True if the element is visible."""
        return self.page.locator(selector).is_visible()

    def wait_for_element(self, selector: str, timeout: int = 30000) -> Locator:
        """Wait until the element is visible and return its locator."""
        locator = self.page.locator(selector)
        locator.wait_for(state="visible", timeout=timeout)
        return locator

    def assert_title(self, expected_title: str) -> None:
        """Assert the page title matches the expected value."""
        expect(self.page).to_have_title(expected_title)

    def assert_url(self, expected_url: str) -> None:
        """Assert the current URL matches the expected value."""
        expect(self.page).to_have_url(expected_url)

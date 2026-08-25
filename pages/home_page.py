from pages.base_page import BasePage


class HomePage(BasePage):
    """Page object for the Automation Exercise home page."""

    PAGE_TITLE = "Automation Exercise"
    SIGNUP_LOGIN_LINK = 'a[href="/login"]'

    def open(self) -> None:
        self.navigate_to("/")

    def go_to_signup_login(self) -> None:
        self.click_element(self.SIGNUP_LOGIN_LINK)

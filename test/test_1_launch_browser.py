from playwright.sync_api import sync_playwright

#Playwright's expect() automatically waits for the expected condition.
from playwright.sync_api import expect

"""def is used to create a function in Python. In automation testing, 
   each test case is written inside a function so it can be executed independently by Pytest."""
def test_launch_browser():
   with sync_playwright() as p:
      browser = p.chromium.launch(headless=False)
      context = browser.new_context(viewport={'width': 1920, 'height': 1080})
      page = context.new_page()
      page.goto("https://automationexercise.com/")

      #This is the Professional way to assert the page.
      #Playwright's expect() automatically waits for the expected condition.
      #Suppose the title takes 2 seconds to update.Playwright keeps checking until the title becomes correct (up to the timeout).
      expect(page).to_have_title("Automation Exercise")
      print("Test case passed: Page title is correct.")

      """This is standard approach.
            assert page.title() == "Automation Exercise"
            assert page.locator("text=products").is_visible()
            print("Test case passed: Page title is correct.")

       This is not standard.
            if page.title() == "Automation Exercise":
               print("Test case passed: Page title is correct.")
            else:
               print("Test case failed: Page title is incorrect.")"""












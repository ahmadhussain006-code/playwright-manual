from asyncio import wait

from playwright.sync_api import sync_playwright
from playwright.sync_api import expect

def test_signup():
   with sync_playwright() as p:
       browser = p.chromium.launch(headless=True)
       context = browser.new_context(viewport={"width": 1920, "height": 1080})
       page = context.new_page()

       #launch website
       page.goto("https://automationexercise.com/")

       #Click on Signup/login header menu
       page.wait_for_selector('//a[@href="/login"]').click()
       page.wait_for_timeout(5000)

       #assertion
       expect(page.get_by_text("Login to your account")).to_be_visible()

       #Fill the signup form
       page.wait_for_selector('//input[@type="text"]').fill('Hussain')
       page.wait_for_selector('//input[@data-qa="signup-email"]').fill('sandy25@test.com')
       page.wait_for_selector('//button[@data-qa="signup-button"]').click()

       #assertion
       expect(page.get_by_text("Enter Account Information")).to_be_visible()

       # Fill the signup account information
       title = page.wait_for_selector('//input[@value="Mr"]')
       title.click()

       password = page.wait_for_selector('//input[@name="password"]')
       password.fill("12345")

       select_day = page.select_option('//select[@id="days"]', '24')
       select_month = page.select_option('//select[@id="months"]', '11')
       select_year = page.select_option('//select[@id="years"]', '1991')

       newsletter = page.wait_for_selector('//input[@name="newsletter"]')
       newsletter.click()

       special_offer = page.wait_for_selector('//input[@name="optin"]')
       special_offer.click()

       first_name = page.wait_for_selector('//input[@name="first_name"]')
       first_name.fill("Ahmad")

       last_name = page.wait_for_selector('//input[@name="last_name"]')
       last_name.fill("Hussain")

       company = page.wait_for_selector('//input[@name="company"]')
       company.fill("Mobikasa")

       address = page.wait_for_selector('//input[@name="address1"]')
       address.fill("Delhi, Jasola")

       country = page.select_option('//select[@name="country"]', "India")

       state = page.wait_for_selector('//input[@name="state"]')
       state.fill("uttar pradesh")

       city = page.wait_for_selector('//input[@name="city"]')
       city.fill("Lucknow")

       zipcode = page.wait_for_selector('//input[@name="zipcode"]')
       zipcode.fill("226020")

       mobile_number = page.wait_for_selector('//input[@id="mobile_number"]')
       mobile_number.fill("1234567890")

       page.wait_for_timeout(4000)

       submit_button = page.wait_for_selector('//button[@type="submit"]')
       submit_button.click()

       #assertion
       expect(page.get_by_text("Account Created!")).to_be_visible()
       expect(page).to_have_url("https://automationexercise.com/account_created")

       #cliking on continue shopping_button
       shopping_button = page.wait_for_selector('//a[@data-qa="continue-button"]')
       shopping_button.click()

       # assertion
       expect(page.get_by_text("Logged in as Hussain")).to_be_visible()

       #scroll the page to the bottom (We will use this code, when we need to scroll to the bottom of the page)
       page.evaluate("window.scrollTo(0, document.body.scrollHeight);")

       # We will use this code, when we need to scroll the page to any section or to the bottom.
       # page.locator("footer").scroll_into_view_if_needed()

       # click on bottom to top button
       bottom_to_top_button = page.wait_for_selector('//i[@class="fa fa-angle-up"]')
       bottom_to_top_button.click()


       page.wait_for_timeout(8000)

















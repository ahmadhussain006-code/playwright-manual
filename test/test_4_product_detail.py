from playwright.sync_api import sync_playwright
from playwright.sync_api import expect
import time

def test_product_detail():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(viewport={'width': 1920, 'height': 1080})
        page = context.new_page()
        page.goto("https://automationexercise.com/product_details/30")

        #assertion
        product_image = page.locator('//div[@class="view-product"]')
        expect(product_image).to_be_visible()
        print("product image is visible")

        # write your review
        review_name = page.wait_for_selector('//input[@id="name"]')
        review_name.fill("Hussain")

        review_email = page.wait_for_selector('//input[@id="email"]')
        review_email.fill("test@test.com")

        review_text = page.wait_for_selector('//textarea[@id="review"]')
        review_text.fill("Hussain test")

        submit_button = page.wait_for_selector('//button[@id="button-review"]')
        submit_button.click()

        page.wait_for_timeout(1000)
        # Assert the "Thank you" message appears
        success_message = page.locator("#review-section .alert-success")
        expect(success_message).to_be_visible()
        expect(success_message).to_have_text("Thank you for your review.")

        print("Review submitted successfully - confirmation message verified.")







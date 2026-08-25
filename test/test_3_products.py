from playwright.sync_api import sync_playwright
from playwright.sync_api import expect
import time

def test_products():
    with sync_playwright () as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()

        #launch products page
        page.goto("https://automationexercise.com/products")

        #assertion
        sales_image = page.locator("#sale_image")
        expect(sales_image).to_be_visible()
        print("logo is visible")

        #search field
        search_field = page.wait_for_selector('//input[@name="search"]')
        search_field.fill("polo")

        #click search button
        search_button = page.wait_for_selector('//button[@id="submit_search"]')
        search_button.click()

        #hover on product
        hover = page.wait_for_selector('//div[@class="productinfo text-center"]')
        hover.click()

        #view product
        view_product = page.wait_for_selector('//div[@class="choose"]')
        view_product.click()

        # assertion
        product_image = page.locator('//div[@class="view-product"]')
        expect(product_image).to_be_visible()
        print("product image is visible")

        page.wait_for_timeout(4000)






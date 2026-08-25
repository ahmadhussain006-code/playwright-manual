from playwright.sync_api import sync_playwright

def test_flipcart():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless= True)
        context = browser.new_context(viewport= {'width': 1920, 'height': 1080})
        page = context.new_page()
        page.goto("https://www.flipkart.com/")
        search_field = page.locator('//input[@name="q"]').locator("visible=true")
        search_field.fill("iphone 14")
        page.wait_for_timeout(3000)
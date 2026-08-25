from playwright.sync_api import sync_playwright
from playwright.sync_api import expect

def test_4_view_cart():
    with sync_playwright() as p:
        browser = p.chromium.launch (headless= False)
        context = browser.new_context (viewport= {'width': 1920, 'height': 1080})
        page = context.new_page()
        page.goto("https://automationexercise.com/view_cart")



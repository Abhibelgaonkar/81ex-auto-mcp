import os
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    page = b.new_page()
    page.goto("https://81ex.com")
    page.fill("#email", os.environ["EX_USER"])
    page.fill("#password", os.environ["EX_PASS"])
    page.click("text=Login")
    page.click("text=Accept")  # replace with your recorded clicks
    page.wait_for_timeout(2000)
    page.screenshot(path="result.png")
    b.close()
import os
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    context = b.new_context()
    page = b.new_page()

    try:
        page.goto("https://mobile.81ex01.com/#/login")
        page.get_by_text("Login").click()
        page.get_by_role("button", name="Log in using email").click()
        page.get_by_role("textbox", name="Please enter your email").click()
        page.get_by_role("textbox", name="Please enter your email").fill(os.environ["EX_USER"])
        page.get_by_role("textbox", name="Please enter your password").click()
        page.get_by_role("textbox", name="Please enter your password").fill(os.environ["EX_PASS"])
        page.get_by_role("img").filter(has_text=re.compile(r"^$")).click()
        page.get_by_role("textbox", name="Verification Code").click()
        page.get_by_role("textbox", name="Verification Code").fill("9348")
        page.get_by_role("button", name="Login").click()
        page.get_by_text("Fast transactions").click()
        page.get_by_text("Copy Trading List").click()
    

    # page.fill("#email", os.environ["EX_USER"])
    # page.fill("#password", os.environ["EX_PASS"])
    # page.click("text=Login")
    # page.click("text=Accept")  # replace with your recorded clicks

    finally:
        page.screenshot(path="result.png", full_page=True)
        context.close()
        b.close()
    
    # page.wait_for_timeout(2000)
    # page.screenshot(path="result.png")

    # context.close()
    # b.close()
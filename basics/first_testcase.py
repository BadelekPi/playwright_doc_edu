import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=100)
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.goto("https://www.google.com/")
    page.get_by_role("button", name="Zaakceptuj wszystko").click()
    page.get_by_label("Szukaj", exact=True).click()
    page.get_by_label("Szukaj", exact=True).fill("Playwright")
    page.get_by_label("Szukaj", exact=True).press("Enter")
    page.get_by_role("link", name="Playwright: Fast and reliable").click()
    context.tracing.stop(path="trace.zip")
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

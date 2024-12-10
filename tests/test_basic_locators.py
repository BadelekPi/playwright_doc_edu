import re
from playwright.sync_api import Page, expect

def test_list_node_links(page: Page):
    page.goto("https://bootswatch.com/darkly/")
    locator_link = page.get_by_role("link", name="Card link")
    # Check second locator
    expect(locator_link.nth(1)).to_be_visible()
    # Check last locator
    expect(locator_link.nth(1)).to_be_visible()
    # Check all nodes
    for li in locator_link.all():
        expect(li).to_be_visible()
    # Get array of texts
    texts = locator_link.all_inner_texts()

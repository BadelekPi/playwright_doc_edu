import re
import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(autouse=True)
def navigate_to_page(page: Page):
    page.goto("https://bootswatch.com/darkly/")

def test_list_node_links(page: Page):
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

def test_label_locators(page:Page):
    # page.get_by_label("Email address").fill("test_test@gmail.com")
    # page.get_by_label("Password").fill("secret")
    page.get_by_placeholder("Password").fill("secret")
    page.locator("#floatingPassword")

def test_innet_text_locator(page:Page):
    locator = page.get_by_text("with faded secondary text")
    expect(locator).to_be_visible()

    locator_btn = page.get_by_text("Middle")
    locator_btn.click()
    expect(locator_btn).to_be_enabled()

@pytest.mark.skip_fixture(fixture_name="navigate_to_page")
def test_another_website(page: Page):
    page.goto("https://unsplash.com")
    locator = page.get_by_alt_text("A person holding a memory card in their hand")

def test_title_locator(page: Page):
    locator = page.get_by_title("attribute")

def test_css_selectors(page: Page):
    # Not recommended!

    # Pick every h1 elements
    locator = page.locator("css=h1")

    # Choose button
    locator = page.locator("button.btn-primary")

    # Choose button by ID
    locator = page.locator("button#btnGroupDrop1")

    # Attribute selector
    locator = page.locator("input[value='correct value']")

def test_css_selectors_hierarchy(page: Page):
    # need to look firstly to class above, to select specified area, then to specified element
    locator = page.locator("nav.bg-dark a.nav-link.active")

    # pick item directly under above class
    locator = page.locator("div.bs-component > ul.list-group")

def test_css_selector_pseudo_classes(page: Page):
    locator = page.locator("h1:text('Navbars')")

    # Pick only visible element follow class and name
    locator = page.locator("div.dropdown-menu:visible")

    # Specified 4th button matching follow class
    locator = page.locator(":nth-match(button.btn-primary, 4)")

def test_xpath_locator(page: Page):
    # Select element explicitly
    # /html/head/title

    # double slash means anywhere in the document
    locator = page.locator("xpath=//h1")

    # @ means value
    locator = page.locator("xpath=//h1[@id='navbars']")

    # specified xpath is optional
    locator = page.locator("//input[ @readonly ]")

    locator = page.locator("//input[@value='wrong value']")

    # specified element based on the text
    locator = page.locator("//h1[ text() = 'Heading 1' ]")
    locator = page.locator("//h1[ contains(text(), 'Head') ]")

    # specified by class name
    locator = page.locator("//h1[ contains(@class, 'btn-outline-primary') ]")

    # specified by value
    locator = page.locator("//input[ contains(@value, 'correct') ]")

def test_other_selectors(page: Page):

    # order selectors, append locators
    locator = page.get_by_role("button", name="Primary").locator("nth=1")

    # parent locator, like parent directory
    locator = page.get_by_label("Email address").locator("..")

    # keyword
    page.locator("div.dropdown-menu").locator("visible=false")

    # certain element
    locator = page.get_by_role("heading").filter(has_text="Heading")

    # filter inside group
    page.locator("div.form-group").filter(has=page.get_by_label("Password"))


def test_mouse_actions(page: Page):
    locator_btn = page.get_by_role("button", name="Block button").first
    page.locator("footer").highlight()
    locator_btn.click()
    locator_btn.dblclick()
    locator_btn.dblclick(delay=500)
    locator_btn.click(button="right")
    locator_btn.click(modifiers=["Shift", "Alt"])
    
    outline_button = page.locator("button.btn-outline-primary")
    
    outline_button.hover()


def test_input_field_actions(page: Page):
    page.get_by_label("Email address")

    page.locator("footer")
    input = page.get_by_placeholder("Enter email")
    input.fill("me@that.site")
    input.clear()

    input.type("me@that.site")

    # delay between every char
    input.type("me@that.site", delay=200)

    valid_input = page.get_by_label("Valid input")
    
    # return value stored by field
    store_val = valid_input.input_value()

def test_radio_button(page: Page):
    # check method to select radio button
    radio_option2 = page.get_by_label("Option two can be something else and selecting it will deselect option one")
    radio_option2.check()

    radio_option1 = page.get_by_label("Option one is this and that—be sure to include why it's great")
    radio_option1.check()

def test_checkboxes(page: Page):
    # select the same as radio buttons
    checkbox = page.get_by_label("Default checkbox")
    checkbox.check()

    expect(checkbox).to_be_checked()

    # deselect this checkbox
    checkbox.uncheck()
    expect(checkbox).not_to_be_checked()

    checkbox.set_checked(True)

    # after double click, normal behaviour - uncheck checkbox
    checkbox.click()
    checkbox.click()
    expect(checkbox).not_to_be_checked()

def test_switches(page: Page):
    switch = page.get_by_label("Checked switch checkbox input")
    switch.uncheck()
    switch.check()

    










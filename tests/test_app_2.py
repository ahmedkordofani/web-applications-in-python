import pytest
from playwright.sync_api import Page, expect


# Your test function
def test_get_goodbye(page, test_web_address):
    page.goto(f"{test_web_address}/goodbye")
    strong_tag = page.locator("strong")
    expect(strong_tag).to_have_text("Bye!")




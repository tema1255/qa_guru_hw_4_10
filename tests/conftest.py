import pytest
from selene import browser

@pytest.fixture
def browser_setup():
    browser.config.window_width = 1280
    browser.config.window_height = 768
    browser.config.hold_browser_open = True
    browser.config.base_url = 'https://demoqa.com'
    yield
    browser.quit()

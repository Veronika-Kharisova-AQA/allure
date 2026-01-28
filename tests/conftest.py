import pytest
from selene import browser


@pytest.fixture(autouse=True)
def browser_setup():
    browser.config.browser_name = 'chrome'
    browser.config.window_width = '1200'
    browser.config.window_height = '900'
    browser.config.timeout = 10

    yield
    browser.quit()
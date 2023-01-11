import pytest
from selene import have, command
from selene.support.shared import browser


@pytest.fixture(scope="function", autouse=True)
def open_browser():
    browser.config.base_url = 'https://demoqa.com'
    #browser.config.window_height = 900
    #browser.config.window_width = 1600

    yield
    browser.quit()

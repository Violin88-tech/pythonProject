from selene.support.shared import browser
from selene import be, have
import pytest


@pytest.fixture
def browser_size():
    browser.driver.set_window_size(height=2560, width=1440)
    yield
    browser.quit()

def test_google_selene():

    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_google():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('tghdsjdkiuefdgf').press_enter()
    browser.element('[div#result-stats"]').should(have.text('Результатов: примерно 0'))




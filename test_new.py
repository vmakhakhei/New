import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture
def browser_size():
    browser.config.window_width = 900
    browser.config.window_height = 1600
    browser.open('https://duckduckgo.com')

def test_positive_search(browser_size):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[data-testid="result"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python - GitHub'))

def test_negavite_search(browser_size):
    browser.element('[name="q"]').should(be.blank).type('olololkqwkew').press_enter()
    browser.element('[id="links_wrapper"]').should(have.text('По запросу olololkqwkew результаты не найдены.'))


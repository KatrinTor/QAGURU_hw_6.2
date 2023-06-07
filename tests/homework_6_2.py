from selene.support.shared import browser
from selene import be, have


def test_succsesful_search():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
    print("По запросу найдена ссылка")

def test_failed_search():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('gjgcxTYYddccv').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
    print("По запросу ничего не найдено")
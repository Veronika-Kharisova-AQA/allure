import allure
from selene import browser, have
from selene.support.shared.jquery_style import ss, s


@allure.step('Перейти на вкладку issue в репозитории')
def open_issue_page(repo):
    browser.open(f'https://github.com/{repo}/issues')

@allure.step('Перейти в issue {expected_title}')
def open_issue_by_title(expected_title):
    ss('[data-testid="issue-pr-title-link"]').element_by(
        have.exact_text(expected_title)
    ).click()

def should_have_issue_title(expected_title):
    s('[data-testid="issue-title"]').should(
        have.exact_text(expected_title)
    )

@allure.title('Проверка заголовка issue')
@allure.tag('Web', 'GitHub', 'Issues')
@allure.severity(allure.severity_level.CRITICAL)
@allure.label('Owner', 'Veronika')
@allure.feature('GitHub Issues')
@allure.story('Просмотр информации об Issue')
@allure.link('https://github.com/Veronika-Kharisova-AQA/allure')
def test_issue_title_is_visible():
    repo = 'Veronika-Kharisova-AQA/allure'
    expected_title = 'Test issue A'

    open_issue_page(repo)
    open_issue_by_title(expected_title)
    should_have_issue_title(expected_title)



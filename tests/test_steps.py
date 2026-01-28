import allure
from selene import browser, have
from selene.support.shared.jquery_style import s


def test_issue_title_is_visible():
    repo = 'Veronika-Kharisova-AQA/allure'
    expected_title = 'Test issue A'

    with allure.step('Перейти на вкладку issues в репозитории'):
        browser.open(f'https://github.com/{repo}/issues')

    with allure.step(f'Переходим в issue {expected_title}'):
        browser.all('[data-testid="issue-pr-title-link"]').element_by(
            have.exact_text(expected_title)
        ).click()

    with allure.step(f'Проверка заголовка issue {expected_title}'):
        s('[data-testid="issue-title"]').should(
            have.exact_text(expected_title)
        )

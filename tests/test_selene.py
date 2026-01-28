from selene import browser, have


def test_issue_title_is_visible():
    repo = 'Veronika-Kharisova-AQA/allure'
    expected_title = 'Test issue A'

    browser.open(f'https://github.com/{repo}/issues')

    # переходим в issue
    browser.all('[data-testid="issue-pr-title-link"]').element_by(
        have.exact_text(expected_title)
    ).click()

    # проверка заголовка issue
    browser.element('[data-testid="issue-title"]').should(
        have.exact_text(expected_title)
    )

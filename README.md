**Allure Reports** — фреймворк для формирования отчётов о прохождении авто тестов. 
Преимущество Allure Reports перед другими фреймворками в том, что он не зависит от языка программирования
и его можно подключить к любому окружению.
___
### Лямбда степы
Разметка сценария в Allure Reports производится с помощью with allure.step('Описание то делает шаг'). 
Это позволяет разбить тест на логические части и добавить к нему описание.
~~~
def test_example():
    with allure.step("Открываем главую страницу GitHub")
        browser.open("https://github.com")
        
    with allure.step("Ищем репозиторий eroshenkoam/allure-example")
        s(".header-search-input").click()
        s(".header-search-input").send_keys(repo)
        s(".header-search-input").submit()
~~~
### Шаги с декоратором @allure.step
Также есть другой способ оформить разметку сценария. Для этого каждый осмысленный и завершённый шаг теста мы оформим в виде отдельной функции, а после вызовем каждый шаг в главной функции. 
Такой подход можно назвать некоторым видом Page Object. Также это помогает переиспользовать код.
~~~
def test_decorator_steps():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_issue_tab()
    should_see_issue_with_number("#76")


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("https://github.com")


@allure.step("Ищем репозиторий {repo}")
def search_for_repository(repo):
    s(".header-search-input").click()
    s(".header-search-input").send_keys(repo)
    s(".header-search-input").submit()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step("Открываем таб Issues")
def open_issue_tab():
    s("#issues-tab").click()


@allure.step("Проверяем наличие Issue с номером {number}")
def should_see_issue_with_number(number):
    s(by.partial_text(number)).click()
~~~

### Добавляем аттачменты
Отчёты можно сопровождать дополнительными материалами и комментариями, которые могут помочь анализировать их состояние.
~~~def test_attachments():
    # Текст
    allure.attach("Text content", name="Text", attachment_type=attachment_type.TEXT)

    # HTML
    allure.attach("<h1>Hello, world</h1>", name="Html", attachment_type=attachment_type.HTML)

    # JSON
    allure.attach(json.dumps({"first": 1, "second": 2}), name="Json", attachment_type=attachment_type.JSON)
~~~
### Добавляем лейблы/аннотации
Также тесты можно оформить другой служебной информацией, которая удобно сгруппируется в отчёте Allure:
~~~
def test_no_labels():
    pass


## Первый способ
def test_dynamic_labels():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Задачи в репозитории")
    allure.dynamic.story("Неавторизованный пользователь не может создать задачу в репозитории")
    allure.dynamic.link("https://github.com", name="Testing")
    pass


## Второй способ
@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "eroshenkoam")
@allure.feature("Задачи в репозитории")
@allure.story("Авторизованный пользователь может создать задачу в репозитории")
@allure.link("https://github.com", name="Testing")
def test_decorator_labels():
    pass
 ~~~
___
- Для генерации отчётов в терминале необходимо выполнить команду allure serve [directory]. Вместо [directory] следует подставить путь до директории, в которой у нас лежат результаты отчётов, к примеру tests/allure-results
from selenium.webdriver import Chrome

import pytest


@pytest.fixture(scope="session")
def driver() -> Chrome:
    driver = Chrome("/home/masha/PycharmProjects/HomeworkQAPyton/homework_18/driver")
    driver.maximize_window()
    driver.get("https://ru.wikipedia.org/")
    yield driver
    driver.quit()


@pytest.fixture
pass

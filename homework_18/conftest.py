from selenium.webdriver import Chrome

import pytest


@pytest.fixture(scope="session")
def driver() -> Chrome:
    driver = Chrome("/home/masha/PycharmProjects/HomeworkQAPyton/homework_18/driver")
    driver.maximize_window()
    yield driver
    driver.quit()


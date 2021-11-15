from selenium.webdriver import Chrome
import pytest
from homework_19.page_object import Dashboard


@pytest.fixture(scope="session")
def driver() -> Chrome:
    driver = Chrome("C:\drivers\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://goodwine.com.ua/")
    yield driver
    driver.quit()


@pytest.fixture
def dashboard(driver):
    yield Dashboard(driver)

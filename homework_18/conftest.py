from selenium.webdriver import Chrome
import pytest


@pytest.fixture(scope="session")
def driver() -> Chrome:
    driver = Chrome("C:\drivers\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://goodwine.com.ua/")
    yield driver
    driver.quit()

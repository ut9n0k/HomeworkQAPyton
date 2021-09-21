from typing import Tuple

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self.__web_driver_wait = WebDriverWait(self._driver, 7)

    def _click(self, locator: Tuple[By, str]) -> WebElement:
        pass

    def _searching(self, locator: Tuple[By, str]):
        pass
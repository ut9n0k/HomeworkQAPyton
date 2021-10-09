from typing import Tuple

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self._driver = driver

    def _find_element(self, locator, time=7):
        return WebDriverWait(self._driver, time).until(EC.presence_of_element_located(locator))

    def _click(self, locator: Tuple[By, str]) -> None:
        self._find_element(locator).click()

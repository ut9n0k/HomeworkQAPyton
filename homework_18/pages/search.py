from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from homework_18.core.page_singleton import singleton
from homework_18.pages.base_page import BasePage


@singleton
class Search(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.__search_locator = (By.XPATH, "//*[@id='searchInput']")


    def search_input(self, text: str):
        self._click(())
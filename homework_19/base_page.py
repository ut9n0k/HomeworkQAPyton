from selenium.webdriver.chrome.webdriver import WebDriver
from homework_19.cookie import Cookie
from homework_19.local_storage import LocalStorage


class BasePage:
    def __init__(self, driver: WebDriver, webdriver_cookie: WebDriver, webdriver_local_storage: WebDriver):
        self.__driver = driver
        self.__cookie = Cookie(webdriver_cookie)
        self.__local_storage = LocalStorage(webdriver_local_storage)

    @property
    def cookies(self) -> Cookie:
        return self.__cookie

    @property
    def local_storage(self) -> LocalStorage:
        return self.__local_storage

from selenium.webdriver.chrome.webdriver import WebDriver


class Cookie:
    def __init__(self, webdriver_cookie: WebDriver):
        self.__webdriver_cookie = webdriver_cookie

    def return_webdriver_cookies(self):
        print(f"COOKIE: {self.__webdriver_cookie.get_cookies()}")

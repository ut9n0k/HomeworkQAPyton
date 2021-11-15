from selenium.webdriver.chrome.webdriver import WebDriver


class LocalStorage:
    def __init__(self, webdriver_local_storage: WebDriver):
        self.__webdriver_local_storage = webdriver_local_storage

    def return_webdriver_local_storage(self):
        local_storage = self.__webdriver_local_storage.execute_script("return window.localStorage;")
        print(f"LOCAL STORAGE: {local_storage}")

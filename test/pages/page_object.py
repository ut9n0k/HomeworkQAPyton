from test.pages.BaseApp import BasePage
from selenium.webdriver.common.by import By


class GoodWineLocators:
    SEARCH_LOCATOR = (By.XPATH, "//input[@placeholder='Искать среди 4000 вин и 1000 виски...']")
    ADD_TO_CART_BUTTON_LOCATOR = (By.XPATH,
                                  "//*[@id='am_search_popup']/div/div[1]/a[1]/div/div[2]/div[3]/div[2]/button"
                                  )


class Search(BasePage):
    def search_input(self, word):
        search_field = self._find_element(GoodWineLocators.SEARCH_LOCATOR)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def add_to_cart(self):
        cart_button = self._find_element(GoodWineLocators.ADD_TO_CART_BUTTON_LOCATOR)
        cart_button.click()


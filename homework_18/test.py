import time
from pages.page_object import Search


def test_search_and_adding_to_cart(driver):
    search = Search(driver)
    search.search_input("Виски Laphroaig")
    search.add_to_cart()
    time.sleep(5)

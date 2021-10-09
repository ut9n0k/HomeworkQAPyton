import time
from homework_18.page_object import Search


def test_search_and_adding_to_cart(driver):
    search = Search(driver)
    time.sleep(3)
    search.search_input("Виски Laphroaig")
    time.sleep(3)
    search.add_to_cart()
    time.sleep(5)

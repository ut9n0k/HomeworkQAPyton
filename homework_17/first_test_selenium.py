# Создать тест в котором происходит инициализация драйвера.
# Перейдите на любой выбранный вами ресурс.
# Нажмите на кнопку либо введите текст в поле ввода.
# В этом же тесте попробуйте реализовать скролинг в окне где есть скрол бар
import time
from selenium.webdriver import Chrome


def test_1st():
    driver = Chrome("/home/masha/PycharmProjects/HomeworkQAPyton/homework_17/drivers/chromedriver")
    search_textbox_locator = "//input[@placeholder='Искать среди 4000 вин и 1000 виски...']"
    add_to_cart_button_locator = "//*[@id='am_search_popup']/div/div[1]/a[1]/div/div[2]/div[3]/div[2]/button"

    """
        Driver inicialization & full-screen opening
    """
    driver.get("https://goodwine.com.ua/")
    from selenium.webdriver.remote.webelement import WebElement

    """
        Input in search textbox
    """
    search_textbox: WebElement = driver.find_element_by_xpath(search_textbox_locator)
    search_textbox.send_keys("Виски Laphroaig")
    time.sleep(3)

    """
        Adding to own cart the product
    """
    add_to_cart_button: WebElement = driver.find_element_by_xpath(add_to_cart_button_locator)
    add_to_cart_button.click()
    time.sleep(3)

    driver.quit()

    # Unfortunately, I didn't find scrollbox on the site;C

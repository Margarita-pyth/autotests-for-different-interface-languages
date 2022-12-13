import time

from selenium.webdriver.common.by import By

link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_the_basket_link(browser):
    browser.get(link)
    time.sleep(20)
    basket_link = browser.find_elements(By.CSS_SELECTOR, "span.btn-group a")
    assert len(basket_link) == 1 , "Нет кнопки корзины"

# pytest --language=es команда запуска скрипта (по умолчанию выполнение в Chrome)





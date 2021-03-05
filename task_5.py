from selenium import webdriver
from selenium.webdriver.common.by import By
import time

login = "admin"

# Проверка тэгов у каждой уточки


def open_browser(driver):
    driver.get("http://localhost/litecart/public_html/admin/")
    driver.find_element_by_name("username").send_keys(login)
    driver.find_element_by_name("password").send_keys(login)
    driver.find_element_by_name("login").click()
    driver.get("http://localhost/litecart/public_html/en/")
    time.sleep(3)


#driver = webdriver.Chrome()
driver = webdriver.Firefox()
open_browser(driver)

products = driver.find_elements_by_css_selector(".listing-wrapper.products li")
for i in products:
    cart = i.find_element_by_css_selector(".name")
    type_cart = i.find_elements_by_css_selector(".sticker")
    if len(type_cart) != 1:
        print(cart.text + "has " + str(len(type_cart) + "types."))
    else:
        print(cart.text + " has only " +
              str(len(type_cart)) + " type: " + str(type_cart[0].text))


driver.quit()

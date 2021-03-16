from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from random import choice
from string import ascii_uppercase
import time


def open_browser():
    driver.get("http://localhost/litecart/public_html/en/")
    time.sleep(3)


Exception


def are_elements_present(driver, locator):
    wait = WebDriverWait(driver, 0)
    return (driver.find_elements_by_css_selector(locator))


driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# driver = webdriver.Ie()
open_browser()
i = 1

while i < 4:
    driver.find_element_by_css_selector("#box-most-popular .content a").click()
    if (are_elements_present(driver, ".options select")):
        selector = Select(
            driver.find_element_by_css_selector(".options select"))
        selector.select_by_index(1)
    wait = WebDriverWait(driver, 10)
    driver.find_element_by_css_selector("[name=add_cart_product").click()
    wait.until(EC.text_to_be_present_in_element(
        (By .CSS_SELECTOR, "#cart .content .quantity"), str(i)))
    i = i+1
    driver.back()

driver.find_element_by_css_selector("#cart-wrapper .content ~ .link").click()
i = 0
rows = len(driver.find_elements_by_css_selector(
    ".dataTable  .header~tr .item"))

while rows != 0:
    button = driver.find_element_by_css_selector("[name=remove_cart_item]")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of(button))
    button.click()
    time.sleep(1)

    rows = len(driver.find_elements_by_css_selector(
        ".dataTable .header~tr .item"))

if rows == 0:
    print("Утки удалены из корзины")
driver.close()

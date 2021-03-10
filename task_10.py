from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Проход по всем разделам на сайте


def open_browser():
    driver.get("http://localhost/litecart/public_html/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.get(
        "http://localhost/litecart/public_html/en/")
    time.sleep(3)


driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver = webdriver.Ie()
open_browser()

driver.find_element_by_css_selector("#box-campaigns .link").click()
print(driver.find_element_by_css_selector(".regular-price").text)
# driver.close()

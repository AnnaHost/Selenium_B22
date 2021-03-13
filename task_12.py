from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from random import choice
from string import ascii_uppercase
from selenium.webdriver.support.select import Select
import time

# Проход по всем разделам на сайте
email_str = ''.join(choice(ascii_uppercase) for i in range(12)) + "@ya.ru"
password_str = "1q2w3e4r5t"


def open_browser():
    driver.get("http://localhost/litecart/public_html/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.get(
        "http://localhost/litecart/public_html/admin/?app=catalog&doc=catalog")

    time.sleep(3)


def add_duck():
    driver.find_element_by_css_selector("#content a:nth-child(2)").click()
    general = driver.find_element_by_css_selector("#tab-general")
    print(general.find_element_by_css_selector("name=code"))
    time.sleep(2)


driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver = webdriver.Ie()
open_browser()
add_duck()

# driver.close()

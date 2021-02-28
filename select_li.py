from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def open_browser(driver):
    driver.get("http://localhost/litecart/public_html/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    time.sleep(3)


def are_elements_present(driver, *args):
    return len(driver.find_elements(*args)) > 0


driver = webdriver.Chrome()
open_browser(driver)

objects = driver.find_elements_by_id("app-")
enum_objects = len(objects)

i = 0
while i < enum_objects:
    objects[i].click()
    sub_elements = driver.find_elements_by_css_selector("li[id*=doc]")
    j = 0
    while j < len(sub_elements):
        sub_elements[j].click()
        print(are_elements_present(driver, By.TAG_NAME, "h1"))
        sub_elements = driver.find_elements_by_css_selector("li[id*=doc]")
        j = j + 1
        time.sleep(1)
    i = i+1
    objects = driver.find_elements_by_id("app-")
    time.sleep(1)


driver.quit()

# 2-ой нерабочий вариант
'''
for obj in objects:
    obj.click()
    sub_objects = driver.find_elements_by_css_selector("li[id*=doc]")
    for sub_obj in sub_objects:
        sub_obj.click()
        print(are_elements_present(driver, By.TAG_NAME, "h1"))
        time.sleep(1)
'''

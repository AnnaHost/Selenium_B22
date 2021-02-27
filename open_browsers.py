from selenium import webdriver
import time


def open_browser(driver):
    driver.get("http://localhost/litecart/public_html/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    time.sleep(5)
    driver.quit()


driver = webdriver.Chrome()
open_browser(driver)
#ie_driver = webdriver.Ie()
# open_browser(ie_driver)
firefox_driver = webdriver.Firefox()
open_browser(firefox_driver)

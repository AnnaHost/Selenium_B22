from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from random import choice
from string import ascii_uppercase
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        "http://localhost/litecart/public_html/admin/?app=countries&doc=countries")
    driver.find_element_by_css_selector("#content div a").click()
    time.sleep(3)


def check_links():
    wait = WebDriverWait(driver, 10)
    original_window = driver.current_window_handle
    links = driver.find_elements_by_css_selector(".fa-external-link")
    for i in links:
        old_windows = driver.window_handles
        i.click()
        wait.until(EC.number_of_windows_to_be(2))
        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                time.sleep(1)
                print("New tab: " + driver.title)

                driver.close()
                driver.switch_to.window(original_window)
                break

        links = driver.find_elements_by_css_selector(".fa-external-link")


options1 = webdriver.ChromeOptions()
options1.add_argument('--ignore-certificate-errors')
options1.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(options=options1)
#profile = webdriver.FirefoxProfile()
#profile.accept_untrusted_certs = True
#driver = webdriver.Firefox()

open_browser()
check_links()

driver.close()

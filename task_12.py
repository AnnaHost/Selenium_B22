from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from random import choice
import os
from string import ascii_letters
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def random_str():
    return (''.join(choice(ascii_letters) for i in range(12)))


def open_browser():
    driver.get("http://localhost/litecart/public_html/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.get(
        "http://localhost/litecart/public_html/admin/?app=catalog&doc=catalog")
    time.sleep(2)


def filling_first_tab():
    time.sleep(2)
    driver.find_element_by_css_selector(".tabs .index li:nth-child(1)").click()
    wait.until(EC.visibility_of(
        driver.find_element_by_css_selector("#tab-general table input:nth-child(2)")))
    name = driver.find_element_by_css_selector(
        "#tab-general table input:nth-child(2)")
    name.send_keys(random_str())
    driver.find_element_by_css_selector(
        "#tab-general > table > tbody > tr:nth-child(7) > td > div > table > tbody > tr:nth-child(2) > td:nth-child(1) > input[type=checkbox]").click()
    driver.find_element_by_css_selector(
        ".content table [name=quantity]").send_keys(Keys.HOME + "1")
    driver.find_element_by_css_selector(
        "input[type='file']").send_keys(os.path.realpath('1.jpg'))
    driver.find_element_by_css_selector(
        "input[name='date_valid_from']").send_keys(Keys.HOME + "10.10.2000")
    driver.find_element_by_css_selector(
        "input[name='date_valid_to']").send_keys(Keys.HOME + "10.10.2025")
    time.sleep(1)


def filling_second_tab():
    driver.find_element_by_css_selector(".tabs .index li:nth-child(2)").click()
    wait.until(EC.visibility_of(
        driver.find_element_by_css_selector("[name=manufacturer_id]")))
    first_select = Select(
        driver.find_element_by_css_selector("[name=manufacturer_id]"))
    first_select.select_by_index(1)
    edits = driver.find_elements_by_css_selector(
        "#tab-information table input")
    for input_edit in edits:
        input_edit.send_keys(random_str())
    driver.find_element_by_css_selector(
        ".trumbowyg-editor").send_keys(random_str())


def filling_last_tab():
    time.sleep(2)
    driver.find_element_by_css_selector(".tabs .index li:nth-child(4)").click()
    driver.find_element_by_css_selector(
        "input[name='purchase_price']").send_keys(Keys.HOME + "1")
    Select(
        driver.find_element_by_css_selector("select[name='purchase_price_currency_code']")).select_by_index(1)
    driver.find_element_by_css_selector(
        "input[name='prices[USD]']").send_keys("15")
    driver.find_element_by_css_selector(
        "input[name='prices[EUR]']").send_keys("20")
    time.sleep(1)


#driver = webdriver.Chrome()
driver = webdriver.Firefox()
# driver = webdriver.Ie()
open_browser()
old_rows = len(driver.find_elements_by_css_selector(".row"))
wait = WebDriverWait(driver, 10)
driver.find_element_by_css_selector("#content a:nth-child(2)").click()
filling_first_tab()
filling_second_tab()
filling_last_tab()
driver.find_element_by_css_selector("button[type='submit']").click()

current_rows = len(driver.find_elements_by_css_selector(".row"))
if current_rows > old_rows:
    print("Товар добавлен")
driver.close()

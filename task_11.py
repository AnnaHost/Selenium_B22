from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from random import choice
from string import ascii_uppercase
import time

# Проход по всем разделам на сайте
email_str = ''.join(choice(ascii_uppercase) for i in range(12)) + "@ya.ru"
password_str = "1q2w3e4r5t"


def open_browser():
    # driver.get("http://localhost/litecart/public_html/admin/")
    # driver.find_element_by_name("username").send_keys("admin")
    # driver.find_element_by_name("password").send_keys("admin")
    # driver.find_element_by_name("login").click()
    driver.get(
        "http://localhost/litecart/public_html/en/")
    time.sleep(3)


def registration_form():
    time.sleep(1)
    tax_id = driver.find_element_by_css_selector("[name=tax_id]")
    tax_id.send_keys("1234")
    time.sleep(1)
    company = driver.find_element_by_css_selector("[name=company]")
    company.send_keys("222")
    time.sleep(1)
    firstname = driver.find_element_by_css_selector("[name=firstname]")
    firstname.send_keys("Anna")
    time.sleep(1)
    lastname = driver.find_element_by_css_selector("[name=lastname]")
    lastname.send_keys("Host")
    time.sleep(1)
    postcode = driver.find_element_by_css_selector("[name=postcode]")
    postcode.send_keys("225844")
    time.sleep(1)
    city = driver.find_element_by_css_selector("[name=city]").send_keys("City")
    time.sleep(1)
    address1 = driver.find_element_by_css_selector(
        "[name=address1]").send_keys("some states 123")
    time.sleep(1)
    email = driver.find_element_by_css_selector(
        "[name=email]").send_keys(email_str)
    time.sleep(1)
    phone = driver.find_element_by_css_selector(
        "[name=phone]").send_keys(Keys.HOME + "+7125487")
    time.sleep(1)
    password = driver.find_element_by_css_selector(
        "[name=password]").send_keys(password_str)
    time.sleep(1)
    confirmed_password = driver.find_element_by_css_selector(
        "[name=confirmed_password]").send_keys(password_str)
    time.sleep(1)
    driver.find_element_by_css_selector("[name=create_account]").click()


def login():
    driver.find_element_by_css_selector("[name=email]").send_keys(email_str)
    driver.find_element_by_css_selector(
        "[name=password]").send_keys(password_str)
    driver.find_element_by_css_selector("[name=login]").click()


driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver = webdriver.Ie()
open_browser()

registration_link = driver.find_element_by_css_selector(
    "[name=login_form] tr:nth-child(5)").click()
registration_form()
time.sleep(1)
driver.find_element_by_css_selector(".list-vertical li:nth-child(4) a").click()
time.sleep(1)
login()
driver.find_element_by_css_selector(".list-vertical li:nth-child(4) a").click()
# driver.close()

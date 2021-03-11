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
        "http://localhost/litecart/public_html/admin/?app=countries&doc=countries")
    time.sleep(3)


def sorted_table():
    table = driver.find_element_by_class_name("dataTable")
    names = table.find_elements_by_css_selector(".row td:nth-child(5)")
    mass = []

    for i in names:
        mass.append(i.text)

    sort_mass = sorted(mass)
    sorted_mass = True
    i = 0

    while i < len(mass):
        if mass[i] != sort_mass[i]:
            sorted_mass = False
            break
        i = i + 1

    if sorted_mass:
        print("Список стран отсортирован")
    else:
        print("Список стран не отсортирован")


def sorted_geozone():
    table = driver.find_element_by_class_name("dataTable")
    names = table.find_elements_by_css_selector(".row")
    count = len(names)
    i = 0
    mass = []
    while i < count:
        zones = names[i].find_element_by_css_selector("td:nth-child(6)")
        if int(zones.text) != 0:
            names[i].find_element_by_css_selector("td:nth-child(5) a").click()
            check_geozones()
            time.sleep(3)
            driver.get(
                "http://localhost/litecart/public_html/admin/?app=countries&doc=countries")
            table = driver.find_element_by_class_name("dataTable")
            names = table.find_elements_by_css_selector(".row")
            count = len(names)
        i = i+1


def check_geozones():
    names = driver.find_elements_by_css_selector(
        ".dataTable td:nth-child(3) input")
    mass = []
    for i in names:
        if ((i.get_attribute("type")) == "hidden"):
            mass.append(i.text)

    sort_mass = sorted(mass)
    sorted_mass = True
    i = 0
    while i < len(mass):
        if mass[i] != sort_mass[i]:
            sorted_mass = False
            break
        i = i + 1
    curr_counrty = driver.find_element_by_css_selector(
        "table #content  tr:nth-child(4) strong ~ input ").get_attribute("value")
    if sorted_mass:
        print("Список геозон отсортирован для страны " + curr_counrty)
    else:
        print("Список геозон не отсортирован")


driver = webdriver.Chrome()
open_browser()
sorted_table()
sorted_geozone()

driver.close()

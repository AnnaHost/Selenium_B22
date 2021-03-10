from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Проход по всем разделам на сайте


def open_browser():
    # driver.get("http://localhost/litecart/public_html/admin/")
    # driver.find_element_by_name("username").send_keys("admin")
    # driver.find_element_by_name("password").send_keys("admin")
    # driver.find_element_by_name("login").click()
    driver.get(
        "http://localhost/litecart/public_html/en/")
    time.sleep(3)


def formate_price(price):
    return int(price[1:])


def compare(L, R, type_compare):
    if L == R:
        print("Значения: \"" + type_compare + "\" совпадают.")
    elif L > R:
        print("Значение \" " + type_compare + "\"" +
              str(L) + "больше чем " + str(R))
    else:
        print("Значение \"" + type_compare + "\"" +
              str(L) + "меньше чем " + str(R))


driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# driver = webdriver.Ie()
open_browser()

curr_duck = driver.find_element_by_css_selector("#box-campaigns .link")

# 1 duck
# campaign_price
name_curr_duck = curr_duck.find_element_by_class_name("name").text
campaign_price = curr_duck.find_element_by_class_name("campaign-price")
formatted_campaign_price = formate_price(campaign_price.text)
font_weight_campaign_price = int(campaign_price.value_of_css_property(
    "font-weight"))
font_color_campaign_price = campaign_price.value_of_css_property("color")
font_size_campaign_price = float(campaign_price.value_of_css_property(
    "font-size").replace("px", ''))
# regular_price
regular_price = curr_duck.find_element_by_class_name("regular-price")
formatted_regular_price = formate_price(regular_price.text)
font_decoration_regular_price = regular_price.value_of_css_property(
    "text-decoration-line")
font_color_regular_price = regular_price.value_of_css_property("color")
font_size_regular_price = float(regular_price.value_of_css_property(
    "font-size").replace("px", ''))


curr_duck.click()
# 2 duck
duck = driver.find_element_by_id("box-product")
name_duck = duck.find_element_by_class_name("title").text

campaign_price_duck = formate_price(
    duck.find_element_by_class_name("campaign-price").text)
regular_price_duck = formate_price(
    duck.find_element_by_class_name("regular-price").text)
if name_duck == name_curr_duck:
    print("Названия совпадают: " + name_duck)
# пункт б
if (formatted_campaign_price == campaign_price_duck) and (formatted_regular_price == regular_price_duck):
    print("Размеры цен совпадают")
# пункт в

if (font_decoration_regular_price == "line-through"):  # todo font_color_campaign_price
    print("Обычная цена серая и зачеркнутая")
# пункт г
if (font_weight_campaign_price >= 700):  # todo font_color_regular_price
    print("Акционная цена красная и жирная")
# пункт д
if (font_size_campaign_price > font_size_regular_price):
    print("Размер акционной цены крупнее обычной, на главной странице")

driver.close()

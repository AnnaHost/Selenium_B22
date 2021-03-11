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


def slpit_rgba(rgba_string):
    curr_string = ""
    if 'rgba' in rgba_string:
        curr_string = rgba_string.replace("rgba(", '')
    else:
        curr_string = rgba_string.replace("rgb(", '')
    curr_string = curr_string.replace(")", '')
    curr_string = curr_string.replace(" ", '')
    curr = curr_string.split(",")
    return curr


#driver = webdriver.Chrome()
#driver = webdriver.Firefox()
driver = webdriver.Ie()
open_browser()

curr_duck = driver.find_element_by_css_selector("#box-campaigns .link")

# 1 duck
# campaign_price
name_curr_duck = curr_duck.find_element_by_class_name("name").text
campaign_price = curr_duck.find_element_by_class_name("campaign-price")
formatted_campaign_price = formate_price(campaign_price.text)
font_weight_campaign_price = int(campaign_price.value_of_css_property(
    "font-weight"))
font_color_campaign_price = slpit_rgba(campaign_price.value_of_css_property(
    "color"))
font_size_campaign_price = float(campaign_price.value_of_css_property(
    "font-size").replace("px", ''))

# regular_price
regular_price = curr_duck.find_element_by_class_name("regular-price")
formatted_regular_price = formate_price(regular_price.text)
font_decoration_regular_price = regular_price.get_attribute("outerHTML")[1:2]
font_color_regular_price = slpit_rgba(
    regular_price.value_of_css_property("color"))
font_size_regular_price = float(regular_price.value_of_css_property(
    "font-size").replace("px", ''))

curr_duck.click()

# 2 duck
time.sleep(3)
duck = driver.find_element_by_css_selector("#box-product")
name_duck = duck.find_element_by_class_name("title").text
# campaign_price
campaign = duck.find_element_by_class_name("campaign-price")

campaign_price_duck = formate_price(campaign.text)
font_weight_campaign_price_duck = int(campaign.value_of_css_property(
    "font-weight"))
font_size_campaign_price_duck = float(campaign.value_of_css_property(
    "font-size").replace("px", ''))
font_color_campaign_price_duck = slpit_rgba(campaign.value_of_css_property(
    "color"))
# regular_price
regular = duck.find_element_by_class_name("regular-price")

regular_price_duck = formate_price(regular.text)
font_decoration_regular_price_duck = regular.get_attribute("outerHTML")[1:2]
font_color_regular_price_duck = slpit_rgba(regular.value_of_css_property(
    "color"))
font_size_regular_price_duck = float(regular.value_of_css_property(
    "font-size").replace("px", ''))


# пункт a
if name_duck == name_curr_duck:
    print("Названия совпадают: " + name_duck)
# пункт б
if (formatted_campaign_price == campaign_price_duck) and (formatted_regular_price == regular_price_duck):
    print("Размеры цен совпадают")
# пункт в

if (font_decoration_regular_price == "s" and font_color_regular_price[0] == font_color_regular_price[1] and font_color_regular_price[1] == font_color_regular_price[2]):
    print("Обычная цена серая и зачеркнутая на главной странице")
if (font_decoration_regular_price_duck == "s" and font_color_regular_price_duck[0] == font_color_regular_price_duck[1] and
        font_color_regular_price_duck[1] == font_color_regular_price_duck[2]):
    print("Обычная цена серая и зачеркнутая на странице с товаром")
# пункт г
if (font_weight_campaign_price >= 700 and font_color_campaign_price[1] == font_color_campaign_price[2]):
    print("Акционная цена красная и жирная на главной странице")

if (font_weight_campaign_price_duck >= 700 and font_color_campaign_price_duck[1] == font_color_campaign_price_duck[2]):
    print("Акционная цена красная и жирная на странице с товаром")
# пункт д
if (font_size_campaign_price > font_size_regular_price):
    print("Размер акционной цены крупнее обычной, на главной странице")
if (font_size_campaign_price_duck > font_size_regular_price_duck):
    print("Размер акционной цены крупнее обычной, на странице с товаром")
driver.close()

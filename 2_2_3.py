import math
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = int(browser.find_element_by_css_selector("#num1").text)
    num2 = int(browser.find_element_by_css_selector("#num2").text)
    res = str(num2 + num1)
    print(res)
    dropdown = browser.find_element_by_css_selector("#dropdown").click()
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(res).click()
    time.sleep(1)
    submit = browser.find_element_by_css_selector("body > div.container > form > button").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
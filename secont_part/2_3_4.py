import os
import math
from selenium import webdriver
import time


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("body > form > div > div > button")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element_by_css_selector("#input_value").text
    print(x)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    res = calc(x)
    print(res)

    input_data = browser.find_element_by_css_selector("#answer")
    input_data.send_keys(res)

    browser.find_element_by_css_selector("body > form > div > div > button").click()

    parse_answer = browser.switch_to.alert
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(4)
    # закрываем браузер после всех манипуляций
    browser.quit()
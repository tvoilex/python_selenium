import math
from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    xd = browser.find_element_by_css_selector("#input_value")
    x = xd.text

    formula = browser.find_element_by_css_selector("body > div.container > form > div.form-group > label > span:nth-child(1)")

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    print(calc(x))

    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(calc(x))

    checkbox = browser.find_element_by_css_selector("#robotCheckbox")
    checkbox.click()

    radiobutton = browser.find_element_by_css_selector("#robotsRule")
    radiobutton.click()
    submit = browser.find_element_by_css_selector("#body > div.container > form > button")
    submit.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
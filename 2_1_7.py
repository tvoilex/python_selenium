import math
from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    picture = browser.find_element_by_css_selector("#treasure")
    x = picture.get_attribute("valuex")

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    res = calc(x)

    input_answer = browser.find_element_by_css_selector("#answer")
    input_answer.send_keys(res)

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
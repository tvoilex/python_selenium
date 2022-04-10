import math
from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_css_selector("#input_value").text
    print(x)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    res = calc(x)
    print(res)

    browser.execute_script("window.scrollBy(0, 130);")

    input_answer = browser.find_element_by_css_selector("#answer")
    input_answer.send_keys(res)

    checkbox = browser.find_element_by_css_selector("#robotCheckbox")
    checkbox.click()

    radiobutton = browser.find_element_by_css_selector("#robotsRule")
    radiobutton.click()
    browser.execute_script("window.scrollBy(0, 20);")
    submit = browser.find_element_by_css_selector("#body > div.container > form > button")
    submit.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
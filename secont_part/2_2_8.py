import os
import math
from selenium import webdriver
import time

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, '../test/empty.txt')           # добавляем к этому пути имя файла


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input_answer = browser.find_element_by_css_selector("body > div.container > form > div > input:nth-child(2)")
    input_answer.send_keys("maximka")

    input_answer2 = browser.find_element_by_css_selector("body > div.container > form > div > input:nth-child(4)")
    input_answer2.send_keys("loktionov")

    input_answer3 = browser.find_element_by_css_selector("body > div.container > form > div > input:nth-child(6)")
    input_answer3.send_keys("123@test.com")

    file = browser.find_element_by_css_selector("#file")
    file.send_keys(file_path)

    # checkbox = browser.find_element_by_css_selector("#robotCheckbox")
    # checkbox.click()
    #
    # radiobutton = browser.find_element_by_css_selector("#robotsRule")
    # radiobutton.click()
    # browser.execute_script("window.scrollBy(0, 20);")
    submit = browser.find_element_by_css_selector("#body > div.container > form > button")
    submit.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(4)
    # закрываем браузер после всех манипуляций
    browser.quit()



from selenium import webdriver
import asyncio
import time

while True:
    link = "https://www.twitch.tv/qwe_wa1ker"
    browser = webdriver.Chrome()
    browser.get(link)

    # # Ваш код, который заполняет обязательные поля
    # input1 = browser.find_element_by_css_selector("body > div.container > form > div.first_block > div.form-group.first_class > input")
    # input1.send_keys("Maximka")
    # input2 = browser.find_element_by_css_selector("body > div.container > form > div.first_block > div.form-group.second_class > input")
    # input2.send_keys("Maximochka")
    # input3 = browser.find_element_by_css_selector("body > div.container > form > div.first_block > div.form-group.third_class > input")
    # input3.send_keys("abrakadabra@asdasd.com")
    #
    # # Отправляем заполненную форму
    # button = browser.find_element_by_css_selector("button.btn")
    # button.click()
    #
    # # Проверяем, что смогли зарегистрироваться
    # # ждем загрузки страницы
    # time.sleep(1)
    #
    # # находим элемент, содержащий текст
    # welcome_text_elt = browser.find_element_by_tag_name("h1")
    # # записываем в переменную welcome_text текст из элемента welcome_text_elt
    # welcome_text = welcome_text_elt.text
    #
    # # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    # assert "Congratulations! You have successfully registered!" == welcome_text

# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
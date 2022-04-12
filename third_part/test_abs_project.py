from selenium import webdriver
import time
import unittest

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector("body > div.container > form > div.first_block > div.form-group.first_class > input")
        input1.send_keys("Maximka")
        input2 = browser.find_element_by_css_selector("body > div.container > form > div.first_block > div.form-group.second_class > input")
        input2.send_keys("Maximochka")
        input3 = browser.find_element_by_css_selector("body > div.container > form > div.first_block > div.form-group.third_class > input")
        input3.send_keys("abrakadabra@asdasd.com")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", "Congratulations! You have successfully registered!")

    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector("body > div.container > form > div.first_block > div.form-group.first_class > input")
        input1.send_keys("Maximka")
        input2 = browser.find_element_by_css_selector("body > div.container > form > div.first_block > div.form-group.second_class > input")
        input2.send_keys("Maximochka")
        input3 = browser.find_element_by_css_selector("body > div.container > form > div.first_block > div.form-group.third_class > input")
        input3.send_keys("abrakadabra@asdasd.com")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", "Congratulations! You have successfully registered!")

if __name__ == "__main__":
    unittest.main()

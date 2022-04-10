from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")
button = browser.find_element_by_css_selector("#book")
price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
button.click()

browser.execute_script("window.scrollTo(0, 100)")

x = browser.find_element_by_css_selector("#input_value").text
print(x)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

res = calc(x)
print(res)

input_data = browser.find_element_by_css_selector("#answer")
input_data.send_keys(res)

browser.find_element_by_css_selector("body > form > div > div > button").click()





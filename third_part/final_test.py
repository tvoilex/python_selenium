import time
import math
import pytest
from selenium import webdriver
correct_answer = "Correct!"


browser = webdriver.Chrome()
links = {"https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1" ,"https://stepik.org/lesson/236905/step/1"}
for link in links:
    browser.get(link)
    time.sleep(7)
    answer_int = math.log(int(time.time()))
    answer = str(answer_int)
    input_text = browser.find_element_by_css_selector(".attempt textarea")
    input_text.send_keys(answer)

    button = browser.find_element_by_css_selector("#ember74 > div > section > div > div.attempt__inner > div.attempt__actions > button").click()
    time.sleep(5)

    key_text = browser.find_element_by_css_selector("div>pre").text

    if key_text != correct_answer:
        print(key_text)



# for link in links:


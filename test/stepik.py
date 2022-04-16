import os
import math
from selenium import webdriver
import time


link = "http://selenium1py.pythonanywhere.com/"
browser = webdriver.Chrome()
browser.get(link)

def test_guest_can_go_to_login_page(browser):
    browser.get(link)
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()
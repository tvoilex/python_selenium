from selenium import webdriver
import time

try:
    link = "link"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    email = browser.find_element_by_css_selector("css_selector_of_email_address_area")
    email.send_keys("testemail@gmail.com")

    currency1 = browser.find_element_by_css_selector("css_selector_of_first_currency_list").click()
    currency1_choice = browser.find_element_by_css_selector("css_selector_of_any_currency_from_first_currency_list").click()

    currency2 = browser.find_element_by_css_selector("css_selector_of_second_currency_list").click()
    currency2_choice = browser.find_element_by_css_selector("css_selector_of_any_currency_from_second_currency_list").click()

    amount = browser.find_element_by_css_selector("css_selector_of_amount area")
    amount.send_keys("our_amount")

    alert_button = browser.find_element_by_css_selector("css_selector_of_alert_button").click()

    alert_text = browser.find_element_by_tag_name("css_selector_of_notification")
    notification = alert_text.text

    time.sleep(60)

    assert "text_of_notification" == notification

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()



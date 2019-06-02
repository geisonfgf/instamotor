from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def login(browser, username, password):
    browser.get("https://www.instagram.com/accounts/login?source=auth_switcher")
    time.sleep(5)

    username_field = browser.find_element_by_xpath("//input[@name='username']")
    username_field.clear()
    username_field.send_keys(username)
    time.sleep(1)

    password_field = browser.find_element_by_xpath("//input[@name='password']")
    password_field.clear()
    password_field.send_keys(password)
    time.sleep(1)

    login_button = browser.find_element_by_xpath("//button[@type='submit']")
    login_button.click()
    time.sleep(1)
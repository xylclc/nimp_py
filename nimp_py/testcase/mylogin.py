import pytest
from selenium import webdriver
from time import sleep

def my_login(browser):

    browser.get("http://192.168.198.92:8080/NIMP/login")
    try:
        browser.find_element("css selector","input#username").send_keys("cctest")
        browser.find_element("css selector", "input#password").send_keys("Aa@123")
        browser.find_element("css selector", "input#login_submit").click()
        sleep(3)
        browser.find_element("css selector","#logobg").click()
    except Exception as e:
        browser.find_element("css selector",".btn.btn-primary.ax-yes").click()
        sleep(3)




import os

import pytest
from testcase import mylogin
from selenium import webdriver
from time import sleep
import allure
import random
from datetime import datetime


@pytest.fixture(scope="session",autouse=False)
def browser():
    global driver
    opt = webdriver.ChromeOptions()
    opt.add_argument('--headless')
#    opt.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=opt)
    driver.maximize_window()
    sleep(2)
    mylogin.my_login(driver)
    yield driver
    driver.close()


@pytest.fixture(scope="function", autouse=True)
def gethome():
    #driver.get("http://192.168.198.92:8080/NIMP/apexIndex?targetMenuId=axHome")
     driver.refresh()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # 获取钩子方法的调用结果
    outcome = yield
    rep = outcome.get_result()
    OUTPUTS_DIR = ".\pic"
    print(os.getcwd())
    file_name = OUTPUTS_DIR + "\\{}.png".format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"))
    try:
        if rep.when == "call" and rep.failed:
            driver.save_screenshot(file_name)
            with open(file_name, mode='rb') as f:
                file = f.read()
            allure.attach(file, "失败截图", allure.attachment_type.PNG)
    except Exception as e:
        print(e)

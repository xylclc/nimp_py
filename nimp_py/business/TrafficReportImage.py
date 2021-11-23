#coding=utf-8

from time import sleep
import logging
import time
import allure
from datetime import datetime
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

#TRAFFIC
def monthly_traffic(browser):
    try:
        browser.find_element("xpath","//*[text()='Traffic Statistic']").click()
        browser.find_element("xpath", "//*[text()='Monthly Traffic Monitor']").click()
        sleep(1)
        browser.switch_to.frame("mainFrame")
        s=browser.find_element("css selector","#body>ul>li:nth-child(2)").text
        assert s=="Month"
        browser.find_element("id","button").click()                   #Total Traffic
        sleep(3)
        browser.find_element("css selector","#canvas_pie1>div>canvas").click()
        browser.find_element("css selector","#canvas>div>canvas").click()
        browser.find_element("id","WebSite").click()                      #WebSite
        sleep(2)
        browser.find_element("id", "button").click()
        sleep(3)
        browser.find_element("css selector", "#canvas_pie1>div>canvas").click()
        browser.find_element("css selector", "#canvas>div>canvas").click()
        browser.find_element("id","StaticIP").click()                      #StaticIP
        sleep(2)
        browser.find_element("id", "button").click()
        sleep(3)
        browser.find_element("css selector", "#canvas_pie1>div>canvas").click()
        browser.find_element("css selector", "#canvas>div>canvas").click()
        browser.find_element("id", "RangeIP").click()                            # RangeIP
        sleep(2)
        browser.find_element("id", "button").click()
        sleep(3)
        browser.find_element("css selector", "#canvas_pie1>div>canvas").click()
        browser.find_element("css selector", "#canvas>div>canvas").click()
        browser.find_element("id", "ProtocolTraffic").click()                            # ProtocolTraffic
        sleep(2)
        browser.find_element("id", "button").click()
        sleep(3)
        browser.find_element("css selector", "#canvas_pie1>div>canvas").click()
        browser.find_element("css selector", "#canvas>div>canvas").click()
        return True
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return False

def daily_traffic(browser):
    try:
        sleep(2)
        browser.find_element("xpath","//*[text()='Traffic Statistic']").click()
        sleep(2)
        browser.find_element("xpath", "//*[text()='Daily Traffic Monitor']").click()
        sleep(1)
        browser.switch_to.frame("mainFrame")
        s = browser.find_element("css selector", "#body>ul>li:nth-child(2)").text
        assert s == "Day"
        browser.find_element("id", "button").click()  # Total Traffic
        sleep(3)
        browser.find_element("css selector", "#canvas_pie1>div>canvas").click()
        browser.find_element("css selector", "#canvas>div>canvas").click()
        browser.find_element("id", "WebSite").click()  # WebSite
        sleep(2)
        browser.find_element("id", "button").click()
        sleep(3)
        browser.find_element("css selector", "#canvas_pie1>div>canvas").click()
        browser.find_element("css selector", "#canvas>div>canvas").click()
        browser.find_element("id", "StaticIP").click()  # StaticIP
        sleep(2)
        browser.find_element("id", "button").click()
        sleep(3)
        browser.find_element("css selector", "#canvas_pie1>div>canvas").click()
        browser.find_element("css selector", "#canvas>div>canvas").click()
        browser.find_element("id", "RangeIP").click()  # RangeIP
        sleep(2)
        browser.find_element("id", "button").click()
        sleep(3)
        browser.find_element("css selector", "#canvas_pie1>div>canvas").click()
        browser.find_element("css selector", "#canvas>div>canvas").click()
        browser.find_element("id", "ProtocolTraffic").click()  # ProtocolTraffic
        sleep(2)
        browser.find_element("id", "button").click()
        sleep(3)
        browser.find_element("css selector", "#canvas_pie1>div>canvas").click()
        browser.find_element("css selector", "#canvas>div>canvas").click()
        return True
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return False

def hourly_traffic(browser):
    try:
        sleep(2)
        browser.find_element("xpath","//*[text()='Traffic Statistic']").click()
        sleep(2)
        browser.find_element("xpath", "//*[text()='Hourly Traffic Monitor']").click()
        sleep(1)
        browser.switch_to.frame("mainFrame")
        s = browser.find_element("css selector", "#body>ul>li:nth-child(2)").text
        assert s == "Hour"
        js = 'document.getElementById("searchBeginDate").value = "2021-10-05 17"'   # Total Traffic
        browser.execute_script(js)
        sleep(1)
        browser.find_element("id", "button").click()
        sleep(3)
        browser.find_element("css selector", "#canvas_pie1>div>canvas").click()
        browser.find_element("css selector", "#canvas>div>canvas").click()
        browser.find_element("id", "WebSite").click()  # WebSite
        sleep(2)
        browser.find_element("id", "button").click()
        sleep(3)
        browser.find_element("css selector", "#canvas_pie1>div>canvas").click()
        browser.find_element("css selector", "#canvas>div>canvas").click()
        browser.find_element("id", "StaticIP").click()  # StaticIP
        sleep(2)
        browser.find_element("id", "button").click()
        sleep(3)
        browser.find_element("css selector", "#canvas_pie1>div>canvas").click()
        browser.find_element("css selector", "#canvas>div>canvas").click()
        browser.find_element("id", "RangeIP").click()  # RangeIP
        sleep(2)
        browser.find_element("id", "button").click()
        sleep(3)
        browser.find_element("css selector", "#canvas_pie1>div>canvas").click()
        browser.find_element("css selector", "#canvas>div>canvas").click()
        browser.find_element("id", "ProtocolTraffic").click()  # ProtocolTraffic
        sleep(2)
        browser.find_element("id", "button").click()
        sleep(3)
        browser.find_element("css selector", "#canvas_pie1>div>canvas").click()
        browser.find_element("css selector", "#canvas>div>canvas").click()
        return True
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return False

def monthly_service(browser):
    try:
        browser.find_element("xpath","//*[text()='Traffic Statistic']").click()
        sleep(1)
        browser.find_element("xpath", "//*[text()='Monthly Service Statistics']").click()
        sleep(1)
        browser.switch_to.frame("mainFrame")
        s = browser.find_element("css selector", "#body>ul>li:nth-child(2)").text
        assert s == "Month"
        browser.find_element("id","button").click()                               #http
        sleep(1)
        browser.find_element("css selector","#protoList>label:nth-child(2)>input").click()
        sleep(3)
        browser.find_element("css selector","#canvas>div>canvas").click()
        browser.find_element("id","EMAIL").click()                            #email
        sleep(1)
        browser.find_element("css selector", "#protoList>label:nth-child(2)>input").click()
        sleep(3)
        browser.find_element("css selector", "#canvas>div>canvas").click()
        browser.find_element("id", "FTP").click()                                 # ftp
        sleep(1)
        browser.find_element("css selector", "#protoList>label>input").click()
        sleep(3)
        browser.find_element("css selector", "#canvas>div>canvas").click()
        return True
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return False

def daily_service(browser):
    try:
        browser.find_element("xpath", "//*[text()='Traffic Statistic']").click()
        sleep(1)
        browser.find_element("xpath", "//*[text()='Daily Service Statistics']").click()
        sleep(1)
        browser.switch_to.frame("mainFrame")
        s = browser.find_element("css selector", "#body>ul>li:nth-child(2)").text
        assert s == "Day"
        browser.find_element("id", "button").click()  # http
        sleep(1)
        browser.find_element("css selector", "#protoList>label:nth-child(2)>input").click()
        sleep(3)
        browser.find_element("css selector", "#canvas>div>canvas").click()
        browser.find_element("id", "EMAIL").click()  # email
        sleep(1)
        browser.find_element("css selector", "#protoList>label:nth-child(2)>input").click()
        sleep(3)
        browser.find_element("css selector", "#canvas>div>canvas").click()
        browser.find_element("id", "FTP").click()  # ftp
        sleep(1)
        browser.find_element("css selector", "#protoList>label>input").click()
        sleep(3)
        browser.find_element("css selector", "#canvas>div>canvas").click()
        return True
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return False

def hourly_service(browser):
    try:
        browser.find_element("xpath", "//*[text()='Traffic Statistic']").click()
        sleep(1)
        browser.find_element("xpath", "//*[text()='Hourly Service Statistics']").click()
        sleep(1)
        browser.switch_to.frame("mainFrame")
        s = browser.find_element("css selector", "#body>ul>li:nth-child(2)").text
        assert s == "Hour"
        browser.find_element("id", "button").click()  # http
        sleep(1)
        browser.find_element("css selector", "#protoList>label:nth-child(2)>input").click()
        sleep(3)
        browser.find_element("css selector", "#canvas>div>canvas").click()
        browser.find_element("id", "EMAIL").click()  # email
        sleep(1)
        browser.find_element("css selector", "#protoList>label:nth-child(2)>input").click()
        sleep(3)
        browser.find_element("css selector", "#canvas>div>canvas").click()
        browser.find_element("id", "FTP").click()  # ftp
        sleep(1)
        browser.find_element("css selector", "#protoList>label>input").click()
        sleep(3)
        browser.find_element("css selector", "#canvas>div>canvas").click()
        return True
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return False

#REPORT
def use_report(browser):
    try:
        browser.find_element("xpath", "//*[text()='Summary Report']").click()
    except:
        browser.find_element("id", "chevronright").click()
        sleep(1)
        browser.find_element("xpath", "//*[text()='Summary Report']").click()
    sleep(2)
    browser.find_element("xpath", "//*[text()='Report List']").click()
    sleep(1)
    browser.switch_to.frame("mainFrame")

def load_report(browser):
    try:
        use_report(browser)
        num= len(browser.find_elements("xpath","//*[contains(text(),'Download Word')]"))
        return num
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return 0

def search_monthlyreport(browser,date):
    try:
        use_report(browser)
        ch=Select(browser.find_element("id","templateName1"))
        ch.select_by_value("Monthly")
        browser.find_element("css selector","input[name='title']").send_keys(date)
        browser.find_element("css selector", "input[type='button']").click()
        sleep(2)
        return browser.find_elements("css selector", ".x_book_box a")[0].text
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return "111"

def search_dailyreport(browser,date):
    try:
        use_report(browser)
        ch=Select(browser.find_element("id","templateName1"))
        ch.select_by_value("Daily")
        browser.find_element("css selector","input[name='title']").send_keys(date)
        browser.find_element("css selector", "input[type='button']").click()
        sleep(2)
        return browser.find_elements("css selector", ".x_book_box a")[0].text
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return "111"

def search_weeklyreport(browser,date):
    try:
        use_report(browser)
        ch=Select(browser.find_element("id","templateName1"))
        ch.select_by_value("Weekly")
        browser.find_element("css selector","input[name='title']").send_keys(date)
        browser.find_element("css selector", "input[type='button']").click()
        sleep(2)
        return browser.find_elements("css selector", ".x_book_box a")[0].text
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return "111"

#IMAGE
def searchimg_name(key,browser):
    try:
        try:
            browser.find_element("xpath", "//*[text()='Image Recognition']").click()
        except:
            browser.find_element("id","chevronright").click()
            sleep(1)
            browser.find_element("xpath", "//*[text()='Image Recognition']").click()
        sleep(3)
        browser.switch_to.frame("mainFrame")
        browser.find_element("id", "names").send_keys(key)
        browser.find_element("id", "btnSimpleSearch").click()
        sleep(2)
        return browser.find_element("css selector","#datagrid-row-r1-2-0>td[field='names']").text
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return ""



def view_httpimage(browser):
    try:
        browser.find_element("xpath", "//*[text()='Image Recognition']").click()
    except:
        browser.find_element("id", "chevronright").click()
        sleep(1)
        browser.find_element("xpath", "//*[text()='Image Recognition']").click()
    sleep(3)
    browser.switch_to.frame("mainFrame")
    date1 = browser.find_element("css selector", "#datagrid-row-r1-2-0 td:nth-child(2)>div").text
    nowtime = time.strftime("%d-%m-%Y")
    day1 = time.strptime(date1, "%d-%m-%Y")
    day2 = time.strptime(nowtime, "%d-%m-%Y")
    day_num = (int(time.mktime(day2)) - int(time.mktime(day1))) / (24 * 60 * 60)

    resource = browser.find_element("css selector", "#datagrid-row-r1-2-0>td:nth-child(3)>div").text
    return (abs(int(day_num)), resource)


def view_mailimage(browser):
    try:
        browser.find_element("xpath", "//*[text()='Image Recognition']").click()
    except:
        browser.find_element("id", "chevronright").click()
        sleep(1)
        browser.find_element("xpath", "//*[text()='Image Recognition']").click()
    sleep(3)
    browser.switch_to.frame("mainFrame")
    ch = Select(browser.find_element_by_id("q_type"))
    ch.select_by_value("mail")
    browser.find_element_by_id("btnSimpleSearch").click()
    sleep(2)
    date1 = browser.find_element("css selector", "#datagrid-row-r1-2-0 td:nth-child(2)>div").text
    nowtime = time.strftime("%d-%m-%Y")
    day1 = time.strptime(date1, "%d-%m-%Y")
    day2 = time.strptime(nowtime, "%d-%m-%Y")
    day_num = (int(time.mktime(day2)) - int(time.mktime(day1))) / (24 * 60 * 60)

    resource = browser.find_element("css selector", "#datagrid-row-r1-2-0>td:nth-child(3)>div").text
    return (abs(int(day_num)), resource)


def httpimgdetail(browser):
    try:
        browser.find_element("xpath", "//*[text()='Image Recognition']").click()
    except:
        browser.find_element("id", "chevronright").click()
        sleep(1)
        browser.find_element("xpath", "//*[text()='Image Recognition']").click()
    sleep(3)
    browser.switch_to.frame("mainFrame")
    browser.find_element("css selector", "td[field='resourceId']>div>a").click()
    sleep(5)
    browser.switch_to.frame("detailBox")
    s = browser.find_element("css selector", "#entity_host").get_attribute("title")
    print(s)
    return s


def mailimgdetail(browser):
    try:
        browser.find_element("xpath", "//*[text()='Image Recognition']").click()
    except:
        browser.find_element("id", "chevronright").click()
        sleep(1)
        browser.find_element("xpath", "//*[text()='Image Recognition']").click()
    sleep(3)
    browser.switch_to.frame("mainFrame")
    ch = Select(browser.find_element_by_id("q_type"))
    ch.select_by_value("mail")
    browser.find_element_by_id("btnSimpleSearch").click()
    sleep(3)
    browser.find_element("css selector", "td[field='resourceId']>div>a").click()
    sleep(5)
    browser.switch_to.frame("detailBox")
    s = browser.find_element("css selector", "#entity_createDate").get_attribute("title")
    print(s)
    return s
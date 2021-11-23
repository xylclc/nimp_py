#coding=utf-8
import time
from time import sleep
import logging
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

def use_emailaccount(browser):
    browser.find_element("xpath", "//*[text()='Cloud Search']").click()
    sleep(1)
    AccountInformation = browser.find_element("xpath", "//*[text()='Account Information']")
    ActionChains(browser).move_to_element(AccountInformation).perform()
    sleep(1)
    browser.find_element("xpath", "//*[text()='Email Account']").click()
    sleep(2)
    browser.switch_to.frame("mainFrame")

def use_httpaccount(browser):
    browser.find_element("xpath", "//*[text()='Cloud Search']").click()
    sleep(2)
    AccountInformation = browser.find_element("xpath", "//*[text()='Account Information']")
    ActionChains(browser).move_to_element(AccountInformation).perform()
    sleep(1)
    browser.find_element("xpath", "//*[text()='HTTP Account']").click()
    sleep(2)
    browser.switch_to.frame("mainFrame")

def use_vid(browser):
    browser.find_element("xpath", "//*[text()='Cloud Search']").click()
    sleep(1)
    AccountInformation = browser.find_element("xpath", "//*[text()='Virtual ID']").click()
    browser.switch_to.frame("mainFrame")
    sleep(2)
    assert browser.find_element("css selector",".breadcrumb>li:nth-child(2)").text=="Virtual ID"

def searchvid_realname(browser):
    try:
        use_vid(browser)
        browser.find_element("id","q_simpleSearch").send_keys("cai")
        browser.find_element("id","btnSimpleSearch").click()
        sleep(2)
        return browser.find_element("css selector","#pnlListTb td:nth-child(4)").text
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return "","1"

def searchvid_vid(browser):
    try:
        use_vid(browser)
        browser.find_element("css selector","[href='#moreQueryView']").click()
        sleep(1)
        browser.find_element("id","q_accountId").send_keys("01139")
        browser.find_element("id","btnSearch").click()
        sleep(1)
        return browser.find_element("css selector","#pnlListTb td:nth-child(3)").text
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return "","1"

def searchvid_email(browser):
    try:
        use_vid(browser)
        browser.find_element("css selector","[href='#moreQueryView']").click()
        sleep(1)
        browser.find_element("id","q_email").send_keys("lili.cui@cssca.com")
        browser.find_element("id","btnSearch").click()
        sleep(1)
        return browser.find_element("css selector","#pnlListTb td:nth-child(6)").text
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return "","1"

def searchvid_clear(browser):
    try:
        use_vid(browser)
        browser.find_element("css selector", "[href='#moreQueryView']").click()
        sleep(1)
        browser.find_element("id", "q_accountId").send_keys("01139")
        browser.find_element("id", "btnClear").click()
        sleep(1)
        return browser.find_element("id", "q_accountId").text
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return "1"

def searchvid_close(browser):
    try:
        use_vid(browser)
        browser.find_element("css selector", "[href='#moreQueryView']").click()
        sleep(1)
        browser.find_element("id", "q_accountId").send_keys("01139")
        browser.find_element("id", "btnClose").click()
        sleep(1)
        num=len(browser.find_elements("css selector","#moreQueryView[style='display: none;']"))
        if num==1:
            return True
        else:
            return False
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return False

def editvid(browser):
    try:
        use_vid(browser)
        browser.find_element("id", "q_simpleSearch").send_keys("cai")
        browser.find_element("id", "btnSimpleSearch").click()
        sleep(1)
        browser.find_element("css selector", "#pnlListTb td:nth-child(11)>a").click()
        sleep(1)
        browser.find_element("id","entity_companyAddress").clear()
        browser.find_element("id","entity_companyAddress").send_keys("NJ")
        browser.find_element("id","btnSave").click()
        sleep(2)
        browser.find_element("id", "q_simpleSearch").send_keys("cai")
        browser.find_element("id", "btnSimpleSearch").click()
        sleep(1)
        return browser.find_element("css selector", "#pnlListTb td:nth-child(8)").text
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return ""

def accountinfo(browser):
    try:
        use_vid(browser)
        browser.find_element("id","q_simpleSearch").send_keys("cai")
        browser.find_element("id","btnSimpleSearch").click()
        sleep(2)
        browser.find_element("css selector","tbody td:nth-child(10)>a").click()
        sleep(3)
        browser.switch_to.default_content()
        browser.switch_to.frame("topPopModalCommonFrame")
        browser.switch_to.frame("mainBody")
        s1= browser.find_element("css selector","#gridviewEmail tbody td:nth-child(5)").text
        return s1
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return "",""


def vid_nextpage(browser):
    try:
        use_vid(browser)
        browser.find_element("css selector", "#gridview tfoot td li:nth-child(3)>a").click()
        sleep(2)
        next = browser.find_element("css selector", "#gridview tbody td:nth-child(2)").text
        assert next=="11."
        browser.find_element("css selector", "#gridview tfoot td li:nth-child(2)>a").click()
        sleep(2)
        pre= browser.find_element("css selector", "#gridview tbody td:nth-child(2)").text
        assert pre == "1."
        browser.find_element("css selector","#gridview tfoot td li:nth-child(4)>a").click()
        sleep(2)
        last = browser.find_elements("css selector", "#gridview tbody td:nth-child(2)")[-1].text
        allnum=browser.find_element("css selector",".pageinfo").text.split(" ")[6]+'.'
        assert last == allnum
        browser.find_element("css selector", "#gridview tfoot td li:nth-child(1)>a").click()
        sleep(2)
        first = browser.find_element("css selector", "#gridview tbody td:nth-child(2)").text
        assert first == "1."
        browser.find_elements("css selector", ".input-mini")[0].send_keys('3')
        browser.find_element("xpath","//*[text()='Go!']").click()
        sleep(2)
        page3 = browser.find_element("css selector", "#gridview tbody td:nth-child(2)").text
        assert page3 == "21."
        ch=Select(browser.find_elements("css selector", ".input-mini")[1])
        ch.select_by_value("20")
        sleep(2)
        twenty = browser.find_elements("css selector", "#gridview tbody td:nth-child(2)")[-1].text
        assert twenty=="20."
        return True
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return False


def view_emailaccount(browser):
    try:
        use_emailaccount(browser)
        s=browser.find_element("css selector","#gridviewEmail td:nth-child(4)").text
        date1=s[0:10]
        nowtime = time.strftime("%d-%m-%Y")
        day1 = time.strptime(date1, "%d-%m-%Y")
        day2 = time.strptime(nowtime, "%d-%m-%Y")
        day_num = (int(time.mktime(day2)) - int(time.mktime(day1))) / (24 * 60 * 60)
        return (abs(int(day_num)))
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return 100

def search_emailaccount(browser):
    try:
        use_emailaccount(browser)
        browser.find_element("id","q_simpleSearchEmail").send_keys("lili")
        browser.find_element("id","btnSimpleSearchEmail").click()
        sleep(1)
        return browser.find_element("css selector","#gridviewEmail tr td:nth-child(2)").text
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return ""

def search_emailaccount_date(browser,begin,end):
    try:
        use_emailaccount(browser)
        sleep(1)
        browser.find_element("css selector","[href='#moreQueryViewEmail']").click()
        sleep(1)
        s1='document.getElementById("updateDateEmail_start").value = "'+begin[:10]+'"'
        s2='document.getElementById("updateDateEmail_end").value = "'+end[:10]+'"'
        browser.execute_script(s1)
        browser.execute_script(s2)
        browser.find_element("id","btnSearchEmail").click()
        sleep(2)
        t1=browser.find_element("css selector","#gridviewEmail tbody td:nth-child(4)").text
        if len(browser.find_elements("css selector",".pagination>ul>li:nth-child(4)[class='disabled']"))>0:
            t2=browser.find_element("css selector","#gridviewEmail tbody tr:last-child>td:nth-child(4)").text
        else:
            browser.find_element("css selector",".pagination>ul>li:nth-child(4)>a").click()
            sleep(1)
            t2=browser.find_element("css selector","#gridviewEmail tbody tr:last-child>td:nth-child(4)").text
        t1=time.strptime(t1, '%d-%m-%Y %H:%M:%S')
        t2=time.strptime(t2, '%d-%m-%Y %H:%M:%S')
        return t1,t2
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return "",""

def search_emailaccount_close(browser):
    try:
        use_emailaccount(browser)
        sleep(1)
        browser.find_element("css selector","[href='#moreQueryViewEmail']").click()
        sleep(1)
        browser.find_element("id","btnCloseEmail").click()
        sleep(1)
        n=len(browser.find_elements("css selector","#moreQueryViewEmail[style='display: none;']"))
        return n
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return 0

def view_emaildetail(browser):
    try:
        use_emailaccount(browser)
        browser.find_element("id","q_simpleSearchEmail").send_keys("lili")
        browser.find_element("id","btnSimpleSearchEmail").click()
        sleep(1)
        browser.find_element("css selector", "#gridviewEmail tr td:nth-child(6)>a").click()
        sleep(4)
        browser.switch_to.default_content()
        browser.switch_to.frame("topPopModalCommonFrame")
        return browser.find_element("css selector","#gridview tr td:nth-child(7)").text
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return ""

def search_httpaccount(browser):
    try:
        use_httpaccount(browser)
        browser.find_element("id","q_simpleSearchHttp").send_keys("jmeter")
        browser.find_element("id","btnSimpleSearchHttp").click()
        sleep(1)
        return browser.find_element("css selector","#gridviewHttp tr td:nth-child(2)").text
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return ""

def search_httpaccount_date(browser,begin,end):
    try:
        use_httpaccount(browser)
        sleep(1)
        browser.find_element("css selector","[href='#moreQueryViewHttp']").click()
        sleep(1)
        s1='document.getElementById("updateDateHttp_start").value = "'+begin[:10]+'"'
        s2='document.getElementById("updateDateHttp_end").value = "'+end[:10]+'"'
        browser.execute_script(s1)
        browser.execute_script(s2)
        browser.find_element("id","btnSearchHttp").click()
        sleep(2)
        t1=browser.find_element("css selector","#gridviewHttp tbody td:nth-child(3)").text
        if len(browser.find_elements("css selector",".pagination>ul>li:nth-child(4)[class='disabled']"))>0:
            t2=browser.find_element("css selector","tbody tr:last-child>td:nth-child(3)").text
        else:
            browser.find_element("css selector",".pagination>ul>li:nth-child(4)>a").click()
            sleep(1)
            t2=browser.find_element("css selector","tbody tr:last-child>td:nth-child(3)").text
        t1=time.strptime(t1, '%d-%m-%Y %H:%M:%S')
        t2=time.strptime(t2, '%d-%m-%Y %H:%M:%S')
        return t1,t2
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return "",""

def search_httpaccount_close(browser):
    try:
        use_httpaccount(browser)
        sleep(1)
        browser.find_element("css selector", "[href='#moreQueryViewHttp']").click()
        sleep(1)
        browser.find_element("id", "btnSearchHttp").click()
        sleep(1)
        n = len(browser.find_elements("css selector", "#moreQueryViewHttp[style='display: none;']"))
        return n
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return 0

def view_httpaccount(browser):
    try:
        use_httpaccount(browser)
        s=browser.find_element("css selector","#gridviewHttp td:nth-child(3)").text
        date1=s[0:10]
        nowtime = time.strftime("%d-%m-%Y")
        day1 = time.strptime(date1, "%d-%m-%Y")
        day2 = time.strptime(nowtime, "%d-%m-%Y")
        day_num = (int(time.mktime(day2)) - int(time.mktime(day1))) / (24 * 60 * 60)
        return (abs(int(day_num)))
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return 100

def view_httpdetail(browser):
    try:
        use_httpaccount(browser)
        browser.find_element("id", "q_simpleSearchHttp").send_keys("jmeter")
        browser.find_element("id", "btnSimpleSearchHttp").click()
        sleep(1)
        browser.find_element("css selector", "#gridviewHttp tr td:nth-child(5)>a").click()
        sleep(4)
        browser.switch_to.default_content()
        sleep(1)
        browser.switch_to.frame("topPopModalCommonFrame")
        return browser.find_element("css selector", "#gridview tr td:nth-child(9)").text
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return ""

def view_emailtrace(browser):
    try:
        browser.find_element("xpath", "//*[text()='Cloud Search']").click()
        sleep(1)
        menu=browser.find_element("xpath","//*[text()='Behavior Trace Information']")
        ActionChains(browser).move_to_element(menu).perform()
        sleep(1)
        browser.find_element("xpath", "//*[text()='Email Trace ']").click()
        sleep(2)
        browser.switch_to.frame("mainFrame")
        s=browser.find_element("css selector","#gridview tr td:nth-child(12)").text
        print(s)
        date1=s[0:10]
        nowtime = time.strftime("%d-%m-%Y")
        day1 = time.strptime(date1, "%d-%m-%Y")
        day2 = time.strptime(nowtime, "%d-%m-%Y")
        day_num = (int(time.mktime(day2)) - int(time.mktime(day1))) / (24 * 60 * 60)
        return (abs(int(day_num)))
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return 100

def search_emailtrace_sender(browser,sender):
    try:
        browser.find_element("xpath", "//*[text()='Cloud Search']").click()
        sleep(1)
        menu=browser.find_element("xpath","//*[text()='Behavior Trace Information']")
        ActionChains(browser).move_to_element(menu).perform()
        sleep(1)
        browser.find_element("xpath", "//*[text()='Email Trace ']").click()
        sleep(2)
        browser.switch_to.frame("mainFrame")
        browser.find_element("id","q_simpleSearch").send_keys(sender)
        browser.find_element("id", "btnSimpleSearch").click()
        sleep(3)
        return browser.find_element("css selector","tbody td:nth-child(7)").text
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return ""

def search_emailtrace_receiver(browser,receiver):
    try:
        browser.find_element("xpath", "//*[text()='Cloud Search']").click()
        sleep(1)
        menu=browser.find_element("xpath","//*[text()='Behavior Trace Information']")
        ActionChains(browser).move_to_element(menu).perform()
        sleep(1)
        browser.find_element("xpath", "//*[text()='Email Trace ']").click()
        sleep(2)
        browser.switch_to.frame("mainFrame")
        browser.find_element("css selector",".btn[href='#moreQueryView']").click()
        sleep(1)
        browser.find_element("id","q_mto").send_keys(receiver)
        browser.find_element("id", "btnSearch").click()
        sleep(3)
        return browser.find_element("css selector","tbody td:nth-child(8)").text
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return ""

def search_emailtrace_subject(browser,s):
    try:
        browser.find_element("xpath", "//*[text()='Cloud Search']").click()
        sleep(1)
        menu=browser.find_element("xpath","//*[text()='Behavior Trace Information']")
        ActionChains(browser).move_to_element(menu).perform()
        sleep(1)
        browser.find_element("xpath", "//*[text()='Email Trace ']").click()
        sleep(2)
        browser.switch_to.frame("mainFrame")
        browser.find_element("css selector",".btn[href='#moreQueryView']").click()
        sleep(1)
        browser.find_element("id","q_subject").send_keys(s)
        browser.find_element("id", "btnSearch").click()
        sleep(3)
        subject= browser.find_elements("css selector","tbody td:nth-child(11)>p")[0].get_attribute('data-teskly-viewitle')
        return subject
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return ""

def search_emailtrace_clear(browser):
    try:
        browser.find_element("xpath", "//*[text()='Cloud Search']").click()
        sleep(1)
        menu = browser.find_element("xpath", "//*[text()='Behavior Trace Information']")
        ActionChains(browser).move_to_element(menu).perform()
        sleep(1)
        browser.find_element("xpath", "//*[text()='Email Trace ']").click()
        sleep(2)
        browser.switch_to.frame("mainFrame")
        browser.find_element("css selector", ".btn[href='#moreQueryView']").click()
        sleep(1)
        browser.find_element("id", "q_mto").send_keys("lili.cui@cssca.com")
        browser.find_element("id","btnClear").click()
        return browser.find_element("id", "q_mto").text
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return 0


def search_emailtrace_close(browser):
    try:
        browser.find_element("xpath", "//*[text()='Cloud Search']").click()
        sleep(1)
        menu = browser.find_element("xpath", "//*[text()='Behavior Trace Information']")
        ActionChains(browser).move_to_element(menu).perform()
        sleep(1)
        browser.find_element("xpath", "//*[text()='Email Trace ']").click()
        sleep(2)
        browser.switch_to.frame("mainFrame")
        browser.find_element("css selector", ".btn[href='#moreQueryView']").click()
        sleep(1)
        browser.find_element("id","btnClose").click()
        sleep(1)
        n=len(browser.find_elements("css selector","#moreQueryView[style='display: none;']"))
        return n
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return 0


def httpresourcesearch(browser):
    browser.find_element("xpath", "//*[text()='Cloud Search']").click()
    sleep(1)
    browser.find_element("xpath", "//*[text()='Resource Search']").click()
    sleep(2)
    browser.switch_to.frame("mainFrame")
    browser.find_element("id","clear").click()
    browser.find_element("id","entity_keyWord").send_keys("jmeter")
    js = 'document.getElementById("q_searchDate_start").value = "01-08-2021"'
    browser.execute_script(js)
    sleep(1)
    js = 'document.getElementById("q_searchDate_end").value = "31-08-2021"'
    browser.execute_script(js)
    sleep(1)
    browser.find_element("id","btnSimpleSearch").click()
    sleep(5)
    return browser.find_element("css selector","#gridview tbody tr:nth-child(6) td:nth-child(4)").text

def view_httpresourcesearch(browser):
    try:
        browser.find_element("xpath", "//*[text()='Cloud Search']").click()
        sleep(1)
        browser.find_element("xpath", "//*[text()='Resource Search']").click()
        sleep(2)
        browser.switch_to.frame("mainFrame")
        browser.find_element("id","clear").click()
        browser.find_element("id","entity_keyWord").send_keys("jmeter")
        js = 'document.getElementById("q_searchDate_start").value = "01-08-2021"'
        browser.execute_script(js)
        sleep(1)
        js = 'document.getElementById("q_searchDate_end").value = "31-08-2021"'
        browser.execute_script(js)
        sleep(1)
        browser.find_element("id","btnSimpleSearch").click()
        sleep(2)
        browser.find_element("css selector", "#gridview tbody tr:nth-child(6)>td:nth-child(6)>a").click()
        sleep(1)
        all_handles = browser.window_handles
        browser.switch_to.window(all_handles[-1])  # 切换到最后一个打开的窗口
        sleep(1)
        browser.switch_to.frame("mainFrame")
        browser.find_element("xpath", "//*[contains(text(), 'jmeter')]").click()
        browser.close()
        browser.switch_to.window(all_handles[0])
        return True
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        browser.close()
        return False
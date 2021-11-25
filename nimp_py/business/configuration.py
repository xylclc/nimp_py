#coding=utf-8

from time import sleep
import logging
import random
import time
from selenium.webdriver.support.ui import Select

def mytraffic(browser):
    try:
        browser.switch_to.frame("mainFrame")
        sleep(1)
        browser.find_element("id","canvas1").click()
        browser.find_element("id", "canvas2").click()
        browser.find_element("id", "canvas3").click()
        browser.find_element("id", "canvas4").click()
        return True
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return False

def use_suspiciousgroup(browser):
    browser.find_element("xpath", "//*[text()='Configuration Management']").click()
    sleep(1)
    browser.find_element("xpath", "//*[text()='Suspicious Group']").click()
    sleep(2)
    browser.switch_to.frame("mainFrame")


def load_suspiciousgroup(browser):
    try:
        use_suspiciousgroup(browser)
        s=browser.find_element("css selector",".breadcrumb li:nth-child(2)").text   #Suspicious Group页面标题
        return s
    except Exception as msg:
        logging.warning("异常原因%s" %msg)
        return ""

def search_suspiciousgroup(browser):
    try:
        use_suspiciousgroup(browser)
        key=browser.find_element("css selector","#gridview tr:nth-child(3) td:nth-child(3)").text
        browser.find_element("id","q_simpleSearch").send_keys(key)
        browser.find_element("id","btnSimpleSearch").click()
        sleep(3)
        s=browser.find_element("css selector","#gridview tr td:nth-child(3)").text
        return s,key
    except Exception as msg:
        logging.warning("异常原因%s" %msg)
        return "","123"

def add_suspiciousgroup(browser):
    try:
        use_suspiciousgroup(browser)
        browser.find_element("css selector",".icon-plus.icon-white").click()         #add
        sleep(1)
        browser.switch_to.frame("_ax_frm_frame_")
        rand = "".join(random.sample('1234567890abcdefg', 6))
        browser.find_element("id","entity_typeName").send_keys(rand)        #group name
        browser.find_element("id","entity_typelaosName").send_keys(rand+"备注")
        browser.find_element("id", "entity_typethailandName").send_keys(rand + "memo")
        browser.find_element("id","btnSubmit").click()
        sleep(3)
        browser.switch_to.parent_frame()
        sleep(1)
        name=browser.find_element("css selector","#gridview tbody>tr>td:nth-child(3)").text
        createtime=browser.find_element("css selector","#gridview tbody>tr>td:nth-child(7)").text[:10]
        mytime=time.strftime("%d-%m-%Y")
        return name,rand,createtime,mytime
    except Exception as msg:
        logging.warning("异常原因%s" %msg)
        return "name", "rand","","1"

def edit_suspiciousgroup(browser):
    try:
        s = browser.find_element("id", "abc").text  # 取自动化账户id
        s1 = s.split(",")[1].strip()
        use_suspiciousgroup(browser)
        author = browser.find_element("css selector", "#gridview tbody>tr>td:nth-child(6)").text
        if author != s1:
            raise Exception("You can't edit this rule,Author is not %s" % s1)
        browser.find_element("css selector","#gridview tbody td:nth-child(10)>a").click()        #edit
        sleep(2)
        newname = "".join(random.sample('1234567890abcdefg', 6))
        browser.find_element("id", "entity_typeName").clear()
        browser.find_element("id","entity_typeName").send_keys(newname)        #group name
        browser.find_element("id","btnSubmit").click()
        sleep(3)
        groupname=browser.find_element("css selector","#gridview tbody>tr>td:nth-child(3)").text
        edittime = browser.find_element("css selector", "#gridview tbody>tr>td:nth-child(9)").text[:10]
        mytime = time.strftime("%d-%m-%Y")
        return groupname,newname, edittime, mytime
    except Exception as msg:
        logging.warning("异常原因%s" %msg)
        return "groupname", "newname","","1"


def del_suspiciousgroup(browser):
    try:
        s = browser.find_element("id", "abc").text  # 取自动化账户id
        s1 = s.split(",")[1].strip()
        use_suspiciousgroup(browser)
        author = browser.find_element("css selector", "#gridview tbody>tr>td:nth-child(6)").text
        if author != s1:
            raise Exception("You can't del this rule,Author is not %s" % s1)
        groupname=browser.find_element("css selector","#gridview tbody>tr>td:nth-child(3)").text
        browser.find_element("css selector","#gridview tbody td:nth-child(10)>a:nth-child(2)").click()        #del
        sleep(1)
        browser.switch_to.default_content()
        browser.find_element("xpath","//*[text()='Yes']").click()
        sleep(2)
        browser.find_elements("xpath", "//*[text()='Yes']")[1].click()
        sleep(6)
        browser.switch_to.frame("mainFrame")
        newgroupname=browser.find_element("css selector","#gridview tbody>tr>td:nth-child(3)").text
        print(groupname,newgroupname)
        return groupname, newgroupname
    except Exception as msg:
        groupname = ""
        newgoupname = ""
        logging.warning("异常原因%s" %msg)
        return groupname, newgoupname

def del2_suspiciousgroup(browser):
    try:
        use_suspiciousgroup(browser)
        groupname=browser.find_element("css selector","#gridview tbody>tr>td:nth-child(3)").text
        if groupname=="ctest3":
            raise Exception("You can't del this group")
        browser.find_element("css selector","#gridview tbody td input").click()            #单选框
        browser.find_element("id","btnDel").click()                                  #del2
        sleep(1)
        browser.switch_to.default_content()
        browser.find_element("xpath","//*[text()='No']").click()
        sleep(3)
        browser.switch_to.frame("mainFrame")
        newgroupname=browser.find_element("css selector","#gridview tbody>tr>td:nth-child(3)").text
        return groupname, newgroupname
    except Exception as msg:
        groupname = ""
        newgoupname = "1"
        logging.warning("异常原因%s" %msg)
        return groupname, newgoupname

def nextpage_suspiciousgroup(browser):
    try:
        use_suspiciousgroup(browser)
        browser.find_element("css selector","#gridview tfoot td li:nth-child(3)>a").click()
        sleep(1)
        page=browser.find_element("css selector","#gridview tbody td:nth-child(2)").text
        return page
    except Exception as msg:
        page = ""
        logging.warning("异常原因%s" % msg)
        return page

def use_keyworddefinition(browser):
    browser.find_element("xpath", "//*[text()='Configuration Management']").click()
    sleep(1)
    browser.find_element("xpath", "//*[text()='Keyword Definition']").click()
    sleep(2)
    browser.switch_to.frame("mainFrame")

def load_keyworddefinition(browser):
    try:
        use_keyworddefinition(browser)
        s=browser.find_element("css selector",".breadcrumb li:nth-child(2)").text   #Suspicious Group页面标题
        return s
    except Exception as msg:
        logging.warning("异常原因%s" %msg)
        return ""

def  search_keyworddefinition(browser):
     try:
        use_keyworddefinition(browser)
        key=browser.find_element("css selector","#gridview tr:nth-child(3) td:nth-child(3)").text
        browser.find_element("id","q_simpleSearch").send_keys(key)
        browser.find_element("id","btnSimpleSearch").click()
        sleep(3)
        s=browser.find_element("css selector","#gridview tr td:nth-child(3)").text
        return s,key
     except Exception as msg:
        logging.warning("异常原因%s" %msg)
        return "","123"

def add_keyworddefinition(browser):
    try:
        use_keyworddefinition(browser)
        browser.find_element("id", "btnAddNew").click()                     # add
        sleep(1)
        browser.switch_to.frame("_ax_frm_frame_")
        randname = "".join(random.sample('1234567890abcdefg', 6))
        browser.find_element("id", "entity_name").send_keys(randname)                       # name
        browser.find_element("id", "btnSubmit").click()
        sleep(3)
        browser.switch_to.parent_frame()
        sleep(1)
        newname = browser.find_element("css selector", "#gridview tbody>tr>td:nth-child(3)").text
        createtime = browser.find_element("css selector", "#gridview tbody>tr>td:nth-child(5)").text[:10]
        mytime = time.strftime("%d-%m-%Y")
        return newname, randname, createtime, mytime
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return "name", "rand", "", "1"

def edit_keyworddefinition(browser):
    try:
        s = browser.find_element("id", "abc").text  # 取自动化账户id
        s1 = s.split(",")[1].strip()
        use_keyworddefinition(browser)
        author = browser.find_element("css selector", "#gridview tbody>tr>td:nth-child(4)").text
        if author != s1:
            raise Exception("You can't del this rule,Author is not %s" % s1)
        browser.find_element("css selector","#gridview tbody td:nth-child(8)>a").click()        #edit
        sleep(2)
        randname = "".join(random.sample('1234567890abcdefg', 6))
        browser.find_element("id", "entity_name").clear()
        browser.find_element("id","entity_name").send_keys(randname)                    #  name
        browser.find_element("id","btnSubmit").click()
        sleep(3)
        newname=browser.find_element("css selector","#gridview tbody>tr>td:nth-child(3)").text
        edittime = browser.find_element("css selector", "#gridview tbody>tr>td:nth-child(7)").text[:10]
        mytime = time.strftime("%d-%m-%Y")
        return newname, randname, edittime, mytime
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return "newname", "randname", "", "1"

def del_keyworddefinition(browser):
    try:
        s = browser.find_element("id", "abc").text  # 取自动化账户id
        s1 = s.split(",")[1].strip()
        use_keyworddefinition(browser)
        author = browser.find_element("css selector", "#gridview tbody>tr>td:nth-child(4)").text
        if author != s1:
            raise Exception("You can't del this rule,Author is not %s" % s1)
        oldname = browser.find_element("css selector", "#gridview tbody>tr>td:nth-child(3)").text
        browser.find_element("css selector", "#gridview tbody td:nth-child(8)>a:nth-child(2)").click()  # del
        sleep(1)
        browser.switch_to.default_content()
        browser.find_element("xpath","//*[text()='Yes']").click()
        sleep(2)
        browser.switch_to.frame("mainFrame")
        newname=browser.find_element("css selector","#gridview tbody>tr>td:nth-child(3)").text
        print(oldname,newname)
        return oldname, newname
    except Exception as msg:
        oldname = ""
        newname = ""
        logging.warning("异常原因%s" %msg)
        return oldname, newname

def del2_keyworddefinition(browser):
    try:
        use_keyworddefinition(browser)
        oldname=browser.find_element("css selector","#gridview tbody>tr>td:nth-child(3)").text
        if oldname=="products" or oldname=="jmeter":
            raise Exception("You can't del this group")
        browser.find_element("css selector","#gridview tbody tr td:nth-child(1)").click()
        browser.find_element("id","btnDel").click()                  #del
        sleep(1)
        browser.switch_to.default_content()
        browser.find_element("xpath","//*[text()='No']").click()
        sleep(2)
        browser.switch_to.frame("mainFrame")
        newname=browser.find_element("css selector","#gridview tbody>tr>td:nth-child(3)").text
        return oldname, newname
    except Exception as msg:
        oldname = ""
        newname = "1"
        logging.warning("异常原因%s" %msg)
        return oldname, newname

def nextpage_keyworddefinition(browser):
    try:
        use_keyworddefinition(browser)
        browser.find_element("css selector", "#gridview tfoot td li:nth-child(3)>a").click()
        sleep(1)
        next = browser.find_element("css selector", "#gridview tbody td:nth-child(2)").text
        assert next == "11."
        browser.find_element("css selector", "#gridview tfoot td li:nth-child(2)>a").click()
        sleep(1)
        pre = browser.find_element("css selector", "#gridview tbody td:nth-child(2)").text
        assert pre == "1."
        browser.find_element("css selector", "#gridview tfoot td li:nth-child(4)>a").click()
        sleep(1)
        last = browser.find_elements("css selector", "#gridview tbody td:nth-child(2)")[-1].text
        allnum =browser.find_element("css selector",".pageinfo").text.split(" ")[6]+'.'
        assert last == allnum
        browser.find_element("css selector", "#gridview tfoot td li:nth-child(1)>a").click()
        sleep(1)
        first = browser.find_element("css selector", "#gridview tbody td:nth-child(2)").text
        assert first == "1."
        browser.find_elements("css selector", ".input-mini")[0].send_keys('3')
        browser.find_element("xpath", "//*[text()='Go!']").click()
        sleep(1)
        page3 = browser.find_element("css selector", "#gridview tbody td:nth-child(2)").text
        assert page3 == "21."
        ch = Select(browser.find_elements("css selector", ".input-mini")[1])
        ch.select_by_value("20")
        sleep(1)
        twenty = browser.find_elements("css selector", "#gridview tbody td:nth-child(2)")[-1].text
        assert twenty == "20."
        return True
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return False

def use_keywordrule(browser):
    browser.find_element("xpath", "//*[text()='Configuration Management']").click()
    sleep(1)
    browser.find_element("xpath", "//*[text()='Keyword Rule']").click()
    sleep(2)
    browser.switch_to.frame("mainFrame")

def load_keywordrule(browser):
    try:
        use_keywordrule(browser)
        s=browser.find_element("css selector",".breadcrumb li:nth-child(2)").text   #页面标题
        return s
    except Exception as msg:
        logging.warning("异常原因%s" %msg)
        return ""

def add_keyword_rule(browser):
        use_keywordrule(browser)
        browser.find_element("id", "btnAddNew").click()  # add
        sleep(1)
        browser.switch_to.frame("_ax_frm_frame_")
        randname = "".join(random.sample('1234567890abcdefg', 6))
        browser.find_element("id", "entity_ruleName").send_keys(randname)  # name
        browser.find_element("id", "entity_rulelaosName").send_keys(randname + "Description")
        browser.find_element("id", "entity_rulethailandName").send_keys(randname + "Memo")
        browser.find_element("id", "btnSubmit").click()
        sleep(3)
        browser.switch_to.parent_frame()
        sleep(1)
        return randname


def add_keywordrule(browser):
    try:
        randname=add_keyword_rule(browser)
        newname = browser.find_element("css selector", "#gridview tbody>tr>td:nth-child(3)").text
        createtime = browser.find_element("css selector", "#gridview tbody>tr>td:nth-child(7)").text[:10]
        mytime = time.strftime("%d-%m-%Y")
        return newname, randname, createtime, mytime
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return "newname", "randname", "", "1"

def edit_keywordrule(browser):
    try:
        s = browser.find_element("id", "abc").text  # 取自动化账户id
        s1 = s.split(",")[1].strip()
        use_keywordrule(browser)
        author = browser.find_element("css selector", "#gridview tbody>tr>td:nth-child(6)").text
        if author != s1:
            raise Exception("You can't del this rule,Author is not %s" % s1)
        browser.find_element("css selector", "#gridview tbody td:nth-child(13)>a:nth-child(1)").click()
        sleep(1)
        randname="".join(random.sample('0123456abcdef',6))
        browser.find_element("id", "entity_ruleName").clear()
        browser.find_element("id","entity_ruleName").send_keys(randname)
        browser.find_element("id","btnSubmit").click()
        sleep(2)
        newname=browser.find_element("css selector","#gridview tbody>tr>td:nth-child(3)").text
        edittime = browser.find_element("css selector", "#gridview tbody>tr>td:nth-child(9)").text[:10]
        mytime = time.strftime("%d-%m-%Y")
        return newname, randname, edittime, mytime
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return "newname", "randname", "", "1"

def search_keywordrule(browser):
    try:
        use_keywordrule(browser)
        key = browser.find_element("css selector", "#gridview tr:nth-child(3) td:nth-child(3)").text
        browser.find_element("id", "q_simpleSearch").send_keys(key)
        browser.find_element("id", "btnSimpleSearch").click()
        sleep(3)
        s = browser.find_element("css selector", "#gridview tr td:nth-child(3)").text
        return s, key
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return "", "123"

def set_regular(browser):
    try:
        s = browser.find_element("id", "abc").text  # 取自动化账户id
        s1 = s.split(",")[1].strip()
        use_keywordrule(browser)
        author = browser.find_element("css selector", "#gridview tbody>tr>td:nth-child(6)").text
        if author != s1:
            raise Exception("You can't del this rule,Author is not %s" % s1)
        browser.find_element("css selector","#gridview tbody td:nth-child(13)>a:nth-child(3)").click()
        sleep(2)
        browser.switch_to.default_content()
        browser.switch_to.frame("topPopModalCommonFrame")
        browser.find_element("id","reset").click()
        browser.find_elements("css selector","#rulesplice>label")[0].click()
        browser.find_elements("css selector","#rulesplice>label")[1].click()
        browser.find_element("id","and").click()
        browser.find_element("id","rulesave").click()
        sleep(1)
        s=browser.find_element("id","Content").text
        assert "AND" in s
        browser.switch_to.default_content()
        browser.find_element("xpath", "//*[contains(text(),'Successful operation')]").click()
        return True
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return False

def del_regular(browser):
    try:
        s = browser.find_element("id", "abc").text  # 取自动化账户id
        s1 = s.split(",")[1].strip()
        use_keywordrule(browser)
        author = browser.find_element("css selector", "#gridview tbody>tr>td:nth-child(6)").text
        if author != s1:
            raise Exception("You can't del this rule,Author is not %s" % s1)
        browser.find_element("css selector", "#gridview tbody td:nth-child(13)>a:nth-child(3)").click()
        sleep(2)
        browser.switch_to.default_content()
        browser.switch_to.frame("topPopModalCommonFrame")
        browser.find_element("id","ruledelete").click()
        sleep(1)
        assert browser.find_element("id","Content").text == ""
        browser.switch_to.default_content()
        browser.find_element("xpath", "//*[contains(text(),'Successful operation')]").click()
        return True
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return False


def reset_regular(browser):
    try:
        s = browser.find_element("id", "abc").text  # 取自动化账户id
        s1 = s.split(",")[1].strip()
        use_keywordrule(browser)
        author = browser.find_element("css selector", "#gridview tbody>tr>td:nth-child(6)").text
        if author != s1:
            raise Exception("You can't del this rule,Author is not %s" % s1)
        browser.find_element("css selector", "#gridview tbody td:nth-child(13)>a:nth-child(3)").click()
        sleep(2)
        browser.switch_to.default_content()
        browser.switch_to.frame("topPopModalCommonFrame")
        browser.find_element("id", "reset").click()
        browser.find_elements("css selector", "#rulesplice>label")[0].click()
        browser.find_elements("css selector", "#rulesplice>label")[1].click()
        browser.find_element("id", "and").click()
        browser.find_element("id","reset").click()
        return browser.find_element("id","currentContent").text
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return "1"

def close_regular(browser):
    try:
        use_keywordrule(browser)
        browser.find_element("css selector", "#gridview tbody td:nth-child(13)>a:nth-child(3)").click()
        sleep(2)
        browser.switch_to.default_content()
        browser.find_element("css selector", "button.btn.ax-close").click()
        sleep(1)
        browser.switch_to.frame("mainFrame")
        return browser.find_element("css selector",".breadcrumb li:nth-child(2)").text
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return ""

def del_keywordrule(browser):
    try:
        s = browser.find_element("id", "abc").text            #取自动化账户id
        s1 = s.split(",")[1].strip()
        use_keywordrule(browser)
        oldname=browser.find_element("css selector","#gridview tbody>tr>td:nth-child(3)").text
        author=browser.find_element("css selector","#gridview tbody>tr>td:nth-child(6)").text
        if author!=s1:
            raise Exception("You can't del this rule,Author is not %s"%s1)
        browser.find_element("css selector","#gridview tbody td:nth-child(13)>a:nth-child(2)").click()        #del
        sleep(1)
        browser.switch_to.default_content()
        browser.find_element("xpath","//*[text()='Yes']").click()
        sleep(2)
        browser.switch_to.frame("mainFrame")
        newname=browser.find_element("css selector","#gridview tbody>tr>td:nth-child(3)").text
        print(oldname,newname)
        return oldname, newname
    except Exception as msg:
        oldname = ""
        newname = ""
        logging.warning("异常原因%s" %msg)
        return oldname, newname

def del2_keywordrule(browser):
    try:
        s = browser.find_element("id", "abc").text            #取自动化账户id
        s1 = s.split(",")[1].strip()
        use_keywordrule(browser)
        author=browser.find_element("css selector","#gridview tbody>tr>td:nth-child(6)").text
        if author!=s1:
            raise Exception("You can't del this rule,Author is not %s"%s1)
        oldname = browser.find_element("css selector", "#gridview tbody>tr>td:nth-child(3)").text
        browser.find_element("css selector", "#gridview tbody>tr>td:nth-child(1)").click()
        browser.find_element("id", "btnDel").click()
        sleep(1)
        browser.switch_to.default_content()
        browser.find_element("xpath","//*[text()='No']").click()
        sleep(2)
        browser.switch_to.frame("mainFrame")
        newname=browser.find_element("css selector","#gridview tbody>tr>td:nth-child(3)").text
        print(oldname,newname)
        return oldname, newname
    except Exception as msg:
        oldname = ""
        newname = "1"
        logging.warning("异常原因%s" %msg)
        return oldname, newname

def nextpage_keywordrule(browser):
    try:
        use_keywordrule(browser)
        browser.find_element("css selector", "#gridview tfoot td li:nth-child(3)>a").click()
        sleep(1)
        next = browser.find_element("css selector", "#gridview tbody td:nth-child(2)").text
        assert next == "11."
        browser.find_element("css selector", "#gridview tfoot td li:nth-child(2)>a").click()
        sleep(1)
        pre = browser.find_element("css selector", "#gridview tbody td:nth-child(2)").text
        assert pre == "1."
        browser.find_element("css selector", "#gridview tfoot td li:nth-child(4)>a").click()
        sleep(1)
        last = browser.find_elements("css selector", "#gridview tbody td:nth-child(2)")[-1].text
        allnum = browser.find_element("css selector", ".pageinfo").text.split(" ")[6] + '.'
        assert last == allnum
        browser.find_element("css selector", "#gridview tfoot td li:nth-child(1)>a").click()
        sleep(1)
        first = browser.find_element("css selector", "#gridview tbody td:nth-child(2)").text
        assert first == "1."
        browser.find_elements("css selector", ".input-mini")[0].send_keys('3')
        browser.find_element("xpath", "//*[text()='Go!']").click()
        sleep(1)
        page3 = browser.find_element("css selector", "#gridview tbody td:nth-child(2)").text
        assert page3 == "21."
        ch = Select(browser.find_elements("css selector", ".input-mini")[1])
        ch.select_by_value("20")
        sleep(1)
        twenty = browser.find_elements("css selector", "#gridview tbody td:nth-child(2)")[-1].text
        assert twenty == "20."
        return True
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return False

def use_focusweb(browser):
    browser.find_element("xpath", "//*[text()='Configuration Management']").click()
    sleep(1)
    browser.find_element("xpath", "//*[text()='Focused Website']").click()
    sleep(2)
    browser.switch_to.frame("mainFrame")

def load_focusweb(browser):
    try:
        use_focusweb(browser)
        s = browser.find_element("css selector", ".breadcrumb li:nth-child(2)").text  # 页面标题
        return s
    except Exception as msg:
        return ""

def search_focusweb(browser):
    try:
        use_focusweb(browser)
        key = browser.find_element("css selector", "#gridview tr:nth-child(3) td:nth-child(3)").text
        browser.find_element("id", "q_simpleSearch").send_keys(key)
        browser.find_element("id", "btnSimpleSearch").click()
        sleep(3)
        s = browser.find_element("css selector", "#gridview tr td:nth-child(3)").text
        return s, key
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return "", "123"

def add_focusweb(browser):
    try:
        use_focusweb(browser)
        browser.find_element("id", "btnAddNew").click()              # add
        sleep(1)
        browser.switch_to.frame("_ax_frm_frame_")
        randname = "".join(random.sample('1234567890abcdefg', 6))
        browser.find_element("id","entity_domainName").send_keys("http://"+randname+".com")
        browser.find_element("id","btnSubmit").click()
        sleep(2)
        browser.switch_to.parent_frame()
        newname=browser.find_element("css selector","#gridview>tbody td:nth-child(3)").text
        createtime = browser.find_element("css selector", "#gridview tbody>tr>td:nth-child(5)").text[:10]
        mytime = time.strftime("%d-%m-%Y")
        return newname, randname, createtime, mytime
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return "newname", "randname", "", "1"

def edit_focusweb(browser):
    try:
        s = browser.find_element("id", "abc").text  # 取自动化账户id
        s1 = s.split(",")[1].strip()
        use_focusweb(browser)
        author = browser.find_element("css selector", "#gridview tbody>tr>td:nth-child(4)").text
        if author != s1:
            raise Exception("You can't del this rule,Author is not %s" % s1)
        browser.find_element("css selector", "#gridview tbody td:nth-child(8)>a:nth-child(1)").click()      #EDIT
        sleep(1)
        randname = "".join(random.sample('1234567890abcdefg', 6))
        browser.find_element("id","entity_domainName").clear()
        browser.find_element("id","entity_domainName").send_keys("http://"+randname+".com")
        browser.find_element("id","btnSubmit").click()
        sleep(2)
        newname=browser.find_element("css selector","#gridview>tbody td:nth-child(3)").text
        edittime = browser.find_element("css selector", "#gridview tbody>tr>td:nth-child(7)").text[:10]
        mytime = time.strftime("%d-%m-%Y")
        return newname, randname, edittime, mytime
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return "newname", "randname", "", "1"

def del_focusweb(browser):
    try:
        s = browser.find_element("id", "abc").text  # 取自动化账户id
        s1 = s.split(",")[1].strip()
        use_focusweb(browser)
        author = browser.find_element("css selector", "#gridview tbody>tr>td:nth-child(4)").text
        if author != s1:
            raise Exception("You can't del this rule,Author is not %s" % s1)
        oldname = browser.find_element("css selector", "#gridview tbody>tr>td:nth-child(3)").text
        browser.find_element("css selector", "#gridview tbody td:nth-child(8)>a:nth-child(2)").click()  # del
        sleep(1)
        browser.switch_to.default_content()
        browser.find_element("xpath","//*[text()='Yes']").click()
        sleep(5)
        browser.switch_to.frame("mainFrame")
        newname=browser.find_element("css selector","#gridview tbody>tr>td:nth-child(3)").text
        print(oldname,newname)
        return oldname, newname
    except Exception as msg:
        logging.warning("异常原因%s" %msg)
        return "", ""

def del2_focusweb(browser):
    try:
        s = browser.find_element("id", "abc").text  # 取自动化账户id
        s1 = s.split(",")[1].strip()
        use_focusweb(browser)
        author = browser.find_element("css selector", "#gridview tbody>tr>td:nth-child(4)").text
        if author != s1:
            raise Exception("You can't del this rule,Author is not %s" % s1)
        oldname = browser.find_element("css selector", "#gridview tbody>tr>td:nth-child(3)").text
        browser.find_element("css selector", "#gridview tbody>tr>td:nth-child(1)").click()
        browser.find_element("id", "btnDelPYQ1").click()
        sleep(1)
        browser.switch_to.default_content()
        browser.find_element("xpath","//*[text()='No']").click()
        sleep(5)
        browser.switch_to.frame("mainFrame")
        newname=browser.find_element("css selector","#gridview tbody>tr>td:nth-child(3)").text
        print(oldname,newname)
        return oldname, newname
    except Exception as msg:
        logging.warning("异常原因%s" %msg)
        return "oldname", "newname"

def page_focusweb(browser):
    try:
        use_focusweb(browser)
        browser.find_element("css selector", "#gridview tfoot td li:nth-child(3)>a").click()
        sleep(1)
        page = browser.find_element("css selector", "#gridview tbody td:nth-child(2)").text
        return page
    except Exception as msg:
        page = ""
        logging.warning("异常原因%s" % msg)
        return page

def add_focuswebip(browser):
    try:
        use_focusweb(browser)
        browser.find_element("css selector", "#gridview tbody>tr>td:nth-child(8)>a:nth-child(3)").click()
        sleep(2)
        browser.find_element("id","btnAddNewIp").click()
        randip='.'.join(str(random.choice(range(255))) for _ in range(4))
        browser.find_element("id","entity_ipaddr").send_keys(randip)
        browser.find_element("id","btnSubmitIp").click()
        sleep(1)
        return browser.find_element("css selector","#pnlListTb1 tbody td:nth-child(3)").text,randip

    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return "","1"


def edit_focuswebip(browser):
    try:
        s = browser.find_element("id", "abc").text  # 取自动化账户id
        s1 = s.split(",")[1].strip()
        use_focusweb(browser)
        author = browser.find_element("css selector", "#gridview tbody>tr>td:nth-child(4)").text
        if author != s1:
            raise Exception("You can't del this rule,Author is not %s" % s1)
        browser.find_element("css selector", "#gridview tbody>tr>td:nth-child(8)>a:nth-child(3)").click()
        sleep(2)
        browser.find_element("css selector","#pnlListTb1 tbody td:nth-child(8)>a").click()
        randip='.'.join(str(random.choice(range(255))) for _ in range(4))
        sleep(1)
        browser.find_element("id", "entity_ipaddr").clear()
        browser.find_element("id","entity_ipaddr").send_keys(randip)
        browser.find_element("id","btnSubmitIp").click()
        sleep(1)
        browser.switch_to.default_content()
        browser.find_element("xpath", "//*[text()='Yes']").click()
        sleep(2)
        browser.switch_to.frame("mainFrame")
        return browser.find_element("css selector","#pnlListTb1 tbody td:nth-child(3)").text,randip
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return "","1"

def del_focuswebip(browser):
    try:
        s = browser.find_element("id", "abc").text  # 取自动化账户id
        s1 = s.split(",")[1].strip()
        use_focusweb(browser)
        author = browser.find_element("css selector", "#gridview tbody>tr>td:nth-child(4)").text
        if author != s1:
            raise Exception("You can't del this rule,Author is not %s" % s1)
        browser.find_element("css selector", "#gridview tbody>tr>td:nth-child(8)>a:nth-child(3)").click()
        sleep(2)
        browser.find_element("css selector","#pnlListTb1 tbody td:nth-child(8)>a:nth-child(2)").click()
        sleep(1)
        browser.switch_to.default_content()
        browser.find_element("xpath", "//*[text()='Yes']").click()
        sleep(2)
        browser.switch_to.frame("mainFrame")
        sleep(2)
        if len(browser.find_elements("xpath","//*[text()='Information requested is not found.']")):
            return True
        else:
            return False
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return False

def close_focuswebip(browser):
    try:
        use_focusweb(browser)
        browser.find_element("css selector", "#gridview tbody>tr>td:nth-child(8)>a:nth-child(3)").click()
        sleep(2)
        browser.find_element("id","btnclose").click()
        return browser.find_element("css selector",".breadcrumb>li:nth-child(2)").text
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return ""

def use_staticip(browser):
    browser.find_element("xpath", "//*[text()='Configuration Management']").click()
    sleep(1)
    browser.find_element("xpath", "//*[text()='Static IP Address']").click()
    sleep(2)
    browser.switch_to.frame("mainFrame")


def load_staticip(browser):
    try:
        use_staticip(browser)
        return browser.find_element("css selector",".breadcrumb>li:nth-child(2)").text
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return ""

def search_focusweb(browser):
    try:
        use_staticip(browser)
        key = browser.find_element("css selector", "#gridview tr:nth-child(3) td:nth-child(3)").text
        browser.find_element("id", "q_simpleSearch").send_keys(key)
        browser.find_element("id", "btnSimpleSearch").click()
        sleep(3)
        s = browser.find_element("css selector", "#gridview tr td:nth-child(3)").text
        return s, key
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return "", "123"

def add_staticip(browser):
    try:
        use_staticip(browser)
        browser.find_element("id","btnAddNew").click()
        browser.switch_to.frame("_ax_frm_frame_")
        randname = "".join(random.sample('1234567890abcdefg', 6))
        randip=".".join(str(random.choice(range(255))) for _ in range(4))
        browser.find_element("id","entity_ipInfo").send_keys(randname)
        browser.find_element("id", "entity_ipaddr").send_keys(randip)
        browser.find_element("id","btnSubmit").click()
        sleep(2)
        browser.switch_to.default_content()
        browser.switch_to.frame("mainFrame")
        newip=browser.find_element("css selector","#gridview tr td:nth-child(4)").text
        createtime = browser.find_element("css selector", "#gridview tbody>tr>td:nth-child(6)").text[:10]
        mytime = time.strftime("%d-%m-%Y")
        return newip, randip, createtime, mytime
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return "newip", "randip", "", "1"

def edit_staticip(browser):
    try:
        s = browser.find_element("id", "abc").text  # 取自动化账户id
        s1 = s.split(",")[1].strip()
        use_staticip(browser)
        author = browser.find_element("css selector", "#gridview tbody>tr>td:nth-child(5)").text
        if author != s1:
            raise Exception("You can't del this rule,Author is not %s" % s1)
        browser.find_element("css selector","#gridview tr td:nth-child(9)>a").click()
        randip=".".join(str(random.choice(range(255))) for _ in range(4))
        sleep(1)
        browser.find_element("id", "entity_ipaddr").clear()
        browser.find_element("id", "entity_ipaddr").send_keys(randip)
        browser.find_element("id","btnSubmit").click()
        browser.switch_to.default_content()
        browser.find_element("xpath", "//*[text()='Yes']").click()
        sleep(2)
        browser.switch_to.frame("mainFrame")
        sleep(2)
        newip=browser.find_element("css selector","#gridview tr td:nth-child(4)").text
        edittime = browser.find_element("css selector", "#gridview tbody>tr>td:nth-child(8)").text[:10]
        mytime = time.strftime("%d-%m-%Y")
        return newip, randip, edittime, mytime
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return "newip", "randip","","1"


def del_staticip(browser):
    try:
        s = browser.find_element("id", "abc").text  # 取自动化账户id
        s1 = s.split(",")[1].strip()
        use_staticip(browser)
        author = browser.find_element("css selector", "#gridview tbody>tr>td:nth-child(5)").text
        if author != s1:
            raise Exception("You can't del this rule,Author is not %s" % s1)
        oldip=browser.find_element("css selector", "#gridview tr td:nth-child(4)").text
        browser.find_element("css selector", "#gridview tr td:nth-child(9)>a:nth-child(2)").click()
        sleep(1)
        browser.switch_to.default_content()
        browser.find_element("xpath", "//*[text()='Yes']").click()
        sleep(3)
        browser.switch_to.frame("mainFrame")
        return browser.find_element("css selector", "#gridview tr td:nth-child(4)").text, oldip
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return "", ""

def del2_staticip(browser):
    try:
        s = browser.find_element("id", "abc").text  # 取自动化账户id
        s1 = s.split(",")[1].strip()
        use_staticip(browser)
        author = browser.find_element("css selector", "#gridview tbody>tr>td:nth-child(5)").text
        if author != s1:
            raise Exception("You can't del this rule,Author is not %s" % s1)
        oldip=browser.find_element("css selector", "#gridview tr td:nth-child(4)").text
        browser.find_element("css selector", "#gridview tbody>tr>td:nth-child(1)").click()
        browser.find_element("id", "btnDelPYQ1").click()
        sleep(1)
        browser.switch_to.default_content()
        browser.find_element("xpath", "//*[text()='No']").click()
        sleep(3)
        browser.switch_to.frame("mainFrame")
        return browser.find_element("css selector", "#gridview tr td:nth-child(4)").text, oldip
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return "", "1"


def use_iprange(browser):
    browser.find_element("xpath", "//*[text()='Configuration Management']").click()
    sleep(1)
    browser.find_element("xpath", "//*[text()='IP Address Range']").click()
    sleep(2)
    browser.switch_to.frame("mainFrame")

def load_iprange(browser):
    try:
        use_iprange(browser)
        s = browser.find_element("css selector", ".breadcrumb li:nth-child(2)").text  # 页面标题
        return s
    except Exception as msg:
        return ""

def search_iprange(browser):
    try:
        use_staticip(browser)
        key=browser.find_element("css selector","#gridview tr:nth-child(3) td:nth-child(3)").text
        browser.find_element("id","q_simpleSearch").send_keys(key)
        browser.find_element("id","btnSimpleSearch").click()
        sleep(3)
        s=browser.find_element("css selector","#gridview tr td:nth-child(3)").text
        return s,key
    except Exception as msg:
        logging.warning("异常原因%s" %msg)
        return "","123"


def add_iprange(browser):
    try:
        use_iprange(browser)
        browser.find_element("id","btnAddNew").click()
        browser.switch_to.frame("_ax_frm_frame_")
        randinfo = "".join(random.sample('1234567890abcdefg', 6))
        randrangestart=".".join(str(random.choice(range(255))) for _ in range(4))
        s = randrangestart.split(".")
        s[3]=str(int(s[3]) + 1)
        randrangeend = ".".join(s)
        browser.find_element("id","entity_rangeInfo").send_keys(randinfo)
        browser.find_element("id", "entity_startIp").send_keys(randrangestart)
        browser.find_element("id", "entity_endIp").send_keys(randrangeend)
        browser.find_element("id","btnSubmit").click()
        sleep(2)
        browser.switch_to.default_content()
        browser.switch_to.frame("mainFrame")
        rinfo = browser.find_element("css selector", "#gridview tr td:nth-child(3)").text          #range info
        newipstart=browser.find_element("css selector","#gridview tr td:nth-child(4)").text
        createtime = browser.find_element("css selector", "#gridview tbody>tr>td:nth-child(7)").text[:10]
        mytime = time.strftime("%d-%m-%Y")
        return rinfo,randinfo,newipstart, randrangestart, createtime, mytime
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return "newip", "randrangestart", "", "1"

def edit_iprange(browser):
    try:
        s = browser.find_element("id", "abc").text  # 取自动化账户id
        s1 = s.split(",")[1].strip()
        use_iprange(browser)
        author = browser.find_element("css selector", "#gridview tbody>tr>td:nth-child(6)").text
        if author != s1:
            raise Exception("You can't del this rule,Author is not %s" % s1)
        browser.find_element("css selector", "#gridview tr td:nth-child(10)>a").click()
        randinfo = "".join(random.sample('1234567890abcdefg', 6))
        sleep(2)
        browser.find_element("id", "entity_rangeInfo").clear()
        browser.find_element("id", "entity_rangeInfo").send_keys(randinfo)
        browser.find_element("id", "btnSubmit").click()
        browser.switch_to.default_content()
        browser.find_element("xpath", "//*[text()='Yes']").click()
        sleep(2)
        browser.switch_to.frame("mainFrame")
        sleep(2)
        newrinfo = browser.find_element("css selector", "#gridview tr td:nth-child(3)").text
        edittime = browser.find_element("css selector", "#gridview tbody>tr>td:nth-child(9)").text[:10]
        mytime = time.strftime("%d-%m-%Y")
        return newrinfo, randinfo, edittime, mytime
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return "newinfo", "rinfo", "", "1"

def del_iprange(browser):
    try:
        s = browser.find_element("id", "abc").text  # 取自动化账户id
        s1 = s.split(",")[1].strip()
        use_iprange(browser)
        author = browser.find_element("css selector", "#gridview tbody>tr>td:nth-child(6)").text
        if author != s1:
            raise Exception("You can't del this rule,Author is not %s" % s1)
        sleep(2)
        oldrange=browser.find_element("css selector","#gridview tbody td:nth-child(3)").text
        browser.find_element("css selector", "#gridview tbody>tr>td:nth-child(10)>a:nth-child(2)").click()
        sleep(1)
        browser.switch_to.default_content()
        browser.find_element("xpath", "//*[text()='Yes']").click()
        sleep(5)
        browser.switch_to.frame("mainFrame")
        return oldrange,browser.find_element("css selector","#gridview tbody td:nth-child(3)").text
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return "",""

def del2_iprange(browser):
    try:
        s = browser.find_element("id", "abc").text  # 取自动化账户id
        s1 = s.split(",")[1].strip()
        use_iprange(browser)
        author = browser.find_element("css selector", "#gridview tbody>tr>td:nth-child(6)").text
        if author != s1:
            raise Exception("You can't del this rule,Author is not %s" % s1)
        sleep(2)
        oldrange=browser.find_element("css selector","#gridview tbody td:nth-child(3)").text
        browser.find_element("css selector", "#gridview tbody>tr>td:nth-child(1)").click()
        browser.find_element("id","btnDelPYQ1").click()
        sleep(1)
        browser.switch_to.default_content()
        browser.find_element("xpath", "//*[text()='No']").click()
        sleep(2)
        browser.switch_to.frame("mainFrame")
        return oldrange,browser.find_element("css selector","#gridview tbody td:nth-child(3)").text
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return "",""

def use_operator(browser):
    browser.find_element("xpath", "//*[text()='Configuration Management']").click()
    sleep(1)
    browser.find_element("xpath", "//*[text()='Operator Information']").click()
    sleep(2)
    browser.switch_to.frame("mainFrame")

def load_operator(browser):
    try:
        use_operator(browser)
        s = browser.find_element("css selector", ".breadcrumb li:nth-child(2)").text  # Suspicious Group页面标题
        return s
    except Exception as msg:
        logging.warning("异常原因%s" % msg)
        return ""

def search_operator(browser):
    try:
        use_operator(browser)
        key=browser.find_element("css selector","#gridview tr:nth-child(3) td:nth-child(5)").text
        browser.find_element("id","q_simpleSearch").send_keys(key)
        browser.find_element("id","btnSimpleSearch").click()
        sleep(3)
        s=browser.find_element("css selector","#gridview tr td:nth-child(5)").text
        return s,key
    except Exception as msg:
        logging.warning("异常原因%s" %msg)
        return "","123"
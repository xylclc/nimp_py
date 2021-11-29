import sys
sys.path.append('D:\\nowwork\\NIMP\\nimp_py')
import time,logging
import pytest
import os
from business import configuration as co
from business import cloudsearch as cs
from business import TrafficReportImage as tr

class TestNimp:

#Configuration Management
    # def test_traffic(self,browser):
    #     s=co.mytraffic(browser)
    #     assert s==True
    #
    # def test_load_suspiciousgroup(self,browser):
    #     s=co.load_suspiciousgroup(browser)
    #     assert s=="Suspicious Group"
    #
    # def test_search_suspiciousgroup(self,browser):
    #     s,key=co.search_suspiciousgroup(browser)
    #     assert key in s
    #
    # def test_add_suspiciousgroup(self,browser):
    #     name,s,createtime,mytime=co.add_suspiciousgroup(browser)
    #     assert name==s and createtime==mytime
    #
    # def test_edit_suspiciousgroup(self,browser):
    #     name,s,edittime,mytime=co.edit_suspiciousgroup(browser)
    #     assert name == s and edittime==mytime
    #
    # def test_del2_suspiciousgroup(self,browser):
    #     groupname, newgoupname = co.del2_suspiciousgroup(browser)
    #     assert newgoupname == groupname
    #
    #
    # def test_del_suspiciousgroup(self,browser):
    #     groupname, newgoupname = co.del_suspiciousgroup(browser)
    #     assert newgoupname != groupname
    #
    # def test_nextpage_suspiciousgroup(self,browser):
    #     page=co.nextpage_suspiciousgroup(browser)
    #     assert page=="11."
    #
    # def test_load_keyworddefinition(self,browser):
    #     s=co.load_keyworddefinition(browser)
    #     assert s=="Keyword Definition"
    #
    # def test_search_keyworddefinition(self,browser):
    #     s,key=co.search_keyworddefinition(browser)
    #     assert key in s
    #
    #
    # def test_add_keyworddefinition(self,browser):
    #     newname, randname,createtime,mytime = co.add_keyworddefinition(browser)
    #     assert newname == randname and createtime==mytime
    #
    # def test_edit_keyworddefinition(self,browser):
    #     newname, randname,edittime,mytime  = co.edit_keyworddefinition(browser)
    #     assert newname==randname and edittime==mytime
    #
    # def test_del2_keyworddefinition(self,browser):
    #     oldname, newname = co.del2_keyworddefinition(browser)
    #     assert oldname == newname
    #
    # def test_del_keyworddefinition(self,browser):
    #     oldname, newname = co.del_keyworddefinition(browser)
    #     assert oldname != newname
    #
    # def test_page_keyworddefinition(self,browser):
    #     result = co.nextpage_keyworddefinition(browser)
    #     assert result==True
    #
    # def test_load_keywordrule(self,browser):
    #     s=co.load_keywordrule(browser)
    #     assert s == "Keyword Rule"
    #
    # def test_search_keywordrule(self,browser):
    #     s,key=co.search_keywordrule(browser)
    #     assert key in s
    #
    # def test_add_keywordrule(self,browser):
    #     newname, randname,createtime,mytime = co.add_keywordrule(browser)
    #     assert newname == randname and createtime==mytime
    #
    # def test_edit_keywordrule(self,browser):
    #     newname, randname,edittime,mytime = co.edit_keywordrule(browser)
    #     assert newname==randname and edittime==mytime
    #
    # def test_set_regular(self,browser):
    #     t=co.set_regular(browser)
    #     assert t==True
    #
    # def test_del_regular(self,browser):
    #     t=co.del_regular(browser)
    #     assert t==True
    #
    # def test_reset_regular(self,browser):
    #     s=co.reset_regular(browser)
    #     assert s==""
    #
    # def test_close_regular(self,browser):
    #     title=co.close_regular(browser)
    #     assert title=="Keyword Rule"
    #
    # def test_del_keywordrule(self,browser):
    #     oldname, newname = co.del_keywordrule(browser)
    #     assert oldname != newname
    #
    # def test_del2_keywordrule(self,browser):
    #     oldname, newname = co.del2_keywordrule(browser)
    #     assert oldname == newname
    #
    # def test_nextpage_keywordrule(self,browser):
    #     result = co.nextpage_keywordrule(browser)
    #     assert result == True
    #
    # def test_load_focusweb(self,browser):
    #     s = co.load_focusweb(browser)
    #     assert s == "Focused Website"
    #
    # def test_search_focusweb(self,browser):
    #     s, key = co.search_focusweb(browser)
    #     assert key in s
    #
    # def test_add_focusweb(self,browser):
    #     newname, randname,createtime,mytime = co.add_focusweb(browser)
    #     assert newname == "http://"+randname+".com" and createtime==mytime
    #
    # def test_edit_focusweb(self,browser):
    #     newname, randname,edittime,mytime = co.edit_focusweb(browser)
    #     assert newname == "http://"+randname+".com" and edittime==mytime

    def test_add_focuswebip(self,browser):
        newip, randip = co.add_focuswebip(browser)
        assert newip == randip

    def test_edit_focuswebip(self,browser):
        newip, randip = co.edit_focuswebip(browser)
        assert newip == randip

    def test_del_focuswebip(self,browser):
        t = co.del_focuswebip(browser)
        assert t==True

#     def test_close_focuswebip(self,browser):
#         title=co.close_focuswebip(browser)
#         assert title=="Focused Website"
#
#
#     def test_del2_focusweb(self, browser):
#         oldname, newname = co.del2_focusweb(browser)
#         assert newname == oldname
#
#
#     def test_del_focusweb(self, browser):
#         oldname, newname = co.del_focusweb(browser)
#         assert newname != oldname
#
#
#     def test_page_focusweb(self, browser):
#         page = co.page_focusweb(browser)
#         assert page == "11."
#
#     def test_load_staticip(self,browser):
#         title=co.load_staticip(browser)
#         assert title=="Static IP Address"
#
#     def test_search_ipinfo(self,browser):
#         s, key = co.search_focusweb(browser)
#         assert key in s
#
#     def test_add_staticip(self,browser):
#         newip, randip,createtime,mytime = co.add_staticip(browser)
#         assert newip == randip and createtime==mytime
#
#     def test_edit_staticip(self,browser):
#         newip, randip,edittime,mytime = co.edit_staticip(browser)
#         assert newip == randip and edittime==mytime
#
#     def test_del_staticip(self,browser):
#         newip, oldip = co.del_staticip(browser)
#         assert newip != oldip
#
#     def test_del2_staticip(self,browser):
#         newip, oldip = co.del2_staticip(browser)
#         assert newip == oldip
#
#     def test_load_iprange(self,browser):
#         s=co.load_iprange(browser)
#         assert s== "IP Address Range"
#
#     def test_search_iprange(self,browser):
#         s, key = co.search_iprange(browser)
#         assert key in s
#
#     def test_add_iprange(self,browser):
#         rinfo,randinfo,newrangestart, randrangestart, createtime, mytime = co.add_iprange(browser)
#         assert rinfo==randinfo and newrangestart == randrangestart and createtime == mytime
#
#     def test_edit_iprange(self,browser):
#         newrinfo, randinfo, edittime, mytime = co.edit_iprange(browser)
#         assert newrinfo == randinfo  and edittime == mytime
#
#     def test_del_iprange(self,browser):
#         newrange, oldrange = co.del_iprange(browser)
#         assert newrange != oldrange
#
#     def test_del2_iprange(self,browser):
#         newip, oldip = co.del2_iprange(browser)
#         assert newip == oldip
#
#     def test_load_operator(self,browser):
#         s = co.load_operator(browser)
#         assert s == "Operator Information"
#
#     def test_search_operator(self,browser):
#         s, key = co.search_operator(browser)
#         assert key in s
#
#
#     #Cloud Search
#
#     def test_searchvid_realname(self,browser):
#         s=cs.searchvid_realname(browser)
#         assert s =="cai"
#
#     def test_searchvid_vid(self,browser):
#         s=cs.searchvid_vid(browser)
#         assert s=="01139"
#
#     def test_searchvid_email(self, browser):
#         s = cs.searchvid_email(browser)
#         assert s == "lili.cui@cssca.com"
#
#     def test_searchvid_clear(self, browser):
#         s = cs.searchvid_clear(browser)
#         assert s == ""
#
#     def test_searchvid_close(self, browser):
#         t = cs.searchvid_close(browser)
#         assert t == True
#
#     def test_editvid(self, browser):
#         s = cs.editvid(browser)
#         assert s == "NJ"
#
#     @pytest.mark.me
#     def test_accountinfo(self, browser):
#         s1= cs.accountinfo(browser)
#         assert s1== "01139"
#
#     @pytest.mark.me
#     def test_vid_nextpage(self, browser):
#         result = cs.vid_nextpage(browser)
#         assert result == True
#
#
#     def test_view_emailaccount(self,browser):
#         n=cs.view_emailaccount(browser)
#         logging.warning('n的天数是{}'.format(n))
#         assert n < 3, '出错了,n的天数是{}'.format(n)
#
#     def test_search_emailaccount(self,browser):
#         s=cs.search_emailaccount(browser)
#         assert s=="lili.cui@cssca.com"
#
#     def test_search_emailaccount_date(self,browser):
#         begin="01-09-2021 00:00:00"
#         end="12-10-2021 23:59:59"
#         t1,t2=cs.search_emailaccount_date(browser,begin,end)
#         begin = time.strptime(begin, '%d-%m-%Y %H:%M:%S')
#         end = time.strptime(end, '%d-%m-%Y %H:%M:%S')
#         assert time.mktime(t2)>time.mktime(begin) and time.mktime(t1)<time.mktime(end)
#
#     def test_search_emailaccount_close(self,browser):
#         t=cs.search_emailaccount_close(browser)
#         assert t
#
#     def test_view_emaildetail(self,browser):
#         s=cs.view_emaildetail(browser)
#         assert s!=""
#
#     def test_search_httpaccount(self,browser):
#         s=cs.search_httpaccount(browser)
#         assert "jmeter" in s
#
#     def test_search_httpaccount_date(self,browser):
#         begin="01-10-2021 00:00:00"
#         end="12-10-2021 23:59:59"
#         t1,t2=cs.search_httpaccount_date(browser,begin,end)
#         begin = time.strptime(begin, '%d-%m-%Y %H:%M:%S')
#         end = time.strptime(end, '%d-%m-%Y %H:%M:%S')
#         assert time.mktime(t2)>time.mktime(begin) and time.mktime(t1)<time.mktime(end)
#
#
#     @pytest.mark.me
#     def test_search_httpaccount_close(self,browser):
#         t=cs.search_httpaccount_close(browser)
#         assert t
#
#     @pytest.mark.me
#     def test_view_httpaccount(self,browser):
#         n=cs.view_httpaccount(browser)
#         logging.warning('n的天数是{}'.format(n))
#         assert n < 3, '出错了,n的天数是{}'.format(n)
#
#
#     def test_view_httpdetail(self,browser):
#         s=cs.view_httpdetail(browser)
#         assert s != ""
#
#     def test_view_emailtrace(self,browser):
#         n=cs.view_emailtrace(browser)
#         logging.warning('n的天数是{}'.format(n))
#         assert n < 3, '出错了,n的天数是{}'.format(n)
#
#     def test_search_emailtrace_sender(self,browser):
#         sender="lili.cui@cssca.com"
#         s=cs.search_emailtrace_sender(browser,sender)
#         assert s==sender
#
#     def test_search_emailtrace_receiver(self,browser):
#         receiver="lili.cui@cssca.com"
#         s=cs.search_emailtrace_receiver(browser,receiver)
#         assert s==receiver
#
#     def test_search_emailtrace_subject(self,browser):
#         s="测试"
#         subject=cs.search_emailtrace_subject(browser,s)
#         assert s in subject
#
#     def test_search_emailtrace_clear(self,browser):
#        s = cs.search_emailtrace_clear(browser)
#        assert s ==""
#
#     def test_search_emailtrace_close(self,browser):
#         t=cs.search_emailtrace_close(browser)
#         assert t
#
#     def test_httpresourcesearch(self,browser):
#         s=cs.httpresourcesearch(browser)
#         assert "jmeter" in s
#
#     # def test_view_httpresourcesearch(self,browser):
#     #     flag=cs.view_httpresourcesearch(browser)
#     #     assert flag==True
#
# # Traffic Statistic
#
#     def test_monthly_traffic(self,browser):
#         t=tr.monthly_traffic(browser)
#         assert t==True
#
#
#     def test_daily_traffic(self,browser):
#         t = tr.daily_traffic(browser)
#         assert t == True
#
#
#     def test_hourly_traffic(self,browser):
#         t = tr.hourly_traffic(browser)
#         assert t == True
#
#     def test_monthly_service(self,browser):
#         t = tr.monthly_service(browser)
#         assert t == True
#
#     def test_daily_service(self,browser):
#         t=tr.daily_service(browser)
#         assert t==True
#
#     def test_hourly_service(self,browser):
#         t=tr.hourly_service(browser)
#         assert t==True
#
#
#     #Summary Report
#
#     def test_load_report(self,browser):
#         t = tr.load_report(browser)
#         assert t
#
#     def test_search_monthlyreport(self,browser):
#         s=tr.search_monthlyreport(browser,"2021-09")
#         assert "Monthly-2021-09" in s
#
#     def test_search_dailyreport(self,browser):
#         s = tr.search_dailyreport(browser, "2021-09-01")
#         assert "Daily-2021-09-01" in s
#
#     def test_search_weeklyreport(self, browser):
#         s = tr.search_weeklyreport(browser, "2021-09")
#         assert "Weekly-2021-09-26" in s
#
#
#     #Image Recognition
#     def test_searchimg_name(self,browser):
#         key="导弹"
#         s = tr.searchimg_name(key,browser)
#         assert key in s
#
#     def test_view_httpimage(self,browser):
#         n,s=tr.view_httpimage(browser)
#         logging.warning('n的天数是{}'.format(n))
#         assert n < 3, '出错了,n的天数是{}'.format(n)
#         assert s=="http", '出错了,s的值是{}'.format(s)
#
#     def test_httpimgdetail(self,browser):
#         s=tr.httpimgdetail(browser)
#         assert s
#
#     def test_mailimgdetail(self,browser):
#         s=tr.mailimgdetail(browser)
#         assert s

    # def test_view_mailimage(self,browser):
    #     n, s = tr.view_mailimage(browser)
    #     logging.warning('n的天数是{}'.format(n))
    #     assert n < 3, '出错了,n的天数是{}'.format(n)
    #     assert s == "mail", '出错了,s的值是{}'.format(s)


if __name__=="__main__":
     pytest.main()
     os.system('allure generate ../temp -o ../report --clean')


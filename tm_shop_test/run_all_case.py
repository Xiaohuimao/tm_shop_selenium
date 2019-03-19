#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from BeautifulReport import BeautifulReport
import os
from tomorrow3 import threads
import time
#import HTMLTestRunnerCN
from send_email import send_email,acquire_report_address


#获取路径

curpath=os.path.abspath(".")
casepath=os.path.join(curpath,"test_Case")
reportpath=os.path.join(curpath,"report")

if not os.path.exists(casepath):
    os.mkdir(casepath)
else:
    pass


'''
def allcase():
    case_dir=casepath
    testcase = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir,
                                                pattern = 'test*.py',
                                                top_level_dir = None)
    for test_suite in discover:
        for test_case in test_suite:
            testcase.addTest(test_case)
    return testcase
now=time.strftime("%Y-%m-%d %H_%M_%S")
report_name=reportpath+"\\"+now+"report.html"
'''

def add_case(case_path=casepath, rule="test*.py"):
    #加载所有的测试用例
    discover = unittest.defaultTestLoader.discover(case_path,
                                                  pattern=rule,
                                                  top_level_dir=None)
    return discover

now=time.strftime("%Y-%m-%d %H_%M_%S")
report_name=now+"report.html"
@threads(3)
def run(test_suit):
    #now=time.strftime("%Y-%m-%d %H_%M_%S")
    #report_name=now+"report.html"
    result = BeautifulReport(test_suit)
    result.report(filename=report_name, description='天马商城自动化测试报告', log_path='report')
    time.sleep(2)
    new_report_addr=acquire_report_address(reportpath)
    send_email(new_report_addr)

if __name__=="__main__":
    '''
    report_path = reportpath
    fp = open(report_name, "wb")
    runner = HTMLTestRunnerCN.HTMLTestReportCN(stream=fp,
                                           title = "自动化测试报告",
                                           description = "用例执行情况：")
    runner.run(allcase())
    fp.close()
    new_report_addr = acquire_report_address(reportpath)
    # print(new_report_addr)
    send_email(new_report_addr)
    '''
    cases=add_case()
    for case in cases:
        run(case)
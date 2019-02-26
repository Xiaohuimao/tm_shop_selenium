#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import os,time
import HTMLTestRunner
from send_email import main

#获得测试用例的路径
case_path = os.path.join(os.getcwd(),"testCase")

def all_case():
	discover = unittest.defaultTestLoader.discover(case_path,pattern="test_*.py",top_level_dir=None)
	return discover
	
if __name__=="__main__":
	#runner=unittest.TextTestRunner()
	#runner.run(all_case())
	report_path="C:/Users/Administrator/qkweb_selenium-python/test_web/testReport/result.html"
	fp=open(report_path,"wb")
	runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title="资源页自动化测试报告",description="用例执行情况：")
	runner.run(all_case())
	fp.close()
	main()

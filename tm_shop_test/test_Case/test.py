"""
import unittest
import mysql_page
from selenium import webdriver
'''
my=mysql_page.To_mysql()
i=my.select_user_kyprice()
print(i)
'''
class Test(unittest.TestCase):
    def test_01(self):
        e=self.assertEqual("0","0")
        print(e)
if __name__=="__main__":
    unittest.main()
"""
'''
import requests
e={"article_id":123,"branch":0,"memberCode":0}
res=requests.post("http://review.360tianma.com/ycbhm_gs45l/article/getArticleDetail",data=e)
print (res.text)
print(res.status_code)
'''
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import os.path


# from framework.logger import Logger

# 创建一个logger实例
# logger = Logger(logger="BasePage").getlog()



webdriver.Firefox()


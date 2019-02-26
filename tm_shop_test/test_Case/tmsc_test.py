#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import time
from selenium import webdriver
from base_page import BasePage
#进入官网，编写支付模块测试用例
class Login(unittest.TestCase):
    def setUp(self):
        self.brower = BasePage()
        self.url="https://shop.360tianma.com/"
        
    def test_login(self):
        self.brower.open_url(self.url)
        #self.brower.maximize_window()
        print(self.brower.get_ck())
        time.sleep(3)
        self.brower.click("/html/body/header/div/div[2]/ul/li[5]/button")
        self.brower.type("//*[@id='username']","17623250366")
        self.brower.type("//*[@id='password']","meng0926")
        time.sleep(30)
        self.brower.click("/html/body/div/div[2]/div/div/div/div[2]/div[4]/input[1]")
        time.sleep(2)
        print(self.brower.get_ck())
        time.sleep(10)
        self.brower.quit_url()

#BasePage.

if __name__ == "__main__":
	unittest.main()

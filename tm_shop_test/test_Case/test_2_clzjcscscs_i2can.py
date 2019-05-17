#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import time
import os
from test_Case import base_page
from test_Case import mysql_page

class A_test_clzjcscscs_i2can(unittest.TestCase):
    '''新版发现组件后端自动化测试用例'''
    def test_01_addlbt(self):
        '''添加轮播图，判断系统提示是否与预期一致'''
        self.brower.xp_click('//*[@id="menu-article"]/dt')
        self.brower.xp_click('//*[@id="menu-article"]/dd/ul/li/a')
        time.sleep(1)
        self.brower.to_iframe('//*[@id="iframe_box"]/div[2]/iframe')
        time.sleep(1)
        self.brower.css_click('.layui-btn.add')
        time.sleep(1)
        self.brower.to_iframe('//*[starts-with(@id,"layui-layer-iframe")]')
        self.brower.xp_click('//*[@id="demo1"]')
        time.sleep(1)
        os.system('D:/job/tm_shop_selenium/tm_shop_test/Aut/clzjcscscs_i2can_upfile_passlbt.exe')
        self.text=self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text,'上传成功')
        # self.brower.css_click('.layui-btn.layui-btn-normal.submit')
    def test_02_nourl(self):
        '''添加轮播图后，未填写跳转地址，点击提交，判断系统提示是否与预期一致'''
        self.brower.css_click('.layui-btn.layui-btn-normal.submit')
        self.text=self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text,'请输入跳转地址')
    def test_03_fsturl(self):
        '''输入不带http/https的跳转链接，点击提交，判断系统提示是否与预期一致'''
        self.brower.css_type('.layui-input.url','www.baidu.com')
        self.brower.css_click('.layui-btn.layui-btn-normal.submit')
        self.text=self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text,'地址请填写包含http://或者https://的链接')
    def test_04_nopx(self):
        '''输入正确跳转地址后，不输入排序，点击提交，判断系统提示是否与预期结果一致'''
        self.brower.css_type('.layui-input.url','http://www.baidu.com')
        self.brower.css_click('.layui-btn.layui-btn-normal.submit')
        self.text=self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text,'请输入排序')
    def test_05_other(self):
        '''点击设置背景色，填写参数，排序保存'''
        self.brower.css_click('.layui-colorpicker-trigger-span')
        # js = 'document.getElementById("layui-colorpicker2").removeAttribute("readonly")'
        # self.brower.driver.execute_script(js,)
        # self.brower.css_type('.layui-input','#f00')
        self.brower.css_click('.layui-colorpicker-basis-black')
        # 输入后清空
        self.brower.css_click('.layui-btn.layui-btn-primary.layui-btn-sm')
        self.brower.css_click('.layui-colorpicker-trigger-span')
        # self.brower.css_type('.layui-input', '#f00')
        self.brower.css_click('.layui-colorpicker-basis-black')
        self.brower.xp_click('/html/body/div[2]/div[3]/div[2]/button[2]')

        """
        self.brower.css_click('.layui-btn.layui-btn-primary.addcanshu')
        self.brower.css_type('.layui-input.key','key')
        self.brower.css_type('.layui-input.value','1')
        self.brower.css_type('.layui-input.sort','1')
        self.brower.css_click('.layui-btn.layui-btn-normal.submit')
    def test_06_tobj_findcsdel(self):
        '''进入编辑，查找页面元素，是否只有刚才创建的参数，如果多于一条，则抛出异常'''
        self.brower.pk_iframe()
        self.brower.xp_click('//*[@id="menu-article"]/dd/ul/li/a')
        self.brower.to_iframe('/html/body/section/div[2]/div[2]/iframe')
        self.brower.css_click('.layui-btn.layui-btn-normal.edit')
        self.brower.to_iframe('//*[starts-with(@id,"layui-layer-iframe")]')
        s=self.brower.driver.find_elements_by_css_selector('.layui-icon.layui-icon-close-fill.deletecanshu')
        #print(len(s))
        self.assertEqual(len(s),'1')
"""








    @classmethod
    def setUpClass(self):
        self.db = mysql_page.To_mysql()
        self.brower = base_page.BasePage()
        self.url = "http://stabletm.360tianma.com/application/clzjcscscs_i2can/html/index.html"
        self.brower.open_url(self.url)
        self.brower.add_localSt()
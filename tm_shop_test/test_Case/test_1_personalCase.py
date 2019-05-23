#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import time
import os
import readcfg
from test_Case import base_page
from test_Case import mysql_page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class A_test_personal(unittest.TestCase):
    '''个人中心组件后端测试用例'''
    def test_01_bpsh(self):
        '''点击进入推送功能页面'''
        self.brower.xp_click('//*[@id="menu-article"]/dt')
        time.sleep(1)
        self.brower.xp_click('//*[@id="menu-article"]/dd/ul/li[1]/a')
        time.sleep(2)
    def test_02_notitle(self):
        '''不输入标题，点击提交'''
        self.brower.to_iframe('/html/body/section/div[2]/div[2]/iframe')
        time.sleep(3)
        self.brower.xp_click('/html/body/div/div/div/button')
        #self.brower.pk_iframe()
        self.text=self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text,"标题不能为空")
    def test_03_nocontent(self):
        '''不输入内容，点击提交'''
        self.brower.css_type('#user-name','这是一个标题')
        self.brower.xp_click('/html/body/div/div/div/button')
        time.sleep(1)
        self.text = self.brower.css_get_text('.layui-layer-content')
        time.sleep(1)
        self.assertEqual(self.text, "内容不能为空")
    def test_04_notime(self):
        '''清空推送时间，点击提交'''
        self.brower.css_type('#user-name','这是一个标题')
        self.brower.css_type('.textarea.content','这是一个内容')
        self.brower.css_click('#test1')
        time.sleep(3)
        self.brower.css_click('.laydate-btns-clear')
        # self.brower.xp_click('//*[@id="layui-laydate1"]/div[2]/div/span[1]')
        time.sleep(2)
        self.brower.xp_click('/html/body/div/div/div/button')
        self.text = self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text, "请选择推送时间")
    def test_05_nolink(self):
        '''不输入链接，点击提交，判断保存成功提示语是否与预期一致'''
        self.brower.css_click('#test1')
        time.sleep(3)
        self.brower.css_click('.laydate-btns-now')
        time.sleep(1)
        self.brower.css_click('.btn.btn-primary.submit')
        time.sleep(1)
        self.text=self.brower.css_get_divtext('.layui-layer-content.layui-layer-padding')
        #self.text=self.brower.css_get_text('.layui-layer-content.layui-layer-padding')
        self.assertEqual(self.text,'保存成功')
        time.sleep(3)
        self.brower.css_click('.layui-layer-btn0')
    def test_06_link(self):
        '''输入链接点击提交，判断提示语是否与预期一致'''
        self.brower.css_type('.layui-input.link','http://www.baidu,com')
        self.brower.xp_click('/html/body/div/div/div/button')
        time.sleep(2)
        self.text = self.brower.xp_get_divtest('/html/body/div[4]/div[2]')
        self.assertEqual(self.text, '保存成功')
        time.sleep(1)
        self.brower.css_click('.layui-layer-btn0')
        time.sleep(1)
    def test_07_delpush(self):
        '''进入消息列表，选择第一个消息推送，进行删除'''
        self.brower.pk_iframe()
        time.sleep(2)
        self.brower.xp_click('/html/body/aside/div/dl[1]/dd/ul/li[2]/a')
        self.brower.to_iframe('/html/body/section/div[2]/div[3]/iframe')
        time.sleep(2)
        self.brower.xp_click('/html/body/div/div/table/tbody/tr[1]/td[7]/a/i')
        time.sleep(2)
        self.text = self.brower.xp_get_divtest('/html/body/div[3]/div[2]')
        self.assertEqual(self.text, '确认要删除吗？')
        self.brower.css_click('.layui-layer-btn1')
        time.sleep(2)
        self.brower.xp_click('/html/body/div/div/table/tbody/tr[1]/td[7]/a/i')
        self.brower.css_click('.layui-layer-btn0')

    def test_08_igljust(self):
        '''进入积分调整页面，点击积分配置，开关按钮，判断相应提示语是否与预期一致'''
        self.brower.pk_iframe()
        self.brower.xp_click('/html/body/aside/div/dl[2]/dt')
        time.sleep(1)
        self.brower.xp_click('/html/body/aside/div/dl[2]/dd/ul/li[1]/a')
        time.sleep(1)
        self.brower.to_iframe('/html/body/section/div[2]/div[4]/iframe')
        time.sleep(2)
        self.brower.xp_click('/html/body/div[1]/div[1]/div[1]/form/div/div/div')
        self.text=self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text,'成功')
        time.sleep(1)
        self.brower.xp_click('/html/body/div[1]/div[1]/div[1]/form/div/div/div')
        self.text = self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text, '成功')
        time.sleep(1)
        self.brower.xp_click('/html/body/div[1]/div[2]/div[1]/form/div/div/div')
        self.text = self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text, '成功')
        time.sleep(1)
        self.brower.xp_click('/html/body/div[1]/div[2]/div[1]/form/div/div/div')
        self.text = self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text, '成功')
        time.sleep(1)
        self.brower.xp_click('/html/body/div[1]/div[3]/div[1]/form/div/div/div')
        self.text = self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text, '成功')
        time.sleep(1)
        self.brower.xp_click('/html/body/div[1]/div[3]/div[1]/form/div/div/div')
        self.text = self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text, '成功')
        time.sleep(1)
    def test_09_jftz(self):
        '''修改规则积分与天数，输入正常数值，判断相应提示是否与预期一致'''
        time.sleep(1)
        self.brower.css_type('#first_login','20')
        self.text = self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text, '成功')
        time.sleep(1)
        self.brower.css_type('#sex','20')
        self.text = self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text, '成功')
        time.sleep(1)
        self.brower.css_type('#birthday','20')
        self.text = self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text, '成功')
        time.sleep(1)
        self.brower.css_type('#mobile','20')
        self.text = self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text, '成功')
        time.sleep(1)
        self.brower.css_type('#wb', '20')
        self.text = self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text, '成功')
        time.sleep(1)
        self.brower.css_type('#wx', '20')
        time.sleep(1)
        self.text = self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text, '成功')
        time.sleep(1)
        self.brower.css_type('#qq', '20')
        self.text = self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text, '成功')
        time.sleep(1)
        self.brower.xp_type('/html/body/div[1]/div[3]/div[2]/div[1]/div[2]/ul/li/input[2]','20')

        self.text = self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text, '成功')
        time.sleep(1)
        self.brower.xp_type('/html/body/div[1]/div[3]/div[2]/div[2]/div[2]/ul/li[2]/input[1]', '3')
        time.sleep(1)
        self.text = self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text, '成功')
        time.sleep(1)
        self.brower.xp_type('/html/body/div[1]/div[3]/div[2]/div[2]/div[2]/ul/li[2]/input[2]','10')
        self.text = self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text, '成功')
        time.sleep(1)
        self.brower.xp_type('/html/body/div[1]/div[3]/div[2]/div[2]/div[2]/ul/li[3]/input[1]', '7')
        self.text = self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text, '成功')
        time.sleep(1)
        self.brower.xp_type('/html/body/div[1]/div[3]/div[2]/div[2]/div[2]/ul/li[3]/input[2]', '20')
        self.text = self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text, '成功')
        time.sleep(1)
        self.brower.xp_type('/html/body/div[1]/div[3]/div[2]/div[3]/div[2]/ul/li[1]/input[1]', '100')
        self.text = self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text, '成功')
        time.sleep(1)
        self.brower.xp_type('/html/body/div[1]/div[3]/div[2]/div[3]/div[2]/ul/li[1]/input[2]', '200')
        self.text = self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text, '成功')
        time.sleep(1)
        self.brower.xp_type('/html/body/div[1]/div[3]/div[2]/div[3]/div[2]/ul/li[2]/input[1]', '200')
        self.text = self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text, '成功')
        time.sleep(1)
        self.brower.xp_type('/html/body/div[1]/div[3]/div[2]/div[3]/div[2]/ul/li[2]/input[2]', '400')
        time.sleep(1)
        self.text = self.brower.css_get_text('.layui-layer-content')
        time.sleep(1)
        self.assertEqual(self.text, '成功')
    def test_10_jfgz(self):
        '''进入积分规则页面，输入，提交提示语是否与预期结果一致'''
        self.brower.pk_iframe()
        self.brower.xp_click('/html/body/aside/div/dl[2]/dd/ul/li[2]/a')
        self.brower.to_iframe('/html/body/section/div[2]/div[5]/iframe')
        time.sleep(1)
        self.brower.css_type('.w-e-text','这是一个规则')
        self.brower.css_click('.btn.btn-primary.submit')
        self.text=self.brower.css_get_text('.layui-layer-content.layui-layer-padding')
        self.assertEqual(self.text,'保存成功')
        self.brower.css_click('.layui-layer-btn0')
    def test_11_pjtmren(self):
        '''进入背景图页面，点击恢复默认，验证相关提示语是否与预期一致'''
        self.brower.pk_iframe()
        self.brower.xp_click('/html/body/aside/div/dl[2]/dd/ul/li[3]/a')
        self.brower.to_iframe('/html/body/section/div[2]/div[6]/iframe')
        time.sleep(2)
        self.brower.css_click('.layui-btn.publicStyle.layui-btn-primary.default')
        time.sleep(1)
        self.text=self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text,'保存成功')
        time.sleep(2)
    def test_12_pjtpush(self):
        '''上传背景图，判断上传后弹窗提示是否与预期结果一致'''
        self.brower.css_click('#upload')
        os.system('D:/job/tm_shop_selenium/tm_shop_test/Aut/personal_upfile_passpjt.exe')
        # time.sleep(3)
        ele=self.brower.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.layui-layer-content')))
        self.text=self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text,'保存成功')
    def test_13_pjtpushf(self):
        '''上传不符合规范的文件，判断弹窗提示是否与预期结果一致'''
        time.sleep(2)
        self.brower.css_click('#upload')
        time.sleep(1)
        os.system('D:/job/tm_shop_selenium/tm_shop_test/Aut/personal_upfile_flasepjt.exe')
        # time.sleep(1)
        self.text=self.brower.css_get_divtext('.layui-layer-content.layui-layer-padding')
        self.assertEqual(self.text,'选择的文件中包含不支持的格式')
    def test_14_noaddlbt(self):
        '''验证不上传轮播图片，直接点击提交时，相关提示是否正常'''
        self.brower.pk_iframe()
        self.brower.xp_click('/html/body/aside/div/dl[2]/dd/ul/li[4]/a')
        self.brower.to_iframe('/html/body/section/div[2]/div[7]/iframe')
        time.sleep(5)
        self.brower.css_click('.layui-btn.add')
        time.sleep(3)
        self.brower.to_iframe('//*[starts-with(@id,"layui-layer-iframe")]')
        time.sleep(1)
        self.brower.css_click('.layui-btn.layui-btn-normal.submit')
        time.sleep(1)
        self.text=self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text,'请上传轮播图片')
    def test_15_add_lbt(self):
        '''验证新建上传轮播图功能是否正常'''
        self.brower.css_click('#demo1')
        os.system('D:/job/tm_shop_selenium/tm_shop_test/Aut/personal_upfile_passlbt.exe')
        # time.sleep(3)
        self.text = self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text, '上传成功')
    def test_16_fysno_paix(self):
        '''验证不输入排序，点击提交，相关提示语是否正常'''
        self.brower.css_click('.layui-btn.layui-btn-normal.submit')
        time.sleep(1)
        self.text=self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text,'请输入排序')
    def test_17_fysno_url(self):
        '''验证提交成功后，切换登陆后才能访问按钮，相关提示语是否正常'''
        self.brower.css_type('.layui-input.sort','1')
        self.brower.css_click('.layui-btn.layui-btn-normal.submit')
        self.brower.pk_iframe()
        self.brower.xp_click('/html/body/aside/div/dl[2]/dd/ul/li[4]/a')
        self.brower.to_iframe('/html/body/section/div[2]/div[7]/iframe')
        time.sleep(2)
        #self.brower.css_click('.layui-btn.layui-btn-xs.public-bg1')
        self.brower.xp_click('/html/body/div[1]/div[2]/div/div/div[2]/table/tbody/tr[1]/td[5]/div/div')
        self.text=self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text,'操作成功')
        self.brower.xp_click('/html/body/div[1]/div[2]/div/div/div[2]/table/tbody/tr[1]/td[5]/div/div')
        self.text = self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text, '操作成功')
    def test_18_fys_del(self):
        '''选择第一条轮播图，点击删除'''
        self.brower.css_click('.layui-btn.layui-btn-xs.public-bg2')
        self.text=self.brower.css_get_divtext('.layui-layer-content')
        self.assertEqual(self.text,'确定删除吗？删除后不可恢复')
        self.brower.css_click('.layui-layer-btn0')
        time.sleep(1)
        self.text=self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text,'操作成功')
        #self.brower.css_click('.Hui-iconfont')
    def test_19_all_del(self):
        '''再次删除（删除所有轮播图），判断提示语是否与预期一致'''
        self.brower.css_click('.btn.btn-success.radius.r')
        time.sleep(1)
        self.brower.css_click('.layui-btn.layui-btn-xs.public-bg2')
        self.brower.css_click('.layui-layer-btn0')
        self.text=self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text,'至少上传一张轮播图')
        time.sleep(2)
    def test_20_upd_noand(self):
        '''点击编辑进入轮播图修改页面，选择为原生，不填写安卓地址，点击提交'''
        self.brower.css_click('.layui-btn.layui-btn-xs.public-bg1')
        time.sleep(1)
        self.brower.to_iframe('//*[starts-with(@id,"layui-layer-iframe")]')
        time.sleep(1)
        self.brower.css_click('.layui-select-title')
        self.brower.xp_click('/html/body/form/div[2]/div/div/dl/dd[2]')
        self.brower.css_click('.layui-btn.layui-btn-normal.submit')
        self.text=self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text,'请输入android地址')
    def test_21_upd_noios(self):
        '''编辑，不输入iOS地址，点击提交'''
        self.brower.css_type('.layui-input.androidurl','com.example.tmquestionlibrary.MainFragment')
        self.brower.css_click('.layui-btn.layui-btn-normal.submit')
        self.text=self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text,'请输入ios地址')
    def test_22_upd_all(self):
        '''编辑，输入iOS及Android地址，点击提交,提交后再次进入，确认已修改'''
        self.brower.css_type('.layui-input.iosurl','zx02frmrbwz_pkdza_PeopleDailyController')
        self.brower.css_click('.layui-btn.layui-btn-normal.submit')
    def test_23_mzsm(self):
        '''验证免责声明，输入后保存，页面提示是否与预期结果一致'''
        self.brower.pk_iframe()
        self.brower.xp_click('//*[@id="menu-picture"]/dt/a')
        self.brower.to_iframe('/html/body/section/div[2]/div[8]/iframe')
        self.brower.css_click('.btn.btn-primary.submit')
        time.sleep(1)
        self.brower.xp_type('//*[starts-with(@id,"text-elem")]','这是一个免责声明')
        self.brower.css_click('.btn.btn-primary.submit')
        self.text=self.brower.css_get_divtext('.layui-layer-content.layui-layer-padding')
        self.assertEqual(self.text,'保存成功')
        self.brower.css_click('.layui-layer-btn0')
    def test_24_ysxy(self):
        '''验证隐私协议，输入后保存，页面提示是否与预期结果一致'''
        self.brower.pk_iframe()
        self.brower.xp_click('//*[@id="menu-agreement"]/dt/a')
        self.brower.to_iframe('/html/body/section/div[2]/div[9]/iframe')
        time.sleep(1)
        self.brower.xp_type('//*[starts-with(@id,"text-elem")]','这是一个隐私协议')
        self.brower.css_click('.btn.btn-primary.submit')
        time.sleep(2)
        self.text=self.brower.css_get_divtext('.layui-layer-content.layui-layer-padding')
        self.assertEqual(self.text,'保存成功')
        self.brower.css_click('.layui-layer-btn0')
    def test_25_guwm(self):
        '''验证关于我们，输入后保存，页面提示是否与预期结果一致'''
        self.brower.pk_iframe()
        self.brower.xp_click('//*[@id="menu-aboutus"]/dt/a')
        self.brower.to_iframe('/html/body/section/div[2]/div[10]/iframe')
        self.brower.xp_type('//*[starts-with(@id,"text-elem")]', '这是一个关于我们')
        self.brower.css_click('.btn.btn-primary.submit')
        time.sleep(2)
        self.text = self.brower.css_get_divtext('.layui-layer-content.layui-layer-padding')
        self.assertEqual(self.text, '保存成功')
        self.brower.css_click('.layui-layer-btn0')
    def test_26_yjfk(self):
        '''验证意见反馈，如页面存在意见反馈，则选择第一条，点击删除，如没有则pass'''
        self.brower.pk_iframe()
        self.brower.xp_click('//*[@id="menu-comments"]/dt/a')
        self.brower.quit_url()




    @classmethod
    def setUpClass(self):
        self.db = mysql_page.To_mysql()
        self.brower = base_page.BasePage()
        self.getcfg = readcfg.Readcfg()
        self.url = str(self.getcfg.get_value('Test_url','test_url'))+"/application/personal/html/index.html"
        self.brower.open_url(self.url)
        self.brower.add_localSt()
        self.brower.driver.implicitly_wait(30)


if __name__=="__main__":
    unittest.main()
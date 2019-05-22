#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import time
import os
import random
# import readcfg
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
        time.sleep(1)
    def test_02_nourl(self):
        '''添加轮播图后，未填写跳转地址，点击提交，判断系统提示是否与预期一致'''
        self.brower.css_click('.layui-btn.layui-btn-normal.submit')
        self.text=self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text,'请输入跳转地址')
        time.sleep(1)
    def test_03_fsturl(self):
        '''输入不带http/https的跳转链接，点击提交，判断系统提示是否与预期一致'''
        self.brower.css_type('.layui-input.url','www.baidu.com')
        self.brower.css_click('.layui-btn.layui-btn-normal.submit')
        self.text=self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text,'地址请填写包含http://或者https://的链接')
        time.sleep(1)
    def test_04_nopx(self):
        '''输入正确跳转地址后，不输入排序，点击提交，判断系统提示是否与预期结果一致'''
        self.brower.css_type('.layui-input.url','http://www.baidu.com')
        self.brower.css_click('.layui-btn.layui-btn-normal.submit')
        self.text=self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text,'请输入排序')
        time.sleep(1)
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
        self.brower.css_click('button[colorpicker-events="confirm"]')
        self.brower.css_click('.layui-btn.layui-btn-primary.addcanshu')
        self.brower.css_type('.layui-input.key','key')
        self.brower.css_type('.layui-input.value','1')
        self.brower.css_type('.layui-input.sort','1')
        self.brower.css_click('.layui-btn.layui-btn-normal.submit')
        time.sleep(1)
    def test_06_tobjys_noadr(self):
        '''编辑，修改为原生，不输入Android地址，点击提交'''
        self.brower.pk_iframe()
        self.brower.xp_click('//*[@id="menu-article"]/dd/ul/li/a')
        self.brower.to_iframe('/html/body/section/div[2]/div[2]/iframe')
        self.brower.css_click('.layui-btn.layui-btn-normal.edit')
        self.brower.to_iframe('//*[starts-with(@id,"layui-layer-iframe")]')
        time.sleep(2)
        self.brower.css_click('input[value="非原生"]')
        time.sleep(1)
        self.brower.xp_click('/html/body/form/div[3]/div/div/dl/dd[2]')
        self.brower.css_click('.layui-btn.layui-btn-normal.submit')
        self.text = self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text, '请输入android地址')
    def test_07_findcsdel(self):
        '''查找页面元素，是否只有刚才创建的参数，如果多于一条，则抛出异常'''
        s=self.brower.driver.find_elements_by_css_selector('.layui-icon.layui-icon-close-fill.deletecanshu')
        # print(len(s))
        self.assertEqual(len(s),'1')
    def test_08_ys_noios(self):
        '''编辑，输入Android地址，不输入iOS地址，点击提交'''
        time.sleep(1)
        self.brower.css_type('.layui-input.androidurl','com.example.tmquestionlibrary.MainFragment')
        self.brower.css_click('.layui-btn.layui-btn-normal.submit')
        self.text=self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text, '请输入ios地址')
    def test_09_ys_typeall(self):
        '''全部输入后，点击提交,判断banner类型已修改'''
        self.brower.css_type('.layui-input.iosurl','zx02frmrbwz_pkdza_PeopleDailyController')
        self.brower.css_click('.layui-btn.layui-btn-normal.submit')
        self.brower.pk_iframe()
        self.brower.xp_click('//*[@id="menu-article"]/dd/ul/li/a')
        self.brower.to_iframe('//*[@id="iframe_box"]/div[2]/iframe')
        time.sleep(1)
        self.text=self.brower.css_get_divtext('.type')
        #print(self.text)
        self.assertEqual(self.text,'原生')
        time.sleep(1)
    def test_10_lb_upbackcolor(self):
        '''banner列表页面修改背景色，验证相关提示是否与预期一致'''
        self.brower.css_click('.layui-colorpicker-trigger-span')
        self.brower.css_click('.layui-btn.layui-btn-primary.layui-btn-sm')
        self.text=self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text,'操作成功')
        self.brower.css_click('.layui-colorpicker-trigger-span')
        self.brower.css_click('.layui-colorpicker-basis-black')
        self.brower.css_click('.layui-btn.layui-btn-sm')
        self.text=self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text,'操作成功')
    def test_11_lb_upbx(self):
        '''banner列表页面修改排序，验证相关提示是否与预期一致'''
        self.brower.css_type('.layui-input.sort','2')
        self.brower.css_click('.type')
        self.text = self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text, '操作成功')
    def test_12_del_banner(self):
        '''删除banner'''
        self.brower.css_click('.layui-btn.layui-btn-normal.delete')
        self.text=self.brower.css_get_divtext('.layui-layer-content')
        self.assertEqual(self.text,'确定删除吗？删除后不可恢复')
        self.brower.css_click('.layui-layer-btn1')
        self.brower.css_click('.layui-btn.layui-btn-normal.delete')
        self.brower.css_click('.layui-layer-ico.layui-layer-close.layui-layer-close2')
        self.brower.css_click('.layui-btn.layui-btn-normal.delete')
        self.brower.css_click('.layui-layer-btn0')
        time.sleep(2)
        self.text = self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text, '删除成功')
        self.brower.css_click('.Hui-iconfont')
    def test_13_no_mokfl(self):
        '''进入模块分类,新建分类，验证不输入分类名称，提交时相关提示是否与预期一致'''
        self.brower.pk_iframe()
        self.brower.xp_click('//*[@id="menu-picture"]/dt/a')
        self.brower.to_iframe('//*[@id="iframe_box"]/div[3]/iframe')
        time.sleep(1)
        self.brower.css_click('.layui-btn.add')
        time.sleep(1)
        self.brower.to_iframe('//*[starts-with(@id,"layui-layer-iframe")]')
        time.sleep(1)
        self.brower.css_click('.layui-btn.layui-btn-normal.submit')
        self.text=self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text,'分类名称不能为空')
    def test_14_no_px(self):
        '''不输入排序，点击提交，判断提示是否与预期结果一致'''
        self.brower.css_type('.layui-input.typename','文化旅游')
        self.brower.css_click('.layui-btn.layui-btn-normal.submit')
        self.text = self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text, '排序不能为空')
    def test_15_alltype(self):
        '''全部输入，点击提交,点击编辑按钮，修改名称和排序，保存,判断是否已修改'''
        self.brower.css_type('.layui-input.sort','9')
        self.brower.css_click('.layui-btn.layui-btn-normal.submit')
        self.brower.pk_iframe()
        self.brower.xp_click('//*[@id="menu-picture"]/dt/a')
        self.brower.to_iframe('//*[@id="iframe_box"]/div[3]/iframe')
        time.sleep(1)
        self.brower.xp_click('/html/body/div/div[2]/table/tbody/tr[1]/td[3]/button[1]')
        time.sleep(1)
        self.brower.to_iframe('//*[starts-with(@id,"layui-layer-iframe")]')
        time.sleep(1)
        self.brower.css_type('.layui-input.typename','便民服务')
        self.brower.css_type('.layui-input.sort','10')
        self.brower.css_click('.layui-btn.layui-btn-normal.submit')
        self.brower.pk_iframe()
        self.brower.xp_click('//*[@id="menu-picture"]/dt/a')
        self.brower.to_iframe('//*[@id="iframe_box"]/div[3]/iframe')
        #self.brower.pk_bkiframe()
        time.sleep(1)
        # self.text=self.brower.xp_get_divtest('/html/body/div/div[2]/table/tbody/tr[1]/td[1]/span')
        # self.assertEqual(self.text,'便民服务')
    def test_16_up_lbpx(self):
        '''分类列表，修改排序，判断提示是否与预期一致'''
        time.sleep(1)
        self.brower.xp_type('/html/body/div/div[2]/table/tbody/tr[1]/td[2]/input','9')
        self.brower.xp_click('/html/body')
        self.text=self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text,'操作成功')
    def test_17_del_fl(self):
        '''删除新建的分类'''
        self.brower.xp_click('/html/body/div[1]/div[2]/table/tbody/tr[1]/td[3]/button[2]')
        time.sleep(1)
        self.brower.css_click('.layui-layer-btn1')
        time.sleep(1)
        self.brower.xp_click('/html/body/div[1]/div[2]/table/tbody/tr[1]/td[3]/button[2]')
        self.brower.css_click('.layui-layer-ico.layui-layer-close.layui-layer-close1')
        self.brower.xp_click('/html/body/div[1]/div[2]/table/tbody/tr[1]/td[3]/button[2]')
        time.sleep(1)
        self.brower.css_click('.layui-layer-btn0')
        time.sleep(1)
        self.brower.css_click('.Hui-iconfont')
        time.sleep(1)
    def test_18_crt_nomk(self):
        '''进入模块列表，新建模块,不进行输入，点击提交'''
        self.brower.pk_iframe()
        self.brower.xp_click('/html/body/aside/div/dl[3]/dt/a')
        time.sleep(1)
        self.brower.to_iframe('/html/body/section/div[2]/div[4]/iframe')
        time.sleep(1)
        self.brower.css_click('.layui-btn.add')
        time.sleep(1)
        self.brower.to_iframe('//*[starts-with(@id,"layui-layer-iframe")]')
        time.sleep(1)
        self.brower.css_click('.layui-btn.layui-btn-normal.submit')
        self.text=self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text,'请输入模块地址')
    def test_19_mk_noimg(self):
        '''填写其他内容，不选择图标，点击提交'''
        self.brower.css_type('.layui-input.name','测试模块')
        self.brower.css_click('.layui-select-title')
        time.sleep(2)
        self.brower.xp_click('/html/body/form/div[3]/div/div/dl/dd['+str(random.randint(2,3))+']')
        time.sleep(2)
        self.brower.css_type('.layui-input.url','http://www.baidu.com')
        self.brower.css_type('.layui-input.sort','9999')
        self.brower.css_click('.layui-btn.layui-btn-normal.submit')
        self.text=self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text,'请勾选图标')
    def test_20_nohturl(self):
        '''勾选图标，填写地址不带http或https，点击提交'''
        self.brower.xp_click('//*[@id="icontable"]/tbody/tr['+str(random.randint(1,8))+']/td['+str(random.randint(1,8))+']/img')
        self.brower.css_type('.layui-input.url', 'www.baidu.com')
        self.brower.css_click('.layui-btn.layui-btn-normal.submit')
        self.text=self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text,'地址请填写包含http://或者https://的链接')
    def test_21_fys_alltype(self):
        '''填写正确地址，填写参数，上传自定义图标，点击保存'''
        self.brower.css_type('.layui-input.url','http://www.baidu.com')
        self.brower.css_click('.layui-btn.layui-btn-primary.addcanshu')
        self.brower.css_type('.layui-input.key','key')
        self.brower.css_type('.layui-input.value','1')
        self.brower.css_click('li[lay-id="1"]')
        time.sleep(2)
        self.brower.css_click('img[id="demo1"]')
        time.sleep(1)
        os.system('D:/job/tm_shop_selenium/tm_shop_test/Aut/clzjcscscs_i2can_upfile_mktb.exe')
        self.text=self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text,'上传成功')
        # self.brower.css_click('.layui-btn.layui-btn-normal.submit')
    def test_22_nopx(self):
        '''不填写排序，点击提交，判断相关提示，是否与预期一致'''
        time.sleep(1)
        self.brower.css_type('.layui-input.sort','test')
        time.sleep(1)
        self.brower.css_click('.layui-btn.layui-btn-normal.submit')
        self.text=self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text,'请输入排序')
    def test_23_fys_allsubmit(self):
        '''全部填写，提交后，模块列表页面点击是/否置顶'''
        self.brower.css_type('.layui-input.sort','9999')
        self.brower.css_click('.layui-btn.layui-btn-normal.submit')
        self.brower.pk_iframe()
        time.sleep(1)
        self.brower.xp_click('//*[@id="menu-agreement"]/dt/a')
        self.brower.to_iframe('//*[@id="iframe_box"]/div[4]/iframe')
        time.sleep(1)
        self.brower.xp_click('/html/body/div[1]/div[2]/table/tbody/tr[1]/td[6]/p[2]')
        time.sleep(1)
        self.text=self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text,'操作成功')
        self.brower.xp_click('/html/body/div[1]/div[2]/table/tbody/tr[1]/td[6]/p[1]')
        time.sleep(1)
        self.text = self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text, '操作成功')
    def test_24_qiyong(self):
        '''模块列表，点击是否启用，判断提示是否与预期结果一致'''
        time.sleep(1)
        self.brower.xp_click('/html/body/div[1]/div[2]/table/tbody/tr[1]/td[7]/p[1]')
        self.text=self.brower.css_get_text('.layui-layer-content')
        time.sleep(1)
        self.assertEqual(self.text,'操作成功')
        self.brower.xp_click('/html/body/div[1]/div[2]/table/tbody/tr[1]/td[7]/p[2]')
        time.sleep(1)
        self.text = self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text, '操作成功')
    def test_25_mklist_uppx(self):
        '''模块列表，修改排序，判断提示是否与预期结果一致'''
        time.sleep(1)
        self.brower.xp_type('/html/body/div[1]/div[2]/table/tbody/tr[1]/td[8]/input','9998')
        time.sleep(1)
        self.brower.xp_click('/html/body')
        time.sleep(1)
        self.text = self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text, '操作成功')
    def test_26_to_bj(self):
        '''选择第一个模块，点击编辑，进入编辑页面,修改为原生，不填Android入口地址，点击提交'''
        self.brower.xp_click('/html/body/div[1]/div[2]/table/tbody/tr[1]/td[9]/button[1]')
        time.sleep(1)
        self.brower.to_iframe('//*[starts-with(@id,"layui-layer-iframe")]')
        time.sleep(2)
        self.brower.xp_click('/html/body/form/div[4]/div/div/div/input')
        time.sleep(5)
        self.brower.xp_click('/html/body/form/div[4]/div/div/dl/dd[2]')
        time.sleep(1)
        self.brower.css_click('.layui-btn.layui-btn-normal.submit')
        self.text = self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text, '请输入android地址')
    def test_27_noiosurl(self):
        '''输入Android地址，不输入iOS地址，点击提交，判断提示是否与预期一致'''
        time.sleep(1)
        self.brower.css_type('.layui-input.androidurl','com.example.tmquestionlibrary.MainFragment')
        time.sleep(1)
        self.brower.css_click('.layui-btn.layui-btn-normal.submit')
        self.text = self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.text, '请输入ios地址')
    def test_28_ys_alltype(self):
        '''输入Android和iOS地址，删除参数，点击提交，确认是否已修改'''
        self.brower.css_type('.layui-input.iosurl','zx02frmrbwz_pkdza_PeopleDailyController')
        self.brower.css_click('.layui-icon.layui-icon-close-fill.deletecanshu')
        self.brower.css_click('.layui-btn.layui-btn-normal.submit')
    def test_29_mk_delete(self):
        '''删除新建模块'''
        self.brower.pk_iframe()
        self.brower.xp_click('//*[@id="menu-agreement"]/dt/a')
        self.brower.to_iframe('//*[@id="iframe_box"]/div[4]/iframe')
        self.brower.css_click('.layui-btn.layui-btn-normal.delete')
        self.test=self.brower.css_get_text('.layui-layer-content')
        self.assertEqual(self.test,'确定删除吗？删除后不可恢复')
        self.brower.css_click('.layui-layer-ico.layui-layer-close.layui-layer-close2')
        self.brower.css_click('.layui-btn.layui-btn-normal.delete')
        self.brower.css_click('.layui-layer-btn1')
        self.brower.css_click('.layui-btn.layui-btn-normal.delete')
        self.brower.css_click('.layui-layer-btn0')
        self.brower.css_click('.Hui-iconfont')

    @classmethod
    def setUpClass(self):
        self.db = mysql_page.To_mysql()
        self.brower = base_page.BasePage()
        self.getcfg = base_page.Readcfg()
        self.url = str(self.getcfg.get_url('test_url')) + "/application/clzjcscscs_i2can/html/index.html"
        self.brower.open_url(self.url)
        self.brower.add_localSt()
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import unittest
import random
import re
#import base_page
from test_Case import base_page
from test_Case import mysql_page

class A_test_buy(unittest.TestCase):
    '''验证购买单个组件，用户及商家金额是否正常'''
    def test_a_login(self):
        '''登陆'''
        self.brower.xp_click('/html/body/header/div/div[2]/ul/li[5]/button')
        self.brower.xp_type('//*[@id="username"]',"17623250366")
        self.brower.xp_type('//*[@id="password"]','meng0926')
        self.brower.xp_click('/html/body/div/div[2]/div/div/div/div[2]/div[4]/input[1]')
        time.sleep(3)

    def test_b_to_shop(self):
        '''进入商城，搜索，点击APP类型,随机选择组件，返回组件id'''
        self.brower.lt_click('商城')
        time.sleep(3)
        self.brower.lt_click('APP')
        self.i=random.randint(1,10)
        self.zj_xp="/html/body/div[3]/div/div[2]/div[2]/ul/li["+str(self.i)+"]/a/div/div[2]"
        self.brower.xp_click(self.zj_xp)
        time.sleep(2)
        self.html=self.brower.get_page_source()
        self.one_regex=re.compile("AjaxAddCart\(.*\)")
        self.gdid=self.one_regex.findall(self.html)
        self.e=(self.gdid[0])
        self.two_regex=re.compile("[0-9]+")
        self.spids=self.two_regex.findall(self.e)
        global zj_money
        zj_money=self.db.select_zj_price(spid=self.spids[0])

        """
        self.brower.xp_type('//*[@id="q"]',"天马小游戏")
        self.brower.xp_click('//*[@id="sourch_form"]/button')
        time.sleep(3)
        self.brower.cn_click('lazy-list')
        '''
    """
    def test_c_buy(self):
        '''先获取用户购买前的可用余额和冻结金额，再购买组件'''
        time.sleep(3)
        self.brower.cn_click('paybybill')
        time.sleep(3)
        self.brower.cn_click('paytotal')
        time.sleep(3)
        self.brower.cn_click('checkout-submit')
        time.sleep(3)
        self.brower.xp_type('/html/body/div[2]/div/div[2]/form/div/div/dl/dd/div/div/ul/input','123456')
        time.sleep(3)
        self.brower.xp_click('/html/body/div[2]/div/div[2]/form/div/div/div/a')
        time.sleep(3)
    def test_d_yq_userprice(self):
        '''查询商品价格，计算是否与可用余额减少一致'''
        self.gh_usermoney = self.db.select_user_kyprice()
        self.gh_userdjprice = self.db.select_user_djprice()
        self.ky_pz=self.gq_usermoney-self.gh_usermoney
        self.assertEqual(self.ky_pz,zj_money)
        print(self.ky_pz,zj_money)
    def test_e_yq_djprice(self):
        '''查询用户冻结金额增加是否与预期结果一致'''
        self.gh_usermoney = self.db.select_user_kyprice()
        self.gh_userdjprice = self.db.select_user_djprice()
        self.dj_pz=self.gq_userdjprice+zj_money
        self.assertEqual(self.gh_userdjprice,self.dj_pz)
    def test_f_yh_userprice(self):
        '''验证手动点击验收后，账户可用余额变化是否与预期结果一致'''
        time.sleep(2)
        self.brower.xp_click('/html/body/div[3]/div/div[2]/div[2]/div[1]/div[4]/table[1]/tbody/tr[1]/td/div[1]/div/a')
        self.brower.cn_click('layui-layer-btn0')
        self.ysh_kyprice=self.db.select_user_kyprice()
        self.dj_pz=self.gq_usermoney - zj_money
        self.assertEqual(self.ysh_kyprice,self.dj_pz)
    def test_g_yh_jdprice(self):
        '''验证手动点击验收后，账户冻结金额是否预期结果一致'''
        self.ysh_djprice=self.db.select_user_djprice()
        self.dj_pz=self.gq_userdjprice+zj_money-zj_money*70/100
        self.assertEqual(self.ysh_djprice,self.dj_pz)
        self.brower.close()
    @classmethod
    def setUpClass(self):
        self.db = mysql_page.To_mysql()
        self.brower = base_page.BasePage()
        self.url = "https://shop.360tianma.com"
        self.brower.open_url(self.url)
        self.gq_usermoney = self.db.select_user_kyprice()
        self.gq_userdjprice = self.db.select_user_djprice()
    @classmethod
    def tearDownClass(self):
        print("测试完成")
'''
class B_test_rd(unittest.TestCase):
    #测试用户退款流程，及金额是否正常
'''
if __name__=="__main__":
    unittest.main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding=utf-8
import time
from selenium import webdriver
import configparser
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.options import Options
import os.path
import os
import login_B_gtoken
import readcfg
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

 
class BasePage(object):
	'''定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类'''
	def __init__(self):
		options = Options()
		options.add_argument('--headless')
		self.driver = webdriver.Firefox(options=options)
		self.wait = WebDriverWait(self.driver, 20)


	def open_url(self,url):
		'''打开url'''
		self.driver.get(url)

	def quit_url(self):
		''' 关闭浏览器'''
		self.driver.quit()

	def forward(self):
		'''浏览器前进操作'''
		self.driver.forward()

	def back(self):
		'''浏览器后退操作'''
		self.driver.back()

	def wait(self, seconds):
		'''隐式等待'''
		self.driver.implicitly_wait(seconds)

	def close(self):
		'''点击关闭当前窗口'''
		self.driver.close()
 
	# 保存图片
	def get_windows_img(self):
		'''在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹.\Screenshots下'''
		file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
		rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
		screen_name = file_path + rq + '.png'
		try:
			self.driver.get_screenshot_as_file(screen_name)
		except NameError as e:
			self.get_windows_img()
 
	#定位元素方法

    #使用xpath定位元素，输入
	def xp_type(self, selector, text):
		el = self.driver.find_element_by_xpath(selector)
		el.clear()
		try:
			el.send_keys(text)
		except NameError as e:
			self.get_windows_img()
	#使用name定位元素，输入
	def nm_type(self,selector,text):
		el=self.driver.find_element_by_name(selector)
		el.clear()
		el.send_keys(text)
	#使用id定位原素，输入
	def id_type(self,selector,text):
		el=self.driver.find_element_by_id(selector)
		el.clear()
		el.send_keys(text)
	#使用css定位元素，输入
	def css_type(self,selector,text):
		el=self.driver.find_element_by_css_selector(selector)
		el.clear()
		el.send_keys(text)

	def clear(self, selector):
		el=self.driver.find_element_by_xpath(selector)
		#try:
		el.clear()
		#except NameError as e:
			#self.get_windows_img()
 
    # 使用Xpath定位，并点击元素
	def xp_click(self, selector):
		el = self.driver.find_element_by_xpath(selector)
		el.click()

	#使用Xpath定位，并打印文本（用于layer弹窗）
	def xp_get_text(self,selector):
		el=self.driver.find_element_by_xpath(selector).get_attribute('textContent')
		return el
	#使用xpath定位，并打印文本（用于div弹窗）
	def xp_get_divtest(self,selector):
		el=self.driver.find_element_by_xpath(selector).text
		return el
	#使用css定位，并打印文本（用于div弹窗）
	def css_get_divtext(self,selector):
		el=self.driver.find_element_by_css_selector(selector).text
		return el
	#使用css定位，并打印文本
	def css_get_text(self,selecter):
		el=self.driver.find_element_by_css_selector(selecter).get_attribute('textContent')
		return el
	#使用link_text定位，点击元素
	def lt_click(self,selector):
		el=self.driver.find_element_by_link_text(selector)
		el.click()
	#使用id定位，点击元素
	def id_click(self,selector):
		el=self.driver.find_element_by_id(selector)
		el.click()
	#使用name定位元素，点击元素
	def nm_click(self,selector):
		el=self.driver.find_element_by_name(selector)
		el.click()
	#使用class定位元素，点击元素
	def cn_click(self,selector):
		el=self.driver.find_element_by_class_name(selector)
		el.click()
	#使用css定位元素，点击元素
	def css_click(self,selector):
		el=self.driver.find_element_by_css_selector(selector)
		el.click()
	#使用xpath定位iframe,进入iframe
	def to_iframe(self,selector):
		iframe=self.driver.find_element_by_xpath(selector)
		self.driver.switch_to.frame(iframe)
	#使用css定位iframe，进入iframe
	def to_css_iframe(self,selector):
		iframe=self.driver.find_element_by_css_selector(selector)
		self.driver.switch_to_frame(iframe)
	#退出iframe(回到主页面)
	def pk_iframe(self):
		self.driver.switch_to_default_content()
	# 退出iframe（回到上一级）
	def pk_bkiframe(self):
		self.driver.switch_to.parent_frame()
	#css判断页面元素是否存在，不存在返回False，存在返回Ture
	def is_element_exist(self,selecter):
		s=self.driver.find_elements_by_xpath(selecter)
		if len(s) == 0:
			return False
		else:
			return True
	# 或者网页标题
	def get_page_title(self):
		return self.driver.title
	#获取页面源码
	def get_page_source(self):
		self.jsym=self.driver.page_source
		return self.jsym
	#等待
	def d(self):
		self.driver.switch_to.alert.accept()
	#隐性等待
	def yx_wait(self,m):
		self.driver.implicitly_wait(m)
	#显性等待,直到找到元素并点击
	def sh_wait(self,selector):
		WebDriverWait(self.driver,20).until(lambda x:x.find_element_by_link_text(selector).click())
	#获取当前页面URL
	def get_url(self):
		self.gurl=self.driver.current_url
		return self.gurl
	#获取页面cookie
	def get_ck(self):
		self.cookies=self.driver.get_cookies()
		return self.cookies
	#添加cookie
	def add_ck(self,ck):
		self.driver.add_cookie(ck)
	#B端后台登陆，向lacalstorage注入token值
	def add_localSt(self):
		# self.driver.execute_script('localStorage.setItem("token", "2A2F0BA8C124851BF641BE481C9CF9FA");')
		s=login_B_gtoken.Get_B_tk()
		code=s.get_code()
		rd=readcfg.Readcfg()
		tk=s.login_get_token(str(rd.get_value('Test_url','user_name')),str(rd.get_value('Test_url','password')),code)
		js='localStorage.setItem("token",'+ "'"+tk+"'"+');'
		self.driver.execute_script(js)
		# return js
	#清除原页面cookie
	def del_ck(self):
		self.driver.delete_all_cookies()
	def del_readonly(self):
		self.driver.execute_script()
	@staticmethod
	def setUpClass(self):
		pass
	def tearDownClass(self):
		pass
	#获取页面cookie
	def get_cookie(self):
		self.cookies=self.driver.get

if __name__ == "__main__":
	s=BasePage()
	print(s.add_localSt())

# -*- coding: utf-8 -*-
import random
import time, re
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
import requests
from io import BytesIO

class Vincent(object):
    def __init__(self):
        '''
        chrome_option = webdriver.ChromeOptions()
        # chrome_option.set_headless()

        self.driver = webdriver.Chrome(executable_path=r"D:\Google\Chrome\Application\chromedriver.exe", chrome_options=chrome_option)
        # self.driver =webdriver.Chrome("D:\Google\Chrome\Application\chromedriver.exe")
        self.driver.set_window_size(1440, 900)
        '''
        self.driver=webdriver.Firefox()

    def visit_index(self):
        self.driver.get("http://stabletm.360tianma.com")
        self.driver.find_element_by_css_selector('input[type="text"]').send_keys('admin')
        self.driver.find_element_by_css_selector('input[type="password"]').send_keys('111111')
        self.frame = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/iframe')
        self.driver.switch_to_frame(self.frame)


    def get_image_url(self, xpath):
        # link = re.compile('background-image: url\("(.*?)"\); background-position: (.*?)px (.*?)px;')
        elements = self.driver.find_elements_by_xpath(xpath)
        for element in elements:
            style = element.get_attribute("style")
            return style

if __name__ == "__main__":
    h = Vincent()
    h.visit_index()
    s=h.get_image_url('/html/body/div/canvas[1]')
    print(s)

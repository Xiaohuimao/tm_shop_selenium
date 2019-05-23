#!/usr/bin/env python
# -*- coding: utf-8 -*-
import configparser
import os

# 获取配置文件绝对路径
class Readcfg():
    def __init__(self):
        # self.xdpath=os.path.abspath(".")
        # self.cfgpath=os.path.join(self.xdpath,"config.ini")
        # # print(self.cfgpath)
        self.conf=configparser.ConfigParser()
        self.conf.read('D:/job/tm_shop_selenium/tm_shop_test/test_Case/config.ini',encoding="utf-8")
    def get_value(self,sct,opt):
        self.value=self.conf.get(sct,opt)
        return self.value
    # def get_sql(self,sct,opt):
    #     self.sql=self.conf.get(sct,opt)
    #     return self.sql
    # def get_url(self,param):
    #     self.url=self.conf.get(section="Test_url",option=param)
    #     return self.url

if __name__=="__main__":
    g=Readcfg()
    # print(g)
    print(g.get_value('Test_url','test_url'))
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import configparser
import os

# 获取配置文件绝对路径
class Readcfg():
    def __init__(self):
        self.xdpath=os.path.abspath(".")
        self.cfgpath=os.path.join(self.xdpath,"config.ini")
        print(self.cfgpath)
        self.conf=configparser.ConfigParser()
        self.conf.read(self.cfgpath,encoding="utf-8")
    def get_database(self,param):
        self.data=self.conf.get(section="DBServer",option=param)
        return self.data
    def get_sql(self,param):
        self.sql=self.conf.get(section="SQL",option=param)
        return self.sql
    def get_url(self,param):
        self.url=self.conf.get(section="Test_url",option=param)
        return self.url

if __name__=="__main__":
    g=Readcfg()
    print(g)
    print(g.get_url('test_url'))
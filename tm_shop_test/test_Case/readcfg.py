import configparser
import os

#获取配置文件绝对路径
class Readcfg():
    def __init__(self):
        self.xdpath=os.path.abspath(".")
        self.cfgpath=os.path.join(self.xdpath,"config.ini")
        self.conf=configparser.ConfigParser()
        self.conf.read(self.cfgpath,encoding="utf-8")
        #sections=self.conf.sections()
        #print(sections)
    def get_database(self,param):
        self.data=self.conf.get("DataBase",param)
        return self.data
    def get_sql(self,param):
        self.sql=self.conf.get("SQL",param)
        return self.sql
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import readcfg

class Get_B_tk():
    def __init__(self):
        self.rd = readcfg.Readcfg()
        self.url = self.rd.get_value('Test_url', 'test_url')
    def get_code(self):
        code=requests.get(str(self.url)+'/system/login/getCode')
        return code.json()
    def login_get_token(self,username,pwd,code):
        response=requests.post(str(self.url)+'/system/login/userLogin',
                            data={"password":pwd,"user_name":username,"verify":code})

        stk=response.json()
        return stk["data"]['token']


if __name__=="__main__":
    s=Get_B_tk()
    tk=s.get_code()
    print(tk)
    # print(s.login_get_token("admin","111111",tk))
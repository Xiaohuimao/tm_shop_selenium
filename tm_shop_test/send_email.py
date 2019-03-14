#!/usr/bin/env python
# -*- coding: utf-8 -*-
import smtplib
import os,time
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

#自动发送邮件
def send_email(new_report):
    #发件人地址
    from_addr = '1715863457@qq.com'
    #收件人地址
    to_addr = 'm0926xf@126.com,mengxuefeng@360tianma.com'
    #发送邮箱的服务器地址
    mail_server = 'smtp.qq.com'
    #邮件的标题
    subject = '商城自动化测试报告'
    #发件人的邮箱地址
    username = '1715863457@qq.com'
    password = 'wledvtuwvthwdhfi'
    #邮箱的内容和标题
    message = MIMEMultipart()
    message['From'] = Header("自动化测试")
    message['To'] = Header("QA")
    subject = '商城自动化测试报告'
    message['Subject'] = Header(subject, 'utf-8')

    # 邮件正文内容
    message.attach(MIMEText('<html><body><h1>测试报告</h1><hr><br>'
                            '<p>见附件</p></body></html>', 'html', 'utf-8'))

    # 构造附件，传送当前目录下的 test.txt 文件
    att=MIMEApplication(open(new_report,'rb').read())
    att["Content-Type"] = 'application/octet-stream'
    att.add_header('Content-Disposition','attachment',filename=('utf-8', '',"test_report.html"))
    message.attach(att)

    #发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(mail_server)
    smtp.login(username,password)
    smtp.sendmail(from_addr,to_addr.split(','),message.as_string())
    smtp.quit()

#获取最新报告的地址
def acquire_report_address(reports_address):
    #测试报告文件夹中的所有文件加入到列表
    test_reports_list = os.listdir(reports_address)
    #按照升序排序生成新的列表
    new_test_reports_list = sorted(test_reports_list)
    #获取最新的测试报告
    the_last_report = new_test_reports_list[-1]
    #最新的测试报告的地址
    the_last_report_address = os.path.join(reports_address,the_last_report)
    return the_last_report_address

if __name__=="__main__":
    i=acquire_report_address('D:/job/tm_shop_selenium/tm_shop_test/report')
    #print(i)
    send_email(i)
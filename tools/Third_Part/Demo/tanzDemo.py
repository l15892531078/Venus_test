# -*- coding: utf-8 -*-
"""
---------------------------------------
    文件名：tanzDemo.py
    描述：
    作者：penglingsen
    创建日期：2020/7/28 16:00
---------------------------------------
"""
from Venus.common.selenium_common import selenium_common
from Venus.common.web_base.login import Login

import time

# loginObj = Login()
# loginObj.open_browser(dev_obj='172.18.60.251',port='8888')
# time.sleep(2)
# selenium_common.input_text(locator='xpath=//*[@id="loginName"]',text='adm')
# selenium_common.input_text(locator='xpath=//*[@id="password"]',text='venus70')
# time.sleep(10)
# selenium_common.click_element('xpath=//*[@id="submit"]')
# time.sleep(3)
# selenium_common.click_element('xpath=//*[@id="main-menu"]/li[8]/a')
# time.sleep(1)
# selenium_common.click_element('xpath=/html/body/div/section/section/main/div/div[1]/div[1]/button[1]')
# time.sleep(1)
# selenium_common.input_text('xpath=/html/body/div[1]/section/section/main/div/div[3]/div/div[2]/form/div[1]/div/div/input','dev1')
# selenium_common.input_text('xpath=/html/body/div[1]/section/section/main/div/div[3]/div/div[2]/form/div[2]/div/div/input','172.18.60.187')
# selenium_common.input_text('xpath=/html/body/div[1]/section/section/main/div/div[3]/div/div[2]/form/div[3]/div/div/input','5555')
# selenium_common.click_element('xpath=/html/body/div[1]/section/section/main/div/div[3]/div/div[3]/div/button[2]')
# time.sleep(10)
# selenium_common.click_element('xpath=/html/body/div/section/header/div/div/i[1]')
# time.sleep(2)

# from Venus.tools.cmd_tools import CmdTools
# from Venus.product.global_variable import *
# data = {'libId':4,'modelId':1,'page':1,'pageSize':20}
# url = 'https://backend.venuscloud.cn/upgradecenter/main/getLibById'
# cm = CmdTools()
# res = cm.send_cmd(command=None,s_type=CMD_SEND_TYPE_POST,url=url,data=data)
# print(res.text)
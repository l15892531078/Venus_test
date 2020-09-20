# -*- coding: utf-8 -*-
"""
---------------------------------------
    文件名：login.py
    描述：
    作者：penglingsen
    创建日期：2020/7/15 17:01
---------------------------------------
"""
from Venus.common.selenium_common import selenium_common
from Venus.product.public.common import CommonXpath
from Venus.product.global_variable import *


class Login:

    def __init__(self):
        self.__dev_obj = None

    def open_browser(self,dev_obj,port=None,br_type='chrome', token=TOKEN):
        if isinstance(dev_obj,str):
            if port != None:
                selenium_common.open_browser(url=dev_obj+':'+str(port),browser=br_type)
            else:
                selenium_common.open_browser(url=dev_obj+':'+str(port)+f'/?token={token}', browser=br_type)
        else:
            if port != None:
                br_id = selenium_common.open_browser(url=dev_obj.get_dev_ip()+":"+str(port)+f'/?token={token}', browser=br_type)
            else:
                br_id = selenium_common.open_browser(url=dev_obj.get_dev_ip()+f'/?token={token}',browser=br_type)
            dev_obj.set_browser_id(browser_id=br_id)
        self.__dev_obj = dev_obj
        time.sleep(0.5)
        selenium_common.maximize_browser_window()

    def login(self,username='',password='',**kwargs):

        xpathObj1 = CommonXpath(target_obj=self.__dev_obj)

        if username == '':
            username = self.__dev_obj.get_dev_username()
            password = self.__dev_obj.get_dev_password()

        selenium_common.input_text(xpathObj1.login_username_xpath(),username)
        selenium_common.input_text(xpathObj1.login_password_xpath(),password)
        # 手动输入验证码
        man_verify_code = input('请填写验证码：')
        selenium_common.input_text('xpath=//*[@id="checkCode"]', man_verify_code)

        selenium_common.click_button('xpath=//*[@id="submit"]')
# ^_^ coding:utf-8 ^_^
"""
-------------------------------------------------
   文件名：selenium_common.py
   描述:
   作者: penglingsen
   创建日期: 2020/07/15
-------------------------------------------------
"""
from Venus.tools.other_library.Selenium2Library import Selenium2Library

class SeleniumCommon(Selenium2Library):

    def __init__(self):
        Selenium2Library.__init__(self, implicit_wait=5.0)

selenium_common = SeleniumCommon()
#-*- coding: utf-8 -*-
"""
---------------------------------------
    文件名：close_browser.py
    描述：
    作者：penglingsen
    创建日期：2020/7/30 16:38
---------------------------------------
"""
from Venus.common.selenium_common import selenium_common


class CloseBrowser:
    def __init__(self):
        selenium_common.close_browser()
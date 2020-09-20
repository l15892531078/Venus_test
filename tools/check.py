#-*- coding: utf-8 -*-
"""
---------------------------------------
    文件名：check.py
    描述：
    作者：penglingsen
    创建日期：2020/9/2 16:28
---------------------------------------
"""

from Venus.product.global_variable import *


class Check:
    def __init__(self, check_type, **kwargs):
        self.check_type = check_type

    def check(self, expect, actual):
        if self.check_type == '事件名称验证':
            if expect == actual:
                LOG.info(f'{expect} 事件已入库，测试结果：pass')
                return True
            else:
                LOG.info(f'{expect} 事件未入库，测试结果：fail')
                return False

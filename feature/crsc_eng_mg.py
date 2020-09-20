# -*- coding: utf-8 -*-
"""
---------------------------------------
    文件名：crsc_eng_mg.py
    描述：探针管理
    作者：penglingsen
    创建日期：2020/7/21 18:20
---------------------------------------
"""
import time
from random import choice
from Venus.common.env import env_info
from Venus.product.global_variable import *
from Venus.common.web_base.tzMngWeb import TzMngWeb
from Venus.common.web_base.login import Login
from Venus.common.web_base.close_browser import CloseBrowser
'''
TODO 判断它是否打开游览器
'''

class CrscEngMng:

    def __init__(self):
        #******* 提取网元信息，区分探针和DC
        self.DC = [] # DC
        self.TZ = [] #探针
        self.USED_TZ_NOT_ISSUE = [] # 已添加的探针，未下发策略
        self.USED_TZ_ISSUEED = [] # 已添加的探针，已下发策略
        # TODO 探针各种状态
        all_ne = env_info['DICT_NE']
        for k,v in all_ne.items():
            if v.get_dev_type() in DEV_TYPE_CRSC:
                if v.get_dev_tag().upper() == 'DC':
                    self.DC.append(v)
                elif v.get_dev_tag().upper() == 'TZ':
                    self.TZ.append(v)
        self.random_tz = choice(self.TZ)

        # 判断当前有没有打开浏览器
        # if self.DC[0].get_browser_id() == 0:
        #     from Venus.common.web_base.login import Login
        #     Login().open_browser(dev_obj=self.DC[0].get_dev_ip(),port=self.DC[0].get_web_port())

    def login(self, tz_obj=None):
        if tz_obj is None:
            tz_obj = choice(self.DC)
        Login().open_browser(tz_obj, port=TH_WEB_PORT)

    def add_tz(self, tz_name, tz_obj=None):
        '''
        添加探针
        TODO tz_obj 传入为IP时，后续实现
        :param tz_obj: 探针对象
        :param tz_name: 探针名称
        :param pro_port: DC管理探针所用的协议端口
        '''
        tz = self.check_page_on_tz_mng(tz_obj)
        self.USED_TZ_NOT_ISSUE.append(tz)

        tz.create_tz_button()
        tz.set_create_tz_config(tz_name)
        tz.click_create_tz_affirm_button()

    def tz_issue_strategy(self, tz_ip, interface=None):
        '''
        下发策略
        :param tz_ip: 探针IP
        :param interface:
        :return:
        '''
        tz = self.check_page_on_tz_mng(tz_ip)
        tz.click_issue_strategy_button(tz_ip)
        tz.set_issue_strategy_config(interface)

    def check_page_on_tz_mng(self, tz_obj=None):
        '''
        检查是否在探针管理页，没有则条钻探针管理页
        :param tz_obj:
        :return:
        '''
        if tz_obj is None:
            tz = TzMngWeb(self.random_tz)
        elif isinstance(tz_obj, str):
            for item in self.TZ:
                if tz_obj == item.get_dev_ip():
                    tz = TzMngWeb(item)
        else:
            tz = TzMngWeb(tz_obj)
        dc = TzMngWeb(self.DC[0])
        if not dc.check_page_on_tz_mng_id():
            dc.skip_tz_mng_page()
        return tz

    def delete_tz(self, ip):
        tz = self.check_page_on_tz_mng(ip)
        tz.click_delete_button(ip)

    def close_browser(self):
        time.sleep(3)
        CloseBrowser()
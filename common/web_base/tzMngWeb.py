# -*- coding: utf-8 -*-
"""
---------------------------------------
    文件名：tzMngWeb.py
    描述：探针管理页面操作
    作者：penglingsen
    创建日期：2020/7/21 19:08
---------------------------------------
"""
from random import choice
from Venus.common.selenium_common import selenium_common
from Venus.common.web_base.login import *
from Venus.product.global_variable import *
from Venus.product.public.crsc_eng_mng_cmd import CrscEngMngCmd

class TzMngWeb:
    def __init__(self, dev_obj):
        self.__dev_obj = dev_obj
        self.xpath_obj = CrscEngMngCmd(self.__dev_obj)

    def check_page_on_tz_mng_id(self):
        '''
        判断是否在探针管理页面
        '''
        now_url = selenium_common.get_location()
        if now_url == f'http://{self.__dev_obj.get_dev_ip()}:{TZ_MNG_PORT}' or now_url == f'http://{self.__dev_obj.get_dev_ip()}:{TZ_MNG_PORT}/#/':
            return True
        else:
            # print('当前页面不是探针管理页')
            return False

    def skip_tz_mng_page(self):
        '''
        跳转探针管理页
        :return:
        '''
        selenium_common.go_to(f'http://{self.__dev_obj.get_dev_ip()}:{TZ_MNG_PORT}')

    def check_page_on_home(self):
        '''
        判断是否在通号首页 暂时弃用
        :return:
        '''
        now_url = selenium_common.get_location()
        if now_url == f'{self.__dev_obj.get_dev_ip()}:{self.__dev_obj.get_dev_web_port()}/':
            # 点击探针管理页图标，进入探针管理界面
            selenium_common.click_element(self.xpath_obj.goto_crsc_eng_mng_xpath())
        else:
            print('当前页面不是首页')

    def create_tz_button(self):
        '''
        点击创建连接按钮  TODO 需判断探针是否已经创建
        '''
        selenium_common.click_button(self.xpath_obj.click_create_tz_xpath())

    def set_create_tz_config(self, name):
        '''
        新建连接配置项设置
        :param name: 名称
        :param tz_ip: IP
        :return:
        '''
        xpaths = self.xpath_obj.set_create_tz_config_xpath()
        selenium_common.input_text(xpaths[0], name)
        selenium_common.input_text(xpaths[1], self.__dev_obj.get_dev_ip())
        selenium_common.input_text(xpaths[2], DEFAULT_TZ_PRO_PORT)

    def click_delete_button(self, ip):
        '''
        点击删除探针按钮
        :return:
        '''
        tz_infos = self.get_all_tzs_info()
        if ip in tz_infos:
            div_xpath = tz_infos[ip]['web_path'] + self.xpath_obj.click_delete_tz_button_xpath()
            # TODO 判断当前探针是否，已经下发。
            selenium_common.click_element(div_xpath)
            selenium_common.click_button(self.xpath_obj.click_delete_tz_confirm_button())
        else:
            print(f'该{ip}并未创建连接')

    def click_create_tz_affirm_button(self):
        '''
        点击新建连接后，确认按钮
        :return:
        '''
        selenium_common.click_button(self.xpath_obj.click_create_tz_affirm_button_xpath())

    def click_issue_strategy_button(self, ip):
        '''
        点击下发策略按钮
        :param ip: 探针IP
        :return:
        '''
        tz_infos = self.get_all_tzs_info()
        if ip in tz_infos:
            div_xpath = tz_infos[ip]['web_path'] + self.xpath_obj.click_issue_strategy_button_xpath()
            # TODO 判断当前探针是否，已经下发。
            selenium_common.click_element(div_xpath)
        else:
            print(f'该{ip}并未创建连接')

    def get_all_tzs_info(self):
        '''
        获取所有探针的信息
        :return:
        '''
        tab_xpath = self.xpath_obj.get_all_tzs_info_xpath()
        tz_count = selenium_common.get_element_count(tab_xpath)
        tz_infos = {}
        for index in range(1, tz_count+1):
            tz_path = f"{tab_xpath}[{index}]"
            tz_info = selenium_common.get_text(tz_path).split('\n')

            tz_infos[tz_info[0]] = {'web_path': tz_path, 'infos': tz_info[1:]}
        return tz_infos

    def set_issue_strategy_config(self, interface=None, src_ip=None, src_port=None, dst_ip=None, dst_port=None, protocol=None):
        '''
        下发策略配置项设置，并点击确定
        TODO 后续应添加判断是否有除 interface 输入外的其他配置
        :param interface: 网口
        :param src_ip:
        :param src_port:
        :param dst_ip:
        :param dst_port:
        :param protocol:
        :return:
        '''
        if interface is None:
            port = choice(choice(self.__dev_obj.get_dev_bd_list()).get_port_list())
        xpath = self.xpath_obj.set_issue_strategy_config_xpath()
        selenium_common.input_text(xpath['config'], port.get_port_name())
        selenium_common.click_button(xpath['confirm'])








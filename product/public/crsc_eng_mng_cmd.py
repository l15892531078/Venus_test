# -*- coding: utf-8 -*-
"""
---------------------------------------
    文件名：crsc_eng_mng_cmd.py
    描述：探针管理
    作者：penglingsen
    创建日期：2020/7/21 10:29
---------------------------------------
"""
from Venus.tools.xpath_tools import XpathTools

class CrscEngMngCmd:

    def __init__(self, target_obj=None):
        self.__xpath_get = XpathTools(target_obj)

    def goto_crsc_eng_mng_xpath(self):
        '''
        进入探针管理页面的web路径 暂时启用
        '''
        xpath = self.__xpath_get.get_xpath(feature='crsc_eng_mng_id', className='CrscEngMngId',
                                           function='goto_crsc_eng_mng_xpath_id').goto_crsc_eng_mng_xpath_id()
        return xpath

    def click_create_tz_xpath(self):
        '''
        点击新建连接的web路径
        '''
        xpath = self.__xpath_get.get_xpath(feature='crsc_eng_mng_id', className='CrscEngMngId', function='click_create_tz_xpath_id').click_create_tz_xpath_id()
        return xpath

    def set_create_tz_config_xpath(self):
        '''
        输入新建连接配置项 页面路径
        :return:
        '''
        xpath = self.__xpath_get.get_xpath(feature='crsc_eng_mng_id', className='CrscEngMngId', function='set_create_tz_config_xpath_id').set_create_tz_config_xpath_id()
        return xpath

    def click_create_tz_affirm_button_xpath(self):
        '''
        点击新建连接后，确认按钮的web路径
        :return:
        '''
        xpath = self.__xpath_get.get_xpath(feature='crsc_eng_mng_id', className='CrscEngMngId', function='click_create_tz_affirm_button_xpath_id').click_create_tz_affirm_button_xpath_id()
        return xpath

    def get_all_tzs_info_xpath(self):
        '''
        获取页面所有探针 web路径
        :return:
        '''
        xpath = self.__xpath_get.get_xpath(feature='crsc_eng_mng_id', className='CrscEngMngId', function='get_all_tzs_info_xpath_id').get_all_tzs_info_xpath_id()
        return xpath

    def click_issue_strategy_button_xpath(self):
        '''
        点击下发策略按钮 web路径
        :return:
        '''
        xpath = self.__xpath_get.get_xpath(feature='crsc_eng_mng_id', className='CrscEngMngId', function='click_issue_strategy_button_xpath_id').click_issue_strategy_button_xpath_id()
        return xpath

    def click_delete_tz_button_xpath(self):
        '''
        点击删除探针按钮
        :return:
        '''
        xpath = self.__xpath_get.get_xpath(feature='crsc_eng_mng_id', className='CrscEngMngId', function='click_delete_tz_button_xpath_id').click_delete_tz_button_xpath_id()
        return xpath

    def click_delete_tz_confirm_button(self):
        '''
        点击删除探针
        :return:
        '''
        xpath = self.__xpath_get.get_xpath(feature='crsc_eng_mng_id', className='CrscEngMngId', function='click_delete_tz_confirm_button_id').click_delete_tz_confirm_button_id()
        return xpath

    def set_issue_strategy_config_xpath(self):
        '''
        下发策略配置项设置，并点击确定 web路径
        :return:
        '''
        xpath = self.__xpath_get.get_xpath(feature='crsc_eng_mng_id', className='CrscEngMngId', function='set_issue_strategy_config_xpath_id').set_issue_strategy_config_xpath_id()
        return xpath
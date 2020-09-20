# -*- coding: utf-8 -*-
"""
---------------------------------------
    文件名：crsc_eng_mng_id.py
    描述：探针管理页面的web路径
    作者：penglingsen
    创建日期：2020/7/21 18:48
---------------------------------------
"""
class CrscEngMngId:

    def __init__(self,devType=None):
        self.__devType = devType

    def goto_crsc_eng_mng_xpath_id(self):
        '''
        进入探针管理页面路径
        '''
        return 'xpath=//*[@id="main-menu"]/li[8]/a'

    def click_create_tz_xpath_id(self):
        '''
        新建连接按钮路径
        '''
        return 'xpath=/html/body/div[1]/section/section/main/div/div[1]/div[1]/button[1]'

    def set_create_tz_config_xpath_id(self):
        '''
        新建连接配置项设置 页面路径
        :return:
        '''
        return ['xpath=/html/body/div[1]/section/section/main/div/div[3]/div/div[2]/form/div[1]/div/div/input', 'xpath=/html/body/div[1]/section/section/main/div/div[3]/div/div[2]/form/div[2]/div/div/input', 'xpath=/html/body/div[1]/section/section/main/div/div[3]/div/div[2]/form/div[3]/div/div/input']

    def click_create_tz_affirm_button_xpath_id(self):
        '''
        点击新建连接后，确认按钮 页面路径
        :return:
        '''
        return 'xpath=/html/body/div[1]/section/section/main/div/div[3]/div/div[3]/div/button[2]'

    def click_delete_tz_button_xpath_id(self):
        '''
        点击删除探针按钮， 页面路径
        :return:
        '''
        return "/td[last()]/div/i[4]"

    def get_all_tzs_info_xpath_id(self):
        '''
        获取页面所有探针 tab路径
        :return:
        '''
        return "xpath=//*[@class='el-table__row' or @class= 'el-table__row el-table__row--striped']"

    def click_issue_strategy_button_xpath_id(self):
        '''
        点击探针下发策略，页面路径
        :return:
        '''
        return "/td[last()]/div/i[1]"

    def set_issue_strategy_config_xpath_id(self):
        return {'config': 'xpath=/html/body/div[1]/section/section/main/div/div[4]/div/div[2]/form/div[5]/div/div/input', 'confirm': 'xpath=/html/body/div[1]/section/section/main/div/div[4]/div/div[3]/div/button[2]'}

    def click_delete_tz_confirm_button_id(self):
        return 'xpath=//*[@class="el-button el-button--default el-button--small el-button--primary "]'

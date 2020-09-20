# -*- coding: utf-8 -*-
"""
---------------------------------------
    文件名：csrc_eng_mng_cmd.py
    描述：探针管理
    作者：penglingsen
    创建日期：2020/7/21 10:29
---------------------------------------
"""
from Venus.tools.xpath_tools import XpathTools

class CsrcEngMngCmd:

    def __init__(self):
        self.__xpath_get = XpathTools()

    def goto_csrc_eng_mng_xpath(self):
        '''
        进入探针管理页面的web路径
        '''
        xpath = self.__xpath_get.get_xpath(feature='csrc_eng_mng_id', className='CsrcEngMngId',
                                           function='goto_csrc_eng_mng_xpath_id').goto_csrc_eng_mng_xpath_id()
        return xpath

    def click_create_tz_xpath(self):
        '''
        点击新建连接的web路径
        '''
        xpath = self.__xpath_get.get_xpath(feature='csrc_eng_mng_id', className='CsrcEngMngId', function='click_create_tz_xpath_id').click_create_tz_xpath_id()

        return xpath

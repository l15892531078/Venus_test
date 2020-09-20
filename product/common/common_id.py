# -*- coding: utf-8 -*-
"""
---------------------------------------
    文件名：common_id.py
    描述：公共操作  公共命名、公共路径
    作者：penglingsen
    创建日期：2020/7/21 11:11
---------------------------------------
"""
from Venus.product.global_variable import *

class CommonXpathId:

    def __init__(self,devType=None):
        self.__devType = devType

    def login_username_xpath_id(self):
        '''
        用户名输入框路径
        '''
        if self.__devType in DEV_TYPE_CRSC or self.__devType in DEV_TYPE_CS:
            return 'xpath=//*[@id="loginName"]'

    def login_password_xpath_id(self):
        '''
        密码输入框路径
        '''
        if self.__devType in DEV_TYPE_CRSC or self.__devType in DEV_TYPE_CS:
            return 'xpath=//*[@id="password"]'

class CommonCmdId:

    def __init__(self,devType=None):
        self.__devType = devType

    def replay_pcap_cmd_id(self,interface, loop_time, bandwidth, pcap_file):
        return 'tcpreplay -i '+str(interface)+' -l '+str(loop_time)+' -M '+str(bandwidth)+' '+ f'"{str(pcap_file)}"'

    def query_event_sql_cmd_id(self, start_time, end_time, event_id, interface):
        return f'''
        SELECT EVENTTIME, EVENTTYPEID, PROBE_INTERFACE
        FROM netids_eventlog_today
        WHERE  EVENTTIME >= {int(start_time)} AND EVENTTIME <= {end_time} and EVENTTYPEID={event_id} and PROBE_INTERFACE= '{interface}'
        ORDER BY EVENTTIME
        '''
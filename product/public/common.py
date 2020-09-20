# ^_^ coding:utf-8 ^_^
"""
-------------------------------------------------
   文件名：public.py
   描述: 公共路径
   作者: penglingsen
   创建日期: 2019/11/25
-------------------------------------------------
"""
from Venus.tools.xpath_tools import XpathTools
from Venus.tools.cmd_tools import CmdTools

class CommonXpath:

    def __init__(self,target_obj=None):
        self.__xpath_obj = XpathTools(target_obj)

    def normal_alert_msg_xpath(self):
        '''
        普通提示信息路径
        :return:
        '''
        xpath = self.__xpath_obj.get_xpath(feature='common_id', className='CommonXpathId', function='normal_alert_msg_xpath_id').normal_alert_msg_xpath_id()
        return xpath

    def login_username_xpath(self):
        '''
        登录时，用户名输入框web路径
        '''
        xpath = self.__xpath_obj.get_xpath(feature='common_id', className='CommonXpathId', function='login_username_xpath_id').login_username_xpath_id()
        return xpath

    def login_password_xpath(self):
        '''
        登录时，用户名输入框web路径
        '''
        xpath = self.__xpath_obj.get_xpath(feature='common_id', className='CommonXpathId', function='login_password_xpath_id').login_password_xpath_id()
        return xpath

class CommonCmd:

    def __init__(self,target_obj=None):
        self.__xpath_obj = XpathTools(target_obj)
        self.__cmd_obj = CmdTools(send_obj=target_obj)

    def replay_pcap_cmd(self,interface,loop_time,bandwidth,pcap_file):
        '''
        使用tcpreplay回放包
        '''
        cmd = self.__xpath_obj.get_xpath(feature='common_id',className='CommonCmdId',function='replay_pcap_cmd_id').replay_pcap_cmd_id(interface,loop_time,bandwidth,pcap_file)
        self.__cmd_obj.send_cmd(command=cmd,s_type='ssh')
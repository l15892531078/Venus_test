# -*- coding: utf-8 -*-
"""
---------------------------------------
    文件名：feature_detection.py
    描述：特征检测模块
    作者：penglingsen
    创建日期：2020/7/21 16:34
---------------------------------------
"""

from random import choice
from Venus.tools.cmd_tools import CmdTools
from Venus.common.env import env_info
from Venus.product.global_variable import *
from Venus.product.common.common_id import CommonCmdId
from Venus.tools.check import Check
from Venus.tools.excel_tool import ExportExcel

class FeatureDetection:

    def __init__(self):

        #******* 提取网元信息，区分探针和DC
        self.DC = [] # DC
        self.TZ = [] #探针

        all_ne = env_info['DICT_NE']
        for k,v in all_ne.items():
            if v.get_dev_type() in DEV_TYPE_CRSC:
                if v.get_dev_tag().upper() == 'DC':
                    self.DC.append(v)
                elif v.get_dev_tag().upper() == 'TZ':
                    self.TZ.append(v)
        self.cmd_obj = CommonCmdId()
        self.cmd_tool_tz = CmdTools(self.TZ[0])
        self.cmd_tool_dc = CmdTools(self.DC[0])

    def verify_event(self, event_name):
        '''
        通过事件名称验证事件是否上报
        :param event_name: 事件名
        :return:
        '''
        if event_name is None:
            event_name = choice(['IP_JOLT_拒绝服务', 'FTP_口令弱', 'HTTP_SQL注入攻击'])
        pcap_name = PCAPMAP[event_name][0]
        event_id = PCAPMAP[event_name][1]
        ports = choice(self.TZ[0].get_dev_bd_list()).get_port_list()
        # TODO 任选一张网卡还是双网卡都下发策略？
        interface = ports[1].get_port_name()
        tcpreplay_cmd = self.cmd_obj.replay_pcap_cmd_id(interface, 1, 1, pcap_name)
        # TODO 判断命名是否下发成功,后期固定pcap包的路径
        pcaps_path = 'cd /home/pcaps'
        start_time = self.cmd_tool_tz.send_cmd(f'{pcaps_path};{tcpreplay_cmd}')
        end_time = start_time + 1
        sql_cmd = self.cmd_obj.query_event_sql_cmd_id(start_time, end_time, event_id, interface)
        query_result = self.retry(9, sql_cmd)
        if query_result:
            query_result = event_name
        verify = Check('事件名称验证')
        result = verify.check(event_name, query_result)
        excel = ExportExcel()
        if result:
            excel.export(event_name, 'pass')
        else:
            excel.export(event_name, 'fail')
        excel.save_excel()

    def retry(self, num, cmd):
        '''
        用于sql等命令重试
        :param num: 重试次数
        :param cmd: 命令
        :return:
        '''
        # 重试次数
        result = False
        count = num
        while count > 0:
            data = self.cmd_tool_dc.send_cmd(cmd, CMD_SEND_TYPE_MYSQL)
            if data:
                result = True
            # 写入时间一分钟以上，
            time.sleep(10)
            count -= 1
        return result

    def test_event(self, event_name=None):
        '''
        当个事件的测试接口
        :param event_name: 事件名，为空则任选
        :return:
        '''
        self.cmd_tool_tz.connect_linux()
        self.cmd_tool_dc.connect_mysql()
        self.verify_event(event_name)
        self.cmd_tool_tz.close_ssh()
        self.cmd_tool_dc.close_mysql()

    def test_events(self):
        '''
        多个事件的测试接口
        :return:
        '''
        self.cmd_tool_tz.connect_linux()
        self.cmd_tool_dc.connect_mysql()

        events = [name for name in PCAPMAP.keys()]
        for event in events:
            self.verify_event(event)
        self.cmd_tool_tz.close_ssh()
        self.cmd_tool_dc.close_mysql()


        # -------- 通号入侵检测初始化 ------------
        # ******* 提取网元信息，区分探针和DC
        self.DC = []  # DC
        self.TZ = []  # 探针
        all_ne = env_info['DICT_NE']
        for k, v in all_ne.items():
            if v.get_dev_type() in DEV_TYPE_CRSC:
                if v.get_dev_tag().upper() == 'DC':
                    self.DC.append(v)
                elif v.get_dev_tag().upper() == 'TZ':
                    self.TZ.append(v)

        # 判断当前有没有打开浏览器
        if self.DC[0].get_browser_id() == 0:
            from Venus.common.web_base.login import Login
            Login().open_browser(dev_obj=self.DC[0].get_dev_ip(), port=self.DC[0].get_web_port())

    def set_event(self,valid=True):
        '''
        设置事件有效性
        :param valid: True False
        :return:
        '''
        print("设置有效性")

#-*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# @project : Venus
# @author: 彭楷棱
# @file: floweye_dc.py
# @ide: PyCharm
# @time: 2020/9/2 20:53

#-*- coding: utf-8 -*-
"""
---------------------------------------
    文件名：floweye_dc.py
    描述：
    作者：penglingsen
    创建日期：2020/9/2 16:28
---------------------------------------
"""
import time
# from global_veriable import *
from telnet_gb import *
import telnetlib


class FlowEyeDc:
    def __init__(self):
        self.tn = telnetlib.Telnet(HOST, port=PORT, timeout=10)

    def command(self, flag='', str_="", func=None, read_all=False, write=False, read=False, timeout=None, decode_='utf8', **kwargs):
        if read_all:
            self.tn.write(str_.encode() + b"\n")
            time.sleep(2)
            data = self.tn.read_very_eager()
            data = data.decode(decode_)
            if func:
                manage_data = func(data, **kwargs)
                return manage_data
            return data
        elif write:
            self.tn.write(str_.encode()+b"\n")
        elif read:
            data = self.tn.read_very_eager()
            data = data.decode(decode_)
            return data
        else:
            data = str(self.tn.read_until(flag.encode(), timeout=timeout), encoding=decode_)
            self.tn.write(str_.encode()+b"\n")
            return data

    def fe_login(self, user, password):
        '''
        登录
        :param user:
        :param password:
        :return:
        '''
        info = self.command(read_all=True, decode_='gbk')
        if 'CyberAudit' in info:
            self.command(str_=user, write=True)
            self.command(flag='Password', str_=password)

    def serial(self, GZ_TYPE):
        '''
        配置序列号
        :return:
        '''
        self.fe_login(FE_USER, FE_PASSWORD)
        time.sleep(1)
        serial_no = f'0636202008029999'
        self.command(str_=f'echo {serial_no} > /doc/boot/serial.no')
        self.command(str_='exit')

    def fedc_init(self):
        '''
        初始化引擎
        :return:
        '''
        self.fe_login(ENGINE_USER, ENGINE_PASSWORD)
        self.command(flag='term', str_='2', decode_='gbk')

    def network(self):
        self.fe_login(CONFIG_USER, CONFIG_PASSWORD)
        time.sleep(1)
        info = self.command(str_='3', decode_='gbk', read_all=True)
        print(info)
        if 'ge0' in info:
            print('good')

    def select_interface(self):
        pass

    def set_capcomm(self):
        pass

    def operation(self):
        self.serial()
        self.fedc_init()


# gb = AutoFilling()
# gb.gb_operation()
fe = FlowEyeDc()
fe.operation()

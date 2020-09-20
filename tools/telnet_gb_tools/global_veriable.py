#-*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
---------------------------------------
    文件名：global_veriable.py
    描述：
    作者：penglingsen
    创建日期：2020/8/27 16:28
---------------------------------------
"""
HOST = '172.18.60.249'
CS_USER = "adm"
CS_PASSWORD = "venus70"
USER = 'dia'
PASSWORD = 'hwlypaqdtk!'

ENGINE_FILE = 'vsos.bin'
DC_FILE = 'ids.tar.gz'
ENGINE_MASK = '24'
ENGINE_INTERFACE = 'eth0'
GATEWAY = '172.18.60.1'

host = input('请输入串口服务器IP(输入空，默认为172.18.60.249):')
PORT = input('请输入串口服务器端口(必填):')
engine_interface = input('请输入引擎硬件设备管理口(输入空，为默认网卡eth0):')
if host:
    HOST = host
if engine_interface:
    ENGINE_INTERFACE = engine_interface

ENGINE_IP = input('请输入引擎设备IP(必填):').strip()
FTP_IP = input('请输入TFTP软件所在的PC机IP地址(必填):').strip()




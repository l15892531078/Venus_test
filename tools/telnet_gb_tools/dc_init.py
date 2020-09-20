#-*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
---------------------------------------
    文件名：dc_init.py
    描述：
    作者：penglingsen
    创建日期：2020/8/31 15:49
---------------------------------------
"""

from telnet灌包.telnet_gb import *
import time
import telnetlib


class DC:
    '''
    控制端配置
    '''
    def __init__(self):
        self.tn = telnetlib.Telnet(HOST, port=PORT, timeout=10)

    def cs_login(self):
        info = self.command(read_all=True)
        if 'Username' in info:
            self.command(str_='adm', write=True)
            self.command('Password:', str_='venus70')

    def command(self, flag='', str_="", func=None, read_all=False, write=False, read=False, timeout=None, **kwargs):
        if read_all:
            self.tn.write(str_.encode() + b"\n")
            time.sleep(1)
            data = self.tn.read_very_eager()
            data = data.decode('utf8')
            if func:
                manage_data = func(data, **kwargs)
                return manage_data
            return data
        elif write:
            self.tn.write(str_.encode()+b"\n")
        elif read:
            data = self.tn.read_very_eager()
            data = data.decode('utf8')
            return data
        else:
            self.tn.read_until(flag.encode(), timeout=timeout)
            self.tn.write(str_.encode()+b"\n")


    def network_config(self, path='/hdisk'):
        '''
        网络及抓包口配置
        :return:
        '''
        info = self.command(read_all=True)
        try:
            if '>' in info:
                self.command(str_='en', write=True)
            info = self.command(str_='configure terminal', read_all=True)
            if 'config' in info:
                ip_check = self.command(str_=f'ip address {ENGINE_IP}/24', read_all=True)
                if 'Repeat Settings' in ip_check:
                    self.command(write=True, str_='q')
                    self.command(write=True, str_=USER)
                    self.command(flag='Password', str_=PASSWORD)
                    time.sleep(0.5)
                    login_check = self.command(read=True)
                    if '/' in login_check:
                        path_check = self.command(str_=f'cd {path}', read_all=True)
                        if path in path_check:
                            return True
        except Exception as e:
            print(e)

    def tftp_file(self):
        self.command(write=True, str_=f'tftp -gr {DC_FILE} {FTP_IP}')

    def reboot_cs(self):
        self.command()
        self.command(write=True, str_='reboot')

    def close(self):
        self.tn.close()

    def operation(self):
        self.cs_login()
        res = self.network_config(path='/doc')
        if res:
            self.tftp_file()
            self.command(flag='/', str_='')


dc = DC()
dc.operation()

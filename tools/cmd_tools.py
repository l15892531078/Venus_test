# -*- coding: utf-8 -*-
"""
---------------------------------------
    文件名：cmd_tools.py
    描述：
    作者：penglingsen
    创建日期：2020/7/21 16:52
---------------------------------------
"""
import json, paramiko, pymysql
from Venus.product.global_variable import *
import Venus.tools.Third_Part.requests as requests


class CmdTools:
    def __init__(self, send_obj=None):
        self.__send_obj = send_obj
        self.ssh_client = None
        self.db = None

    def connect_linux(self):
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh_client.connect(hostname=self.__send_obj.get_dev_ip(), port=22,
                           username=self.__send_obj.get_dev_username(), password=self.__send_obj.get_dev_password())

    def close_ssh(self):
        self.ssh_client.close()

    def connect_mysql(self):
        self.db = pymysql.connect(host=self.__send_obj.get_dev_ip(), port=3306,
                                  user=self.__send_obj.get_dev_db_username(),
                                  password=self.__send_obj.get_dev_db_password(),
                                  database=self.__send_obj.get_dev_database())

    def close_mysql(self):
        self.db.close()

    def send_cmd(self, command, s_type=CMD_SEND_TYPE_SSH, **kwargs):
        '''
        命令下发
        '''
        if s_type == CMD_SEND_TYPE_SSH:
            start_time = time.time()
            try:
                stdin, stdout, stderr = self.ssh_client.exec_command(command)
                out = stdout.read()
                err = stderr.read()
                if out:
                    LOG.info(f"\n回放结果：\n{out.decode('utf8')}")
                if err:
                    LOG.info(f"\n回放结果：\n{err.decode('utf8')}")
            except Exception as e:
                LOG.error(e)
            return start_time
        elif s_type == CMD_SEND_TYPE_MYSQL:
            cursor = self.db.cursor()
            cursor.execute(command)
            data = cursor.fetchall()
            self.db.commit()
            return data
        else:
            if 'data' in kwargs:
                data = json.dumps(kwargs['data'])
                kwargs['data'] = data
            if s_type == CMD_SEND_TYPE_POST:
                return requests.post(headers=CMD_POST_GET_HEADER,**kwargs)
            elif s_type == CMD_SEND_TYPE_GET:
                return requests.get(headers=CMD_POST_GET_HEADER,**kwargs)
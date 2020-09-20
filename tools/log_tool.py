#-*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
---------------------------------------
    文件名：log_tool.py
    描述：
    作者：penglingsen
    创建日期：2020/8/4 14:16
---------------------------------------
"""

import logging
import time
import os

current_path = os.path.abspath(__file__)
father_path = os.path.abspath(os.path.dirname(os.path.dirname(current_path)))
class TestLog(object):
    '''
    封装后的logging
    '''
    def __init__(self, logger=None, name=None):
        '''

        :param logger:
        '''
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        self.log_time = time.strftime("%Y_%m_%d_")
        self.log_path = father_path
        if name:
            self.log_name = self.log_path + self.log_time + f'{name}'
        self.log_name = self.log_path + os.path.sep + self.log_time + 'test.log'

        fh = logging.FileHandler(self.log_name, 'a', encoding='utf8')
        fh.setLevel(logging.INFO)

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        formatter = logging.Formatter('[%(asctime)s] %(filename)s->%(funcName)s line:%(lineno)d [%(levelname)s]%(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        self.logger.addHandler(fh)
        self.logger.addHandler(ch)



        fh.close()
        ch.close()

    def getlog(self):
        return self.logger
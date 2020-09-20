#-*- coding: utf-8 -*-
"""
---------------------------------------
    文件名：parsePcapmap.py
    描述：
    作者：penglingsen
    创建日期：2020/8/3 17:53
---------------------------------------
"""


import json, os, sys

filepath = 'E:\Python\Python38-32\Lib\site-packages\Venus'
class parsePcapmap:
    @staticmethod
    def parse_pcap_map():
        with open(os.path.join(filepath, 'pcap_map.conf'), 'r', encoding='gbk') as f:
            data = json.loads(f.read())
            return data

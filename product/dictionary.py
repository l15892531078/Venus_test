# ^_^ coding:utf-8 ^_^
"""
-------------------------------------------------
   文件名：dictionary.py
   描述: 数据字典，定义规格数据等
   作者: penglingsen
   创建日期: 2019/11/5
-------------------------------------------------
"""
import random
import time
from Venus.tools.parse_tools.parsePcapmap import parsePcapmap


DEV_TYPE = {'ids':['IDS','IDS7050'],'cs':['CS','CS7060'],'crsc':['CRSC']}

CMD_SEND_TYPE = {'POST':'POST','GET':'GET','SSH':'SSH', 'MYSQL':'MYSQL'}

PCAPS = parsePcapmap().parse_pcap_map()

RANDOM_PCAP = [event for event in PCAPS.keys()]

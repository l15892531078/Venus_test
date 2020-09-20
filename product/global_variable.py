# ^_^ coding:utf-8 ^_^
"""
-------------------------------------------------
   文件名：global_variable.py
   描述: 全局变量，直接定义或者从数据字典取数据，供支撑和脚本调用
   作者: penglingsen
   创建日期: 2019/11/5
-------------------------------------------------
"""
from Venus.product.dictionary import *
from Venus.tools.log_tool import TestLog


DEV_TYPE_CS = DEV_TYPE['cs']
DEV_TYPE_IDS = DEV_TYPE['ids']
DEV_TYPE_CRSC = DEV_TYPE['crsc']

DEFAULT_TZ_PRO_PORT = 5555  # 探针默认连接端口
TH_WEB_PORT = 8888  #通号检测中心访问端口
TZ_MNG_PORT = 8082
MOLOCH_PORT = 9005
EXCHANGE_PORT = 8082
TOKEN = '97624c57e74b9a7803c1cd329eed34ee' # 通号免登录的token
PCAPMAP = PCAPS
RANDOM_PCAP = RANDOM_PCAP

CMD_SEND_TYPE_POST = CMD_SEND_TYPE['POST']
CMD_SEND_TYPE_GET = CMD_SEND_TYPE['GET']
CMD_SEND_TYPE_SSH = CMD_SEND_TYPE['SSH']
CMD_SEND_TYPE_MYSQL = CMD_SEND_TYPE['MYSQL']

CMD_POST_GET_HEADER = {'Content-Type':'application/json'}

LOG = TestLog().getlog()
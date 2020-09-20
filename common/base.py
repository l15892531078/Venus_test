# ^_^ coding:utf-8 ^_^
"""
-------------------------------------------------
   文件名：base.py.py
   描述: 设备组网相关基类
   作者: penglingsen
   创建日期: 2019/11/5
-------------------------------------------------
"""
class Ne:

    def __init__(self,ip,dev_type,version,id,username,password,ne_name,bd_list):
        self.__ip = ip
        self.__dev_type = dev_type
        self.__version = version
        self.__id = id
        self.__username = username
        self.__password = password
        self.__ne_name = ne_name
        self.__bd_list = bd_list
        self.__browser_id = 0
    def get_ne_ip(self):
        '''
        获取网元IP
        :return: 网元IP
        '''
        return self.__ip

    def get_dev_type(self):
        '''
        获取网元类型
        :return: 网元类型
        '''
        return self.__dev_type

    def get_version(self):
        '''
        获取网元版本（组网图）
        :return: 网元版本
        '''
        return self.__version

    def get_ne_id(self):
        '''
        获取网元ID
        :return: 网元ID
        '''
        return self.__id

    def get_username(self):
        '''
        获取用户名
        :return: 用户名
        '''
        return self.__username

    def get_password(self):
        '''
        获取网元密码
        :return: 密码
        '''
        return self.__password

    def get_ne_name(self):
        '''
        获取网元名称
        :return: 网元名称
        '''
        return self.__ne_name

    def get_bd_list(self):
        '''
        获取网元下所存在的单板列表
        :return: 单板列表
        '''
        return self.__bd_list

    def set_bd_list(self,bd_list):
        '''
        设置网元下的单板列表，只在组网初始化时使用，其他模块不允许修改
        :param bd_list: 单板对象列表
        :return: NA
        '''
        self.__bd_list = bd_list

    # def set_browser_id(self,browser_id):
    #     '''
    #     打开对应的ne web界面传递时，设置web browser的id
    #     :param id: browser id
    #     :return:
    #     '''
    #     self.__browser_id = browser_id
    # 
    # def get_browser_id(self):
    #     return self.__browser_id

class Board:

    def __init__(self,bid,bd_type,bd_name,port_list,ne_obj):

        self.__bid = bid
        self.__bd_type = bd_type
        self.__bd_name = bd_name
        self.__port_list = port_list
        self.__ne_obj = ne_obj

    def get_bid(self):
        '''
        获取单板ID
        :return: 单板ID
        '''
        return self.__bid

    def get_bd_type(self):
        '''
        获取单板类型
        :return: 单板类型
        '''
        return self.__bd_type

    def get_bd_name(self):
        '''
        获取单板名称
        :return: 单板名称
        '''
        return self.__bd_name

    def get_port_list(self):
        '''
        获取单板下的端口对象列表
        :return: 端口对象列表
        '''
        return self.__port_list

    def set_port_list(self,port_list):
        '''
        设置单板下的端口对象列表，只在组网初始化时使用，其它模块不允许调用
        :param port_list:端口列表对象
        :return:NA
        '''
        self.__port_list = port_list

    def get_ne_obj(self):
        '''
        获取单板所在的网元对象
        :return: 网元对象
        '''
        return self.__ne_obj

class Port:

    def __init__(self,pid,port_type,port_name,port_mode,bd_obj):

        self.__pid = pid
        self.__port_type = port_type
        self.__port_name = port_name
        self.__port_mode = port_mode
        self.__bd_obj = bd_obj

    def get_pid(self):
        '''
        获取端口ID
        :return: 端口ID
        '''
        return self.__pid

    def get_port_type(self):
        '''
        获取端口类型
        :return: 端口类型
        '''
        return self.__port_type

    def get_port_name(self):
        '''
        获取端口名称
        :return: 端口名称
        '''
        return self.__port_name

    def set_port_name(self,name):
        '''
        设置端口名称
        @param name: 新端口名称
        '''
        self.__port_name = name

    def get_port_mode(self):
        '''
        获取端口工作模式
        '''
        return self.__port_mode

    def get_bd_obj(self):
        '''
        获取端口所在的单板对象
        :return: 单板对象
        '''
        return self.__bd_obj
	

class Link:

    def __init__(self,link_id,link_type,link_name,source,destination,direction):

        self.__link_id = link_id
        self.__link_type = link_type
        self.__link_name = link_name
        self.__source = source
        self.__destination = destination
        self.__direction = direction

    def get_link_id(self):
        '''
        获取链路ID
        :return:链路ID
        '''
        return self.__link_id

    def get_link_type(self):
        '''
        获取链路类型
        :return: 链路类型
        '''
        return self.__link_type

    def get_link_name(self):
        '''
        获取链路名称
        :return: 链路名称
        '''
        return self.__link_name

    def set_link_name(self,link_name):
        '''
        设置链路名称
        :param link_name: 链路名称
        :return: NA
        '''
        self.__link_name = link_name

    def get_source(self):
        '''
        获取链路源端口（源通道）
        :return: 源端口（源通道）
        '''
        return self.__source

    def set_source(self,source):
        '''
        设置链路源端口（源通道）
        :param source: 源端口（源通道）
        :return: NA
        '''
        self.__source = source

    def get_destination(self):
        '''
        获取链路目的端口（目的通道）
        :return: 目的端口（目的通道）
        '''
        return self.__destination

    def set_destination(self,destination):
        '''
        s设置链路目的端口（目的通道）
        :param destination: 目的端口（目的通道）
        :return: NA
        '''
        self.__destination = destination

    def get_direction(self):
        '''
        获取链路方向
        :return: 链路方向(前向：tx,反向：rx,双向：bi)
        '''
        return self.__direction

    def set_direction(self,direction):
        '''
        设置链路方向
        :param direction:链路方向
        :return: NA
        '''
        self.__direction = direction
		

class Instrument:

    def __init__(self,ins_name,ins_type,ins_ip,api_server_ip,bd_list):
        self.__ins_name = ins_name
        self.__ins_type = ins_type
        self.__ins_ip = ins_ip
        self.__api_server_id = api_server_ip
        self.__bd_list = bd_list

    def get_ins_name(self):
        '''
        获取仪表名称
        :return: 仪表名称
        '''
        return self.__ins_name

    def get_dev_type(self):
        '''
        获取仪表类型
        :return: 仪表类型
        '''
        return self.__ins_type

    def get_ins_ip(self):
        '''
        获取仪表IP
        :return: 仪表IP
        '''
        return self.__ins_ip

    def get_api_server_ip(self):
        '''
        获取仪表api接口服务器IP
        :return:
        '''
        return self.__api_server_id

    def get_bd_list(self):
        '''
        获取仪表下面的单板对象
        :return: list[单板对象列表]
        '''
        return self.__bd_list

    def set_bd_list(self,bd_list):
        '''
        设置仪表的单板对象列表
        :param bd_list: 新的单板对象列表
        :return: 新的仪表对象
        '''
        self.__bd_list = bd_list

class VenusDev:

    def __init__(self,ne_name, ip, dev_type, version, username, password, web_port, bd_list, database, db_username, db_password, tag=''):
        self.__ne_name = ne_name
        self.__ip = ip
        self.__dev_type = dev_type
        self.__version = version
        self.__username = username
        self.__password = password
        self.__bd_list = bd_list
        self.__web_port = web_port
        self.__browser_id = 0
        self.__database = database
        self.__db_username = db_username
        self.__db_password = db_password
        self.__tag = tag

    def get_dev_database(self):
        return self.__database

    def set_dev_database(self, database):
        self.__database = database

    def get_dev_db_username(self):
        return self.__db_username

    def set_dev_db_username(self, db_username):
        self.__db_username = db_username

    def get_dev_db_password(self):
        return self.__db_password

    def set_dev_db_password(self, db_password):
        self.__db_password = db_password

    def get_dev_web_port(self):
        return self.__web_port

    def set_dev_web_port(self, web_port):
        self.__web_port = web_port

    def get_dev_ne_name(self):
        return self.__ne_name

    def set_dev_ne_name(self,ne_name):
        self.__ne_name = ne_name

    def get_dev_ip(self):
        return self.__ip

    def set_dev_ip(self,dev_ip):
        self.__ip = dev_ip

    def get_dev_type(self):
        return self.__dev_type

    def set_dev_type(self,dev_type):
        self.__dev_type = dev_type

    def get_dev_version(self):
        return self.__version

    def set_dev_version(self,version):
        self.__version = version

    def get_dev_username(self):
        return self.__username

    def set_dev_username(self,username):
        self.__username = username

    def get_dev_password(self):
        return self.__password

    def set_dev_password(self,password):
        self.__password = password

    def get_dev_bd_list(self):
        return self.__bd_list

    def set_dev_bd_list(self,bd_list):
        self.__bd_list = bd_list

    def get_dev_tag(self):
        return self.__tag

    def set_dev_tag(self,new_tag):
        self.__tag = new_tag
        
    def set_browser_id(self,browser_id):
        '''
        打开对应的ne web界面传递时，设置web browser的id
        :param id: browser id
        :return:
        '''
        self.__browser_id = browser_id

    def get_browser_id(self):
        return self.__browser_id

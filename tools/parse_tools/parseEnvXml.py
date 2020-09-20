# -*- coding: utf-8 -*-
"""
---------------------------------------
    文件名：parseEnvXml.py
    描述：
    作者：penglingsen
    创建日期：2020/7/20 15:02
---------------------------------------
"""
import xmltodict,json,os
from Venus.common.base import VenusDev,Board,Port

current_path = os.path.abspath(os.path.dirname(__file__))
class ParseEnvXml:

    def __init__(self, xml=os.path.join(current_path, 'env.xml')):
        self.xml_file = xml

    def __parse_xml(self):
        '''
        解析xml文件，得到网元设备信息
        :param xml: xml文件
        :return: dict ne
        '''
        xml_file = open(self.xml_file,'r',encoding='utf-8')
        xmlStr = xml_file.read()
        convertJson = xmltodict.parse(xmlStr,encoding='utf-8')
        jsonStr = json.dumps(convertJson,indent=4)
        jsonDict = json.loads(jsonStr)
        xml_file.close()
        return list(jsonDict.values())[0]['ne']

    def init_env(self):
        '''
        初始化组网对象
        '''
        ENV_DICT = {'DICT_NE':{},'DICT_BOARD':{},'DICT_PORT':{}}

        ne_info = self.__parse_xml()
        for ne in ne_info:
            names = locals()
            names[ne['@ne_name']] = type(ne['@ne_name'], (VenusDev,), {})(ne_name=ne['@ne_name'],
                                                                          ip=ne['@ip'],
                                                                          dev_type=ne['@dev_type'],
                                                                          version=ne['@version'],
                                                                          username=ne['@username'],
                                                                          web_port=ne['@web_port'],
                                                                          password=ne['@password'],
                                                                          database=ne['@database'],
                                                                          db_username=ne['@db_username'],
                                                                          db_password=ne['@db_password'],
                                                                          bd_list=None,
                                                                          tag=ne['@tag'])

            if 'board' in list(ne.keys()):
                bd_list = []
                board = ne['board']
                if isinstance(board,dict):
                    board = [board]
                for bd in board:
                    names[bd['@bd_name']] = type(bd['@bd_name'],(Board,),{})(bid=bd['@bid'],bd_type=bd['@bd_type'],
                                                                             bd_name=bd['@bd_name'],
                                                                             port_list=None,
                                                                             ne_obj=names[ne['@ne_name']])
                    bd_list.append(names[bd['@bd_name']])

                    if 'port' in list(bd.keys()):
                        port_list = []
                        port = bd['port']
                        if isinstance(port,dict):
                            port = [port]
                        for pt in port:
                            names[pt['@port_name']] = type(pt['@port_name'],(Port,),{})(pid=pt['@pid'],port_type=pt['@port_type'],
                                                                                        port_name=pt['@port_name'],port_mode=pt['@port_mode'],
                                                                                        bd_obj=names[bd['@bd_name']])
                            port_list.append(names[pt['@port_name']])
                            ENV_DICT['DICT_PORT'].update({pt['@port_name']:names[pt['@port_name']]})
                        names[bd['@bd_name']].set_port_list(port_list=port_list)
                    ENV_DICT['DICT_BOARD'].update({bd['@bd_name']:names[bd['@bd_name']]})
                names[ne['@ne_name']].set_dev_bd_list(bd_list=bd_list)
            ENV_DICT['DICT_NE'].update({ne['@ne_name']:names[ne['@ne_name']]})
        return ENV_DICT

parese = ParseEnvXml()
parese.init_env()
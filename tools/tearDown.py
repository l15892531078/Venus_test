# ^_^ coding:utf-8 ^_^
"""
-------------------------------------------------
   文件名：tearDown.py
   描述:
   作者: penglingsen
   创建日期: 2019/11/22
-------------------------------------------------
"""
import os

class TearDown:

    def __kill_chrome_driver(self):
        '''
        杀死后台全部的chrome_driver进程
        :return:
        '''
        os.system('tskill chromedriver')
        os.system('tskill chrome')

    def __release_api_server_port(self):
        '''
        测试套执行完成后释放仪表端口
        :return:
        '''
        # from Venus.tools.instrument.source_mng import ApiServMng
        # ApiServMng().release_serv_port()
        pass

    def clean_up(self,obj='tc'):
        self.__kill_chrome_driver()
        if obj == 'ts':
            self.__release_api_server_port()

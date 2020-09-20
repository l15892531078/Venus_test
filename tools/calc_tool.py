# ^_^ coding:utf-8 ^_^
"""
-------------------------------------------------
   文件名：calc_tool.py
   描述: 计算相关工具
   作者: penglingsen
   创建日期: 2019/11/25
-------------------------------------------------
"""
class CalcTool:

    def create_dict_without_none(self,**kwargs):
        '''
        根据传入的参数创建一个新的字典变量，当参数取值为None时，则不创建该参数
        :param kwargs:
        :return: new para dict
        '''
        new_para_dict = {}
        for k,v in kwargs.items():
            if v != None and v != 'None':
                new_para_dict.update({k:v})

        return new_para_dict
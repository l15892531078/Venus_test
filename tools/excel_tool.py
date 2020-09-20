#-*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
---------------------------------------
    文件名：excel_tool.py
    描述：excle相关工具
    作者：penglingsen
    创建日期：2020/7/21 16:52
---------------------------------------
"""

import os
import xlwt
import xlrd
from xlutils.copy import copy


current_path = os.path.abspath(__file__)
father_path = os.path.dirname(os.path.abspath(os.path.dirname(current_path) + os.path.sep + "."))

EXPORT_PATH = father_path
class ExportExcel():
    def __init__(self, filename='cs_test_result.xls'):
        self.export_file = os.path.join(EXPORT_PATH, filename)
        if not os.path.exists(self.export_file):
            self.write_header()
        self.workbook = xlrd.open_workbook(self.export_file)
        self.sheet = self.workbook.sheet_by_index(0)
        self.excel = copy(self.workbook)

    def write_header(self):
        # 写入表头
        workbook = xlwt.Workbook(encoding='utf-8')
        sheet = workbook.add_sheet('CS事件上报测试结果')
        sheet.write(0, 0, '事件名称')
        sheet.write(0, 1, '测试结果')
        workbook.save(self.export_file)

    def export(self, event_name, result):
        rows = self.sheet.nrows
        table = self.excel.get_sheet(0)
        table.write(rows, 0, event_name)
        table.write(rows, 1, result)

    def save_excel(self):
        self.excel.save(self.export_file)



if __name__ == '__main__':
    workbook = ExportExcel()
    workbook.export()

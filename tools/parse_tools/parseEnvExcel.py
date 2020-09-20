# ^_^ coding:utf-8 ^_^
"""
-------------------------------------------------
   文件名：parseEnvExcel.py
   描述: 解析excel格式的组网图
   作者: penglingsen
   创建日期: 2019/11/5
-------------------------------------------------
"""
import xlrd,xlwt
import os,sys,time
import re

class parseExcel:

    def read_env_excel(self,run_level=4):
        '''
        解析测试组网文件
        :param run_level: 执行级别
                            4: 测试套执行
                            3: 3级目录执行
                            2: 2级目录执行
                            1: 1级目录执行
                            0: 场景入口执行
        :return:
        '''

        if os.getcwd() != '':
            cur_path = os.getcwd()
        else:
            cur_path = os.path.dirname(sys.argv[0])

        env_sence_name = os.path.basename(cur_path)

        level4_path = cur_path
        level3_path = os.path.dirname(level4_path)
        level2_path = os.path.dirname(level3_path)
        level1_path = os.path.dirname(level2_path)

        if run_level == 4:
            env_path = os.path.dirname(level4_path)
        elif run_level == 3:
            env_path = os.path.dirname(level2_path)
        elif run_level == 2:
            env_path = os.path.dirname(level3_path)
        elif run_level == 1:
            env_path = os.path.dirname(level4_path)
        else:
            env_path = cur_path

        env_file = None
        for file in os.listdir(env_path):
            index = file.find('.xlsx')
            if index > -1:
                if re.search(env_sence_name.upper(),file.upper()) != None:
                    env_file = file
        print(env_path)
        if env_file != None:
            real_env_file = env_path + '/' + env_file
        else:
            raise AssertionError(" ERRO: Has no env file or link file,Please check...")

        excel_env = xlrd.open_workbook(real_env_file)
        env_sheets = excel_env.sheet_names()

        ne_info_all = []
        instrument_info_all = []
        link_info_all = []
        for sheet_name in env_sheets:
            env_sheet = excel_env.sheet_by_name(sheet_name)
            # 设备为网元
            ne_dict = {}
            ne_sheet = env_sheet.cell_value(0, 0)
            if 'ne' in ne_sheet or 'ncs' in ne_sheet:

                all_bd_key = []
                all_bd_value = []

                all_port_key = []
                all_port_value = []

                all_ch_key = []
                all_ch_value = []

                bd_key = env_sheet.col_values(2)
                bd_value = env_sheet.col_values(3)
                for index in range(0,len(bd_key)):
                    if bd_key[index] != '':
                        all_bd_key.append(bd_key[index])
                        all_bd_value.append(bd_value[index])

                port_key = env_sheet.col_values(4)
                port_value = env_sheet.col_values(5)
                for index in range(0,len(port_key)):
                    if port_key[index] != '':
                        all_port_key.append(port_key[index])
                        all_port_value.append(port_value[index])

                ch_key = env_sheet.col_values(6)
                ch_value = env_sheet.col_values(7)
                for index in range(0,len(ch_key)):
                    if ch_key[index] != '':
                        all_ch_key.append(ch_key[index])
                        all_ch_value.append(ch_value[index])

                # 取 ne
                ne_col_keys = env_sheet.col_values(0)
                ne_col_values = env_sheet.col_values(1)
                for index in range(0,len(ne_col_keys)):
                    if ne_col_keys[index] != '':
                        if type(ne_col_values[index]) == float:
                            ne_dict[ne_col_keys[index]] = str(int(ne_col_values[index]))
                        else:
                            ne_dict[ne_col_keys[index]] = ne_col_values[index]
                bid_list = ne_dict['bd_list'].split(',')

                # 取 board
                bd_list = []
                for index_bd in range(0,len(bid_list)):
                    bd_dict = {}
                    for index_bd_i in range(0,4):
                        if type(all_bd_value[4*index_bd+index_bd_i]) == float:
                            bd_dict[all_bd_key[4*index_bd+index_bd_i]] = str(int(all_bd_value[4*index_bd+index_bd_i]))
                        else:
                            bd_dict[all_bd_key[4*index_bd + index_bd_i]] = all_bd_value[4*index_bd + index_bd_i]

                    # 取 port
                    pid_list = bd_dict['port_list'].split(',')
                    port_list = []
                    if 'null' not in pid_list:
                        for index_port in range(0,len(pid_list)):
                            port_dict = {}
                            for index_port_i in range(0,5):
                                if type(all_port_value[index_port_i]) == float:
                                    port_dict[all_port_key[index_port_i]] = str(int(all_port_value[index_port_i]))
                                else:
                                    port_dict[all_port_key[index_port_i]] = all_port_value[index_port_i]

                            # 取出chaanel
                            ch_id_list = port_dict['ch_list'].split(',')
                            ch_list = []
                            if 'null' not in ch_id_list:
                                for index_ch in range(0,len(ch_id_list)):
                                    ch_dict = {}
                                    for index_ch_i in range(0,3):
                                        if type(all_ch_value[index_ch_i]) == float:
                                            ch_dict[all_ch_key[index_ch_i]] = str(int(all_ch_value[index_ch_i]))
                                        else:
                                            ch_dict[all_ch_key[index_ch_i]] = all_ch_value[index_ch_i]
                                    ch_list.append(ch_dict)

                                # 移除已经取出的channel
                                    for index_ch_i in range(2,-1,-1):
                                        all_ch_key.remove(all_ch_key[index_ch_i])
                                        all_ch_value.remove(all_ch_value[index_ch_i])
                            # 移除已经提取出的port
                            for index_port_i in range(4,-1,-1):
                                all_port_key.remove(all_port_key[index_port_i])
                                all_port_value.remove(all_port_value[index_port_i])

                            port_dict['ch_list'] = ch_list
                            port_list.append(port_dict)

                    bd_dict['port_list'] = port_list
                    bd_list.append(bd_dict)

                ne_dict['bd_list'] = bd_list

                ne_info_all.append(ne_dict)

            # 设备为仪表
            instrument_dict = {}
            if 'instrument' in env_sheet.cell_value(0,0):

                # 提取仪表
                instrument_col_keys = env_sheet.col_values(0)
                instrument_col_values = env_sheet.col_values(1)
                for instrument_index in range(0,len(instrument_col_keys)):
                    if instrument_col_keys[instrument_index] != '':
                        if type(instrument_col_values[instrument_index]) == float:
                            instrument_dict[instrument_col_keys[instrument_index]] = str(int(instrument_col_values[instrument_index]))
                        else:
                            instrument_dict[instrument_col_keys[instrument_index]] = instrument_col_values[instrument_index]

                all_bd_key = []
                all_bd_value = []
                bd_keys = env_sheet.col_values(2)
                bd_values = env_sheet.col_values(3)
                for index in range(0,len(bd_keys)):
                    if bd_keys[index] != '':
                        all_bd_key.append(bd_keys[index])
                        if type(bd_values[index]) == float:
                            all_bd_value.append(str(int(bd_values[index])))
                        else:
                            all_bd_value.append(bd_values[index])

                all_port_key = []
                all_port_value = []
                port_keys = env_sheet.col_values(4)
                port_values = env_sheet.col_values(5)
                for index in range(0,len(port_keys)):
                    if port_keys[index] != '':
                        all_port_key.append(port_keys[index])
                        if type(port_values[index]) == float:
                            all_port_value.append(str(int(port_values[index])))
                        else:
                            all_port_value.append(port_values[index])

                # 提取仪表单板
                bid_list = instrument_dict['bd_list'].split(',')
                bd_list = []
                for index_bd in range(0,len(bid_list)):
                    bd_dict = {}
                    for index_bd_i in range(0,4):
                        bd_dict[all_bd_key[4*index_bd+index_bd_i]] = all_bd_value[4*index_bd+index_bd_i]

                    # 提取仪表端口
                    pid_list = bd_dict['port_list'].split(',')
                    port_list = []
                    for index_port in range(0,len(pid_list)):
                        port_dict = {}
                        for index_port_i in range(0,3):
                            port_dict[all_port_key[index_port_i]] = all_port_value[index_port_i]
                        port_list.append(port_dict)

                        # 移除已经提取出的端口
                        for index_port_i in range(2,-1,-1):
                            all_port_key.remove(all_port_key[index_port_i])
                            all_port_value.remove(all_port_value[index_port_i])

                    bd_dict['port_list'] = port_list
                    bd_list.append(bd_dict)
                instrument_dict['bd_list'] = bd_list
                instrument_info_all.append(instrument_dict)

            # 对象是连线
            try:
                if 'link' in env_sheet.cell_value(0, 0):
                    link_key_list = []
                    link_value_list = []
                    link_col_keys = env_sheet.col_values(0)
                    link_col_value = env_sheet.col_values(1)
                    for index in range(0, len(link_col_keys)):
                        if link_col_keys[index] != '':
                            link_key_list.append(link_col_keys[index])
                            if type(link_col_value[index]) == float:
                                link_value_list.append(str(int(link_col_value[index])))
                            else:
                                link_value_list.append(link_col_value[index])

                    link_dict = {}
                    for index in range(0, len(link_key_list)):
                        link_dict[link_key_list[index]] = link_value_list[index]
                        if (index + 1) % 8 == 0:
                            link_info_all.append(link_dict)
                            link_dict = {}

                    break
            except:
                print('链路文件异常')

        env_info = {}
        env_info['ne'] = ne_info_all
        env_info['instrument'] = instrument_info_all
        env_info['link'] = link_info_all

        return env_info

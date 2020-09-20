#-*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
---------------------------------------
    文件名：down_file.py
    描述：
    作者：penglingsen
    创建日期：2020/8/26 17:38
---------------------------------------
"""

import os
import sys
from ftplib import FTP

# 连接ftp服务器
def ftpConnect(ftpserver, port, usrname, password):
    ftp = FTP()
    try:
        ftp.connect(ftpserver, port)
        ftp.login(usrname, password)
    except:
        raise IOError('\n FTP connection failed, please check the code!')
    else:
        print(ftp.getwelcome()) # 打印登陆成功后的欢迎信息
        print('\n+------- ftp connection successful!!! --------+')
        return ftp

# 下载单个文件
def ftpDownloadFile(ftp, ftpfile, localfile):
    # fid = open(localfile, 'wb') # 以写模式打开本地文件
    bufsize =  1024
    with open(localfile, 'wb') as fid:
        ftp.retrbinary('RETR {0}'.format(ftpfile), fid.write, bufsize) # 接收服务器文件并写入本地文件
    return True


# 退出ftp连接
def ftpDisConnect(ftp):
    ftp.quit()


# 程序入口
if __name__ == '__main__':
    # 输入参数
    ftpserver = '172.18.60.230'
    port = 21
    usrname = 'bin_upload'
    pwd = 'upload'
    ftpath = '/IDS/CS7060/HW/控制端/ids.md5'
    localpath = r'E:\启明\个人-常用工具\CS7060\ftp下载\ids.md5'

    ftp = ftpConnect(ftpserver, 21, usrname, pwd)
    flag = ftpDownloadFile(ftp, ftpath, localpath)
    print(flag)
    ftpDisConnect(ftp)
    print("\n+-------- OK!!! --------+\n")
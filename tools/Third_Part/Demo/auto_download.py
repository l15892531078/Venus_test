# -*- coding: utf-8 -*-
"""
---------------------------------------
    文件名：auto_download.py
    描述：从官网事件库上自动下载最新的事件库
    作者：penglingsen
    创建日期：2020/7/27 15:41
---------------------------------------
"""
import json,os,sys
import Venus.tools.Third_Part.requests as requests
import urllib3

url = 'https://backend.venuscloud.cn/upgradecenter/main/getLibById'

urllib3.disable_warnings()
data_dumps = json.dumps({'libId':4,'modelId':1,'page':1,'pageSize':20})
response = requests.post(url=url,data=data_dumps,headers={'Content-Type':'application/json'})
dat_list = response.json()['data']
download_url = dat_list[0]['downloadLink']
print('\t事件库名称：',dat_list[0]['upgradeContent'],'\n',
      '\t更新时间：',dat_list[0]['update'],'\n',
      '\t事件库大小：',dat_list[0]['size'],'\n',
      '\tMD5：',dat_list[0]['md5'],'\n',
      '\t下载链接：',download_url)

print ('\n\n正在下载，请稍后...')
download_res = requests.get(url=download_url)
file_name_list = download_url.split('/')
file_name = os.path.dirname(sys.argv[0])+'/'+file_name_list[-2]+'_'+file_name_list[-1]
with open(file_name,'wb') as f:
    f.write(download_res.content)

# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 13:58:03 2020

@author: 28446
"""

import requests


# 测试链接
# 运行代码
# 要求 post 用户名 代码为字典格式{’code':'上传的代码'(类型str)}
# 如果需要使用到上传到的文件或需要保存文件
# 路径应写为 static/用户名/上传的文件名or要保存的文件名
user_info = {'code': "print('a')\nprint('b')\nprint(a)"}
r = requests.post("http://jiutian.51vip.biz?id=100", data=user_info)  # 测试ip地址
# 错误返回报错信息，正确返回输出结果，可同时输出
# 如果有上传的文件或者生成的图片会在files返回文件列表
# 如果代码存在危险词如cd ls remove等返回安全状态false否则返回true

'''
#上传文件
#要求post+用户名+上传的文件
f=open('123.zip','rb')
file_info={'touch':f}
r = requests.post("http://jiutian.51vip.biz/upload?id=100", files=file_info)
f.close()
#响应state:success/error
'''
'''
#删除文件  id(用户id)  file_name(要删除的文件名)
r=requests.get("http://jiutian.51vip.biz/delete?id=100&file_name=123.zip")
#响应state:success/error
'''

print(r.text)

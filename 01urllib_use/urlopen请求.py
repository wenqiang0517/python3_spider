#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import urllib.request
import urllib.parse

"""
response = urllib.request.urlopen('https://www.baidu.com/')
print(response.read().decode('utf-8'))
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))
"""

"""
# data参数
data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read())
"""

# 超时时间设置
import socket
import urllib.error
try:
    response = urllib.request.urlopen('https://www.httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    # isinstance()判断2个类型是否相同，相同返回true, 不同返回false
    if isinstance(e.reason, socket.timeout):
        print(e.reason, '---------', socket.timeout)
        print(type(e.reason), '---------', type(socket.timeout))
        print('TIME OUT')




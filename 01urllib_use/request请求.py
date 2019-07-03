#!/usr/bin/env python3
# -*- coding: UTF-8 -*-



"""
from urllib import request, parse

url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org',
}
dict = {
    'name': 'Germey',
}
data = bytes(parse.urlencode(dict), encoding='utf8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))
"""


# BaseHandler类
# 针对弹出的提示登录框进行验证登录
from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError
username = 'qiangge'
pwd = '123456'
url = 'http://139.224.95.172/wechat-web/login'
p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, pwd)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)
try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)




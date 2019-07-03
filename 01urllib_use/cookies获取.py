#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


import http.cookiejar, urllib.request

"""
cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://139.224.95.172/wechat-web/login')
for item in cookie:
    print(item.name + "=" + item.value)
"""

"""
# 将cookie保存到文件
filename = 'cookies2.txt'
# cookie = http.cookiejar.MozillaCookieJar(filename)  # 保存成Mozilla型浏览器的cookie文件
cookie = http.cookiejar.LWPCookieJar(filename)   # 保存成LMP格式的cookie文件
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.baidu.com/')
cookie.save(ignore_discard=True, ignore_expires=True)
"""

# 通过cookies文件获取源码
cookie = http.cookiejar.LWPCookieJar()
cookie.load('cookies2.txt', ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.baidu.com/')
print(response.read().decode('utf-8'))


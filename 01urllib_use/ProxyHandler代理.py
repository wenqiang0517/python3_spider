#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

proxy_handler = ProxyHandler({
    'http': 'http://127.0.0.1:9743',
    'https': 'https://127.0.0.1:9743'
})
opener = build_opener(proxy_handler)
# try:
response = opener.open('http://139.224.95.148/yx-leex-web/login')
print(response.read().decode('utf-8'))
# except URLError as e:
#     print(e)
#     print(e.reason)







#!/usr/bin/env python3
# coding:utf-8

from requests import get

url = "http://www.pythonchallenge.com/pc/stuff/violin.php"
cookie = {"info": "the flowers are on their way"}
res = get(url, cookies=cookie)
print(res.text)

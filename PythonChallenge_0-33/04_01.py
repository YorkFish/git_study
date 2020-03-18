#!/usr/bin/env python3
# coding:utf-8

from re import findall
from requests import get

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
num = 44827
res = get(url + str(num))
try:
    while True:
        num = findall(r"\d{3,}", res.text)[0]
        print(num)
        res = get(url + num)
except:
    print(res.text)

#!/usr/bin/env python3
# coding:utf-8

from requests import get

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing="
num = "12345"
lst = []
while num.isdecimal():
    res = get(url + num)
    lst.append(res.cookies.get("info"))
    num = res.text.split()[-1]
    print(num)
print(res.text)

tmp = ''.join(lst)
print(tmp)
with open("17_cookies.txt", 'w') as f:
    f.write(tmp)

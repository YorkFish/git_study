#!/usr/bin/env python3
# coding:utf-8

from requests import get

num = 16044 // 2
while True:
    res = get(f"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={num}")
    num = res.text.split()[-1]
    if num.isdigit():
        print(num)
    else:
        print(res.text)
        break

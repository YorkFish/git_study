#!/usr/bin/env python3
# coding:utf-8

from bz2 import decompress
from urllib.parse import unquote_to_bytes

with open("17_cookies.txt", 'r') as f:
    text = f.readline()
    res = text.replace('+', ' ')
    ans = unquote_to_bytes(res)
    print(decompress(ans))

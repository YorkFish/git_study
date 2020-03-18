#!/usr/bin/env python3
# coding:utf-8

from collections import Counter

with open("ocr.txt") as f:
    c = Counter(f.read())
    res = [e for e in c if c[e] == 1]
    print(''.join(res))

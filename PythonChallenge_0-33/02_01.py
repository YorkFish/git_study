#!/usr/bin/env python3
# coding:utf-8

with open("ocr.txt") as f:
    d = {}
    for e in f.read():
        d[e] = d.get(e, 0) + 1
    lst = [e for e in d.keys()]
    lst.sort(key=lambda x: d[x])
    print(''.join(lst))

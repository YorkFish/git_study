#!/usr/bin/env python3
# coding:utf-8

'''
本程序不是题目的解，
是出于好奇，考察一下 0 ~ 10000+268 的 len(str(sqrt(n)))
'''
from math import sqrt

d = {}
for i in range(10269):
    length1 = len(str(sqrt(i)))
    d[length1] = d.get(length1, 0) + 1

items = list(d.items())
items.sort( key=lambda x:x[0], reverse=False) 
items.insert(0, ('length', 'count'))
for i in range(len(items)):
    length2, count = items[i]
    print("{0:<8}{1:>8}".format(length2, count))


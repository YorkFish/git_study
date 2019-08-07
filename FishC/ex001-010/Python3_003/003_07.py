#!/usr/bin/env python3
# coding:utf-8

from math import sqrt

'''
算式 sqrt(n + 100) 与 sqrt(n + 268) 成立
=> n >= -100

>>> (-2.0).is_integer()
True
>>> (3.2).is_integer()
False
'''
for x in range(-100, 10001):
    if sqrt(x+100).is_integer() and sqrt(x+268).is_integer():
        print(x)


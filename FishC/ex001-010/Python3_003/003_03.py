#!/usr/bin/env python3
# coding:utf-8

from math import sqrt

'''
算式 sqrt(n + 100) 与 sqrt(n + 268) 成立
=> n >= -100
'''
for i in range(-100, 10001):
    temp1 = int(sqrt(i + 100))
    temp2 = int(sqrt(i + 268))

    if temp1**2 == i+100 and temp2**2 == i+268:
        print(i)


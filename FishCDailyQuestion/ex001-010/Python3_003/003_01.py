#!/usr/bin/env python3
# coding:utf-8

import math

'''
由题意得，某数 n 加上 100 或 268 能开方，
=> sqrt(n + 100) and sqrt(n + 268) 均成立
=> n >= -100
'''
num = -100

while num < 10000:
    temp1 = math.sqrt(num + 100)
    temp2 = math.sqrt(num + 268)
    if temp1 == int(temp1) and temp2 == int(temp2):
        print(num)
    num += 1

